# 🌤️ Custom Weather Agent

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![LLM Provider](https://img.shields.io/badge/LLM-Groq-orange?logo=google-cloud)](https://groq.com/)
[![Validation](https://img.shields.io/badge/Validation-Pydantic-green)](https://docs.pydantic.dev/)

Welcome to the **Custom Weather Agent** project! This folder demonstrates how to build an AI agent entirely from scratch without relying on heavy frameworks like LangChain.

## 🚀 Key Features

- **Custom Run-Loop**: Implements a `Runner` class that manages the conversation and tool execution loop.
- **API Integration**: Fetches real-time weather data using the OpenWeatherMap API.
- **Structured Output**: Enforces strict JSON output formatting using Pydantic, ensuring predictable responses for downstream applications.
- **Groq LLM**: Utilizes ultra-fast inference via Groq to power the agent's decision-making.

## 📁 File Structure

- `agent.py`: Defines the Agent schema and system prompts.
- `tool.py`: Contains the actual Python function that queries the OpenWeatherMap API.
- `runner.py`: The core execution engine that loops through LLM thoughts, tool executions, and final responses.
- `main.py`: The entry point to run the interactive agent.

## 🛠️ Setup & Execution

1. **Install Dependencies**: Ensure you have installed the root `requirements.txt`.
2. **Environment Variables**: Create a `.env` file containing:
   ```env
   GROQ_API_KEY=your_groq_api_key
   weather_api_key=your_openweathermap_api_key
   ```
3. **Run the Agent**:
   ```bash
   python main.py
   ```
