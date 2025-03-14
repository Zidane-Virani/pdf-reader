# PDF Query App

## 📖 Overview
PDF Query App is an intelligent document reader that allows users to upload PDFs and ask questions about their content. Powered by **React (TypeScript)** on the frontend and **Flask, LangChain, Pinecone, Redis, and Langfuse** on the backend, the app provides an interactive and efficient way to search and retrieve information from PDF documents.

---

## 🚀 Features
- 📂 **Upload PDFs** – Drag and drop or select files to upload.
- 🔍 **Query PDFs** – Ask natural language questions and get precise answers.
- ⚡ **Fast Response Time** – Optimized retrieval using **Pinecone** for vector storage.
- 🧠 **AI-Powered Search** – Uses **LangChain** for intelligent document parsing.
- 🎯 **Session Management** – Efficient query caching with **Redis**.
- 📊 **Usage Analytics** – Track performance and user queries with **Langfuse**.

---

## 🛠️ Tech Stack
### **Frontend:**
- **React** (TypeScript) – Modern UI framework
- **Tailwind CSS** – Styling
- **React Query** – Data fetching and caching

### **Backend:**
- **Flask** – Lightweight API server
- **LangChain** – Natural language processing and document querying
- **Pinecone** – Vector database for fast similarity search
- **Redis** – Caching layer for queries
- **Langfuse** – Logging and observability for LLM interactions

---

## 🎯 Installation & Setup

### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf-query-app.git
   cd pdf-query-app/backend


Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Set up environment variables:


OPENAI_API_KEY = 


SECRET_KEY=


SQLALCHEMY_DATABASE_URI=

UPLOAD_URL=

 
REDIS_URI=

PINECONE_API_KEY= 

PINECONE_ENV_NAME=

PINECONE_INDEX_NAME=
 
LANGFUSE_PUBLIC_KEY= 

LANGFUSE_SECRET_KEY= 

PYTHONIOENCODING = utf-8


Run the Flask server:
python app.py
