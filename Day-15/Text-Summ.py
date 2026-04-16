import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

# API key
os.environ["GROQ_API_KEY"] = "Api key"

st.title("Text Summarizer")

# Model
llm = ChatGroq(model="llama-3.1-8b-instant")

# Input text
text = st.text_area("Enter text to summarize")

# Summary type
style = st.selectbox("Select summary style", [
    "Short (2-3 lines)",
    "Bullet points",
    "Detailed explanation"
])

if st.button("Summarize"):
    prompt = PromptTemplate(
        input_variables=["text", "style"],
        template="""
        Summarize the following text in {style}:

        {text}
        """
    )

    chain = prompt | llm

    response = chain.invoke({
        "text": text,
        "style": style
    })

    st.subheader("Summary:")
    st.write(response.content)
