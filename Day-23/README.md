# Financial Risk Intelligence System

A **production-style multi-agent fraud detection system** built using **Python, Machine Learning, and LangGraph**.
This project analyzes financial transactions, detects fraud patterns, assigns risk scores, and presents insights through an interactive dashboard.

---

##  Project Overview

This system simulates a real-world fintech risk intelligence pipeline by combining:

*  Multi-agent architecture
*  Machine learning + rule-based fraud detection
*  Workflow orchestration using LangGraph
*  Interactive dashboard using Streamlit
*  Logging and monitoring system

---

##  Objective

The goal of this project is to build a **scalable multi-agent system** where:

* Each agent performs a specific role
* Agents communicate through a shared state
* Workflow is controlled using LangGraph
* The system generates meaningful fraud insights

---

##  System Workflow

```
User Upload → Researcher → Analyzer → Critic → Writer → Dashboard Output
```

### Step-by-step:

1. User uploads transaction dataset
2. Researcher loads the data
3. Analyzer detects fraud using ML + rules
4. Critic validates the results
5. Writer generates final report
6. Results displayed in UI

---

##  Project Structure

```
Day-23/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── data/
├── logs/
│
├── agents/
├── models/
├── tools/
├── utils/
├── graph/
├── ui/
└── tests/
```

---
##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (Isolation Forest)
* LangGraph
* Streamlit
* Logging

---

##  Agents Description

| Agent      | Role                               |
| ---------- | ---------------------------------- |
| Researcher | Loads dataset                      |
| Analyzer   | Detects fraud & generates insights |
| Critic     | Validates output & handles retry   |
| Writer     | Generates final report             |

---

##  Models Used

* Isolation Forest (Anomaly Detection)
* Rule-based detection (high-value transactions)
* Risk scoring system

---

##  Features

* Fraud detection system
* Risk scoring (Low / Medium / High)
* Transaction-level insights
* Interactive dashboard
* Downloadable reports (TXT + JSON)
* Logging system
* Modular architecture

---

##  How to Run

### 1. Clone the repository

```
git clone <https://github.com/Shashankalok/multi-agent-ai.git>
cd Day-23
```

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run backend

```
python main.py
```

### 5. Run UI

```
streamlit run ui/app.py
```

---

##  Sample Output

* Fraud detection report
* Risk metrics dashboard
* High-risk transaction list
* System logs

---

##  Testing

Test cases are available in:

```
tests/
```

Includes:

* Agent testing
* Workflow testing
* Model validation

---

##  Logging

Logs are stored in:

```
logs/system.log
```

Used for:

* Monitoring execution
* Debugging errors

---

##  Key Highlights

* Multi-agent architecture (advanced concept)
* Real-world fintech use case
* End-to-end system (not just ML model)
* Clean modular design
* Production-style implementation

---

##  Future Improvements

* Add FastAPI for real-time prediction
* Deploy on cloud (AWS / Azure)
* Add model evaluation metrics (Precision, Recall)
* Improve UI with advanced charts
* Add real-time streaming data

---

##  Author

**Shashank Alok**

---

##  Final Note

This project demonstrates how to build a **complete AI-powered system**, not just a model.
It combines data engineering, machine learning, system design, and UI into one integrated solution.

---
