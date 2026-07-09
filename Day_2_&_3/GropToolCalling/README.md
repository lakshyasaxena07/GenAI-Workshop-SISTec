# 🛠️ Native Groq Tool Calling

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![SDK](https://img.shields.io/badge/SDK-OpenAI%20Python-orange)](https://github.com/openai/openai-python)
[![LLM](https://img.shields.io/badge/LLM-Groq-green)](https://groq.com/)

Welcome to the **Native Groq Tool Calling** project! This folder demonstrates how to integrate native function calling using Groq's high-speed inference engine, wrapped within the standard OpenAI Python SDK syntax.

## 🚀 Key Features

- **Standardized Schemas**: Defines JSON function schemas (`weather_tool`) to formally introduce capabilities to the LLM.
- **Message Chaining**: Shows the exact message chain required for tool execution: `User -> LLM -> Tool Call -> Tool Result -> Final Answer`.
- **OpenAI Client**: Utilizes the familiar `openai.OpenAI` client by overriding the base URL to point to Groq's API endpoint (`https://api.groq.com/openai/v1`).

## 📁 File Structure

- `tool.py`: Contains the `get_current_weather` implementation interacting with the OpenWeatherMap API.
- `main.py`: The core script that defines the tool schema, interacts with the LLM, parses the tool call request, executes the local python function, and returns the result to the LLM.
- `requirements.txt`: Lightweight dependencies specifically for this tool calling demo.

## 🛠️ Setup & Execution

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables**: Ensure your `.env` is configured:
   ```env
   GROQ_API_KEY=your_groq_api_key
   weather_api_key=your_openweathermap_api_key
   ```
3. **Run the Demo**:
   ```bash
   python main.py
   ```
