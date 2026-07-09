# 🔌 Model Context Protocol (MCP) Examples

[![Architecture](https://img.shields.io/badge/Architecture-Client%2FServer-blue)](https://github.com)
[![Protocol](https://img.shields.io/badge/Protocol-MCP-orange)](https://github.com)

Welcome to the **Model Context Protocol (MCP)** project! This folder explores building decoupled tool-provisioning systems using the FastMCP framework, allowing AI agents to securely interact with remote tools, databases, and APIs.

## 🚀 Key Features

- **Client-Server Architecture**: Separates the execution of tools (Server) from the LLM routing logic (Client).
- **FastMCP Integration**: Uses `FastMCP` to quickly wrap standard Python functions into discoverable MCP tools.
- **Database & Local Contexts**: Demonstrates providing access to static dictionaries (employees) and simulated database interactions securely over the protocol.

## 📁 Folder Structure

- `MCP_1` / `MCP_2` / `MCP_Example3_DB`: Contain progressively advanced examples of client-server setups.
- `server.py`: Defines the FastMCP server, exposing tools like `add` and `get_employee`.
- `client.py`: The consumer application that connects to the server and feeds the tool outputs into an LLM interaction loop.

## 🛠️ Setup & Execution

1. **Install Dependencies**: Ensure dependencies inside the folder are installed.
   ```bash
   pip install -r requirements.txt
   ```
2. **Environment Variables**: Include your LLM API keys in the `.env` file.
3. **Execution**: Typically requires starting the server and then initiating the client. Ensure to check individual subfolders for specific run commands.
