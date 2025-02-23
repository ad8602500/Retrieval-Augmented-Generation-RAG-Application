import os
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer

# Set up Streamlit UI
st.title("Chat with Your Documents (RAG)")

# File uploader for multiple documents
uploaded_files = st.file_uploader("Upload Documents (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"], accept_multiple_files=True)


def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    elif file.name.endswith(".docx"):
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file.name.endswith(".txt"):
        text = file.read().decode("utf-8")
    return text

if uploaded_files:
    documents = []
    
  
    for file in uploaded_files:
        text = extract_text(file)
        documents.append(text)

   
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.create_documents(documents)

    # Use Hugging Face model for embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

   
    vector_store = FAISS.from_documents(chunks, embeddings)

    st.success("Documents processed successfully! You can now chat with them.")

    # Query input from user
    query = st.text_input("Ask something about the documents:")
    
    if query:
        docs = vector_store.similarity_search(query, k=5)
        response = "\n".join([doc.page_content for doc in docs])
        st.write("### Response:", response)



