from pydantic import BaseModel
from fastapi import FastAPI
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Text(BaseModel):
    text: str

sentiment = SentimentIntensityAnalyzer()
app = FastAPI()

@app.post("/")
async def root(text:Text):
    text_sentiment = sentiment.polarity_scores(text.text)
    print(text_sentiment)
    return text_sentiment
