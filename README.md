#Chat with Your Documents (RAG)
This project enables users to upload PDF, DOCX, or TXT documents and interact with them using Retrieval-Augmented Generation (RAG). It leverages FAISS for vector search and Hugging Face embeddings to retrieve the most relevant document chunks based on user queries.

#How It Works
Upload Documents – Users can upload multiple PDFs, DOCX, or TXT files.
Text Extraction – The script extracts text from the uploaded documents.
Chunking – The extracted text is split into smaller chunks (500 characters with 50 overlap) using RecursiveCharacterTextSplitter.
Embedding Generation – The Hugging Face MiniLM model converts text chunks into vector embeddings.
FAISS Indexing – The chunks are stored in a FAISS vector store for efficient similarity search.
User Query – Users can enter a question related to the documents.
Similarity Search – FAISS retrieves the most relevant text chunks based on the query.
Response Display – The most relevant document snippets are shown as the response.

#Technologies Used
Streamlit – Web UI for document upload & interaction.
FAISS – Efficient vector search for retrieving document chunks.
Hugging Face Embeddings – all-MiniLM-L6-v2 model for text embeddings.
PyPDF2 & python-docx – Extracting text from PDFs and DOCX files.
LangChain – Text processing and chunking.


Install dependencies:

pip install streamlit langchain faiss-cpu sentence-transformers PyPDF2 python-docx
Run the app:

streamlit run app.py
