import streamlit as st
import pandas as pd

def upload_file():
    uploaded_file = st.file_uploader(" Upload Transaction Dataset", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        st.subheader(" Data Preview")
        st.dataframe(df.head())

        return df

    return None