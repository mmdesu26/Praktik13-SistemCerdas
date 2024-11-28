import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# membaca file csv nya
df = pd.read_csv('Top_Anime_data.csv')

# definisikan gambarnya
image_paths = {
    'Home': 'home.png',
    'About': 'about.png',
    'Contact': 'contact.png',
}

# definisikan nama sidebar nya
page_names = ['Home', 'About', 'Contact']

# buat sidebar nya
st.sidebar.title('Select Page')
selected_page = st.sidebar.selectbox('Page', page_names)

# atur logika untuk pemilihan sidebar
if selected_page == 'Home':
    # tampilkan gambar
    st.image(image_paths[selected_page])

    # tampilkan dataset
    st.write(df)

    # tampilkan grafik
    plt.figure()  
    plt.hist(df['Rating'], bins=10)
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of Anime Ratings')
    st.pyplot(plt)  

elif selected_page == 'About':
    # tampilkan gambar
    st.image(image_paths[selected_page])

    # tampilkan informasi
    st.write('This is the about page.')

elif selected_page == 'Contact':
    st.image(image_paths[selected_page])

    st.write('This is the contact page.')