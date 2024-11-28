import streamlit as st

# Slider untuk memilih angka
st.number_input("Pick a number", 0, 100, 1)

# Input teks untuk alamat email
st.text_input("Email address")

# Input tanggal untuk travelling date
st.date_input("Travelling date")

# Input waktu untuk school time
st.time_input("School time", value="now")

# Text area untuk deskripsi
st.text_area("Description")

# Upload file
st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])

# Input warna
st.color_picker("Choose your favourite color", "#FF00FF")

