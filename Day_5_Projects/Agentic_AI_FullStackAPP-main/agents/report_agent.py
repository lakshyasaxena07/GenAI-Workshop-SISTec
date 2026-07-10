from config.llm import llm

def report_agent(state):

    prompt = f"""
    Create final report.

    Roadmap:

    {state['learning_plan']}

    Resources:

    {state['resources']}
    """

    response = llm.invoke(
        prompt
    )

    return {
        "final_report":
        response.content
    }