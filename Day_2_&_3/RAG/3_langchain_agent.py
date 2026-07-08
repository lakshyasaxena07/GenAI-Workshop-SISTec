import os
import requests  # noqa: F401
import datetime

import pandas as pd
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq


load_dotenv()

# -------------------------------------------
# Tool 1: Get current date and time
# -------------------------------------------

@tool
def get_current_time(dummy: str="") -> str:
    """return current date and time"""
    return str(datetime.datetime.now())


# -------------------------------------------
# Tool 2: Simple calculator
# -------------------------------------------

@tool
def calculator(expression: str) -> str:
    """Evaluate a mathematical expression and return the result."""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"

# -------------------------------------------
# Tool 3: CSV analyzer
# -------------------------------------------

file_path="data/sample.csv"
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "data", "Sample.csv")  # Default path if not set in .env


@tool
def analyse_csv(dummy: str="") -> str:
    """Reads a CSV file and returns column average"""
    try:
        df = pd.read_csv(file_path)
        numeric_means = df.mean(numeric_only=True)
        return numeric_means.to_string()
    except Exception as e:
        return f"Error  reading CSV: {str(e)}"
    
# -------------------------------------------
# Memory
# -------------------------------------------

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)


# -------------------------------------------
# Groq Model
# -------------------------------------------
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing GROQ_API_KEY. Add it to your environment or .env file before running this script."
    )

llm=ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile",
    temperature=0
)

# -------------------------------------------
# Tools
# -------------------------------------------

tools=[
    get_current_time,
    calculator,
    analyse_csv
]

# -------------------------------------------
# Prompt
# -------------------------------------------


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that can provide current date and time, perform calculations, and analyze CSV files.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# -------------------------------------------
# Agent Create
# -------------------------------------------

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# -------------------------------------------
#   Agent Executor
# -------------------------------------------

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True)


# -------------------------------------------
#   chat loop
# -------------------------------------------


print("\n\nAdvanced langchain + Groq Agent started\n")
print("type 'exit' to stop\n")

while True:
    user_input = input("Ask a question : ")
    if user_input.lower() == "exit":
        print("Exiting the chat...")
        break

    response = agent_executor.invoke(
        {"input": user_input})
    print(f"Agent: {response['output']}\n")
    print("--------------------------------------------------\n")
    print("type 'exit' to stop\n")
    print("--------------------------------------------------\n")