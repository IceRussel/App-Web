import streamlit as st

st.title("Dall-e 3")

# Texte
dalle.e = st.write("Veuiller entré une description de l'image que vous souhaitez")

# Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)
