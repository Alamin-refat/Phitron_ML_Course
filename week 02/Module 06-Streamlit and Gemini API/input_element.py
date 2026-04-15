import streamlit as st

st.title("Input your information",anchor=False)

st.divider()

name = st.text_input("Enter your name")

st.write("your name is: ",name)

st.divider()

age = st.number_input("Enter your age", value=None,placeholder="type your age......")

st.write("your age is: ",age)
