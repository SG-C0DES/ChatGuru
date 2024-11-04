pip install google.generativeai
import google.generativeai as genai
import streamlit as st
from PIL import Image
import time

API_KEY = "AIzaSyDRmG9A4IIKlsGHFcVsIZSg4m4Bc7IrStc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')


def respond(query):
    res = model.generate_content(query)
    return res


tabs = st.tabs(["Home", "Chat"])
with tabs[0]:
    st.title("ChatGuru- The New Chat Bot")
    st.header("*" * 20)
    st.subheader(
        "ChatHQU is a chatbot that can answer your questions about anything. And by anything, we mean ANYTHING."
    )
    with Image.open("my_image.png") as image:
        st.sidebar.write('Meet the Creator')
        st.sidebar.image(image, caption='Programmer')
        st.sidebar.write('Shaurya Garg')
    st.subheader("Click on the sidebar menu to view more.")
with tabs[1]:
    query = st.text_input("Enter your query here: ")
    if st.button("Ask query"):
        if query != '':
            response = respond(query)
            with st.spinner("Generating a great answer..."):
                time.sleep(3)
            st.success(response.text)
            rating = st.select_slider('Select Rating of Answer',
                                      options=[1, 2, 3, 4, 5],
                                      value=5)
            st.write("Selected rating:", str(rating), "/5")
        else:
            st.warning("Please enter query first.")
