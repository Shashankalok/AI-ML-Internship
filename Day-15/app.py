import os
import json
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

#  Set your Groq API key here
os.environ["GROQ_API_KEY"] = "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"

# Page config
st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title(" Day-15 Chatbot ")

#  Stop button
if st.button(" Stop Chatbot"):
    st.warning("Chatbot stopped. Refresh page to restart.")
    st.stop()

# Initialize model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# File to store chat
FILE_PATH = "chat_history.json"

# Load memory from file
def load_memory():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []

# Save memory to file
def save_memory(messages):
    with open(FILE_PATH, "w") as f:
        json.dump(messages, f)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = load_memory()

# Display old messages
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.write(msg)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append(("user", user_input))
    save_memory(st.session_state.messages)

    with st.chat_message("user"):
        st.write(user_input)

    # Prepare conversation history for AI
    conversation_text = ""
    for role, msg in st.session_state.messages:
        if role == "user":
            conversation_text += f"User: {msg}\n"
        else:
            conversation_text += f"AI: {msg}\n"

    # Add instruction (your specialization )
    final_prompt = (
        "You are a helpful statistics tutor.\n"
        "Continue the conversation below:\n\n"
        + conversation_text
    )

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... ⏳"):
            response = llm.invoke(final_prompt)
            st.write(response.content)

    # Save AI response
    st.session_state.messages.append(("assistant", response.content))
    save_memory(st.session_state.messages)