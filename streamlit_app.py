import streamlit as st
import gradio as gr
def hello(name):
    return "Hello " + name
st.title("An application deployment using Streamlit ")
name = st.text_input("Enter your name")
result = hello(name)
st.write("-->", result)
gr.Interface(fn=hello, inputs='text', outputs='text').launch()
