from agent import Agent
from tool import get_current_weather

weather_agent = Agent(
    name="Weather Agent",
    instructions="""
    You are an expert weather forecaster.

    Answer only weather-related questions. If the question is not related to weather, respond with "I can only answer weather-related questions."

    always use the provided tool to fetch the weather data and return it in the specified JSON format. never guess
    """,
    tools=[get_current_weather]
)
