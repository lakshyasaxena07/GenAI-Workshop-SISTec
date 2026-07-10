from config.llm import llm

def learning_agent(state):

    prompt = f"""
    Create learning roadmap.

    Topic:

    {state['user_query']}
    """

    response = llm.invoke(
        prompt
    )

    return {
        "learning_plan":
        response.content
    }