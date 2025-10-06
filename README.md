# Temperature Converter System - Versi Sederhana

Sistem konversi suhu sederhana yang mendukung 3 satuan suhu: **Celsius (°C)**, **Fahrenheit (°F)**, dan **Kelvin (K)**.

## Fitur Utama

- ✅ Konversi antar 3 satuan suhu utama
- ✅ Interface command line yang mudah digunakan
- ✅ Kategori suhu otomatis untuk Celsius
- ✅ Format output yang rapi
- ✅ Input validation sederhana

## Satuan Suhu yang Didukung

| Satuan | Simbol | Deskripsi |
|--------|--------|-----------|
| Celsius | C | Satuan suhu standar internasional |
| Fahrenheit | F | Satuan suhu yang umum di Amerika |
| Kelvin | K | Satuan suhu absolut dalam sains |

## Formula Konversi

### Celsius ↔ Fahrenheit
- **C ke F**: `F = (C × 9/5) + 32`
- **F ke C**: `C = (F - 32) × 5/9`

### Celsius ↔ Kelvin
- **C ke K**: `K = C + 273.15`
- **K ke C**: `C = K - 273.15`

### Fahrenheit ↔ Kelvin
- **F ke K**: `F → C → K`
- **K ke F**: `K → C → F`

## Cara Penggunaan

### 1. Menjalankan Program
```bash
python SuhuConverter.py
```

### 2. Input Data
- Masukkan nilai suhu (angka)
- Pilih satuan asal (C/F/K)
- Pilih satuan tujuan (C/F/K)

### 3. Contoh Penggunaan
```
Masukkan nilai suhu: 100
Dari satuan (C/F/K): C
Ke satuan (C/F/K): F

Hasil: 100.00°C = 212.00°F
Kategori: Sangat Panas
```

## Kategori Suhu (Celsius)

| Range Suhu | Kategori |
|------------|----------|
| < -50°C | Sangat Dingin Ekstrim |
| -50°C hingga 0°C | Sangat Dingin |
| 0°C hingga 10°C | Dingin |
| 10°C hingga 20°C | Sejuk |
| 20°C hingga 30°C | Hangat |
| 30°C hingga 40°C | Panas |
| > 40°C | Sangat Panas |

## Contoh Konversi

| Dari | Ke | Hasil |
|------|-------|-------|
| 0°C | 32°F | Titik beku air |
| 100°C | 212°F | Titik didih air |
| 25°C | 77°F | Suhu ruangan |
| 37°C | 98.6°F | Suhu tubuh normal |
| 273.15K | 0°C | Titik beku dalam Kelvin |

## Error Handling

Program akan menampilkan pesan error untuk:
- Input bukan angka
- Satuan tidak valid (selain C, F, K)
- Error sistem lainnya

## Keluar dari Program

Ketik salah satu dari:
- `keluar`
- `exit`
- `quit`

## File Struktur

```
SuhuConverter/
├── SuhuConverter.py          # Program utama
├── README.md                 # Dokumentasi
└── requirements.txt          # Dependencies (jika ada)
```

## Requirements

- Python 3.6 atau lebih baru
- Tidak memerlukan library eksternal

## Pengembangan

Versi sederhana ini menghilangkan:
- ❌ Satuan Reamur
- ❌ Validasi absolute zero
- ❌ Fungsi freezing/boiling point
- ❌ Database dan autentikasi
- ❌ Kompleksitas yang tidak perlu

Fokus pada:
- ✅ Konversi 3 satuan utama
- ✅ Interface sederhana
- ✅ Performa cepat
- ✅ Mudah dipahami

---

**Dibuat untuk pembelajaran dan penggunaan praktis konversi suhu sehari-hari.**
