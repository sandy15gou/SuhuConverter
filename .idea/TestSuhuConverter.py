import pytest
from SuhuConverter import (
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
    fahrenheit_ke_celsius,
    fahrenheit_ke_kelvin,
    kelvin_ke_celsius,
    kelvin_ke_fahrenheit
)

class TestCelsiusKonversi:
    def test_celsius_ke_fahrenheit(self):
        assert celsius_ke_fahrenheit(0) == 32
        assert celsius_ke_fahrenheit(100) == 212
        assert celsius_ke_fahrenheit(-40) == -40
        assert round(celsius_ke_fahrenheit(37), 2) == 98.6

    def test_celsius_ke_kelvin(self):
        assert celsius_ke_kelvin(0) == 273.15
        assert celsius_ke_kelvin(100) == 373.15
        assert celsius_ke_kelvin(-273.15) == 0

class TestFahrenheitKonversi:
    def test_fahrenheit_ke_celsius(self):
        assert fahrenheit_ke_celsius(32) == 0
        assert fahrenheit_ke_celsius(212) == 100
        assert fahrenheit_ke_celsius(-40) == -40
        assert round(fahrenheit_ke_celsius(98.6), 1) == 37.0

    def test_fahrenheit_ke_kelvin(self):
        assert fahrenheit_ke_kelvin(32) == 273.15
        assert round(fahrenheit_ke_kelvin(212), 2) == 373.15
        assert fahrenheit_ke_kelvin(-40) == pytest.approx(233.15)

class TestKelvinKonversi:
    def test_kelvin_ke_celsius(self):
        assert kelvin_ke_celsius(273.15) == 0
        assert kelvin_ke_celsius(373.15) == 100
        assert kelvin_ke_celsius(0) == -273.15

    def test_kelvin_ke_fahrenheit(self):
        assert kelvin_ke_fahrenheit(273.15) == 32
        assert kelvin_ke_fahrenheit(373.15) == 212
        assert kelvin_ke_fahrenheit(233.15) == pytest.approx(-40)

class TestKonversiDuaArah:
    def test_celsius_fahrenheit_bolak_balik(self):
        nilai = 25
        hasil = fahrenheit_ke_celsius(celsius_ke_fahrenheit(nilai))
        assert round(hasil, 2) == nilai

    def test_celsius_kelvin_bolak_balik(self):
        nilai = 50
        hasil = kelvin_ke_celsius(celsius_ke_kelvin(nilai))
        assert round(hasil, 2) == nilai

    def test_fahrenheit_kelvin_bolak_balik(self):
        nilai = 77
        hasil = kelvin_ke_fahrenheit(fahrenheit_ke_kelvin(nilai))
        assert round(hasil, 2) == nilai