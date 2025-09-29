"""
Modul Konversi Suhu
Mendukung konversi antara Celsius, Fahrenheit, Kelvin, dan Reamur
"""

class TemperatureError(Exception):
    """Custom exception untuk error terkait suhu"""
    pass


def celsius_to_fahrenheit(celsius):
    """
    Konversi Celsius ke Fahrenheit
    Formula: F = (C × 9/5) + 32
    """
    if celsius < -273.15:
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-273.15°C)")
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Konversi Fahrenheit ke Celsius
    Formula: C = (F - 32) × 5/9
    """
    if fahrenheit < -459.67:
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-459.67°F)")
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """
    Konversi Celsius ke Kelvin
    Formula: K = C + 273.15
    """
    if celsius < -273.15:
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-273.15°C)")
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Konversi Kelvin ke Celsius
    Formula: C = K - 273.15
    """
    if kelvin < 0:
        raise TemperatureError("Suhu tidak boleh di bawah 0 Kelvin (absolute zero)")
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    """Konversi Fahrenheit ke Kelvin"""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_fahrenheit(kelvin):
    """Konversi Kelvin ke Fahrenheit"""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)


def celsius_to_reamur(celsius):
    """
    Konversi Celsius ke Reamur
    Formula: R = C × 4/5
    """
    if celsius < -273.15:
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-273.15°C)")
    return celsius * 4/5


def reamur_to_celsius(reamur):
    """
    Konversi Reamur ke Celsius
    Formula: C = R × 5/4
    """
    if reamur < -218.52:  # -273.15 * 4/5
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-218.52°R)")
    return reamur * 5/4


def convert_temperature(value, from_unit, to_unit):
    """
    Konversi suhu dari satu satuan ke satuan lainnya

    Args:
        value: Nilai suhu
        from_unit: Satuan asal ('C', 'F', 'K', 'R')
        to_unit: Satuan tujuan ('C', 'F', 'K', 'R')
    """
    from_unit = from_unit.upper().strip()
    to_unit = to_unit.upper().strip()

    valid_units = ['C', 'F', 'K', 'R']

    if from_unit not in valid_units:
        raise ValueError(f"Satuan asal tidak valid: {from_unit}. Gunakan: C, F, K, atau R")

    if to_unit not in valid_units:
        raise ValueError(f"Satuan tujuan tidak valid: {to_unit}. Gunakan: C, F, K, atau R")

    if from_unit == to_unit:
        return value

    # Konversi ke Celsius terlebih dahulu
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'K':
        celsius = kelvin_to_celsius(value)
    elif from_unit == 'R':
        celsius = reamur_to_celsius(value)

    # Konversi dari Celsius ke satuan tujuan
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'K':
        return celsius_to_kelvin(celsius)
    elif to_unit == 'R':
        return celsius_to_reamur(celsius)


def get_temperature_category(celsius):
    """Mendapatkan kategori suhu berdasarkan nilai Celsius"""
    if celsius < -273.15:
        raise TemperatureError("Suhu tidak boleh di bawah absolute zero (-273.15°C)")
    elif celsius < -50:
        return "Sangat Dingin Ekstrim"
    elif celsius < 0:
        return "Sangat Dingin"
    elif celsius < 10:
        return "Dingin"
    elif celsius < 20:
        return "Sejuk"
    elif celsius < 30:
        return "Hangat"
    elif celsius < 40:
        return "Panas"
    else:
        return "Sangat Panas"


def is_freezing_point(celsius, tolerance=0.1):
    """Cek apakah suhu mendekati titik beku air (0°C)"""
    return abs(celsius - 0) <= tolerance


def is_boiling_point(celsius, tolerance=0.1):
    """Cek apakah suhu mendekati titik didih air (100°C)"""
    return abs(celsius - 100) <= tolerance


def format_temperature(value, unit, decimal_places=2):
    """Format tampilan suhu dengan satuan"""
    unit = unit.upper().strip()

    unit_symbols = {
        'C': '°C',
        'F': '°F',
        'K': 'K',
        'R': '°R'
    }

    if unit not in unit_symbols:
        raise ValueError(f"Satuan tidak valid: {unit}")

    return f"{value:.{decimal_places}f}{unit_symbols[unit]}"


def main():
    """Program CLI untuk konversi suhu"""
    print("="*50)
    print("KONVERSI SUHU")
    print("="*50)
    print("\nSatuan yang tersedia:")
    print("C = Celsius")
    print("F = Fahrenheit")
    print("K = Kelvin")
    print("R = Reamur")
    print("-"*50)

    try:
        value = float(input("\nMasukkan nilai suhu: "))
        from_unit = input("Dari satuan (C/F/K/R): ").strip().upper()
        to_unit = input("Ke satuan (C/F/K/R): ").strip().upper()

        result = convert_temperature(value, from_unit, to_unit)

        print("\n" + "="*50)
        print("HASIL KONVERSI")
        print("="*50)
        print(f"{format_temperature(value, from_unit)} = {format_temperature(result, to_unit)}")

        if to_unit == 'C':
            category = get_temperature_category(result)
            print(f"Kategori: {category}")

        print("="*50)

    except ValueError as e:
        print(f"\nError: {e}")
    except TemperatureError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nError tidak terduga: {e}")


if __name__ == "__main__":
    main()