# Skenario Pengujian Fungsional dan Non-Fungsional
## Temperature Converter System

---

## 1. Functional Testing

| No | Fitur yang Diuji | Skenario Uji | Input | Output yang Diharapkan |
|----|------------------|--------------|-------|------------------------|
| F1 | Konversi Celsius ke Fahrenheit | Masukkan nilai Celsius valid dan konversi ke Fahrenheit | 100 / C / F | "100.00°C = 212.00°F" + Kategori: Sangat Panas |
| F2 | Konversi Fahrenheit ke Celsius | Masukkan nilai Fahrenheit valid dan konversi ke Celsius | 32 / F / C | "32.00°F = 0.00°C" + Kategori: Sejuk |
| F3 | Konversi Celsius ke Kelvin | Masukkan nilai Celsius valid dan konversi ke Kelvin | 0 / C / K | "0.00°C = 273.15K" |
| F4 | Konversi Celsius ke Reamur | Masukkan nilai Celsius valid dan konversi ke Reamur | 100 / C / R | "100.00°C = 80.00°R" |
| F5 | Input Bukan Angka | Masukkan karakter non-numerik sebagai nilai suhu | abc / C / F | Peringatan: "Input harus berupa angka! Contoh: 100, 25.5, -40" |
| F6 | Input Satuan Invalid | Masukkan satuan yang tidak tersedia | 100 / X / F | Error: "Satuan asal tidak valid: X. Gunakan: C, F, K, atau R" |
| F7 | Suhu Di Bawah Absolute Zero (Celsius) | Masukkan suhu -300°C | -300 / C / F | Error: "Suhu tidak boleh di bawah absolute zero (-273.15°C)" |
| F8 | Suhu Di Bawah Absolute Zero (Fahrenheit) | Masukkan suhu -500°F | -500 / F / C | Error: "Suhu tidak boleh di bawah absolute zero (-459.67°F)" |
| F9 | Suhu Di Bawah Absolute Zero (Kelvin) | Masukkan suhu -10K | -10 / K / C | Error: "Suhu tidak boleh di bawah 0 Kelvin (absolute zero)" |
| F10 | Konversi Satuan yang Sama | Konversi dari Celsius ke Celsius | 25 / C / C | "25.00°C = 25.00°C" + Kategori: Hangat |
| F11 | Input Nilai Negatif Valid | Masukkan suhu negatif yang masih di atas absolute zero | -40 / C / F | "-40.00°C = -40.00°F" |
| F12 | Input Desimal | Masukkan nilai suhu dengan desimal | 36.5 / C / F | "36.50°C = 97.70°F" |
| F13 | Keluar dari Program | Ketik 'keluar' untuk menghentikan program | keluar | "Terima kasih telah menggunakan program konversi suhu!" |
| F14 | Case Insensitive Satuan | Masukkan satuan dengan huruf kecil | 100 / c / f | "100.00°C = 212.00°F" (berfungsi normal) |
| F15 | Konversi Berantai (F→K) | Konversi Fahrenheit ke Kelvin | 212 / F / K | "212.00°F = 373.15K" |

