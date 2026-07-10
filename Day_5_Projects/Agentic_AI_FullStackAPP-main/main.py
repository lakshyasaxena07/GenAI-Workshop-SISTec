from graph.workflow import app

query = input(
    "Enter Topic: "
)

config = {
    "configurable": {
        "thread_id":
        "student_001"
    }
}

result = app.invoke(
    {
        "user_query":
        query,

        "learning_plan":
        "",

        "resources":
        "",

        "final_report":
        ""
    },
    config=config
)

print(
    result[
        "final_report"
    ]
)