import json
import re
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI client redirected to Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1"
)


class Response:
    def __init__(self, output):
        self.final_output = output


class Runner:
    @staticmethod
    def run_sync(agent, query):
        tool_result = None

        if "weather" in query.lower():
            location = "LONDON"
            match = re.search(r"in\s+([A-Za-z\s]+)", query)

            if match:
                location = match.group(1).strip()

            tool = agent.tools[0]  # Assuming the first tool is the weather tool
            tool_result = tool(location)

            prompt = f"""
                {agent.instructions}
                Weather Data :
                {json.dumps(tool_result)}
                Return ONLY JSON in this format:
                {{
                "location": "",
                "temperature": 0,
                "condition": ""
                }}
                """
        else:
            prompt = f"""
                {agent.instructions}

                Question:

                {query}
                """

        response = client.chat.completions.create(
            model=agent.model,
            messages=[{"role": "system", "content": prompt}],
            response_format={"type": "json_object"},
        )

        result = response.choices[0].message.content

        if agent.output_type:
            result = agent.output_type.model_validate_json(result)

        return Response(result)
