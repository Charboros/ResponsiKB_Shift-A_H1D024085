# 🧠 Sistem Logika Fuzzy - Kualitas Makanan MBG

Sistem ini menggunakan **Logika Fuzzy (Mamdani)** untuk mengevaluasi kualitas makanan berdasarkan parameter yang bersifat subjektif menjadi nilai kuantitatif (persentase).

## 🛠️ Spesifikasi Sistem
Sistem ini dibangun menggunakan library `scikit-fuzzy` dengan komponen sebagai berikut:

### 1. Variabel Input (Antecedents)
- **Kesegaran** (0-10): Buruk, Sedang, Baik.
- **Kandungan Nutrisi** (0-10): Rendah, Cukup, Tinggi.
- **Kebersihan Penyajian** (0-10): Kotor, Bersih, Sangat Bersih.

### 2. Variabel Output (Consequent)
- **Skor Kualitas** (0-100%): Rendah, Standar, Premium.

### 3. Aturan Fuzzy (Beberapa Contoh)
- JIKA Kesegaran **Buruk** ATAU Kebersihan **Kotor**, MAKA Kualitas **Rendah**.
- JIKA Kesegaran **Baik** DAN Nutrisi **Tinggi** DAN Kebersihan **Sangat Bersih**, MAKA Kualitas **Premium**.

## 🖥️ Fitur Antarmuka
- **Slider Interaktif**: Memudahkan pengguna menginput data observasi.
- **Visualisasi Grafik**: Menampilkan fungsi keanggotaan dan hasil defuzzifikasi secara real-time.
- **Badge Status**: Memberikan label instan (Premium/Standar/Rendah).

## 🏃 Cara Menjalankan
```bash
streamlit run fuzzy_system.py
```
