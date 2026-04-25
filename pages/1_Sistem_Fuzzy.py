import streamlit as st
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="MBG Fuzzy Quality", page_icon="🥗", layout="wide")

# CSS Kustom untuk Tampilan Premium
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    * { font-family: 'Outfit', sans-serif; }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .stApp {
        background-color: #ffffff;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
        margin-top: 20px;
    }

    .score-text {
        font-size: 64px;
        font-weight: 700;
        color: #2ECC71;
        margin: 10px 0;
    }

    .status-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .status-premium { background-color: #D4EFDF; color: #1D8348; }
    .status-standar { background-color: #FEF5E7; color: #AF601A; }
    .status-rendah { background-color: #FADBD8; color: #943126; }

    h1, h2, h3 { color: #2C3E50; }
    
    .stSlider > div > div > div > div {
        background-color: #2ECC71;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE LOGIKA FUZZY ---

# 1. Definisi Variabel (Antecedents & Consequent)
kesegaran = ctrl.Antecedent(np.arange(0, 11, 1), 'kesegaran')
nutrisi = ctrl.Antecedent(np.arange(0, 11, 1), 'nutrisi')
kebersihan = ctrl.Antecedent(np.arange(0, 11, 1), 'kebersihan')
kualitas = ctrl.Consequent(np.arange(0, 101, 1), 'kualitas')

# 2. Fungsi Keanggotaan (Membership Functions)
kesegaran['Buruk'] = fuzzy.trimf(kesegaran.universe, [0, 0, 5])
kesegaran['Sedang'] = fuzzy.trimf(kesegaran.universe, [3, 5, 8])
kesegaran['Baik'] = fuzzy.trimf(kesegaran.universe, [6, 10, 10])

nutrisi['Rendah'] = fuzzy.trimf(nutrisi.universe, [0, 0, 5])
nutrisi['Cukup'] = fuzzy.trimf(nutrisi.universe, [3, 5, 8])
nutrisi['Tinggi'] = fuzzy.trimf(nutrisi.universe, [6, 10, 10])

kebersihan['Kotor'] = fuzzy.trimf(kebersihan.universe, [0, 0, 5])
kebersihan['Bersih'] = fuzzy.trimf(kebersihan.universe, [3, 5, 8])
kebersihan['Sangat Bersih'] = fuzzy.trimf(kebersihan.universe, [6, 10, 10])

kualitas['Rendah'] = fuzzy.trimf(kualitas.universe, [0, 0, 40])
kualitas['Standar'] = fuzzy.trimf(kualitas.universe, [30, 60, 90])
kualitas['Premium'] = fuzzy.trimf(kualitas.universe, [70, 100, 100])

# 3. Aturan Fuzzy (Rule Base)
rule1 = ctrl.Rule(kesegaran['Buruk'] | kebersihan['Kotor'], kualitas['Rendah'])
rule2 = ctrl.Rule(nutrisi['Rendah'], kualitas['Rendah'])
rule3 = ctrl.Rule(kesegaran['Baik'] & nutrisi['Tinggi'] & kebersihan['Sangat Bersih'], kualitas['Premium'])
rule4 = ctrl.Rule(kesegaran['Sedang'] & nutrisi['Cukup'] & kebersihan['Bersih'], kualitas['Standar'])
rule5 = ctrl.Rule(kesegaran['Baik'] & nutrisi['Cukup'], kualitas['Standar'])
rule6 = ctrl.Rule(kesegaran['Sedang'] & nutrisi['Tinggi'], kualitas['Standar'])
rule7 = ctrl.Rule(kebersihan['Sangat Bersih'] & kesegaran['Baik'], kualitas['Premium'])

# 4. Sistem Kontrol
kualitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
kualitas_sim = ctrl.ControlSystemSimulation(kualitas_ctrl)

# --- UI STREAMLIT ---

st.title("🥗 MBG Fuzzy Quality Checker")
st.markdown("Sistem Logika Fuzzy untuk Menilai Kualitas Makanan Bergizi Gratis")

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("📊 Input Parameter")
    val_kesegaran = st.slider("Tingkat Kesegaran (Aroma & Tekstur)", 0, 10, 6)
    val_nutrisi = st.slider("Kandungan Nutrisi (Kelengkapan Lauk)", 0, 10, 4)
    val_kebersihan = st.slider("Kebersihan Penyajian (Wadah & Proses)", 0, 10, 7)

    st.info("💡 Geser slider untuk menyesuaikan kondisi makanan yang diamati.")

# Perhitungan
kualitas_sim.input['kesegaran'] = val_kesegaran
kualitas_sim.input['nutrisi'] = val_nutrisi
kualitas_sim.input['kebersihan'] = val_kebersihan
kualitas_sim.compute()

skor_kualitas = kualitas_sim.output['kualitas']

# Menentukan Status & Pesan
if skor_kualitas >= 75:
    status = "PREMIUM"
    badge_class = "status-premium"
    msg = "Makanan sangat layak untuk didistribusikan kepada siswa. Kualitas terjaga dengan sangat baik!"
elif skor_kualitas >= 45:
    status = "STANDAR"
    badge_class = "status-standar"
    msg = "Makanan dalam kondisi cukup baik, namun perlu diperhatikan lagi aspek penyajiannya."
else:
    status = "RENDAH"
    badge_class = "status-rendah"
    msg = "⚠️ Makanan tidak direkomendasikan untuk didistribusikan. Segera cek kembali unit penyedia."

with col2:
    st.markdown(f"""
        <div class="result-card">
            <div class="status-badge {badge_class}">{status}</div>
            <div style="color: #7F8C8D; font-size: 16px;">Skor Kualitas MBG</div>
            <div class="score-text">{skor_kualitas:.1f}%</div>
            <p style="color: #34495E; font-size: 18px; line-height: 1.5;">{msg}</p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("📈 Lihat Grafik Logika Fuzzy"):
        fig, ax = plt.subplots(figsize=(10, 4))
        for label in kualitas.terms:
            ax.plot(kualitas.universe, kualitas[label].mf, label=label, linewidth=2)
        ax.axvline(x=skor_kualitas, color='red', linestyle='--', label=f'Skor: {skor_kualitas:.1f}')
        ax.set_title('Distribusi Kualitas Makanan (Logika Fuzzy)')
        ax.set_xlabel('Skor (0-100)')
        ax.set_ylabel('Derajat Keanggotaan')
        ax.legend()
        st.pyplot(fig)

st.markdown("---")
st.caption("Responsi Praktikum KB - MBG System © 2026")
