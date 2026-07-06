from openai import OpenAI
from dotenv import load_dotenv
import os

# Load env
load_dotenv(override=True)

api_key = os.getenv('GROQ_API_KEY')

client = OpenAI(
    api_key=api_key,
    base_url='https://api.groq.com/openai/v1',
)

topics = input('Enter the topics for the email: ')

prompt = f'''
Write a professional email about :

{topics}
'''

response = client.responses.create(
    model='llama-3.3-70b-versatile',
    input=prompt,
)

print('Generated Email:\n')
print(response.output_text)


