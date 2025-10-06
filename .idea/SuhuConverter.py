from Login import LoginDatabase, AuthSystem
import sys

def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15

def fahrenheit_ke_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_ke_celsius(k):
    return k - 273.15

def kelvin_ke_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def converter_menu(user=None):
    if user is None:
        print("⚠️ Akses ditolak. Silakan login terlebih dahulu.")
        return

    print("\n=== KONVERTER SUHU ===")
    print(f"User: {user['username']} ({user['role']})")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("4. Keluar")

    asal = input("\nPilih skala suhu asal (1-4): ")

    if asal == "4":
        print("Terima kasih telah menggunakan aplikasi konverter suhu!")
        return

    try:
        nilai = float(input("Masukkan nilai suhu: "))
        tujuan = input("Pilih skala suhu tujuan (1-3): ")

        if asal == "1":
            if tujuan == "2":
                hasil = celsius_ke_fahrenheit(nilai)
                print(f"{nilai}°C = {hasil:.2f}°F")
            elif tujuan == "3":
                hasil = celsius_ke_kelvin(nilai)
                print(f"{nilai}°C = {hasil:.2f}K")
            else:
                print(f"{nilai}°C")

        elif asal == "2":
            if tujuan == "1":
                hasil = fahrenheit_ke_celsius(nilai)
                print(f"{nilai}°F = {hasil:.2f}°C")
            elif tujuan == "3":
                hasil = fahrenheit_ke_kelvin(nilai)
                print(f"{nilai}°F = {hasil:.2f}K")
            else:
                print(f"{nilai}°F")

        elif asal == "3":
            if tujuan == "1":
                hasil = kelvin_ke_celsius(nilai)
                print(f"{nilai}K = {hasil:.2f}°C")
            elif tujuan == "2":
                hasil = kelvin_ke_fahrenheit(nilai)
                print(f"{nilai}K = {hasil:.2f}°F")
            else:
                print(f"{nilai}K")

        # Ask if user wants to continue
        cont = input("\nLakukan konversi lagi? (y/n): ").lower()
        if cont == "y":
            converter_menu(user)

    except ValueError:
        print("⚠️ Input tidak valid. Masukkan angka untuk nilai suhu.")
        converter_menu(user)

def login_screen():
    db = LoginDatabase()
    auth = AuthSystem(db)

    while True:
        print("\n=== SISTEM LOGIN KONVERTER SUHU ===")
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
                converter_menu(user)
            else:
                print("✗ Username atau password salah!")

        elif choice == "3":
            print("Terima kasih!")
            db.close()
            sys.exit()
        else:
            print("✗ Pilihan tidak valid!")

def main():
    login_screen()

if __name__ == "__main__":
    main()