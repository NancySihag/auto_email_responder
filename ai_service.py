import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def generate_reply(email_text):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or api_key == "your_openai_api_key_here":
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": f"Reply professionally:\n{email_text}",
            }
        ],
    )

    return response.choices[0].message.content

