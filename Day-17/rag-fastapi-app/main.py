from fastapi import FastAPI, UploadFile, File
from PyPDF2 import PdfReader
import docx
import numpy as np
import faiss
from groq import Groq
import uuid
from datetime import datetime

app = FastAPI()

#  Global storage
model = None
index = None
stored_chunks = []
documents = {}
history = []

#  Groq client (API KEY)
client = Groq(api_key="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")

# File validation
ALLOWED_TYPES = [".pdf", ".txt", ".docx"]
MAX_SIZE = 5 * 1024 * 1024  # 5MB


# Load embedding model (lazy loading)
def load_model():
    global model
    if model is None:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


#  Home route
@app.get("/")
def home():
    return {"message": "RAG App is running 🚀"}


#  PDF reader
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


#  DOCX reader
def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text


#  Chunking
def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


#  Embeddings
def create_embeddings(chunks):
    model = load_model()
    embeddings = model.encode(chunks, batch_size=8, show_progress_bar=False)
    return np.array(embeddings)


#  Upload API (store embeddings)
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global index, stored_chunks

    filename = file.filename

    #  Validate file type
    if not any(filename.endswith(ext) for ext in ALLOWED_TYPES):
        return {"error": "Invalid file type"}

    #  Read content (for size check)
    content = await file.read()

    if len(content) > MAX_SIZE:
        return {"error": "File too large"}

    # Reset file pointer
    file.file.seek(0)




    if filename.endswith(".txt"):
        text = content.decode("utf-8")

    elif filename.endswith(".pdf"):
        text = read_pdf(file.file)

    elif filename.endswith(".docx"):
        text = read_docx(file.file)

    else:
        return {"error": "Unsupported file type"}

    # Chunking
    chunks = chunk_text(text)
    embeddings = create_embeddings(chunks)

    # Initialize FAISS
    dimension = embeddings.shape[1]
    if index is None:
        index = faiss.IndexFlatL2(dimension)


    # Create document ID
    doc_id = str(uuid.uuid4())

    # Store metadata
    documents[doc_id] = {
        "filename": filename,
        "num_chunks": len(chunks)
    }

    # Store chunks with metadata
    for i, chunk in enumerate(chunks):
        stored_chunks.append({
            "doc_id": doc_id,
            "chunk_id": i,
            "text": chunk
        })

    # Add embeddings
    index.add(embeddings)

    return {
    "message": "Document uploaded successfully",
    "document_id": doc_id,
    "filename": filename,
    "total_chunks": len(chunks),
    "embedding_vectors_created": len(embeddings),
    "sample_chunk": chunks[0] if chunks else ""
}


#  Generate answer using LLM
def generate_answer(context, question):
    try:
        prompt = f"""
        Answer the question based ONLY on the context below.

        Context:
        {context}

        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ updated working model
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}"


#  Query API
@app.post("/query")
async def query(question: str):
    global index, stored_chunks

    if index is None:
        return {"error": "No documents uploaded yet"}

    try:
        model = load_model()

        # Convert question to embedding
        query_embedding = model.encode([question])
        query_embedding = np.array(query_embedding)

        # Search similar chunks
        k = 3
        distances, indices = index.search(query_embedding, k)

        retrieved_chunks = [stored_chunks[i]["text"] for i in indices[0]]

        # Combine context
        context = "\n".join(retrieved_chunks)

        # Generate answer
        answer = generate_answer(context, question)


        #  Save history
        history.append({
            "question": question,
            "answer": answer,
            "time": str(datetime.now())
        })

        return {
            "question": question,
            "answer": answer,
            "source_chunks": retrieved_chunks
        }

    except Exception as e:
        return {"error": str(e)}



        #  Get all documents
@app.get("/documents")
def get_documents():
    return documents


#  Delete document
@app.delete("/document/{doc_id}")
def delete_document(doc_id: str):
    global documents

    if doc_id not in documents:
        return {"error": "Document not found"}

    del documents[doc_id]

    return {"message": "Document deleted"}


#  Get history
@app.get("/history")
def get_history():
    return history