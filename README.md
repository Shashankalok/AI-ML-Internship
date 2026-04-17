

---

#  `README.md`

```markdown
#  Multi-Agent AI Research Assistant

A production-style **Multi-Agent AI System** that performs research, analysis, critique, and report generation using LLMs and real-time web data.

---

##  Overview

This project simulates a team of AI agents working together to generate high-quality research reports.

It combines:
-  Real-time web search
-  LLM-based reasoning
-  Iterative self-improvement
-  Coordinated multi-agent workflow

---

##  System Architecture

```

User Input
↓
Coordinator Agent
↓
Researcher → Analyzer → Critic → (Feedback Loop)
↓
Writer
↓
Final Report

```

---

##  Agents

| Agent        | Role |
|-------------|------|
|  Researcher | Fetches real-world data using Tavily API |
|  Analyzer   | Extracts insights using LLM (Groq) |
|  Critic     | Evaluates and suggests improvements |
|  Writer     | Generates structured professional reports |
|  Coordinator | Orchestrates workflow and manages iteration |

---

## Tech Stack

- **Python**
- **Streamlit** (UI)
- **Groq API** (LLM inference)
- **Tavily API** (Web search)
- **dotenv** (Environment management)

---

##  Project Structure

```

multi_agent_system/
│
├── agents/         # Agent logic (Researcher, Analyzer, etc.)
├── tools/          # External tools (LLM + APIs)
├── config/         # Settings and API keys
├── app.py          # Streamlit UI
├── main.py         # CLI runner
├── requirements.txt
└── .env

````

---

##  Features

-  Multi-agent architecture  
-  Real-time web search integration  
-  LLM-powered analysis and critique  
-  Feedback loop for iterative improvement  
-  Professional report generation  
-  Streamlit UI for interactive usage  
-  Optimized for API limits (token + rate handling)  

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shashankalok/multi-agent-ai.git
cd multi-agent-ai
````

---

### 2. Create virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
MODEL_NAME=llama-3.1-8b-instant
```

---

##  Usage

### Run CLI version

```bash
python main.py
```

---

### Run Web App (Streamlit)

```bash
streamlit run app.py
```

---

##  Example Output

The system generates structured reports like:

* Title
* Key Insights
* Challenges
* Recommendations
* Conclusion

---

##  Key Learnings

* Designing scalable **multi-agent systems**
* Handling **LLM constraints (tokens, rate limits)**
* Implementing **feedback-driven AI pipelines**
* Integrating **real-time data with AI reasoning**

---

##  Future Improvements

*  Add memory (persistent context)
*  Deploy live on cloud (Streamlit / AWS)
*  Export reports as PDF
*  Chat-style interface
*  Show sources and citations

---

##  Author

**Shashank Alok**

---

