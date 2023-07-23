import os
import praw
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ["REDDIT_CLIENT_ID"]
client_secret = os.environ["REDDIT_CLIENT_SECRET"]
subreddit = os.environ["SUBREDDIT"]
webhook_url = os.environ["WEBHOOK_URL"]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="reddit-stream-script",
)

financenews = reddit.subreddit(subreddit)

for submission in financenews.stream.submissions():
    print(submission.title,submission.url)
    # send webhook
    submission_dict = {
        "id": submission.id,
        "name":submission.name,
        "title": submission.title,
        "url": submission.url,
        "permalink":submission.permalink,
        "shortlink":submission.shortlink,
        "thumbnail":submission.thumbnail,
    }
    requests.post(webhook_url,json=submission_dict)
