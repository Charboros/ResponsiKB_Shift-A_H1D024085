import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="MBG Portal - Responsi KB", page_icon="🍱", layout="centered")

# CSS Kustom
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    * { font-family: 'Outfit', sans-serif; }
    
    .main-header {
        text-align: center;
        padding: 50px 0;
        background: linear-gradient(135deg, #2ECC71 0%, #27AE60 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 30px;
    }

    .card-container {
        display: flex;
        gap: 20px;
        margin-top: 20px;
    }

    .info-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border: 1px solid #EAEAEA;
        flex: 1;
    }

    .info-card h3 { color: #27AE60; margin-top: 0; }
    </style>
    """, unsafe_allow_html=True)

# UI Konten
st.markdown("""
    <div class="main-header">
        <h1>🍱 MBG Quality Portal</h1>
        <p>Sistem Pemantauan Makanan Bergizi Gratis - Responsi KB</p>
    </div>
""", unsafe_allow_html=True)

st.write("### Selamat Datang!")
st.write("""
Aplikasi ini dirancang untuk memastikan kualitas dan keamanan makanan dalam program 
**Makan Bergizi Gratis (MBG)**. Silakan pilih sistem yang ingin Anda gunakan melalui 
sidebar di sebelah kiri:
""")

st.markdown("""
<div class="card-container">
    <div class="info-card">
        <h3>🧠 Sistem Fuzzy</h3>
        <p>Digunakan untuk menghitung <b>Skor Kualitas</b> makanan (0-100%) berdasarkan parameter kontinu seperti kesegaran dan nutrisi.</p>
    </div>
    <div class="info-card">
        <h3>👨‍⚕️ Sistem Pakar</h3>
        <p>Digunakan untuk melakukan <b>Diagnosis Keamanan</b> berdasarkan aturan pakar terkait bau, warna, dan kondisi fisik makanan.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.info("👈 Pilih menu di samping untuk memulai analisis.")

st.markdown("---")
st.caption("Responsi Praktikum KB - Shift A - H1D024085 © 2026")
