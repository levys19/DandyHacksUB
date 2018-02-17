from credentials import *
import tweepy
from time import sleep
import pprint

class twit:
    @classmethod
    def search(cls, keyword):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        for tweets in tweepy.Cursor(api.search,q= keyword, lang = 'en', rpp = '100').pages():
            for items in tweets:
                print(items.text)
                print("-----------------------")
