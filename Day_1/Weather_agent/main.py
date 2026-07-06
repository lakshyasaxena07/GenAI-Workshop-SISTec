from dotenv import load_dotenv
from pydantic import BaseModel
from agent import Agent
from runner import Runner
from tool import get_current_weather

load_dotenv()


class weather(BaseModel):
    location: str
    temperature: float
    condition: str


weather_agent = Agent(
    name="Weather Agent",
    instructions="You are a weather agent. You can provide current weather information for a given location. Use the provided tool to fetch the weather data and return it in the specified JSON format. never guess",
    tools=[get_current_weather],
    model="llama-3.3-70b-versatile",
    output_type=weather,
)

city = input("Enter city name: ")

response = Runner.run_sync(weather_agent, f"What is the current weather in {city}?")
print(response.final_output)


"""
    complete flow

    main.py
    │
    ▼
    Create Agent Object
    │
    ▼
    Agent.tools
    │
    ▼
    Stores function reference
    (get_current_weather)
    │
    ▼
    Runner.run_sync()
    │
    ▼
    Detect "weather"
    │
    ▼
    tool = agent.tools[0]
    │
    ▼
    tool(location)
    │
    ▼
    get_current_weather()
    │
    ▼
    Weather API
    │
    ▼
    Weather JSON
    │
    ▼
    Runner builds Prompt
    │
    ▼
    client.chat.completions.create()
    │
    ▼
    Groq LLM
    │
    ▼
    JSON Response
    │
    ▼
    Pydantic Validation
    │
    ▼
    Response Object
    │
    ▼
    Print

"""

"""
    The OpenAI Agents SDK is built on top of the OpenAI Responses API. Although Groq provides an
    OpenAI-compatible Chat Completions API, it does not implement the Agents SDK backend.      
    
"""
