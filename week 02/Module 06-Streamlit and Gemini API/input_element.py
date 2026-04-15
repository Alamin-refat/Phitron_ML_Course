import streamlit as st

st.title("Input your information",anchor=False)

st.divider()

name = st.text_input("Enter your name")

st.write("your name is: ",name)

