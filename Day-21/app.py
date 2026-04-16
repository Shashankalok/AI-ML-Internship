import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Healthcare Monitoring", layout="centered")

st.title(" Patient Monitoring Dashboard")

# Sidebar navigation
option = st.sidebar.selectbox(
    "Choose Feature",
    ("Single Patient Check", "Multiple Patients Check", "Patient History")
)

#  Helper Function

def display_result(data):
    st.write(f"###  Patient: {data['name']}")
    st.write(f" Heart Rate: {data['heart_rate']} bpm")
    st.write(f"🫁 Oxygen Level: {data['oxygen_level']} %")
    st.write(f" Risk Score: {data['risk_score']}")

    #  ML Output
    if "ml_prediction" in data:
        st.write(f" ML Prediction: {data['ml_prediction']}")
        
        if "confidence" in data:
            st.write(f" Confidence: {data['confidence']}%")

    # Status styling
    if data["status"] == "CRITICAL":
        st.error(f"🚨 {data['status']}")
    elif data["status"] == "WARNING":
        st.warning(f" {data['status']}")
    else:
        st.success(f" {data['status']}")



#  SINGLE PATIENT
if option == "Single Patient Check":
    st.subheader("Check Single Patient Status")

    name = st.text_input("Patient Name")
    heart_rate = st.number_input("Heart Rate", min_value=0)
    oxygen_level = st.number_input("Oxygen Level", min_value=0)

    if st.button("Check Status"):
        if name == "":
            st.warning("Please enter patient name")
        else:
            data = {
                "name": name,
                "heart_rate": heart_rate,
                "oxygen_level": oxygen_level
            }

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/monitor-alert",
                    json=data,
                    timeout=5
                )

                if response.status_code == 200:
                    result = response.json()
                    display_result(result)
                else:
                    st.error("API Error")

            except:
                st.error("FastAPI server not running")



#  MULTIPLE PATIENTS
elif option == "Multiple Patients Check":
    st.subheader("Monitor Multiple Patients")

    patients = []

    for i in range(2):
        st.markdown(f"### Patient {i+1}")
        name = st.text_input(f"Name {i}", key=f"name{i}")
        hr = st.number_input(f"Heart Rate {i}", min_value=0, key=f"hr{i}")
        ox = st.number_input(f"Oxygen Level {i}", min_value=0, key=f"ox{i}")

        patients.append({
            "name": name,
            "heart_rate": hr,
            "oxygen_level": ox
        })

    if st.button("Monitor All Patients"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/monitor-multiple",
                json=patients,
                timeout=5
            )

            if response.status_code == 200:
                results = response.json()

                for res in results:
                    st.divider()
                    display_result(res)

            else:
                st.error("API Error")

        except:
            st.error("FastAPI server not running")



#  PATIENT HISTORY

elif option == "Patient History":
    st.subheader(" Patient History Dashboard")

    try:
        response = requests.get(
            "http://127.0.0.1:8000/history",
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()

            if len(data) == 0:
                st.warning("No data available")
            else:
                df = pd.DataFrame(data)
                df["timestamp"] = pd.to_datetime(df["timestamp"])

                #  PATIENT FILTER
                patient_names = df["name"].unique()
                selected_patient = st.selectbox("Select Patient", patient_names)

                filtered_df = df[df["name"] == selected_patient]

                st.write("### 📋 Filtered Records")
                st.dataframe(filtered_df.sort_values(by="timestamp", ascending=True))

                #  Check for enough data
                if len(filtered_df) < 2:
                    st.warning("Not enough data to display chart. Add more records.")
                else:
                    #  HEART RATE
                    st.write("###  Heart Rate Trend")
                    plt.clf()
                    plt.plot(filtered_df["timestamp"], filtered_df["heart_rate"])
                    plt.xlabel("Time")
                    plt.ylabel("Heart Rate (bpm)")
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

                    #  OXYGEN
                    st.write("### 🫁 Oxygen Level Trend")
                    plt.clf()
                    plt.plot(filtered_df["timestamp"], filtered_df["oxygen_level"])
                    plt.xlabel("Time")
                    plt.ylabel("Oxygen Level (%)")
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

                    #  RISK SCORE
                    st.write("###  Risk Score Trend")
                    plt.clf()
                    plt.plot(filtered_df["timestamp"], filtered_df["risk_score"])
                    plt.xlabel("Time")
                    plt.ylabel("Risk Score")
                    plt.xticks(rotation=45)
                    st.pyplot(plt)

        else:
            st.error("API Error")

    except:
        st.error("FastAPI server not running")