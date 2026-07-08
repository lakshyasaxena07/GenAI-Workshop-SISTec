"""
Assignment 4: AI Financial Advisor
Dataset
Bank CSV
Features
•	Expense Analysis
•	Monthly Savings
•	Spending Categories
•	Budget Suggestions
Prompt
Analyze my expenses.

Where am I spending the most?
"""

from dotenv import load_dotenv

import os
import requests     # noqa: F401
import pandas as pd
import matplotlib.pyplot as plt
import smtplib  # noqa: F401
from email.message import EmailMessage  # noqa: F401

from langchain_groq import ChatGroq
from langchain_core.tools import tool

from langchain.agents import AgentExecutor, create_tool_calling_agent

from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain.memory import ConversationBufferMemory

load_dotenv(override=True)


# --------------------------------------
# TOOL 1 - Check Bank Data
# --------------------------------------
@tool
def check_bank_data(dummy: str = "") -> str:
    """
    Checks if the bank CSV file exists.
    """
    file_path = "data/bank_data.csv"
    if os.path.exists(file_path):
        return f"{file_path} is available."
    return "bank data not found."


# --------------------------------------
# TOOL 2 - Expense Analysis
# --------------------------------------
@tool
def analyze_expenses(file_path: str = "data/bank_data.csv") -> str:
    """
    Analyzes expenses from the bank CSV file.
    """
    df = pd.read_csv(file_path)
    expenses = df[df["Type"] == "Debit"]
    total_expenses = expenses["Amount"].sum()
    summary = expenses.describe().to_string()
    return f"Total Expenses: {total_expenses}\nExpense Summary:\n{summary}"


# --------------------------------------
# TOOL 3 - Monthly Savings
# --------------------------------------
@tool
def calculate_monthly_savings(file_path: str = "data/bank_data.csv") -> str:
    """
    Calculates monthly savings from the bank CSV file.
    """
    df = pd.read_csv(file_path)
    total_income = df[df["Type"] == "Credit"]["Amount"].sum()
    total_expenses = df[df["Type"] == "Debit"]["Amount"].sum()
    savings = total_income - total_expenses
    return f"Total Income: {total_income}\nTotal Expenses: {total_expenses}\nMonthly Savings: {savings}"


# --------------------------------------
# TOOL 4 - Spending Categories
# --------------------------------------
@tool
def categorize_spending(file_path: str = "data/bank_data.csv") -> str:
    """
    Analyzes spending categories and creates a pie chart.
    """
    df = pd.read_csv(file_path)
    expenses = df[df["Type"] == "Debit"].copy()
    category_sums = expenses.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(
        category_sums, labels=category_sums.index, autopct="%1.1f%%", startangle=140
    )
    plt.title("Spending Categories")
    
    os.makedirs("output", exist_ok=True)
    plt.savefig("output/spending_chart.png")
    plt.close()

    return f"Spending by Category:\n{category_sums.to_string()}\nChart saved as output/spending_chart.png"


# --------------------------------------
# TOOL 5 - Budget Suggestions
# --------------------------------------
@tool
def suggest_budget(file_path: str = "data/bank_data.csv") -> str:
    """
    Provides budget suggestions based on spending categories.
    """
    df = pd.read_csv(file_path)
    expenses = df[df["Type"] == "Debit"].copy()
    category_sums = expenses.groupby("Category")["Amount"].sum()

    suggestions = "Budget Suggestions based on your spending:\n"
    for category, amount in category_sums.items():
        if category == "Food" and amount > 4000:
            suggestions += "- Your food expenses are high. Consider meal planning to reduce costs.\n"
        elif category == "Entertainment" and amount > 1000:
            suggestions += "- Your entertainment expenses are a bit high. Look for free or low-cost activities.\n"
        elif category == "Rent" and amount > 20000:
            suggestions += "- Housing takes up a large portion of your budget. Ensure you have emergency savings.\n"

    if len(suggestions.split("\n")) <= 2:
        suggestions += (
            "- Your spending looks well-balanced across categories. Continue saving!\n"
        )

    return suggestions


# --------------------------------------
# TOOL 6 - Save Report
# --------------------------------------
@tool
def save_report(content: str) -> str:
    """
    Saves a text report of the financial analysis.
    """
    os.makedirs("output", exist_ok=True)
    with open("output/financial_report.txt", "w") as f:
        f.write(content)
    return "Report saved successfully to output/financial_report.txt"


# --------------------------------------
# MEMORY
# --------------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


# --------------------------------------
# GROQ MODEL
# --------------------------------------
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


# --------------------------------------
# TOOLS
# --------------------------------------
tools = [
    check_bank_data,
    analyze_expenses,
    calculate_monthly_savings,
    categorize_spending,
    suggest_budget,
    save_report,
]


# --------------------------------------
# PROMPT
# --------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an Autonomous Workflow AI Agent acting as a Financial Advisor.

You can:
- check if bank data is available
- analyze expenses
- calculate monthly savings
- categorize spending and create charts
- suggest budgets
- save final reports to the output folder
- execute tasks step-by-step autonomously

Always use the available tools whenever required to help the user manage their finances.
""",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)


# --------------------------------------
# CREATE AGENT
# --------------------------------------
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)


# --------------------------------------
# AGENT EXECUTOR
# --------------------------------------
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)


# --------------------------------------
# CHAT LOOP
# --------------------------------------
print("\nAutonomous Workflow Agent (Financial Advisor) Started")
print("Type 'exit' to stop\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye")
        break

    response = agent_executor.invoke({"input": user_input})

    print("\nAgent Response:")
    print("--------------------------------")
    print(response["output"])
    print("--------------------------------\n")
