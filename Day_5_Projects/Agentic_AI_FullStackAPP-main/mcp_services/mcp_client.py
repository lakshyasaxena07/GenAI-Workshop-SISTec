from pathlib import Path

# pyrefly: ignore [missing-import]
from langchain_mcp_adapters.client import (
    MultiServerMCPClient
)

BASE_DIR = Path(__file__).resolve().parent

SERVER_FILE = (
    BASE_DIR /
    "course_mcp_server.py"
)

client = MultiServerMCPClient(
{
    "course_server": {

        "transport": "stdio",

        "command": "python",

        "args": [
            str(SERVER_FILE)
        ]
    }
}
)

course_tool = None


async def initialize_tools():

    global course_tool

    if course_tool:
        return

    tools = await client.get_tools()

    print("\nAvailable MCP Tools:\n")

    for tool in tools:
        print(tool.name)

    course_tool = next(
        t
        for t in tools
        if t.name == "search_course"
    )


async def search_course_mcp(
    topic: str
):

    await initialize_tools()

    result = await course_tool.ainvoke(
        {
            "topic": topic
        }
    )

    return result