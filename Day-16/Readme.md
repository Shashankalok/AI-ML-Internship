# 🚀 Day 16: Vector Stores, Embeddings & RAG System

## 📌 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG) system** that enables users to upload documents (PDFs) and ask questions. The system retrieves relevant information from the document and generates accurate, context-aware answers using an LLM.

---

## 🎯 Objectives

* Understand embeddings and vector similarity
* Learn vector databases (ChromaDB)
* Implement semantic search
* Build a working RAG pipeline
* Develop a ChatGPT-like interface using Streamlit

---

## 🧠 Key Concepts

### 🔹 Embeddings

Numerical representation of text that captures semantic meaning.

### 🔹 Vector Database

Stores embeddings for efficient similarity-based retrieval.

### 🔹 Semantic Search

Search based on meaning rather than exact keywords.

### 🔹 RAG (Retrieval-Augmented Generation)

A pipeline that combines:

* **Retrieve** relevant data
* **Augment** the prompt with context
* **Generate** accurate responses using an LLM

---

## ⚙️ Tech Stack

* Python
* Streamlit (UI)
* ChromaDB (Vector Database)
* Sentence Transformers (Embeddings)
* Groq API (LLM)
* PyPDF (PDF processing)

---

## 🔄 How It Works

1. 📄 Upload PDF document
2. ✂️ Split text into chunks (chunking with overlap)
3. 🔢 Convert chunks into embeddings
4. 🗄️ Store embeddings in ChromaDB
5. 💬 User asks a question
6. 🔍 Retrieve relevant chunks using semantic similarity
7. 🧠 Send context to LLM (Groq)
8. ✨ Generate accurate answer

---

## 🔁 RAG Pipeline

**User Query → Retrieve → Augment → Generate**

---

## 📊 Features

* ✅ ChatGPT-like UI
* ✅ PDF Question Answering
* ✅ Semantic Search
* ✅ Persistent Vector Database
* ✅ Multi-document Support
* ✅ Context-aware Responses
* ✅ Conversation Memory

---

## 📁 Project Structure

```
rag-system/
│── app.py
│── requirements.txt
│── chroma_db/
│── README.md
```

---

## ▶️ Installation

```bash
pip install streamlit chromadb sentence-transformers groq pypdf
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example

**Query:** What is the main topic of the document?
**Answer:** The system retrieves relevant sections and generates a context-based answer.

---

## ⚠️ Limitations

* Basic chunking strategy
* No re-ranking mechanism
* No hybrid search (keyword + vector)

---

## 🚀 Future Improvements

* Add re-ranking for better retrieval
* Implement hybrid search
* Improve chunking strategy
* Deploy application online
* Add support for more file types

---

## 🧠 Conclusion

This project demonstrates how **RAG combines retrieval and generation** to build intelligent AI systems that provide accurate answers using custom data instead of relying solely on pre-trained knowledge.

---

## 🎯 Key Learning

* Practical implementation of RAG
* Understanding embeddings and vector similarity
* Building real-world AI applications
* Integrating LLMs with external data

---

## 👨‍💻 Author

Shashank Alok
M.Sc. Statistics | Aspiring Data Scientist