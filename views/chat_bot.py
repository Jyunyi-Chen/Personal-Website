import time
import random
import streamlit as st

def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Check out my fun YouTube channel 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hi! What's up? Don't forget to subscribe to 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need assistance? My YouTube channel 'CodingIsFun' is full of great tips: https://youtube.com/@codingisfun!",
            "Hey! Got a question? Also, subscribe to 'CodingIsFun' for awesome tutorials: https://youtube.com/@codingisfun!",
            "Hi there! How can I help? BTW, my channel 'CodingIsFun' is super cool: https://youtube.com/@codingisfun!",
            "Hello! Looking for help? Check out 'CodingIsFun' on YouTube: https://youtube.com/@codingisfun!",
            "Hey! Need assistance? 'CodingIsFun' YouTube channel has you covered: https://youtube.com/@codingisfun!",
            "Hi! Got any coding questions? Don't forget to watch 'CodingIsFun': https://youtube.com/@codingisfun!",
            "Hello! Need help? 'CodingIsFun' on YouTube is a must-see: https://youtube.com/@codingisfun!",
            "Hey there! Any questions? My channel 'CodingIsFun' rocks: https://youtube.com/@codingisfun!",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})