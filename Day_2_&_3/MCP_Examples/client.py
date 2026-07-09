import asyncio

from mcp import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    server_params = StdioServerParameters(command="python", args=["server.py"])

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            print("Connected!\n")

            tools = await session.list_tools()

            print("Available tools:")
            for tool in tools.tools:
                print(f"- {tool.name}")

            print("\nCalling add()...")

            result = await session.call_tool("add", {"a": 10, "b": 20})

            print("Result:", result.content[0].text)

            print("\nCalling get_employee()...")

            result = await session.call_tool("get_employee", {"emp_id": 102})

            print("Result:", result.content[0].text)


if __name__ == "__main__":
    asyncio.run(main())
