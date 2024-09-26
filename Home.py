import streamlit as st

# Titre
st.title("Mon formulaire")


# Texte
st.write("Ceci est un formulaire de contrat")

# Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)

# Image 1
st.image("https://i.pinimg.com/originals/47/7a/86/477a86ad9caab74f42e4bf5357b70446.gif")

# Video
st.video("https://www.youtube.com/watch?v=84034w0UhxI")

# Sidebare
st.sidebar.title("Koba la D aka Marcel Junior Loutarila")

# Vidéo dans la sidebare
st.sidebar.video("https://www.youtube.com/watch?v=-C9Izxw3rOw")

# Select Bar
student_grad = st.selectbox("Selectionner votre niveau d'étude", ["Bac", "Bac+2", "Bac+5"])

# Select slider
age = st.select_slider("Quel est votre age ?", range(0,99))
