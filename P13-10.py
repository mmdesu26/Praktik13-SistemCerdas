import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Load model
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

# Judul aplikasi
st.title('Prediksi Harga Mobil')

# Header dan dataset
st.header("Dataset")
df1 = pd.read_csv('HargaMobil.csv')
st.dataframe(df1)

# Grafik
st.write("Grafik Highway-mpg")
st.line_chart(df1[['highwaympg']])

st.write("Grafik curbweight")
st.line_chart(df1[['curbweight']])

st.write("Grafik horsepower")
st.line_chart(df1[['horsepower']])

# Input nilai variabel independen
st.subheader("Masukkan Nilai untuk Prediksi")
highwaympg = st.number_input('Highway MPG', min_value=0, value=30)
curbweight = st.number_input('Curb Weight', min_value=0, value=2000)
horsepower = st.number_input('Horsepower', min_value=0, value=100)

# Prediksi
if st.button('Prediksi'):
    # Persiapkan data input
    input_data = pd.DataFrame([[highwaympg, curbweight, horsepower]], columns=['highwaympg', 'curbweight', 'horsepower'])
    
    # Prediksi harga mobil
    car_prediction = model.predict(input_data)
    
    # Ambil hasil prediksi
    harga_mobil_float = float(car_prediction[0])
    
    # Format hasil prediksi
    harga_mobil_formatted = f"${harga_mobil_float:,.2f}"
    
    # Tampilkan hasil prediksi
    st.subheader("Hasil Prediksi")
    st.write(f"Harga Mobil yang Diprediksi: {harga_mobil_formatted}")

st.write('by Dira')