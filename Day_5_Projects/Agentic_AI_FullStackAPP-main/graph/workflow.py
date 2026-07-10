# pyrefly: ignore [missing-import]
from langgraph.graph import (
    StateGraph,
    START,
    END
)

from graph.state import (
    LearningState
)

from agents.learning_agent import (
    learning_agent
)

from agents.resource_agent import (
    resource_agent
)
from agents.quiz_agent import (
    quiz_agent
)

from agents.report_agent import (
    report_agent
)

# from memory.memory_config import (
#     checkpointer
# )

from memory.postgres_memory import (
    checkpointer
)
graph = StateGraph(
    LearningState
)

graph.add_node(
    "learning",
    learning_agent
)

graph.add_node(
    "resource",
    resource_agent
)

graph.add_node(
    "quiz",
    quiz_agent
)

graph.add_node(
    "report",
    report_agent
)

graph.add_edge(
    START,
    "learning"
)

graph.add_edge(
    "learning",
    "resource"
)
graph.add_edge(
    "resource",
    "quiz"
)
graph.add_edge(
    "quiz",
    "report"
)

graph.add_edge(
    "report",
    END
)

app = graph.compile(
    checkpointer=checkpointer
)

png_data = app.get_graph().draw_mermaid_png()

with open("career_graph.png", "wb") as f:
    f.write(png_data)

print("Graph saved as career_graph.png")