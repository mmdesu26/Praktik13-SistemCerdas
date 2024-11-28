import streamlit as st

# Membuat checkbox
st.checkbox("yes")

# Membuat button
st.button("Click")

# Membuat radio button untuk memilih gender
gender = st.radio("Pick your gender", ["Male", "Female"])

# Dropdown untuk memilih planet
st.selectbox("Choose a planet", ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])

# Slider dengan label teks langsung
level = st.select_slider(
    "Pick a level",
    options=["Bad", "Good", "Excellent"],
    value="Good"  # Nilai default
)

# Slider dengan nilai 
st.slider("Pick a number", 0, 50, 9)
