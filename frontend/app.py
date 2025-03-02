import streamlit as st
import requests

# FastAPI Backend URL
BACKEND_URL = "http://127.0.0.1:8080/chat/"

# Set Streamlit page config (Dark mode)
st.set_page_config(page_title="Chatbot", layout="centered", page_icon="💬")

# Set custom CSS for chat bubbles and dark mode
st.markdown("""
    <style>
    .user-bubble {
        background-color: #1e90ff;
        color: white;
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
        align-self: flex-end;
    }
    .assistant-bubble {
        background-color: #444;
        color: white;
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
        align-self: flex-start;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chatbot")
st.subheader("Powered by Falcon-7B & FastAPI")

# Unique user ID
user_id = "user_123"

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history with message bubbles
st.write('<div class="chat-container">', unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    role_class = "user-bubble" if chat["role"] == "USER" else "assistant-bubble"
    st.markdown(f'<div class="{role_class}">{chat["message"]}</div>', unsafe_allow_html=True)
st.write("</div>", unsafe_allow_html=True)

# Input field
user_input = st.text_input("Type your message...")

# Send button
if st.button("Send"):
    if user_input:
        # Send request to FastAPI backend
        response = requests.post(BACKEND_URL, json={"user_id": user_id, "message": user_input})
        
        if response.status_code == 200:
            reply = response.json()["response"]
            # Update chat history
            st.session_state.chat_history.append({"role": "USER", "message": user_input})
            st.session_state.chat_history.append({"role": "ASSISTANT", "message": reply})
            # Refresh UI
            st.rerun()
        else:
            st.error("Error communicating with the chatbot.")

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
