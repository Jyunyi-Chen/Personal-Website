import time
import ollama
import streamlit as st

st.title("Chatbot (Powered by Ollama)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your question ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        partial_response = ""

        for chunk in ollama.chat(
            model="llama3.2:3b",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        ):
            if "message" in chunk and "content" in chunk["message"]:
                partial_response += chunk["message"]["content"]
                message_placeholder.markdown(partial_response)
                time.sleep(0.05)

    st.session_state.messages.append({"role": "assistant", "content": partial_response})
