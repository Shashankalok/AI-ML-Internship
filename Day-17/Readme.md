# 🤖 RAG Chatbot using FastAPI + Streamlit

## 🚀 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to upload documents and ask questions based on their content. The system uses semantic search and a Large Language Model (LLM) to generate accurate, context-aware answers.

---

## 🧠 Features

- 📂 Upload documents (PDF, DOCX, TXT)
- ✂️ Automatic text extraction and chunking
- 🔢 Embedding generation using Sentence Transformers
- 📦 Vector storage using FAISS
- 🔍 Semantic search for relevant content
- 🤖 LLM-based answer generation (Groq API)
- 💬 Interactive chatbot UI using Streamlit
- 🧾 Source citation (shows relevant document chunks)
- 🗂️ Document management (list & delete)
- 🕘 Conversation history tracking
- 🔐 File validation (type & size)

---

## 🏗️ Architecture


User → Streamlit UI → FastAPI Backend → FAISS Vector DB → LLM → Response


---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Vector DB:** FAISS
- **Embeddings:** Sentence Transformers
- **LLM:** Groq (LLaMA 3)
- **Document Processing:** PyPDF2, python-docx
- **Language:** Python

---

## 📂 Project Structure


rag-fastapi-app/
│
├── main.py # FastAPI backend
├── app.py # Streamlit frontend
├── requirements.txt
├── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone <your-repo-link>
cd rag-fastapi-app


### 2️⃣ Create virtual environment

python -m venv .venv


### 3️⃣ Activate environment

..venv\Scripts\activate


### 4️⃣ Install dependencies

pip install -r requirements.txt


---

## 🔑 Environment Setup

Set your Groq API key:


set GROQ_API_KEY=your_api_key_here


---

## ▶️ Run the Application

### Start Backend

uvicorn main:app --reload


### Start Frontend

streamlit run app.py


---

## 🌐 Access the Application

- FastAPI Docs: http://127.0.0.1:8000/docs  
- Streamlit UI: http://localhost:8501  

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|--------|------------|
| POST | /upload | Upload document |
| POST | /query | Ask question |
| GET | /documents | List documents |
| DELETE | /document/{id} | Delete document |
| GET | /history | Get conversation history |

---
[User]
   ↓
[Streamlit UI]  (optional)
   ↓
[FastAPI Backend]
   ↓
 ┌───────────────┬───────────────┐
 ↓                               ↓
[Upload Flow]                [Query Flow]
 ↓                               ↓
[Text Extraction]         [User Question]
 ↓                               ↓
[Chunking]                [Embedding]
 ↓                               ↓
[Embeddings]              [FAISS Search]
 ↓                               ↓
[FAISS DB]               [Top Chunks]
          └───────────────┬───────────────┘
                          ↓
                  [LLM (Groq)]
                          ↓
                  [Final Answer]
                          ↓
                    [User Output]



## 🧪 Example Workflow

1. Upload a PDF/DOCX/TXT file  
2. Ask a question in the chatbot  
3. System retrieves relevant chunks  
4. LLM generates answer  
5. Sources are displayed  

---

## 📊 Results

- Successfully implemented semantic document search  
- Improved answer accuracy using retrieval  
- Reduced hallucination using context-based generation  

---

## 🚧 Future Improvements

- Streaming responses (real-time output)
- FAISS index update on deletion
- Authentication system
- Deployment on cloud (Render/AWS)
- Multi-user support

---

## 👨‍💻 Author

**Shashank Alok**  
 

---

## ⭐ Acknowledgment

This project was built as part of learning **RAG systems, FastAPI, and LLM integration**.

---