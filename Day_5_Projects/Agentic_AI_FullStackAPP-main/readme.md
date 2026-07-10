# 🌐 Agentic AI Full-Stack App

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-LangGraph-purple)](https://langchain-ai.github.io/langgraph/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue)](https://www.postgresql.org/)
[![UI](https://img.shields.io/badge/UI-Streamlit-red)](https://streamlit.io/)

Welcome to the **Agentic AI Full-Stack App**! This project demonstrates a production-grade multi-agent architecture built with **LangGraph**, utilizing a **PostgreSQL** database for persistent state management (checkpointing) and **Streamlit** for the frontend user interface.

## 🚀 Key Features

- **LangGraph State Management**: Employs LangGraph's `PostgresSaver` to persist entire agent conversational states, workflows, and metadata using MessagePack serialization.
- **Multi-Agent Collaboration**: Features distinct agents (e.g., Learning Agent, Resource Agent, Report Agent) collaborating to generate comprehensive outputs (like a learning plan).
- **RAG Integration**: Includes modules for document ingestion and retrieval (`rag/`).
- **Interactive UI**: A Streamlit-based frontend (`frontend.py`) for seamless user interaction.

## 📁 Project Structure

- `frontend.py` / `main.py`: Entry points for the Streamlit UI and CLI applications.
- `agents/`: Contains definitions for the specific LangGraph agents.
- `memory/` & `rag/`: Handles PostgreSQL state checkpointing and Retrieval-Augmented Generation ingestion.
- `config/` & `docs/`: Configuration files and project documentation.
- `mcp_services/`: Demonstrates integration with Model Context Protocol tools.

## 🛠️ Setup & Installation

### 1. PostgreSQL Database Setup
LangGraph requires a PostgreSQL database to store state checkpoints.
1. Download and install [PostgreSQL 17](https://www.postgresql.org/download/windows/).
2. During installation, set the password for the `postgres` user (e.g., `postgres123`).
3. Open **pgAdmin 4**, connect to your server, and create a new database named **`langgraph_db`**.

### 2. Python Environment
```bash
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on macOS/Linux
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Environment Variables
Ensure your `.env` file is properly configured with your Groq API key and database credentials:
```env
GROQ_API_KEY=your_groq_api_key_here
# Add Postgres URI if required by your config
```

## 🏃 Running the Application

1. **Data Ingestion (Optional but recommended for RAG)**:
   ```bash
   python -m rag.ingest
   ```

2. **Launch the Application**:
   - **Streamlit UI**:
     ```bash
     streamlit run frontend.py
     ```
   - **CLI Mode**:
     ```bash
     python main.py
     ```

## 🧠 Understanding LangGraph Checkpointing in Postgres

Unlike traditional chat applications that store row-by-row messages, this application stores the entire state object using LangGraph's `PostgresSaver`.

Key tables created in `langgraph_db`:
- `checkpoints`: Workflow snapshot metadata (thread ID, parent checkpoint).
- `checkpoint_blobs`: Serialized state data (MessagePack).
- `checkpoint_writes`: Incremental updates during node execution (e.g., `user_query` -> `learning_plan` -> `resources` -> `final_report`).