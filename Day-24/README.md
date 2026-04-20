#  Multi-Agent System with Testing, Logging & Monitoring

##  Project Overview

This project implements a **multi-agent system** where different agents collaborate to process a user query and generate a final structured report.

Each agent performs a specific role:

Researching the topic
Analyzing the information
Critiquing the content
 Generating a final report

The system is designed with **modularity, testing, logging, and cost tracking**, making it aligned with production-level practices.

---

##  Architecture / Workflow

```
User Input 
   ↓
Coordinator Agent
   ↓
Researcher Agent
   ↓
Analyzer Agent
   ↓
Critic Agent
   ↓
Writer Agent
   ↓
Final Output
```

---

##  Project Structure

```
Day-24/
│
├── agents/
│   ├── researcher.py
│   ├── analyzer.py
│   ├── critic.py
│   ├── writer.py
│   └── coordinator.py
│
├── tools/
│   └── calculator.py
│
├── utils/
│   ├── logger.py
│   └── cost_tracker.py
│
├── tests/
│   ├── test_basic.py
│   ├── test_calculator.py
│   ├── test_researcher.py
│   ├── test_analyzer.py
│   ├── test_critic.py
│   ├── test_writer.py
│   ├── test_coordinator.py
│   └── test_workflow.py
│
├── main.py
├── README.md
```

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd Day-24
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate environment

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install pytest pytest-cov
```

---

## ▶️ How to Run the Project

```bash
python main.py
```

### Example Input:

```
What is financial risk?
```

### Example Output:

```
Final Report: ...
Tokens Used: 40
Total Cost: $0.000080
```

---

##  Testing

### Run all tests:

```bash
pytest -v
```

### Run with coverage:

```bash
pytest --cov=.
```

###  Achieved:

* Unit Tests 
* Integration Tests 
* Workflow Tests 
* Edge Case Testing 
* **84% Code Coverage** 

---

##  Logging & Monitoring

* Logging implemented using Python `logging` module
* Logs stored in:

```
app.log
```

### Logs include:

* Agent execution steps
* Workflow progress
* Cost tracking

---

##  Cost Tracking

* Token usage is estimated based on text length
* Cost calculated using a predefined rate

Example:

```
Tokens Used: 40
Total Cost: $0.000080
```

---

##  Key Features

* Multi-agent architecture
* Modular and scalable design
* Comprehensive testing (pytest)
* Logging and monitoring
* Cost tracking simulation
* Clean and simple implementation

---

##  Learning Outcomes

* Writing unit and integration tests
* Achieving high code coverage
* Designing modular systems
* Implementing logging and monitoring
* Understanding workflow orchestration

---

##  Conclusion

This project successfully demonstrates a **production-style multi-agent system** with:

* Testing
* Monitoring
* Clean architecture

It fulfills all requirements of **Day 24: Testing, Documentation, Deployment Preparation & Monitoring**.

---

##  Author

**Shashank Alok**
