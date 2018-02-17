from credentials import *
import tweepy
# from gcp_sentiment_analysis import gcp_stuff

class twit:

    @classmethod
    def analyze(cls, tweetList):
        gcp_analyze = gcp_stuff()
        for tweets in tweetList:
            sentimentList.append(gcp_analyze(tweets))
        sentimentList = []
        return sentimentList

    @classmethod
    def search(cls, keyword):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        file_object  = open("tweets.txt", "w")
        for page in tweepy.Cursor(api.search,q= keyword, lang = 'en', rpp = '100').pages():
            try:
                for tweets in page:
                    file_object.write(str(tweets.text) + "\n" + "\n")
            except StopIteration:
                break
        file_object.close()
