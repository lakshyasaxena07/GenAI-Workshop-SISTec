# 🤖 Multi-Agent Supervisor Router

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Supervisor%20Routing-purple)](https://github.com)

Welcome to the **Multi-Agent Supervisor Router** project! This project demonstrates how to coordinate multiple specialized AI agents using a central router, built entirely from scratch.

## 🚀 Key Features

- **Domain-Specific Agents**: Features specialized agents (e.g., Weather Agent and Coding Agent) equipped with domain-specific tools and prompts.
- **Supervisor Routing**: A keyword-based routing mechanism analyzes user intents and dynamically delegates the task to the most appropriate agent.
- **Custom Orchestration**: Avoids heavy agentic frameworks by implementing a lightweight, transparent execution engine.

## 📁 File Structure

- `agent.py`: Base definitions for the agents.
- `weather_agent.py` & `coding_agent.py`: Specialized instructions and configurations for individual domains.
- `tool.py`: Helper functions (such as weather API requests) provided to the agents.
- `runner.py`: The shared execution engine that processes tool calls and generates final answers.
- `main.py`: The supervisor entry point that intercepts the user's prompt and routes it accordingly.

## 🛠️ Setup & Execution

1. **Install Dependencies**: Make sure you have installed the root `requirements.txt`.
2. **Environment Variables**: Configure your `.env` with:
   ```env
   GROQ_API_KEY=your_groq_api_key
   weather_api_key=your_openweathermap_api_key
   ```
3. **Run the Router**:
   ```bash
   python main.py
   ```
