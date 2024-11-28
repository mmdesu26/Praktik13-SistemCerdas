import streamlit as st

# Membuat title
st.title('title DIRA')

# Membuat markdown
st.markdown('### this is the markdown')
st.markdown('this is the markdown tanpa pagar')

# Membuat header
st.header('this is the header')
st.write('this is the header')

# Membuat subheader
st.subheader('this is the subheader')

# Membuat caption
st.caption('this is the caption')

# Menampilkan nilai variabel, cara 1
st.code(f'x = 2025')
# Menampilkan nilai variabel, cara 2
x = 2024
st.code(f'x = {x}', language='python')
# Menampilkan nilai variabel, cara 3
st.code('x = 2026')