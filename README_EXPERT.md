# 👨‍⚕️ Sistem Pakar - Diagnosis Keamanan MBG

Sistem ini merupakan implementasi **Sistem Pakar (Rule-Based)** yang meniru pengetahuan seorang pakar nutrisi atau pengawas pangan dalam menentukan kelayakan konsumsi sebuah hidangan.

## 🧠 Basis Pengetahuan (Knowledge Base)
Sistem menggunakan metode **Forward Chaining** untuk memproses observasi sensorik:

- **Bau**: Normal, Agak Asem, Busuk.
- **Warna**: Segar, Pucat, Berubah (Lendir/Jamur).
- **Tekstur**: Padat/Normal, Lembek/Berair.
- **Kemasan**: Utuh, Rusak/Penyok.
- **Waktu**: Baru Dimasak, 4-8 Jam, > 8 Jam.

## 📜 Contoh Aturan (Rules)
- **R1**: IF Bau = "Busuk" OR Warna = "Berubah", THEN Status = "Bahaya/Tidak Layak".
- **R2**: IF Bau = "Agak Asem" AND Waktu = "4-8 Jam", THEN Status = "Waspada".
- **R3**: IF Semua parameter Normal, THEN Status = "Sangat Layak".

## 🖥️ Fitur Antarmuka
- **Diagnostic Wizard**: Langkah-demi-langkah pemilihan kondisi makanan.
- **Reasoning Box**: Penjelasan mengapa sistem memberikan diagnosis tertentu.
- **Pesan Aksi**: Memberikan instruksi tindakan (misal: "Segera Buang" atau "Segera Konsumsi").

## 🏃 Cara Menjalankan
```bash
streamlit run expert_system.py
```
