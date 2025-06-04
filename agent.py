import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1")

client = OpenAI(base_url=base_url, api_key=api_key)

def ask_agent(user_query: str) -> str:
    chat = client.chat.completions.create(
        model="openhermes",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
    )
    return chat.choices[0].message.content
