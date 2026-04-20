import streamlit as st
import os
from config import Config


def show_logs():
    st.subheader(" System Logs")

    log_path = Config.LOG_FILE  # use same path as logger

    if os.path.exists(log_path):

        with open(log_path, "r") as f:
            logs = f.readlines()

        if logs:
            for log in logs[-20:]:  # last 20 logs
                st.text(log)
        else:
            st.info("Log file is empty.")

    else:
        st.warning("Log file not found.")