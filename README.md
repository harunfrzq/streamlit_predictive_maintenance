# 🏭 Predictive Maintenance: End-to-End Machine Learning Project

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://share.streamlit.io/USER_ANDA/REPO_ANDA)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-CRISP--DM-orange)](#)

## 🎯 Business Overview
Kerusakan mesin yang mendadak seringkali menyebabkan *downtime* produksi yang mahal dan biaya perbaikan yang tidak terencana. Proyek ini bertujuan untuk membangun model **Predictive Maintenance** yang mampu mendeteksi potensi kegagalan mesin sebelum terjadi, sehingga tim teknis dapat melakukan tindakan preventif.

### Goals:
* **Deteksi Dini:** Mengurangi risiko kerusakan fatal pada komponen mesin.
* **Efisiensi Biaya:** Mengoptimalkan jadwal pemeliharaan (maintenance).
* **KPI Utama:** Memaksimalkan **Recall** pada kelas kegagalan (*failure*) agar tidak ada kerusakan yang terlewat.

---

## 📊 Dataset & Metodologi
Proyek ini mengikuti standar industri **CRISP-DM** (Cross-Industry Standard Process for Data Mining):

1.  **Business Understanding**: Identifikasi masalah operasional dan target KPI.
2.  **Data Understanding**: Eksplorasi data sensor (`metric1` hingga `metric9`).
3.  **Data Preparation**: Cleaning, feature selection, dan penanganan ketidakseimbangan data (*Imbalanced Class*).
4.  **Modeling**: Implementasi Random Forest Classifier dengan Pipeline Scikit-Learn.
5.  **Evaluation**: Analisis performa menggunakan Classification Report dan Confusion Matrix.

---

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, Joblib.
* **Deployment:** Streamlit & GitHub.
* **Model:** Random Forest Classifier.

---

## 🚀 Fitur Aplikasi
Aplikasi web ini memungkinkan pengguna untuk:
-   Memasukkan nilai sensor mesin secara *real-time* melalui sidebar.
-   Melihat probabilitas prediksi kegagalan mesin dalam bentuk persentase.
-   Mendapatkan indikator visual (Hijau/Merah) untuk status kesehatan mesin.

---

## 📦 Cara Menjalankan Secara Lokal

1. **Clone Repository**
   ```bash
   git clone [https://github.com/USERNAME_ANDA/REPO_ANDA.git](https://github.com/USERNAME_ANDA/REPO_ANDA.git)
   cd REPO_ANDA