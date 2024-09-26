import streamlit as st

st.title("ChatGPT-Rédacteur Web")

user_input = st.text_input("Choisissez une thématique")

open_key = st.sidebar.text_input("Tape une clé")
