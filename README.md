# 🧠 GenAI & Multi-Agent Workshop (SISTec)

Welcome to the **GenAI and Multi-Agent Systems Workshop** repository! This project serves as a hands-on guide to building custom agent architectures, tool integration, and multi-agent orchestration from scratch using Python, **Groq LLM**, and **Pydantic** for structured output validation.

---

## 🚀 Key Features

* **Custom Agent & Runner Architecture**: Implements lightweight `Agent` and `Runner` classes from scratch without heavy framework overhead.
* **Tool Calling**: Connects LLMs to real-world data (specifically, live weather data via the OpenWeatherMap API).
* **Structured Output**: Guarantees output formats matching Python data structures using Pydantic validation models.
* **Multi-Agent Routing (Supervisor Pattern)**: Orchestrates query delegation between specialized agents (Weather Agent vs. Coding Agent) via a keyword-based supervisor routing logic.

---

## 📁 Repository Structure

```directory
.
├── Day_1/
│   ├── Weather_agent/
│   │   ├── agent.py               # Custom Agent class definition
│   │   ├── tool.py                # OpenWeatherMap tool implementation
│   │   ├── runner.py              # Synchronous runner logic with LLM integration
│   │   ├── main.py                # Entry point for the single weather agent
│   │   └── email_generatrion.py   # Helper script for draft email generation
│   │
│   ├── Multi_Agent/
│   │   ├── agent.py               # Custom base Agent class
│   │   ├── weather_agent.py       # Weather-specific agent instructions
│   │   ├── coding_agent.py        # Coding-specific agent instructions
│   │   ├── tool.py                # Helper tools (weather API query)
│   │   ├── runner.py              # Shared execution runner logic
│   │   └── main.py                # Supervisor/router entry point
│   │
│   └── .env                       # Local API keys (ignored by git)
│
├── .gitignore                     # Git ignore rules for virtual envs and credentials
├── requirements.txt               # Dependencies list
└── README.md                      # Project documentation
```

---

## 🛠️ Setup & Installation

### 1. Clone this Repository
If you haven't cloned this repository yet:
```bash
git clone <your-repository-url>
cd "GenAI Workshop SISTec"
```

### 2. Configure a Virtual Environment
Create and activate a python virtual environment:
```powershell
# Create environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Activate environment (macOS/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a file named `.env` in the `Day_1` directory (or workspace root if run from root) and add your keys:
```env
GROQ_API_KEY=your_groq_api_key_here
weather_api_key=your_openweather_api_key_here
```
> [!IMPORTANT]
> Keep your `.env` file secret! It is already added to `.gitignore` to prevent committing it to GitHub.

---

## 🏃 Running the Code

### Single Agent (Weather Agent)
Run the Weather Agent to query live weather data with dynamic tool execution:
```bash
python Day_1/Weather_agent/main.py
```
* **Process Flow**:
  1. Prompts for a city name.
  2. Resolves the request using the OpenWeatherMap API tool.
  3. Formats results using Groq LLM under a strict Pydantic JSON template.

### Multi-Agent Routing System
Run the supervisor agent router to delegate queries automatically:
```bash
python Day_1/Multi_Agent/main.py
```
* **Process Flow**:
  1. Prompts for a general query.
  2. Uses supervisor keyword detection to route to the **Weather Agent** or the **Coding Agent**.
  3. Executes the selected agent using the runner.
