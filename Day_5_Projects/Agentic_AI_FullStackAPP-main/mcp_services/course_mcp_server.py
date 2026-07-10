# pyrefly: ignore [missing-import]
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "Course Server"
)

COURSES = {

    "python": {
        "course":
        "Python for Everybody",

        "duration":
        "6 Weeks",

        "level":
        "Beginner"
    },

    "numpy": {
        "course":
        "NumPy Fundamentals",

        "duration":
        "2 Weeks",

        "level":
        "Beginner"
    },

    "pandas": {
        "course":
        "Pandas Data Analysis",

        "duration":
        "3 Weeks",

        "level":
        "Intermediate"
    }
}

@mcp.tool()
def search_course(topic: str):

    return COURSES.get(
        topic.lower(),
        {
            "message":
            "No Course Found"
        }
    )

# @mcp.tool()
# def get_weather(city: str):

#     response = requests.get(
#         "https://api.openweathermap.org/data/2.5/weather",
#         params={
#             "q": city,
#             "appid": API_KEY
#         }
#     )

#     return response.json()

if __name__ == "__main__":
    mcp.run()