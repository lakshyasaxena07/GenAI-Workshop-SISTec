from config.llm import llm

def quiz_agent(state):

    print("\n[Quiz Agent Running]\n")

    prompt = f"""
    Create 5 MCQ Questions.

    Learning Plan:

    {state['learning_plan']}
    """

    response = llm.invoke(prompt)

    return {
        "quiz": response.content
    }