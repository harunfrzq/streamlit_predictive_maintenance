import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Predictive Maintenance App", layout="wide")

# 2. Load Model
@st.cache_resource
def load_model():
    # Pastikan file model_final.pkl ada di folder yang sama
    return joblib.load("model_final.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop()

# 3. Header
st.title("🏭 Mesin Predictive Maintenance")
st.markdown("""
Aplikasi ini memprediksi apakah mesin akan mengalami **Failure (Kerusakan)** atau **Normal** berdasarkan data sensor (metric1 - metric9).
""")

# 4. Sidebar untuk Input Data
st.sidebar.header("Input Data Sensor")

def user_input_features():
    # Sesuaikan rentang min/max dengan data di notebook Anda
    m1 = st.sidebar.number_input("Metric 1", value=215630672)
    m2 = st.sidebar.number_input("Metric 2", value=55)
    m3 = st.sidebar.number_input("Metric 3", value=0)
    m4 = st.sidebar.number_input("Metric 4", value=52)
    m5 = st.sidebar.number_input("Metric 5", value=6)
    m6 = st.sidebar.number_input("Metric 6", value=407438)
    m7 = st.sidebar.number_input("Metric 7", value=0)
    m8 = st.sidebar.number_input("Metric 8", value=0)
    m9 = st.sidebar.number_input("Metric 9", value=7)
    
    data = {
        'metric1': m1, 'metric2': m2, 'metric3': m3,
        'metric4': m4, 'metric5': m5, 'metric6': m6,
        'metric7': m7, 'metric8': m8, 'metric9': m9
    }
    features = pd.DataFrame(data, index=[0])
    return features

df_input = user_input_features()

# 5. Tampilan Utama
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Input")
    st.write(df_input)

with col2:
    st.subheader("Hasil Prediksi")
    
    # Melakukan Prediksi
    prediction = model.predict(df_input)
    prediction_proba = model.predict_proba(df_input)

    if prediction[0] == 1:
        st.error("⚠️ PERINGATAN: Mesin Diprediksi FAILURE")
    else:
        st.success("✅ STATUS: Mesin NORMAL")

    st.write(f"**Probabilitas Failure:** {prediction_proba[0][1]:.2%}")
    st.write(f"**Probabilitas Normal:** {prediction_proba[0][0]:.2%}")

# 6. Informasi Tambahan
st.divider()
st.info("Catatan: Model ini menggunakan data sensor historis untuk memprediksi risiko kegagalan.")