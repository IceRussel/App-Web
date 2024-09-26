import streamlit as st

st.title("Dall-e 3")

# Champ de saisi
dalle_input = st.text_input ("Veuiller entré une description de l'image que vous souhaitez générez")
st.write(dalle_input)

st.sidebar.text_input("Veuillez entré la clé Open IA")
