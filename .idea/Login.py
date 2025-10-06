import sqlite3
import hashlib
import os
import sys

# ========== DATABASE ==========
class LoginDatabase:
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.setup_database()

    def setup_database(self):
        cursor = self.conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS users (
                                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            username TEXT UNIQUE NOT NULL,
                                                            password TEXT NOT NULL,
                                                            role TEXT NOT NULL
                       )
                       ''')
        self.conn.commit()

        # Buat admin jika belum ada
        cursor.execute("SELECT id FROM users WHERE username='admin'")
        if not cursor.fetchone():
            admin_password = hashlib.sha256("admin123".encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', ?, 'admin')",
                           (admin_password,))
            self.conn.commit()

    def close(self):
        self.conn.close()


# ========== AUTHENTICATION ==========
class AuthSystem:
    def __init__(self, db):
        self.db = db

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        cursor = self.db.conn.cursor()
        try:
            hashed_password = self.hash_password(password)
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, 'user')",
                           (username, hashed_password))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, username, password):
        cursor = self.db.conn.cursor()
        hashed_password = self.hash_password(password)
        cursor.execute("SELECT id, username, role FROM users WHERE username=? AND password=?",
                       (username, hashed_password))
        result = cursor.fetchone()
        if result:
            return {"user_id": result[0], "username": result[1], "role": result[2]}
        return None

    def get_all_users(self):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT id, username, role FROM users")
        return cursor.fetchall()


# ========== INTERFACE ==========
def admin_panel(auth):
    print("\n=== ADMIN PANEL ===")
    print("1. Lihat Semua User")
    print("2. Kembali")

    choice = input("\nPilih menu (1-2): ")

    if choice == "1":
        users = auth.get_all_users()
        print("\n=== DAFTAR USER ===")
        print(f"{'ID':<5} {'Username':<20} {'Role':<10}")
        print("-" * 35)
        for user in users:
            print(f"{user[0]:<5} {user[1]:<20} {user[2]:<10}")


def main():
    db = LoginDatabase()
    auth = AuthSystem(db)

    user = None

    # Loop sampai berhasil login
    while user is None:
        print("\n=== SISTEM LOGIN ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nPilih menu (1-3): ")

        if choice == "1":
            print("\n=== REGISTER ===")
            username = input("Username: ")
            password = input("Password: ")
            confirm = input("Konfirmasi Password: ")

            if password != confirm:
                print("✗ Password tidak cocok!")
            elif len(password) < 6:
                print("✗ Password minimal 6 karakter!")
            else:
                if auth.register(username, password):
                    print("✓ Registrasi berhasil! Silakan login.")
                else:
                    print("✗ Username sudah digunakan!")

        elif choice == "2":
            print("\n=== LOGIN ===")
            username = input("Username: ")
            password = input("Password: ")

            user = auth.login(username, password)
            if user:
                print(f"✓ Login berhasil! Selamat datang {user['username']}!")
                db.close()

                # Jalankan file SuhuConverter.py
                print("\n" + "="*50)
                print("Menjalankan Konverter Suhu...")
                print("="*50 + "\n")

                os.system('python SuhuConverter.py')
                return

            else:
                print("✗ Username atau password salah!")

        elif choice == "3":
            print("Terima kasih!")
            db.close()
            return

        else:
            print("✗ Pilihan tidak valid!")

    db.close()


if __name__ == "__main__":
    main()