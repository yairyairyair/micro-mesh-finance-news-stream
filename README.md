# micro-mesh-finance-news-stream
An example micro mesh project for finance news streaming

Built using micro-services event-driven architecture.


## Services:

reddit-stream - listens to a subreddit and sends webhooks when new subreddit

sentiment-service - listens to http and says what is the sentiment

discord-webhook-service - listens to http and sends discord webhooks

is-significant-news - a function that decides whether a news is significant

 