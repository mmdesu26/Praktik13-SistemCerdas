import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Memuat data
data_path = 'Top_Anime_data.csv'
data = pd.read_csv(data_path)

# Judul aplikasi utama
st.title("Analisis Data Anime Terpopuler")

# Sidebar untuk navigasi
st.sidebar.title("Pilih Halaman")
page_names = ['Home', 'Ringkasan', 'Tabel Data', 'Visualisasi', 'Machine Learning', 'Contact', 'About']
selected_page = st.sidebar.selectbox("Halaman", page_names)

# Logika untuk setiap halaman
if selected_page == 'Home':
    st.markdown("""
        <style>
            /* Menyisipkan font dari Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Rock+Salt&display=swap');
            
            /* Styling untuk header */
            .header-home {
                background-color: #d3d3d3; /* Warna abu-abu muda */
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                font-size: 24px;
                font-family: 'Rock Salt', cursive; /* Font grafiti */
                color: #333; /* Warna teks */
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="header-home">Selamat Datang di Aplikasi Analisis Data Anime Terpopuler!</div>', unsafe_allow_html=True)
    
    st.write("""Aplikasi ini membantu Anda menganalisis data anime terpopuler. Anda dapat menavigasi melalui sidebar untuk:
    - Melihat ringkasan dataset
    - Menjelajahi tabel data
    - Membuat visualisasi interaktif""")

    # Menampilkan gambar
    image_path = "anime.jpg"
    if os.path.exists(image_path):
        st.subheader("Anime Favorit")
        st.image(image_path, caption="Kumpulan Anime", use_container_width=True)
    else:
        st.warning(f"Gambar '{image_path}' tidak ditemukan.")
    
    # Menampilkan video
    gif_path = "gif.gif"
    if os.path.exists(gif_path):
        st.subheader("Cuplikan Anime")
        st.image(gif_path, caption="Cuplikan Anime", use_container_width=True)
    else:
        st.warning(f"GIF '{gif_path}' tidak ditemukan.")

elif selected_page == 'About':
    st.header("Tentang Aplikasi")
    st.write(""" 
    Website ini dibuat untuk memvisualisasikan dan menganalisis data anime terpopuler dari berbagai platform. 
    Dengan menggunakan aplikasi ini, Anda dapat:
    - Melihat data anime terpopuler yang tersedia.
    - Menganalisis statistik dasar dari dataset.
    - Membuat visualisasi interaktif untuk mendapatkan wawasan lebih lanjut.
    Website ini dirancang menggunakan **Streamlit**, platform interaktif berbasis Python yang memungkinkan pembuatan aplikasi web dengan cepat dan mudah.
    """)

elif selected_page == 'Contact':
    st.header("Hubungi Kami")
    st.write("""
    **Kontak Pengembang:**
    - Nama: Dirajati Kusuma Wardani
    - Email: mmdesu26@gmail.com
    - GitHub: [GitHub Ku](https://github.com/mmdesu26)
    Kami terbuka untuk saran dan masukan Anda!
    """)
    # Menambahkan Logo Instagram dan WhatsApp dengan link
    st.write("### Ikuti Kami")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            "[![Instagram](https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Instagram_logo_2022.svg/1200px-Instagram_logo_2022.svg.png)](https://www.instagram.com/@2.dzxraxx5)"
        )
    with col2:
        st.markdown(
            "[![WhatsApp](https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg)](https://wa.me/082238393338)"
        )
    
elif selected_page == 'Ringkasan':
    st.header("Ringkasan Dataset")
    st.write("### Contoh Data")
    st.write(data.head())
    st.write("### Statistik Deskriptif")
    st.write(data.describe())
    st.write(f"### Total Entri: {data.shape[0]}")
elif selected_page == 'Tabel Data':
    st.header("Tabel Data Anime")
    st.write("### Dataset Lengkap")
    st.dataframe(data)
elif selected_page == 'Visualisasi':
    st.header("Visualisasi Data")
    
    # Dropdown untuk kolom numerik
    kolom_numerik = data.select_dtypes(include=["int64", "float64"]).columns
    if kolom_numerik.empty:
        st.write("Tidak ada kolom numerik untuk divisualisasikan.")
    else:
        st.sidebar.subheader("Pengaturan Visualisasi")
        sumbu_x = st.sidebar.selectbox("Pilih Sumbu X", kolom_numerik)
        sumbu_y = st.sidebar.selectbox("Pilih Sumbu Y", kolom_numerik)
        
        if sumbu_x and sumbu_y:
            st.write(f"### Scatter Plot: {sumbu_x} vs {sumbu_y}")
            fig, ax = plt.subplots()
            ax.scatter(data[sumbu_x], data[sumbu_y], alpha=0.7, color='blue')
            ax.set_xlabel(sumbu_x)
            ax.set_ylabel(sumbu_y)
            ax.set_title(f"{sumbu_x} vs {sumbu_y}")
            st.pyplot(fig)

elif selected_page == 'Machine Learning':
    st.header("Prediksi dengan Machine Learning")

    # Pilih kolom untuk fitur dan target
    features = data.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if len(features) >= 2:
        st.write("### Pilih Fitur dan Target untuk Prediksi")

        # Dropdown untuk memilih fitur dan target
        feature_cols = st.multiselect("Pilih Fitur", features)
        target_col = st.selectbox("Pilih Target", features)

        if feature_cols and target_col:
            # Persiapan data
            X = data[feature_cols]
            y = data[target_col]

            # Split data untuk pelatihan dan pengujian
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Membuat dan melatih model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Melakukan prediksi
            y_pred = model.predict(X_test)

            # Menampilkan hasil evaluasi
            mse = mean_squared_error(y_test, y_pred)
            st.write(f"### Mean Squared Error: {mse}")
            st.write(f"### Prediksi vs Nilai Sebenarnya")
            st.write(f"Prediksi: {y_pred[:10]}")
            st.write(f"Nilai Sebenarnya: {y_test[:10].values}")
    else:
        st.write("Tidak cukup fitur numerik untuk melakukan prediksi.")
