import asyncio
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()


async def main():

    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    client = MultiServerMCPClient(
        {
            "employee_db": {
                "command": "python",
                "args": ["server.py"],
                "transport": "stdio"
            }
        }
    )

    tools = await client.get_tools()
    # print("\nLoaded Tools")
    # print("=" * 50)

    # for tool in tools:
    #     print(tool.name)
    #     print(tool.description)
    #     print("=" * 50)

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    while True:

        question = input("\nYou : ")

        if question.lower() == "exit":
            break

        response = await agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        print("\nAssistant :")
        print(response["messages"][-1].content)


asyncio.run(main())