
---

#  Healthcare Monitoring System (FastAPI + Streamlit + ML)

##  Project Overview

This project is a **real-time healthcare monitoring system** built using FastAPI, Streamlit, and Machine Learning. It takes patient inputs such as heart rate and oxygen level, analyzes them using rule-based logic and ML, stores the data, and visualizes trends through a dashboard.

---

##  Objective

The main objective of this project is to implement **advanced FastAPI concepts** such as:

* Async/Await programming
* Concurrency
* Background tasks
* Middleware
* High-performance API design

These concepts are applied in a real-world healthcare use case.

---

##  Tech Stack

* Python
* FastAPI (Backend API)
* Streamlit (Frontend UI)
* SQLite (Database)
* Scikit-learn (Machine Learning)
* Pandas & Matplotlib (Visualization)
* Pydantic (Data validation)
* Asyncio (Concurrency)

---

##  Project Structure

```
project/
│
├── main.py            # FastAPI app (API endpoints)
├── app.py             # Streamlit frontend
├── models/
│   └── patient.py     # Data validation (Pydantic)
├── services/
│   └── monitor.py     # Core logic (processing + ML + DB)
├── ml/
│   └── model.py       # Machine Learning model
├── db/
│   └── database.py    # SQLite database
├── middleware/
│   └── logger.py      # Logging middleware
├── patients.db        # Database file
└── alerts.txt         # Alert logs
```

---

##  How It Works (Flow)

1. User enters patient data in **Streamlit (app.py)**
2. Data is sent to **FastAPI (main.py)**
3. **monitor.py** processes the data:

   * Validates input
   * Calculates risk score
   * Calls ML model
4. **model.py** predicts risk (LOW / MEDIUM / HIGH)
5. Data is stored in **SQLite database**
6. Response is sent back to frontend
7. Charts are displayed in dashboard

---

##  Features

###  Async & High Performance

* Uses `async/await` for non-blocking operations
* Handles multiple requests efficiently

###  Concurrency

* Processes multiple patients simultaneously using:

```python
asyncio.gather()
```

###  Background Tasks

* Sends alerts without delaying API response

###  Machine Learning Integration

* Logistic Regression model for risk prediction
* Outputs prediction + confidence score

### Data Validation

* Uses Pydantic to validate input data

###  Database Integration

* Stores patient history in SQLite

###  Data Visualization

* Displays charts for:

  * Heart Rate
  * Oxygen Level
  * Risk Score

---

##  API Endpoints

| Endpoint            | Description               |
| ------------------- | ------------------------- |
| `/monitor`          | Monitor single patient    |
| `/monitor-multiple` | Monitor multiple patients |
| `/monitor-alert`    | Monitor + trigger alerts  |
| `/history`          | Get patient history       |
| `/timeout-check`    | Test timeout handling     |

---

##  How to Run

### 1. Clone Repository

```bash
git clone <repo-url>
cd project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Backend

```bash
uvicorn main:app --reload
```

 Open:

```
http://127.0.0.1:8000/docs
```

---

### 4. Run Frontend

```bash
streamlit run app.py
```

👉 Open:

```
http://localhost:8501
```

---

##  Example Output

```json
{
  "name": "John",
  "heart_rate": 120,
  "oxygen_level": 90,
  "risk_score": 6,
  "status": "WARNING",
  "ml_prediction": "HIGH",
  "confidence": 74.71
}
```

---

##  Concepts Covered

* Synchronous vs Asynchronous Programming
* Async/Await
* Concurrency (asyncio)
* Background Tasks
* Middleware
* API Design
* Machine Learning Integration
* Data Visualization

---

##  Real-World Relevance

This project simulates a **real healthcare system** where:

* Patients are monitored in real time
* Risks are predicted using ML
* Alerts are generated automatically
* Historical data is tracked and visualized

---
##  Future Improvements

* Real-time streaming using WebSockets
* Integration with wearable devices
* Advanced ML models
* Cloud deployment

---

##  Author

Shashank Alok

---

