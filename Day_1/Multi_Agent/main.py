from weather_agent import weather_agent
from coding_agent import coding_agent
from runner import Runner

query = input("Ask Anything : ")

# Supervisor Logic

weather_keywords = [
    "weather",
    "temperature",
    "rain",
    "humidity",
    "forecast"
]

coding_keywords = [
    "python",
    "java",
    "oop",
    "exception",
    "api",
    "program",
    "class"
]

if any(word in query.lower() for word in weather_keywords):

    selected_agent = weather_agent

elif any(word in query.lower() for word in coding_keywords):

    selected_agent = coding_agent

else:

    print("No suitable agent found.")
    exit()

print(f"\nDelegating to : {selected_agent.name}\n")

response = Runner.run_sync(
    selected_agent,
    query
)

print(response.final_output)