import streamlit as st
def hello(name):
    return "Hello " + name
st.title("An application deployment using Streamlit ")
name = st.text_input("Enter your name")
result = hello(name)
st.write("-->", result)

