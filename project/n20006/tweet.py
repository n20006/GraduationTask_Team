import os

import tweepy
from dotenv import load_dotenv

load_dotenv(".env")

api_key = os.environ.get("API_KEY")
api_key_secret = os.environ.get("API_KEY_SECRET")
access_token = os.environ.get("ACESS_TOKEN")
access_token_secret = os.environ.get("ACESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = ""
keyword = input()

for tweet in tweepy.Cursor(api.search_tweets, q=keyword).items(10):
    if list(tweet.text)[:2] != ["R", "T"]:
        tweets += f"{tweet.user.name} : {tweet.text}\nid : {tweet.id}\n"

print(tweets)
