from credentials import *
import tweepy
from time import sleep
import pprint


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

query = "donald trump"
for tweets in tweepy.Cursor(api.search,q='query').items():
    print(tweets.text)
