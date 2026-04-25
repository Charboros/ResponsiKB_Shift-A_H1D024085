import streamlit as st
import time

# Konfigurasi Halaman
st.set_page_config(page_title="MBG Expert System", page_icon="👨‍⚕️", layout="centered")

# CSS Kustom untuk Tampilan Premium
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    * { font-family: 'Outfit', sans-serif; }

    .stApp {
        background: linear-gradient(135deg, #FFF5E1 0%, #FFFFFF 100%);
    }

    .expert-card {
        background: white;
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        border: 1px solid #F1C40F;
        margin-bottom: 30px;
    }

    .header-box {
        text-align: center;
        margin-bottom: 40px;
    }

    .diagnosis-result {
        padding: 25px;
        border-radius: 15px;
        font-weight: 600;
        margin-top: 20px;
        border-left: 10px solid;
    }

    .layak { background-color: #D4EFDF; color: #1D8348; border-color: #27AE60; }
    .waspada { background-color: #FCF3CF; color: #9A7D0A; border-color: #F1C40F; }
    .bahaya { background-color: #FADBD8; color: #943126; border-color: #E74C3C; }

    .reasoning-box {
        background: #F8F9F9;
        padding: 15px;
        border-radius: 10px;
        font-size: 14px;
        margin-top: 10px;
        color: #566573;
    }
    
    .stButton>button {
        background-color: #F1C40F;
        color: white;
        border-radius: 50px;
        padding: 10px 30px;
        border: none;
        width: 100%;
        font-weight: 700;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #D4AC0D;
        box-shadow: 0 5px 15px rgba(241, 196, 15, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE SISTEM PAKAR ---

def diagnose(bau, warna, tekstur, kemasan, waktu):
    reasons = []
    status = "Sangat Layak"
    css_class = "layak"
    
    # Rule 1: Bau atau Warna Berubah (Kritikal)
    if bau == "Busuk" or warna == "Berubah (Berlendir/Jamur)":
        status = "TIDAK LAYAK (BAHAYA)"
        css_class = "bahaya"
        reasons.append("- Terdeteksi tanda pembusukan aktif pada aroma atau visual.")
    
    # Rule 2: Tekstur dan Waktu
    if status != "TIDAK LAYAK (BAHAYA)":
        if tekstur == "Lembek/Berair" or waktu == "> 8 Jam (Kemarin)":
            status = "TIDAK LAYAK (KADALUARSA)"
            css_class = "bahaya"
            reasons.append("- Tekstur sudah tidak layak atau waktu masak sudah terlalu lama.")
        
        # Rule 3: Kondisi Waspada
        elif bau == "Agak Asem" or warna == "Pucat" or kemasan == "Rusak/Penyok":
            status = "WASPADA (RESIKO TINGGI)"
            css_class = "waspada"
            if bau == "Agak Asem": reasons.append("- Aroma mulai berubah, kemungkinan fermentasi bakteri.")
            if warna == "Pucat": reasons.append("- Warna memudar, indikasi nutrisi menurun atau oksidasi.")
            if kemasan == "Rusak/Penyok": reasons.append("- Kemasan tidak utuh, resiko kontaminasi silang.")
            
        # Rule 4: Waktu tunggu moderat
        elif waktu == "4 - 8 Jam":
            status = "LAYAK DENGAN CATATAN"
            css_class = "waspada"
            reasons.append("- Makanan sudah cukup lama di suhu ruang, sebaiknya segera dikonsumsi.")

    if not reasons:
        reasons.append("- Semua parameter sensorik dalam kondisi optimal.")
        
    return status, css_class, reasons

# --- UI STREAMLIT ---

st.markdown("""
    <div class="header-box">
        <h1 style="color: #F1C40F;">👨‍⚕️ MBG Expert Diagnostic</h1>
        <p style="color: #7F8C8D;">Asisten Pakar Keamanan Makanan Bergizi Gratis</p>
    </div>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="expert-card">', unsafe_allow_html=True)
    st.subheader("📋 Observasi Fisik Makanan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bau = st.selectbox("Aroma Makanan:", ["Normal", "Agak Asem", "Busuk"])
        warna = st.selectbox("Warna Visual:", ["Segar", "Pucat", "Berubah (Berlendir/Jamur)"])
        tekstur = st.selectbox("Tekstur:", ["Padat/Normal", "Lembek/Berair"])
        
    with col2:
        kemasan = st.selectbox("Kondisi Kemasan:", ["Utuh & Rapi", "Rusak/Penyok"])
        waktu = st.selectbox("Waktu Sejak Dimasak:", ["Baru Dimasak", "4 - 8 Jam", "> 8 Jam (Kemarin)"])
        
    st.markdown("<br>", unsafe_allow_html=True)
    btn_check = st.button("MULAIDIAGNOSIS 🚀")
    
    if btn_check:
        with st.spinner('Menganalisis basis aturan pakar...'):
            time.sleep(1.5)
            res_status, res_class, res_reasons = diagnose(bau, warna, tekstur, kemasan, waktu)
            
            st.markdown(f"""
                <div class="diagnosis-result {res_class}">
                    HASIL DIAGNOSIS: {res_status}
                </div>
                <div class="reasoning-box">
                    <strong>Analisis Pakar:</strong><br>
                    {"<br>".join(res_reasons)}
                </div>
            """, unsafe_allow_html=True)
            
            if res_class == "layak":
                st.balloons()
            elif res_class == "bahaya":
                st.error("TINDAKAN: Jangan dibagikan! Segera buang makanan ini sesuai prosedur limbah.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Responsi Praktikum KB - Afkar Aufaa Farros (H1D024085) - Shift A © 2026")
