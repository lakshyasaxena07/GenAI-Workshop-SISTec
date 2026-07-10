from typing import TypedDict

class LearningState(TypedDict):

    user_query: str

    learning_plan: str

    resources: str
    
    quiz: str

    final_report: str