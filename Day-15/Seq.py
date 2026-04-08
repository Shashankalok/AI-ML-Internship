import os
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# 🔑 API Key
os.environ["GROQ_API_KEY"] = "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"

# UI
st.set_page_config(page_title="Sequential Chain App", layout="centered")
st.title("🔗 Sequential Chain: Explain → Summarize")

# Model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# Input
topic = st.text_input("Enter a topic")

if st.button("Run Chain") and topic:

    # Step 1: Explain
    prompt1 = PromptTemplate(
        input_variables=["topic"],
        template="Explain {topic} in simple words with examples."
    )

    chain1 = prompt1 | llm
    explanation = chain1.invoke({"topic": topic}).content

    st.subheader("📘 Explanation")
    st.write(explanation)

    # Step 2: Summarize
    prompt2 = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text in 3 bullet points:\n{text}"
    )

    chain2 = prompt2 | llm
    summary = chain2.invoke({"text": explanation}).content

    st.subheader("📝 Summary")
    st.write(summary)