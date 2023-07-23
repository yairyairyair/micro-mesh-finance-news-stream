import os
from pydantic import BaseModel
from fastapi import FastAPI
import requests
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.environ["WEBHOOK_URL"]

class Text(BaseModel):
    text: str

app = FastAPI()

@app.post("/")
async def root(text:Text):
    discord_message = {
        "content": text.text
    }
    response = requests.post(webhook_url,json=discord_message)
    response_json = response.json()
    print(response_json)
    return response_json
