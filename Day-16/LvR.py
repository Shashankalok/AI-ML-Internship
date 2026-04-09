import streamlit as st
from groq import Groq
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import uuid

# 
#  Setup
# 
st.set_page_config(page_title="Production RAG", layout="wide")
st.title("🚀 RAG Chatbot with Comparison")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Persistent ChromaDB
client_db = chromadb.Client(
    Settings(persist_directory="./chroma_db")
)

collection = client_db.get_or_create_collection(name="rag_collection")

#  Add your Groq API key here
groq_client = Groq(api_key="Aki key")

# 
#  Functions
#

# PDF Loader
def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

# Chunking with overlap
def chunk_text(text, chunk_size=200, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# Store documents
def store_documents(text, source="pdf"):
    chunks = chunk_text(text)

    if not chunks:
        st.error("No text found in PDF")
        return

    embeddings = model.encode(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=[{"source": source}] * len(chunks),
        ids=[str(uuid.uuid4()) for _ in chunks]
    )

# Retrieve context
def retrieve_context(query):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )

    if not results['documents'] or not results['documents'][0]:
        return "No relevant data found."

    return "\n".join(results['documents'][0])

# RAG Response
def generate_response(query, context, history):
    prompt = f"""
You are an expert AI assistant.

Rules:
- Answer ONLY from the provided context
- Be clear and structured
- If answer not found, say "I don't know"

Conversation History:
{history}

Context:
{context}

Question:
{query}

Answer:
"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

#  Direct LLM (NO RAG)
def direct_llm(query):
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": query}]
    )
    return response.choices[0].message.content

# -------------------------------
# 🔹 Sidebar (PDF Upload)
# -------------------------------
st.sidebar.header("📄 Upload PDFs")

uploaded_files = st.sidebar.file_uploader(
    "Upload documents", type="pdf", accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        text = load_pdf(file)

        if text.strip():
            store_documents(text, source=file.name)
        else:
            st.sidebar.error(f"No text in {file.name}")

    st.sidebar.success("✅ Documents indexed!")

# -------------------------------
# 🔹 Chat System
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input
query = st.chat_input("Ask something...")

if query:
    # Show user message
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Retrieve context
    context = retrieve_context(query)

    # Prepare history
    history = "\n".join([m["content"] for m in st.session_state.messages])

    try:
        # RAG Answer
        rag_answer = generate_response(query, context, history)

        # Direct LLM Answer
        direct_answer = direct_llm(query)

    except Exception as e:
        rag_answer = f"Error: {str(e)}"
        direct_answer = "Error"

    # Show comparison
    st.chat_message("assistant").write("### ✅ RAG Answer")
    st.write(rag_answer)

    st.chat_message("assistant").write("### ⚠️ Direct LLM Answer")
    st.write(direct_answer)

    # Save RAG answer in history
    st.session_state.messages.append({"role": "assistant", "content": rag_answer})
