# Local RAG System

## Overview

This project is a Retrieval-Augmented Generation (RAG) system built using LlamaIndex, ChromaDB, HuggingFace Embeddings, and Ollama.

The system processes documents by:

1. Loading and splitting documents into chunks.
2. Converting chunks into vector embeddings using HuggingFace models.
3. Storing embeddings in a persistent ChromaDB vector database.
4. Retrieving relevant context based on a user's query.
5. Generating grounded responses using a locally hosted LLM through Ollama.

## Technologies Used

* Python
* LlamaIndex
* ChromaDB
* HuggingFace Embeddings
* Ollama

## Prerequisites

Before running the project, install:

* Python 3.11+
* Ollama
* Required Python dependencies

Install Ollama and download your preferred model:

```bash
ollama pull llama3
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

### 1. Add Documents

Place your documents inside:

```text
data/raw_docs/
```

### 2. Build the Vector Database

```bash
python ingest.py
```

This will:

* Load documents
* Split them into chunks
* Generate embeddings
* Store vectors in ChromaDB

### 3. Start the Chat Application

```bash
python app.py
```

Example:

```text
Ask: What is randomness?
```

## Project Structure

```text
.
├── app.py
├── ingest.py
├── data
│   └── raw_docs
├── rag_engine
│   ├── ingestion
│   ├── llm
│   ├── memory
│   ├── vectorstore
│   └── config.py
└── vector_db
```

## Notes

* Run `ingest.py` whenever documents are added or modified.
* The vector database is stored locally using ChromaDB.
* All inference runs locally through Ollama.
* This project was built as a learning project to understand the fundamentals of Retrieval-Augmented Generation (RAG) systems.

