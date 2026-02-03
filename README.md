

# QA System using LlamaIndex and Google Gemini

This project implements a **Question Answering (QA) system** using **LlamaIndex** and **Google Gemini**. It enables users to ask natural language questions and receive accurate, context-aware answers from a set of documents by combining **semantic retrieval** with **LLM-based reasoning**.

The project demonstrates a practical **Retrieval-Augmented Generation (RAG)** pipeline, commonly used in real-world AI applications such as document assistants, internal knowledge bases, and intelligent search systems.

---

## Project Overview

The system first indexes documents using LlamaIndex, converting text into embeddings for efficient semantic search. When a user submits a query, the most relevant document chunks are retrieved and provided as context to the Gemini language model, which then generates a precise and meaningful response.

This approach significantly improves answer quality compared to traditional keyword-based search systems.

---

## Architecture & Workflow

1. **Document Loading**
   * Text documents are loaded from the local data source.

2. **Chunking & Indexing**

   * Documents are split into smaller chunks.
   * Chunks are converted into embeddings using LlamaIndex.
   * Embeddings are stored in a vector index.

3. **Query Processing**

   * User queries are matched semantically with indexed content.
   * Relevant chunks are retrieved based on similarity.

4. **Answer Generation**

   * Retrieved context is passed to Google Gemini.
   * Gemini generates a context-aware natural language answer.

---

## Key Features

* Retrieval-Augmented Generation (RAG) implementation
* Semantic document search using embeddings
* Integration with Google Gemini LLM
* Modular and extensible project structure
* Suitable for real-world AI knowledge systems

---

## Technologies Used

* Python
* LlamaIndex
* Google Gemini API
* Natural Language Processing (NLP)
* Vector embeddings and semantic search

---

## Installation

```bash
git clone https://github.com/Luciesprogram/QA_with_llamaindex_gemini.git
cd QA_with_llamaindex_gemini
pip install -r requirements.txt
```

Set your Gemini API key:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

---

## Usage

1. Place your text documents inside the data directory.
2. Run the indexing process to build the vector index.
3. Execute the application and ask questions.

Example:

```bash
python main.py
```

---

## Learning Outcomes

This project helped me gain hands-on experience with:

* Building Retrieval-Augmented Generation (RAG) systems
* Working with Large Language Model APIs
* Semantic search using vector embeddings
* Designing end-to-end AI pipelines
* Applying AI concepts to real-world document QA problems

---

## Future Enhancements

* Support for PDF and web-based documents
* Persistent vector storage (FAISS / ChromaDB)
* Web interface using Streamlit or FastAPI
* Improved response ranking and confidence scoring

---

## Author

**Vikrant Singh**
GitHub: [https://github.com/Luciesprogram](https://github.com/Luciesprogram)

---

