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
    # F1, F2, F3: Test login functionality
    def test_login_functionality(self, auth_system):
        """
        F1: Login Berhasil - Login dengan kredensial yang benar
        F2: Login Gagal - Password Salah
        F3: Login User Tidak Terdaftar
        """
        # Setup test users
        auth_system.register("loginuser", "correctpass")

        # F1: Test successful login
        user = auth_system.login("loginuser", "correctpass")
        assert user is not None, "F1 FAILED: Login dengan kredensial benar harus berhasil"
        assert user["username"] == "loginuser"
        assert user["role"] == "user"

        # F2: Test failed login - wrong password
        user_wrong_pass = auth_system.login("loginuser", "wrongpass")
        assert user_wrong_pass is None, "F2 FAILED: Login dengan password salah harus gagal"

        # F3: Test failed login - nonexistent user
        user_nonexist = auth_system.login("nonexistent", "anypass")
        assert user_nonexist is None, "F3 FAILED: Login dengan user tidak terdaftar harus gagal"

    # F4, F5: Test user registration
    def test_user_registration(self, auth_system):
        """
        F4: Register Berhasil - Registrasi user baru dengan data valid
        F5: Register Gagal - Username Sudah Ada
        """
        # F4: Test successful registration
        result = auth_system.register("testuser1", "password123")
        assert result is True, "F4 FAILED: Registrasi dengan data valid harus berhasil"

        # F5: Test duplicate registration fails
        result_duplicate = auth_system.register("testuser1", "newpassword")
        assert result_duplicate is False, "F5 FAILED: Registrasi dengan username yang sudah ada harus gagal"

        # Verify user was added correctly
        cursor = auth_system.db.conn.cursor()
        cursor.execute("SELECT username, role FROM users WHERE username='testuser1'")
        user = cursor.fetchone()
        assert user is not None
        assert user[0] == 'testuser1'
        assert user[1] == 'user'

    def test_database_setup(self, test_db):
        """Test database initialization and admin creation"""
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
        """Test password hashing"""
        password = "securepassword"
        hashed = auth_system.hash_password(password)
        expected = hashlib.sha256(password.encode()).hexdigest()
        assert hashed == expected

    def test_user_management(self, auth_system):
        """Test user listing functionality"""
        auth_system.register("user1", "pass1")
        auth_system.register("user2", "pass2")

        users = auth_system.get_all_users()
        assert len(users) >= 3  # admin + user1 + user2

        usernames = [user[1] for user in users]
        assert "admin" in usernames
        assert "user1" in usernames
        assert "user2" in usernames

    # F8, F9: Test SQL injection protection
    def test_sql_injection(self, auth_system):
        """
        F8: Login SQL Injection — Password
        F9: Login SQL Injection — Username
        Test SQL injection protection in login and register
        """
        # Create a legitimate user for testing
        auth_system.register("victim", "securepass")

        # F9: Test SQL injection in username field
        username_payloads = [
            "victim' OR '1'='1",
            "victim' --",
            "victim\" OR \"1\"=\"1",
            "admin' --",
            "' OR '1'='1' --",
            "admin'/*",
        ]

        for payload in username_payloads:
            result = auth_system.login(payload, "anypass")
            assert result is None, f"F9 FAILED: SQL Injection via username succeeded with: {payload}"

        # F8: Test SQL injection in password field
        password_payloads = [
            "1234' OR '1'='1",
            "' OR '1'='1' --",
            "anything' OR 'x'='x",
            "1234' OR 1=1--",
        ]

        for payload in password_payloads:
            result = auth_system.login("admin", payload)
            assert result is None, f"F8 FAILED: SQL Injection via password succeeded with: {payload}"

        # Test register with suspicious username (should not drop table)
        auth_system.register("user'); DROP TABLE users; --", "password")

        # Verify table still exists and no extra admins were created
        cursor = auth_system.db.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE role='admin'")
        admin_count = cursor.fetchone()[0]
        assert admin_count == 1, "SQL Injection affected admin count"

        # Verify table still exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        assert cursor.fetchone() is not None, "Table was dropped by SQL injection"


# VALIDATION TESTS (For UI-level validations)
# Note: F6 and F7 are UI-level validations that should be tested via integration tests
# or by refactoring the validation logic into the AuthSystem class
class TestValidationLogic:
    """
    These tests demonstrate the validation logic that should be in place.
    In the current implementation, F6 and F7 validations are in the UI layer (main function).
    For proper unit testing, these should be refactored into the AuthSystem class.
    """

    def test_password_validation_helper(self):
        """
        Helper function to demonstrate F6 and F7 validation logic.
        This should ideally be a method in AuthSystem class.
        """
        def validate_password(password, confirm_password):
            """Returns (is_valid, error_message)"""
            # F6: Check if passwords match
            if password != confirm_password:
                return False, "✗ Password tidak cocok!"

            # F7: Check minimum length
            if len(password) < 6:
                return False, "✗ Password minimal 6 karakter!"

            return True, None

        # F6: Test password mismatch
        is_valid, msg = validate_password("pass123", "pass456")
        assert is_valid is False, "F6 FAILED: Password tidak cocok harus ditolak"
        assert msg == "✗ Password tidak cocok!"

        # F7: Test password too short
        is_valid, msg = validate_password("abc", "abc")
        assert is_valid is False, "F7 FAILED: Password kurang dari 6 karakter harus ditolak"
        assert msg == "✗ Password minimal 6 karakter!"

        # Test valid password
        is_valid, msg = validate_password("password123", "password123")
        assert is_valid is True, "Password valid harus diterima"
        assert msg is None


# NOTE ABOUT F10 (Logout):
# F10 is not testable at the unit test level because there's no explicit logout function
# in the AuthSystem class. The "logout" happens implicitly when:
# 1. User selects "Exit" from menu (choice == "3")
# 2. User completes temperature conversion and chooses not to continue
#
# To test F10 properly, you would need integration tests that test the main() function
# or converter_menu() function flows.

# INTEGRATION TESTS FOR F10 (LOGOUT)
import io
import sys
from unittest.mock import patch, MagicMock

class TestLogoutIntegration:
    """
    Integration tests for F10 (Logout) functionality.
    Tests the complete flow of login -> temperature conversion -> logout -> back to login menu
    """



    def test_F10_logout_via_converter_exit(self):
        """
        F10: Test logout via temperature converter exit (choice == "4" in converter menu)
        User should return to login menu after exiting from temperature converter
        """
        inputs = [
            '2', 'admin', 'admin123',  # Login
            '4',  # Exit from converter menu (simulated via SuhuConverter.py)
            '3'   # Final exit
        ]

