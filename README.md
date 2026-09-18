# 🤖 Natural Language Text-to-Query RAG System

An AI-powered application that allows users to query databases using natural language instead of writing SQL manually.

**Python • RAG • LLMs • NLP • SQL • LangChain**

## Overview

The Natural Language Text-to-Query RAG System is an AI-powered application that enables users to interact with databases using natural language queries instead of manually writing SQL statements.

The system combines **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and **Natural Language Processing (NLP)** techniques to understand user queries, retrieve relevant database context, generate accurate SQL queries, execute them, and return meaningful responses.

The goal of this project is to simplify data access by allowing non-technical users to retrieve insights from structured databases through conversational interactions.

---

## Problem Statement

Traditional database interaction requires users to have SQL knowledge. Business users and analysts often depend on technical teams to write queries and extract information.

This project addresses this challenge by providing a natural language interface that converts user questions into executable database queries while maintaining accuracy through context retrieval.

---

## Features

### Natural Language Query Processing

* Allows users to ask questions in plain English.
* Converts natural language instructions into structured SQL queries.
* Eliminates the need for manual query writing.

### Retrieval-Augmented Generation Pipeline

* Retrieves relevant database schema information before query generation.
* Provides contextual information to the language model.
* Reduces incorrect query generation and hallucination.

### Automated SQL Generation

* Understands user intent.
* Identifies relevant tables and columns.
* Generates optimized SQL queries.
* Executes queries against connected databases.

### Result Interpretation

* Converts raw database outputs into understandable responses.
* Provides concise explanations and insights from retrieved data.

### Conversational Query Support

* Supports follow-up questions.
* Maintains context for improved user interaction.

---

## System Architecture

```
User Input
    |
    v
Natural Language Understanding
    |
    v
Schema Retrieval using RAG
    |
    v
Context Augmentation
    |
    v
LLM-based SQL Generation
    |
    v
SQL Query Execution
    |
    v
Result Processing
    |
    v
Natural Language Response
```

---

## Technology Stack

### Programming Language

* Python

### Backend Framework

* Flask / FastAPI

### Artificial Intelligence

* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Natural Language Processing

### RAG Components

* LangChain
* Embedding Models
* Vector Search

### Vector Database

* FAISS / ChromaDB

### Database

* MySQL
* PostgreSQL
* SQLite

### Data Processing

* Pandas
* NumPy

### Development Tools

* VS Code
* Git
* GitHub

---

## Project Structure

```
Natural-Language-Text-to-Query-RAG/

│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── rag/
│   │   ├── retriever.py
│   │   ├── embeddings.py
│   │   └── vector_store.py
│   │
│   ├── query_engine/
│   │   ├── sql_generator.py
│   │   └── query_executor.py
│   │
│   ├── database/
│   └── utils/
│
├── frontend/
│
├── data/
│   └── schema_information.json
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation and Setup

### Clone Repository

```bash
git clone https://github.com/yourusername/Natural-Language-Text-to-Query-RAG.git

cd Natural-Language-Text-to-Query-RAG
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file:

```
LLM_API_KEY=your_api_key
DATABASE_URL=your_database_connection
VECTOR_DB_PATH=./vector_store
```

---

## Running the Application

Start the backend server:

```bash
python app.py
```

The application will be available at:

```
http://localhost:5000
```

---

## Example Workflow

### User Query

```
Find the top five customers based on total purchase amount.
```

### Generated SQL Query

```sql
SELECT customer_name, SUM(amount) AS total_purchase
FROM transactions
GROUP BY customer_name
ORDER BY total_purchase DESC
LIMIT 5;
```

### Final Response

```
The top five customers based on total purchase amount are displayed with their respective values.
```

---

## Applications

* Business intelligence systems
* Data analytics platforms
* Self-service reporting tools
* Enterprise database assistants
* Automated data exploration systems

---

## Future Enhancements

* Support for multiple database connections
* Query optimization using AI agents
* Data visualization generation
* Voice-based database interaction
* Domain-specific fine-tuned models
* Role-based access management

---

## Project Objective

The objective of this project is to build an intelligent interface that enables users to access and analyze structured data efficiently through natural language communication, reducing dependency on manual SQL query development.

---

## Author

**Natali Sonawane**

B.E. Information Technology

