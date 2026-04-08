import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = "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"

st.title("📧 AI Email Writer")

llm = ChatGroq(model="llama-3.1-8b-instant")

topic = st.text_input("Enter email topic")
tone = st.selectbox("Select tone", ["formal", "friendly"])
recipient = st.text_input("Recipient")
sender = st.text_input("Your Name (Sender)")

if st.button("Generate Email"):
    prompt = PromptTemplate(
        input_variables=["topic", "tone", "recipient", "sender"],
        template="""
        Write a {tone} email to {recipient} about: {topic}

        Include subject, greeting, body, and closing.
        End the email with: Regards,
        {sender}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "topic": topic,
        "tone": tone,
        "recipient": recipient,
        "sender": sender
    })

    st.write(response.content)