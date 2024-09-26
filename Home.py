import streamlit as st

# Titre
st.title("Mon formulaire")


# Texte
st.write("Ceci est un formulaire de contrat")

# Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)

# Image
st.image("https://i.makeagif.com/media/6-13-2019/gLyUlA.gif")

# Image 2
st.image("https://i.pinimg.com/originals/47/7a/86/477a86ad9caab74f42e4bf5357b70446.gif")
