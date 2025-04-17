from openai import AsyncOpenAI
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv('API_KEY'))


async def gpt_text(req, model):
    completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": req,
            }
        ],
        model=model
    )
    return {
        'response': completion.choices[0].message.content,
        'usage': completion.usage.total_tokens
    }
