from openai import AsyncOpenAI, api_key
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


async def gpt_image(req, model):
    response = await client.images.generate(
        model="dall-e-3",
        prompt=req,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return {
        'response': response.data[0].url,
        'usage': 1,
    }


async def gpt_vision(req, model, file):
    # Path to your image
    image_path = "path_to_your_image.jpg"

    # Getting the Base64 string
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        'model': 'gpt-4o',
        'messages': [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64, {base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300,
    }

