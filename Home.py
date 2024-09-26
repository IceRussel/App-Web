import streamlit as st

# Titre
st.title("Mon formulaire")


# Texte
st.write("Ceci est un formulaire de contrat")

# Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)

# Image
st.image("https://www.booska-p.com/wp-content/uploads/2022/08/Koba-LaD-Visu-News-1-1024x750.jpg")
