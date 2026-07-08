import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tool import get_current_weather

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# -----------------------------
# Tool Definition
# -----------------------------

weather_tool = {
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get current weather of any city.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City Name"
                }
            },
            "required": ["location"]
        }
    }
}

# -----------------------------
# User Input
# -----------------------------

query = input("Ask: ")

# -----------------------------
# First LLM Call
# -----------------------------

response = client.chat.completions.create(

    model="llama-3.3-70b-versatile",

    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        },
        {
            "role": "user",
            "content": query
        }
    ],

    tools=[weather_tool],

    tool_choice="auto"
)

message = response.choices[0].message

# -----------------------------
# Tool Calling
# -----------------------------

if message.tool_calls:

    print("\nLLM decided to call a tool...\n")

    tool_call = message.tool_calls[0]

    function_name = tool_call.function.name

    arguments = json.loads(tool_call.function.arguments)

    if function_name == "get_current_weather":

        tool_result = get_current_weather(
            arguments["location"]
        )

    # -----------------------------
    # Second LLM Call
    # -----------------------------

    final_response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":"You are a helpful AI assistant."
            },

            {
                "role":"user",
                "content":query
            },

            message,

            {
                "role":"tool",
                "tool_call_id":tool_call.id,
                "content":json.dumps(tool_result)
            }

        ]
    )

    print("\nFinal Answer:\n")

    print(final_response.choices[0].message.content)

else:

    print("\nLLM didn't call any tool.\n")

    print(message.content)


    """
    User
 │
 ▼
What's the weather in Delhi?
 │
 ▼
LLM
 │
 ▼
Available Tools

get_current_weather()

Description:
Get current weather
 │
 ▼
LLM says

Call:

get_current_weather(
    location="Delhi"
)
 │
 ▼
Python receives request
 │
 ▼
if function_name == "get_current_weather":
 │
 ▼
Python calls

get_current_weather("Delhi")
 │
 ▼
Weather API
 │
 ▼
Returns result

    """