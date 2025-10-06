import pytest
import sqlite3
import hashlib
from Login import LoginDatabase, AuthSystem
from SuhuConverter import (
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
    fahrenheit_ke_celsius,
    fahrenheit_ke_kelvin,
    kelvin_ke_celsius,
    kelvin_ke_fahrenheit
)

@pytest.fixture
def test_db():
    db = LoginDatabase(":memory:")
    yield db
    db.close()

@pytest.fixture
def auth_system(test_db):
    return AuthSystem(test_db)

# TEMPERATURE CONVERSION TESTS
class TestTemperatureConverter:
    # Test all Celsius conversions together
    def test_celsius_conversions(self):
        # Celsius to Fahrenheit
        assert pytest.approx(celsius_ke_fahrenheit(0), 0.1) == 32      # Freezing
        assert pytest.approx(celsius_ke_fahrenheit(100), 0.1) == 212   # Boiling
        assert pytest.approx(celsius_ke_fahrenheit(-40), 0.1) == -40   # Equal point
        assert pytest.approx(celsius_ke_fahrenheit(37), 0.1) == 98.6   # Body temp

        # Celsius to Kelvin
        assert pytest.approx(celsius_ke_kelvin(0), 0.1) == 273.15      # Freezing
        assert pytest.approx(celsius_ke_kelvin(100), 0.1) == 373.15    # Boiling
        assert pytest.approx(celsius_ke_kelvin(-273.15), 0.1) == 0     # Absolute zero

    # Test all Fahrenheit conversions together
    def test_fahrenheit_conversions(self):
        # Fahrenheit to Celsius
        assert pytest.approx(fahrenheit_ke_celsius(32), 0.1) == 0      # Freezing
        assert pytest.approx(fahrenheit_ke_celsius(212), 0.1) == 100   # Boiling
        assert pytest.approx(fahrenheit_ke_celsius(-40), 0.1) == -40   # Equal point

        # Fahrenheit to Kelvin
        assert pytest.approx(fahrenheit_ke_kelvin(32), 0.1) == 273.15  # Freezing
        assert pytest.approx(fahrenheit_ke_kelvin(-459.67), 0.1) == 0  # Absolute zero

    # Test all Kelvin conversions together
    def test_kelvin_conversions(self):
        # Kelvin to Celsius
        assert pytest.approx(kelvin_ke_celsius(273.15), 0.1) == 0      # Freezing
        assert pytest.approx(kelvin_ke_celsius(373.15), 0.1) == 100    # Boiling
        assert pytest.approx(kelvin_ke_celsius(0), 0.1) == -273.15     # Absolute zero

        # Kelvin to Fahrenheit
        assert pytest.approx(kelvin_ke_fahrenheit(273.15), 0.1) == 32  # Freezing
        assert pytest.approx(kelvin_ke_fahrenheit(373.15), 0.1) == 212 # Boiling

    # Test bidirectional conversions
    def test_bidirectional_conversions(self):
        # Test a few key values for round-trip conversions
        for value in [0, 25, 100]:
            # C → F → C
            assert pytest.approx(fahrenheit_ke_celsius(celsius_ke_fahrenheit(value)), 0.01) == value

            # C → K → C
            assert pytest.approx(kelvin_ke_celsius(celsius_ke_kelvin(value)), 0.01) == value

            # F → K → F (using 32, 77, 212 as Fahrenheit values)
            f_value = celsius_ke_fahrenheit(value)
            assert pytest.approx(kelvin_ke_fahrenheit(fahrenheit_ke_kelvin(f_value)), 0.01) == f_value

    # Test precision for body temperature range
    def test_precision(self):
        assert pytest.approx(celsius_ke_fahrenheit(36.5), abs=1e-10) == 97.7
        assert pytest.approx(celsius_ke_fahrenheit(36.9), abs=1e-10) == 98.42

# LOGIN SYSTEM TESTS
class TestLoginSystem:
    def test_database_setup(self, test_db):
        # Test database initialization and admin creation
        cursor = test_db.conn.cursor()

        # Check table creation
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        assert cursor.fetchone() is not None

        # Check admin user creation
        cursor.execute("SELECT username, role, password FROM users WHERE username='admin'")
        user = cursor.fetchone()
        assert user is not None
        assert user[0] == 'admin'
        assert user[1] == 'admin'

        # Check password hashing
        expected_hash = hashlib.sha256("admin123".encode()).hexdigest()
        assert user[2] == expected_hash

    def test_password_security(self, auth_system):
        # Test password hashing
        password = "securepassword"
        hashed = auth_system.hash_password(password)
        expected = hashlib.sha256(password.encode()).hexdigest()
        assert hashed == expected

    def test_user_registration(self, auth_system):
        # Test successful registration
        assert auth_system.register("testuser1", "password123") is True

        # Test duplicate registration fails
        assert auth_system.register("testuser1", "newpassword") is False

        # Verify user was added correctly
        cursor = auth_system.db.conn.cursor()
        cursor.execute("SELECT username, role FROM users WHERE username='testuser1'")
        user = cursor.fetchone()
        assert user is not None
        assert user[0] == 'testuser1'
        assert user[1] == 'user'

    def test_login_functionality(self, auth_system):
        # Setup test users
        auth_system.register("loginuser", "correctpass")

        # Test successful login
        user = auth_system.login("loginuser", "correctpass")
        assert user is not None
        assert user["username"] == "loginuser"
        assert user["role"] == "user"

        # Test failed login - wrong password
        assert auth_system.login("loginuser", "wrongpass") is None

        # Test failed login - nonexistent user
        assert auth_system.login("nonexistent", "anypass") is None

    def test_user_management(self, auth_system):
        # Test user listing functionality
        auth_system.register("user1", "pass1")
        auth_system.register("user2", "pass2")

        users = auth_system.get_all_users()
        assert len(users) >= 3  # admin + user1 + user2

        usernames = [user[1] for user in users]
        assert "admin" in usernames
        assert "user1" in usernames
        assert "user2" in usernames

    def test_sql_injection(self, auth_system):
        """Test SQL injection protection in login and register"""
        # Create a legitimate user for testing
        auth_system.register("victim", "securepass")

        # Test SQL injection in login
        payloads = [
            "victim' OR '1'='1",
            "victim' --",
            "victim\" OR \"1\"=\"1"
        ]

        for payload in payloads:
            result = auth_system.login(payload, "anypass")
            assert result is None, f"SQL Injection succeeded with: {payload}"

        # Test register with suspicious username
        auth_system.register("user'); DROP TABLE users; --", "password")

        # Verify table still exists and no extra admins were created
        cursor = auth_system.db.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
        assert cursor.fetchone()[0] == 1, "SQL Injection affected admin count"