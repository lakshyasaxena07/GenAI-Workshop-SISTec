# 🧠 LangChain RAG & Autonomous Workflow Agents

[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://python.langchain.com/)
[![Embeddings](https://img.shields.io/badge/Embeddings-HuggingFace-yellow)](https://huggingface.co/)
[![VectorDB](https://img.shields.io/badge/VectorDB-FAISS-blue)](https://github.com/facebookresearch/faiss)

Welcome to the **RAG & Autonomous Agents** project! This folder constitutes the advanced sections of the workshop, covering both document-based Retrieval-Augmented Generation (RAG) pipelines and stateful autonomous `AgentExecutor` workflows.

## 🚀 Key Features

### 1. Retrieval-Augmented Generation (RAG)
- **Multi-Format Document Loaders**: Integrates LangChain loaders for Plain Text, PDF, JSON, and live Web Pages (Browserbase).
- **External API Semantic Search**: Vectors dummy user data and posts from external JSON APIs to enable natural language semantic querying.
- **Local Embedding Stack**: Uses `sentence-transformers/all-MiniLM-L6-v2` and `FAISS` for fast, local vectorization and similarity search.

### 2. Autonomous Workflow Agents
- **LangChain Tool Calling**: Leverages `create_tool_calling_agent` and `AgentExecutor` to build loop-driven, self-correcting agents.
- **AI Financial Advisor**: Parses CSV transaction data, calculates savings, plots spending pie charts, and generates budget reports.
- **Sales Data Analyzer**: Downloads sales datasets from Google Drive, plots trends, and autonomously emails the report via SMTP SSL.

## 📁 File Structure

- **RAG Pipelines**:
  - `2_Rag_ReadTxt.py` / `2_Rag_ReadPDF.py` / `2_Rag_ReadJson.py` / `2_Rag_ReadWebPage.py`
  - `2_rag_api.py` / `2_movie_recommendation.py`
- **Agent Workflows**:
  - `3_AI_Financial_Advisor.py`: Autonomous budget analysis agent.
  - `3_langchain_agent.py`: Math, date, and general utility agent.
  - `3_sales_Analyzer.py`: Automated CSV plotting and email reporting agent.
- `data/`: Contains CSVs, PDFs, Text, and JSON files used for RAG and agent queries.

## 🛠️ Setup & Execution

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables**: Configure your `.env` (note the added SMTP credentials for the Sales Analyzer):
   ```env
   GROQ_API_KEY=your_groq_api_key
   EMAIL_USER=your_gmail_address
   EMAIL_PASSWORD=your_gmail_app_password
   ```
3. **Run Scripts**:
   ```bash
   python 2_Rag_ReadPDF.py
   # Or
   python 3_AI_Financial_Advisor.py
   ```
