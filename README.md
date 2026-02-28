# Parallel Sum di Python

Repositori ini berisi implementasi dari komputasi paralel untuk melakukan penjumlahan angka (Parallel Sum) menggunakan bahasa Python. Kode ini membandingkan pendekatan penjumlahan secara serial dan paralel.

## Konsep yang Digunakan

- **`multiprocessing.Process`**: Digunakan untuk memecah tugas penjumlahan menjadi beberapa proses yang berjalan secara bersamaan (konkuren).
- **`multiprocessing.Queue`**: Digunakan sebagai struktur data antrean untuk mengumpulkan hasil perhitungan (partial sum) dari masing-masing proses agar bisa dijumlahkan di akhir.

## Cara Kerja

Tugas utamanya adalah menjumlahkan angka 1 sampai 5.
Beban kerja dipecah menjadi dua:

1. **Proses 1**: Menjumlahkan angka 1, 2, dan 3.
2. **Proses 2**: Menjumlahkan angka 4 dan 5.
   Kedua proses berjalan bersamaan, lalu hasilnya digabungkan di akhir menghasilkan total akhir.

## Cara Menjalankan

Jalankan perintah berikut di terminal:

```bash
python main.py
```
