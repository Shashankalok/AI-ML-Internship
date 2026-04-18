import sys
import os

# Fix import path (IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
from main import run_pipeline

# Import UI components
from ui.components.upload import upload_file
from ui.components.dashboard import show_metrics, show_chart
from ui.components.transactions import show_high_risk
from ui.components.logs_viewer import show_logs

# -----------------------------
#  Page Config
# -----------------------------
st.set_page_config(page_title="FinTech Risk Intelligence", layout="wide")

st.title(" Financial Risk Intelligence Platform")
st.markdown("Production-grade fraud detection system")

# -----------------------------
#  Upload Section
# -----------------------------
df = upload_file()

# -----------------------------
#  Run Pipeline
# -----------------------------
if df is not None:

    if st.button(" Run Risk Analysis"):

        with st.spinner("Running analysis..."):

            temp_path = "temp.csv"
            df.to_csv(temp_path, index=False)

            result = run_pipeline(temp_path)

        if result:

            analysis = result.get("analysis", {})
            report = result.get("final_output", "")
            report_json = result.get("report_json", {})

            # -----------------------------
            #  KPI Metrics
            # -----------------------------
            show_metrics(analysis)

            # -----------------------------
            #  Risk Indicator
            # -----------------------------
            risk = analysis.get("risk_level")

            if risk == "HIGH":
                st.error(" HIGH RISK DETECTED")
            elif risk == "MEDIUM":
                st.warning(" MEDIUM RISK")
            else:
                st.success(" LOW RISK")

            # -----------------------------
            #  Chart
            # -----------------------------
            show_chart(analysis)

            # -----------------------------
            #  Transactions
            # -----------------------------
            show_high_risk(analysis)

            # -----------------------------
            #  Report
            # -----------------------------
            st.subheader("📄 Full Report")
            st.markdown(f"```text\n{report}\n```")

            # -----------------------------
            #  Download
            # -----------------------------
            st.subheader("📥 Export Report")

            col1, col2 = st.columns(2)

            col1.download_button(
                "Download TXT",
                report,
                file_name="report.txt"
            )

            col2.download_button(
                "Download JSON",
                json.dumps(report_json, indent=2),
                file_name="report.json"
            )

            # -----------------------------
            #  Logs
            # -----------------------------
            show_logs()

else:
    st.info("Upload a dataset to begin.")