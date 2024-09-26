import streamlit as st

# Titre
st.title("Mon formulaire")


# Texte
st.write("Ceci est un formulaire de contrat")

# Champ de saisi
user_input = st.text_input("Tapez votre texte : ")

st.write(user_input)

# Image
st.image("https://media0.giphy.com/media/IkPdFNLIcqITymFiJ3/giphy.gif?cid=6c09b952dj3916gklb7egdc5tgiqf0dcwkoq86ftta346gyt&ep=v1_gifs_search&rid=giphy.gif&ct=g")

# Image 2
st.image("https://i.pinimg.com/originals/47/7a/86/477a86ad9caab74f42e4bf5357b70446.gif")
