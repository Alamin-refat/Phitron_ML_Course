import streamlit as st

st.title("Input your information",anchor=False)
st.divider()
name = st.text_input("Enter your name")

#st.write("your name is: ",name)

st.divider()

age = st.number_input("Enter your age", value=None,placeholder="type your age......")

#st.write("your age is: ",age)

presesed =st.button("Submit",type="primary")


selected =  st.selectbox("choose your profession",
                         ("Student","Employee","Buisenessman"),
                         index=None
                         )


st.write("your profession is: ",selected)

if presesed:
    st.write(f"your name is: {name} and your age is: {age}")
    

