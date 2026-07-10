import asyncio

from mcp_services.mcp_client import (
    search_course_mcp
)

async def main():

    result = await search_course_mcp(
        "python"
    )

    print(result)

asyncio.run(main())