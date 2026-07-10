# pyrefly: ignore [missing-import]
import streamlit as st

from graph.workflow import app


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="AI Student Learning Assistant",
    page_icon="🎓",
    layout="wide"
)


# -----------------------------------
# Header
# -----------------------------------

st.title("🎓 AI Student Learning Assistant")

st.markdown(
    """
    This application uses:

    - LangGraph
    - Supervisor Agent
    - MCP Tools
    - RAG (FAISS)
    - MemorySaver / PostgresSaver

    Enter a learning goal and generate a roadmap.
    """
)


# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("Settings")

    user_id = st.text_input(
        "User ID",
        value="student_001"
    )

    st.markdown("---")

    st.info(
        """
        Features

        ✅ LangGraph

        ✅ MCP

        ✅ RAG

        ✅ PostgreSQL Memory

        ✅ Supervisor Agent
        """
    )


# -----------------------------------
# User Input
# -----------------------------------

learning_goal = st.text_area(
    "What do you want to learn?",
    placeholder="Example: Learn Python for Data Science"
)


# -----------------------------------
# Generate Button
# -----------------------------------

if st.button("🚀 Generate Learning Plan"):

    if not learning_goal.strip():

        st.warning(
            "Please enter a learning goal."
        )

    else:

        # Thread ID for memory
        config = {
            "configurable": {
                "thread_id": user_id
            }
        }

        with st.spinner(
            "Generating roadmap..."
        ):

            result = app.invoke(

                {
                    "user_query": learning_goal,

                    "learning_plan": "",

                    "resources": "",

                    "quiz": "",

                    "final_report": ""
                },

                config=config
            )

        st.success(
            "Plan Generated Successfully!"
        )

        # ---------------------------
        # Tabs
        # ---------------------------

        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📚 Learning Plan",
                "📖 Resources",
                "❓ Quiz",
                "📄 Final Report"
            ]
        )

        # ---------------------------
        # Learning Plan
        # ---------------------------

        with tab1:

            st.subheader(
                "Learning Roadmap"
            )

            st.write(
                result.get(
                    "learning_plan",
                    "No roadmap available."
                )
            )

        # ---------------------------
        # Resources
        # ---------------------------

        with tab2:

            st.subheader(
                "Recommended Resources"
            )

            st.write(
                result.get(
                    "resources",
                    "No resources available."
                )
            )

        # ---------------------------
        # Quiz
        # ---------------------------

        with tab3:

            st.subheader(
                "Practice Quiz"
            )

            st.write(
                result.get(
                    "quiz",
                    "No quiz available."
                )
            )

        # ---------------------------
        # Final Report
        # ---------------------------

        with tab4:

            st.subheader(
                "Complete Learning Report"
            )

            st.write(
                result.get(
                    "final_report",
                    "No report available."
                )
            )

        # ---------------------------
        # Previous Memory
        # ---------------------------

        try:

            snapshot = app.get_state(
                config
            )

            st.markdown("---")

            st.subheader(
                "🧠 Previous Session Memory"
            )

            st.json(
                snapshot.values
            )

        except Exception:

            st.info(
                "Memory not available yet."
            )