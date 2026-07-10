import asyncio

from config.llm import llm

from mcp_services.mcp_client import (
    search_course_mcp
)

from rag.retriever import (
    search_documents
)

def resource_agent(state):

    query = state[
        "user_query"
    ]

    course_info = asyncio.run(
        search_course_mcp(
            "python"
        )
    )

    docs = search_documents(
        query
    )

    context = "\n".join(
        [
            doc.page_content
            for doc in docs
        ]
    )

    prompt = f"""
    User Query:

    {query}

    MCP Course:

    {course_info}

    PDF Knowledge:

    {context}

    Generate study resources.
    """

    response = llm.invoke(
        prompt
    )

    return {
        "resources":
        response.content
    }