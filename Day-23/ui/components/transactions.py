import streamlit as st
import pandas as pd

def show_high_risk(analysis):
    st.subheader("High-Risk Transactions")

    insights = analysis.get("insights", {})
    high_risk = insights.get("high_risk_transactions", [])

    if high_risk:
        df = pd.DataFrame(high_risk)

        st.dataframe(df, use_container_width=True)

        st.subheader(" Drill-Down")

        selected = st.selectbox("Select Transaction", options=df.index)

        st.json(df.loc[selected].to_dict())

    else:
        st.info("No high-risk transactions detected.")