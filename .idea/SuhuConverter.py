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

def main():
    print("=== KONVERTER SUHU ===")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    asal = input("\nPilih skala suhu asal : ")
    nilai = float(input("Masukkan nilai suhu: "))
    tujuan = input("Pilih skala suhu tujuan : ")

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

if __name__ == "__main__":
    main()