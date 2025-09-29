"""
Unit Testing untuk Modul Konversi Suhu
Comprehensive test coverage untuk semua fungsi
"""

import pytest
import SuhuConverter as tc


# === TEST CELSIUS TO FAHRENHEIT ===

class TestCelsiusToFahrenheit:
    """Test konversi Celsius ke Fahrenheit"""

    def test_freezing_point(self):
        """Test titik beku air (0°C = 32°F)"""
        assert tc.celsius_to_fahrenheit(0) == 32

    def test_boiling_point(self):
        """Test titik didih air (100°C = 212°F)"""
        assert tc.celsius_to_fahrenheit(100) == 212

    def test_negative_temperature(self):
        """Test suhu negatif"""
        assert tc.celsius_to_fahrenheit(-40) == -40

    def test_room_temperature(self):
        """Test suhu ruangan (25°C)"""
        result = tc.celsius_to_fahrenheit(25)
        assert result == pytest.approx(77, abs=0.1)

    def test_absolute_zero(self):
        """Test absolute zero (-273.15°C)"""
        result = tc.celsius_to_fahrenheit(-273.15)
        assert result == pytest.approx(-459.67, abs=0.1)

    def test_below_absolute_zero(self):
        """Test suhu di bawah absolute zero (harus error)"""
        with pytest.raises(tc.TemperatureError):
            tc.celsius_to_fahrenheit(-300)

    def test_decimal_values(self):
        """Test dengan nilai desimal"""
        result = tc.celsius_to_fahrenheit(36.5)
        assert result == pytest.approx(97.7, abs=0.1)


# === TEST FAHRENHEIT TO CELSIUS ===

class TestFahrenheitToCelsius:
    """Test konversi Fahrenheit ke Celsius"""

    def test_freezing_point(self):
        """Test titik beku air (32°F = 0°C)"""
        result = tc.fahrenheit_to_celsius(32)
        assert result == pytest.approx(0, abs=0.1)

    def test_boiling_point(self):
        """Test titik didih air (212°F = 100°C)"""
        result = tc.fahrenheit_to_celsius(212)
        assert result == pytest.approx(100, abs=0.1)

    def test_negative_temperature(self):
        """Test suhu negatif"""
        result = tc.fahrenheit_to_celsius(-40)
        assert result == pytest.approx(-40, abs=0.1)

    def test_body_temperature(self):
        """Test suhu tubuh normal (98.6°F ≈ 37°C)"""
        result = tc.fahrenheit_to_celsius(98.6)
        assert result == pytest.approx(37, abs=0.1)

    def test_absolute_zero(self):
        """Test absolute zero (-459.67°F)"""
        result = tc.fahrenheit_to_celsius(-459.67)
        assert result == pytest.approx(-273.15, abs=0.1)

    def test_below_absolute_zero(self):
        """Test suhu di bawah absolute zero (harus error)"""
        with pytest.raises(tc.TemperatureError):
            tc.fahrenheit_to_celsius(-500)


# === TEST CELSIUS TO KELVIN ===

class TestCelsiusToKelvin:
    """Test konversi Celsius ke Kelvin"""

    def test_absolute_zero(self):
        """Test absolute zero (-273.15°C = 0K)"""
        assert tc.celsius_to_kelvin(-273.15) == 0

    def test_freezing_point(self):
        """Test titik beku air (0°C = 273.15K)"""
        assert tc.celsius_to_kelvin(0) == 273.15

    def test_boiling_point(self):
        """Test titik didih air (100°C = 373.15K)"""
        assert tc.celsius_to_kelvin(100) == 373.15

    def test_room_temperature(self):
        """Test suhu ruangan (25°C)"""
        result = tc.celsius_to_kelvin(25)
        assert result == pytest.approx(298.15, abs=0.1)

    def test_below_absolute_zero(self):
        """Test suhu di bawah absolute zero (harus error)"""
        with pytest.raises(tc.TemperatureError):
            tc.celsius_to_kelvin(-300)


# === TEST KELVIN TO CELSIUS ===

class TestKelvinToCelsius:
    """Test konversi Kelvin ke Celsius"""

    def test_absolute_zero(self):
        """Test absolute zero (0K = -273.15°C)"""
        assert tc.kelvin_to_celsius(0) == -273.15

    def test_freezing_point(self):
        """Test titik beku air (273.15K = 0°C)"""
        result = tc.kelvin_to_celsius(273.15)
        assert result == pytest.approx(0, abs=0.1)

    def test_boiling_point(self):
        """Test titik didih air (373.15K = 100°C)"""
        result = tc.kelvin_to_celsius(373.15)
        assert result == pytest.approx(100, abs=0.1)

    def test_negative_kelvin(self):
        """Test nilai Kelvin negatif (harus error)"""
        with pytest.raises(tc.TemperatureError):
            tc.kelvin_to_celsius(-10)


# === TEST FAHRENHEIT TO KELVIN ===

class TestFahrenheitToKelvin:
    """Test konversi Fahrenheit ke Kelvin"""

    def test_freezing_point(self):
        """Test titik beku air (32°F)"""
        result = tc.fahrenheit_to_kelvin(32)
        assert result == pytest.approx(273.15, abs=0.1)

    def test_boiling_point(self):
        """Test titik didih air (212°F)"""
        result = tc.fahrenheit_to_kelvin(212)
        assert result == pytest.approx(373.15, abs=0.1)


# === TEST KELVIN TO FAHRENHEIT ===

class TestKelvinToFahrenheit:
    """Test konversi Kelvin ke Fahrenheit"""

    def test_freezing_point(self):
        """Test titik beku air (273.15K)"""
        result = tc.kelvin_to_fahrenheit(273.15)
        assert result == pytest.approx(32, abs=0.1)

    def test_boiling_point(self):
        """Test titik didih air (373.15K)"""
        result = tc.kelvin_to_fahrenheit(373.15)
        assert result == pytest.approx(212, abs=0.1)


# === TEST REAMUR CONVERSIONS ===

class TestReamurConversions:
    """Test konversi Reamur"""

    def test_celsius_to_reamur_freezing(self):
        """Test 0°C = 0°R"""
        assert tc.celsius_to_reamur(0) == 0

    def test_celsius_to_reamur_boiling(self):
        """Test 100°C = 80°R"""
        assert tc.celsius_to_reamur(100) == 80

    def test_reamur_to_celsius_freezing(self):
        """Test 0°R = 0°C"""
        assert tc.reamur_to_celsius(0) == 0

    def test_reamur_to_celsius_boiling(self):
        """Test 80°R = 100°C"""
        assert tc.reamur_to_celsius(80) == 100

    def test_celsius_to_reamur_negative(self):
        """Test suhu negatif"""
        assert tc.celsius_to_reamur(-10) == -8

    def test_reamur_below_absolute_zero(self):
        """Test Reamur di bawah absolute zero"""
        with pytest.raises(tc.TemperatureError):
            tc.reamur_to_celsius(-250)


# === TEST CONVERT TEMPERATURE (UNIVERSAL) ===

class TestConvertTemperature:
    """Test fungsi konversi universal"""

    def test_celsius_to_fahrenheit(self):
        """Test C ke F"""
        result = tc.convert_temperature(0, 'C', 'F')
        assert result == 32

    def test_fahrenheit_to_celsius(self):
        """Test F ke C"""
        result = tc.convert_temperature(32, 'F', 'C')
        assert result == pytest.approx(0, abs=0.1)

    def test_celsius_to_kelvin(self):
        """Test C ke K"""
        result = tc.convert_temperature(0, 'C', 'K')
        assert result == 273.15

    def test_celsius_to_reamur(self):
        """Test C ke R"""
        result = tc.convert_temperature(100, 'C', 'R')
        assert result == 80

    def test_same_unit(self):
        """Test konversi ke satuan yang sama"""
        result = tc.convert_temperature(25, 'C', 'C')
        assert result == 25

    def test_case_insensitive(self):
        """Test case insensitive"""
        result1 = tc.convert_temperature(0, 'c', 'f')
        result2 = tc.convert_temperature(0, 'C', 'F')
        assert result1 == result2

    def test_with_spaces(self):
        """Test dengan spasi"""
        result = tc.convert_temperature(0, ' C ', ' F ')
        assert result == 32

    def test_invalid_from_unit(self):
        """Test satuan asal tidak valid"""
        with pytest.raises(ValueError):
            tc.convert_temperature(0, 'X', 'C')

    def test_invalid_to_unit(self):
        """Test satuan tujuan tidak valid"""
        with pytest.raises(ValueError):
            tc.convert_temperature(0, 'C', 'X')

    def test_fahrenheit_to_kelvin_via_convert(self):
        """Test F ke K melalui fungsi universal"""
        result = tc.convert_temperature(32, 'F', 'K')
        assert result == pytest.approx(273.15, abs=0.1)

    def test_kelvin_to_reamur_via_convert(self):
        """Test K ke R melalui fungsi universal"""
        result = tc.convert_temperature(273.15, 'K', 'R')
        assert result == pytest.approx(0, abs=0.1)


# === TEST TEMPERATURE CATEGORY ===

class TestGetTemperatureCategory:
    """Test kategori suhu"""

    def test_very_cold_extreme(self):
        """Test kategori sangat dingin ekstrim"""
        assert tc.get_temperature_category(-100) == "Sangat Dingin Ekstrim"

    def test_very_cold(self):
        """Test kategori sangat dingin"""
        assert tc.get_temperature_category(-10) == "Sangat Dingin"

    def test_cold(self):
        """Test kategori dingin"""
        assert tc.get_temperature_category(5) == "Dingin"

    def test_cool(self):
        """Test kategori sejuk"""
        assert tc.get_temperature_category(15) == "Sejuk"

    def test_warm(self):
        """Test kategori hangat"""
        assert tc.get_temperature_category(25) == "Hangat"

    def test_hot(self):
        """Test kategori panas"""
        assert tc.get_temperature_category(35) == "Panas"

    def test_very_hot(self):
        """Test kategori sangat panas"""
        assert tc.get_temperature_category(45) == "Sangat Panas"

    def test_below_absolute_zero_category(self):
        """Test kategori di bawah absolute zero"""
        with pytest.raises(tc.TemperatureError):
            tc.get_temperature_category(-300)


# === TEST SPECIAL POINTS ===

class TestSpecialPoints:
    """Test pengecekan titik khusus"""

    def test_is_freezing_point_exact(self):
        """Test titik beku tepat"""
        assert tc.is_freezing_point(0) == True

    def test_is_freezing_point_close(self):
        """Test mendekati titik beku"""
        assert tc.is_freezing_point(0.05) == True
        assert tc.is_freezing_point(-0.05) == True

    def test_is_not_freezing_point(self):
        """Test bukan titik beku"""
        assert tc.is_freezing_point(5) == False

    def test_is_boiling_point_exact(self):
        """Test titik didih tepat"""
        assert tc.is_boiling_point(100) == True

    def test_is_boiling_point_close(self):
        """Test mendekati titik didih"""
        assert tc.is_boiling_point(100.05) == True
        assert tc.is_boiling_point(99.95) == True

    def test_is_not_boiling_point(self):
        """Test bukan titik didih"""
        assert tc.is_boiling_point(95) == False

    def test_custom_tolerance(self):
        """Test dengan toleransi custom"""
        assert tc.is_freezing_point(0.5, tolerance=0.5) == True
        assert tc.is_freezing_point(0.5, tolerance=0.1) == False


# === TEST FORMAT TEMPERATURE ===

class TestFormatTemperature:
    """Test formatting suhu"""

    def test_format_celsius(self):
        """Test format Celsius"""
        assert tc.format_temperature(25.5, 'C') == "25.50°C"

    def test_format_fahrenheit(self):
        """Test format Fahrenheit"""
        assert tc.format_temperature(77.5, 'F') == "77.50°F"

    def test_format_kelvin(self):
        """Test format Kelvin"""
        assert tc.format_temperature(298.15, 'K') == "298.15K"

    def test_format_reamur(self):
        """Test format Reamur"""
        assert tc.format_temperature(20, 'R') == "20.00°R"

    def test_format_custom_decimal(self):
        """Test format dengan desimal custom"""
        assert tc.format_temperature(25.12345, 'C', 1) == "25.1°C"
        assert tc.format_temperature(25.12345, 'C', 3) == "25.123°C"

    def test_format_invalid_unit(self):
        """Test format dengan satuan tidak valid"""
        with pytest.raises(ValueError):
            tc.format_temperature(25, 'X')

    def test_format_case_insensitive(self):
        """Test format case insensitive"""
        assert tc.format_temperature(25, 'c') == "25.00°C"
        assert tc.format_temperature(25, 'C') == "25.00°C"


# === INTEGRATION TESTS ===

class TestIntegration:
    """Test integrasi antar fungsi"""

    def test_round_trip_celsius_fahrenheit(self):
        """Test konversi bolak-balik C->F->C"""
        original = 25
        fahrenheit = tc.celsius_to_fahrenheit(original)
        back_to_celsius = tc.fahrenheit_to_celsius(fahrenheit)
        assert back_to_celsius == pytest.approx(original, abs=0.001)

    def test_round_trip_celsius_kelvin(self):
        """Test konversi bolak-balik C->K->C"""
        original = 25
        kelvin = tc.celsius_to_kelvin(original)
        back_to_celsius = tc.kelvin_to_celsius(kelvin)
        assert back_to_celsius == pytest.approx(original, abs=0.001)

    def test_round_trip_celsius_reamur(self):
        """Test konversi bolak-balik C->R->C"""
        original = 100
        reamur = tc.celsius_to_reamur(original)
        back_to_celsius = tc.reamur_to_celsius(reamur)
        assert back_to_celsius == pytest.approx(original, abs=0.001)

    def test_multiple_conversions(self):
        """Test konversi berantai C->F->K->C"""
        original = 20
        f = tc.convert_temperature(original, 'C', 'F')
        k = tc.convert_temperature(f, 'F', 'K')
        back = tc.convert_temperature(k, 'K', 'C')
        assert back == pytest.approx(original, abs=0.001)

    def test_category_after_conversion(self):
        """Test kategori setelah konversi"""
        fahrenheit = 77
        celsius = tc.fahrenheit_to_celsius(fahrenheit)
        category = tc.get_temperature_category(celsius)
        assert category == "Hangat"


# === EDGE CASES & BOUNDARY TESTS ===

class TestEdgeCases:
    """Test edge cases dan boundary values"""

    def test_zero_values(self):
        """Test nilai nol"""
        assert tc.celsius_to_fahrenheit(0) == 32
        assert tc.celsius_to_kelvin(0) == 273.15
        assert tc.celsius_to_reamur(0) == 0

    def test_very_large_values(self):
        """Test nilai sangat besar"""
        result = tc.celsius_to_fahrenheit(1000)
        assert result == 1832

    def test_very_small_decimals(self):
        """Test desimal sangat kecil"""
        result = tc.celsius_to_fahrenheit(0.001)
        assert result == pytest.approx(32.0018, abs=0.0001)

    def test_negative_zero(self):
        """Test negative zero"""
        result = tc.celsius_to_fahrenheit(-0.0)
        assert result == 32.0


# === PARAMETRIZED TESTS ===

class TestParametrized:
    """Test dengan data parametrized"""

    @pytest.mark.parametrize("celsius,fahrenheit", [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
        (25, 77),
    ])
    def test_celsius_to_fahrenheit_parametrized(self, celsius, fahrenheit):
        """Test berbagai nilai C ke F"""
        result = tc.celsius_to_fahrenheit(celsius)
        assert result == pytest.approx(fahrenheit, abs=0.1)

    @pytest.mark.parametrize("celsius,kelvin", [
        (0, 273.15),
        (100, 373.15),
        (-273.15, 0),
        (25, 298.15),
    ])
    def test_celsius_to_kelvin_parametrized(self, celsius, kelvin):
        """Test berbagai nilai C ke K"""
        result = tc.celsius_to_kelvin(celsius)
        assert result == pytest.approx(kelvin, abs=0.1)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])