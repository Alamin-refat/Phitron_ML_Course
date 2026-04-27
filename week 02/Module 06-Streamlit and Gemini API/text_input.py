import streamlit as st

st.title("🗺  My First Streamlit Web App", anchor=False)
st.header("Content 1", divider=True)

st.subheader("Content 2 subheader")
st.text("Hello world!")

st.markdown(":red[**hello**] *world*")
st.markdown(":red-background[:orange[**hello**] *world*]  :world_map:")

a=10
b=20
st.write(a,b)
