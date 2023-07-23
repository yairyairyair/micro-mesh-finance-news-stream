import os
from pydantic import BaseModel
from fastapi import FastAPI
import requests
from dotenv import load_dotenv

load_dotenv()

threshold = float(os.getenv('THRESHOLD','0.5'))
sentiment_service_url = os.environ["SENTIMENT_SERVICE_URL"]
webhook_url = os.environ["WEBHOOK_URL"]

class News(BaseModel):
    title: str
    url: str


app = FastAPI()

@app.post("/")
async def root(news:News):
    sentiment_message = {
        "text": news.title
    }
    response = requests.post(sentiment_service_url,json=sentiment_message)
    response_json = response.json()
    news_negative_sentiment = response_json['neg']
    news_positive_sentiment = response_json['pos']

    if news_negative_sentiment > threshold or news_positive_sentiment > threshold:
        # send webhook
        discord_service_message = {
            "text": f"Significant news - {news.title} at {news.url}"
        }
        response = requests.post(webhook_url,json=discord_service_message)
        return {"status":'above threshold'}
    return {"status":'below threshold'}
