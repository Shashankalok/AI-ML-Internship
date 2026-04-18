import streamlit as st
import pandas as pd

def show_metrics(analysis):
    st.subheader(" Key Risk Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Txns", analysis.get("total_transactions"))
    col2.metric("Fraud Cases", analysis.get("fraud_cases"))
    risk = analysis.get("risk_score", 0)
    col3.metric("Risk Score", f"{round(risk, 2)}%")
    col4.metric("Risk Level", analysis.get("risk_level"))

def show_chart(analysis):
    st.subheader(" Fraud vs Normal Distribution")

    fraud = analysis.get("fraud_cases", 0)
    total = analysis.get("total_transactions", 1)

    chart_df = pd.DataFrame({
        "Category": ["Fraud", "Normal"],
        "Count": [fraud, total - fraud]
    })

    chart_df["Percentage"] = chart_df["Count"] / total * 100

    st.bar_chart(chart_df.set_index("Category")["Count"])