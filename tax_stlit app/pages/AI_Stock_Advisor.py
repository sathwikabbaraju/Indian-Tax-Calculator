import openai
import streamlit as st
from dotenv import load_dotenv
import os


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

# Title of the app
st.title("Financial Advisor ChatBot")

# Initialize session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Enter your financial situation or question here:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        full_response = response['choices'][0]['message']['content']
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Instructions
st.markdown("### Instructions")
st.markdown("""
- Enter your financial situation or questions related to finance in the input box.
- The chatbot will provide a summary and advice based on your input.
- You can ask about investment plans, savings, loans, and other financial matters.
""")
