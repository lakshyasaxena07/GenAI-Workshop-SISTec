import asyncio
import sys

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():

    server_params = StdioServerParameters(
        command=sys.executable, 
        args=["server.py"]
        )

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            print("Connected!\n")

            tools = await session.list_tools()

            print("Available tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            print("\nCalling get_user()...")

            result = await session.call_tool("get_user", {"user_id": 1})

            print("Result:", result.content[0].text)

            print("\nCalling get_user()...")

            result = await session.call_tool("get_user", {"user_id": 2})

            print("Result:", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
