import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

os.environ["GROQ_API_KEY"] = "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"

st.title("AI Data Extractor")

llm = ChatGroq(model="llama-3.1-8b-instant")

text = st.text_area("Enter text to extract data from")

if st.button("Extract Data"):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        Extract the following details from the text:

        - Name
        - Age
        - City
        - Profession

        Return ONLY valid JSON.

        Text:
        {text}
        """
    )

    chain = prompt | llm

    response = chain.invoke({"text": text})

    st.subheader("Extracted Data:")
    st.code(response.content, language="json")