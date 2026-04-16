# 🧠 LangGraph Basics – Healthcare Workflows

This project demonstrates the fundamentals of **LangGraph**, a framework for building stateful and modular workflows using nodes and edges. The examples are based on simple healthcare scenarios to make concepts easy to understand.

---

## 🚀 What is LangGraph?

LangGraph is a framework used to build workflows as graphs where:

- **Nodes** → Functions (tasks)
- **Edges** → Flow between tasks
- **State** → Shared data passed across nodes

It helps in designing **AI agents and multi-step workflows** in a structured way.

---

## 🧩 Core Concepts

### 🔹 State
A shared dictionary-like object that stores and updates data across all nodes.

### 🔹 Node
A function that performs a specific task (e.g., calculate BMI).

### 🔹 Edge
Defines how nodes are connected and executed.

### 🔹 Conditional Edges
Allow dynamic routing (if-else logic).

### 🔹 Loop
Repeats steps until a condition is satisfied.

---

## 📁 Project Structure


langgraph-basics/
│
├── linear_graph.py
├── conditional_graph.py
├── loop_graph.py
├── multipath_graph.py
├── state_management.py
│
└── README.md


---

## 🏥 Implemented Workflows

### 1️⃣ Linear Workflow
A simple step-by-step pipeline.

**Flow:**

Input → Calculate BMI → Classify → Output


✔ Demonstrates basic node execution and state passing.

---

### 2️⃣ Conditional Workflow
Routes based on a condition.

**Flow:**

Check BMI → Diet → Repeat until normal → End


✔ Demonstrates iterative execution.

---

### 4️⃣ Multi-Path Workflow
Multiple possible paths based on conditions.

**Flow:**

BMI → Nutrition / Maintain / Exercise / Medical Plan


✔ Demonstrates complex decision-making.

---

### 5️⃣ State Management Example
Shows how data is updated step-by-step.

**Flow:**

Add Info → BMI → Diagnosis → Recommendation


✔ Demonstrates how state evolves across nodes.

---

## 📊 Visualization

Each workflow can be visualized using:

```python
graph.get_graph().draw_mermaid_png()

This helps in understanding the structure of the workflow.

How to Run
Install dependencies:
pip install langgraph
Run any file:
python linear_graph.py

Key Learnings
Built modular workflows using graphs
Understood state management
Implemented conditional routing
Created loop-based workflows
Designed multi-path decision systems

Conclusion

This project demonstrates how LangGraph can be used to build structured, scalable, and intelligent workflows, which are useful for AI agents and real-world applications.

Author
Shashank Alok