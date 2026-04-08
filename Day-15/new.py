import os
import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# 🔑 API Key
os.environ["GROQ_API_KEY"] = "Api key"

# UI
st.set_page_config(page_title="AI Data Analyst", layout="wide")
st.title("📊 AI Data Analysis Assistant")

# Model
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# Upload dataset
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Basic stats
    st.subheader("📈 Basic Statistics")
    st.write(df.describe())

    # User question
    user_input = st.text_input("Ask a question about your data")

    if user_input:
        # Convert data summary to text
        data_info = df.describe().to_string()

        prompt = PromptTemplate(
            input_variables=["data", "question"],
            template="""
            You are a professional data analyst.

            Here is dataset summary:
            {data}

            User question:
            {question}

            Provide clear statistical explanation.
            """
        )

        chain = prompt | llm

        response = chain.invoke({
            "data": data_info,
            "question": user_input
        })

        st.subheader("🤖 AI Response")
        st.write(response.content)
