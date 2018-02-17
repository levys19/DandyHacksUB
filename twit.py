from credentials import *
import tweepy
import gcp_sentiment_analysis

class twit:



    @classmethod
    def search(cls, keyword):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        file_object  = open("tweets.txt", "w")
        counter = 0
        results = tweepy.Cursor(api.search,q= keyword, lang = 'en', rpp = '100', pages= '1').pages()
        for page in results:
            if counter > 50:
                break
            try:
                for tweets in page:
                    file_object.write(str(tweets.text) + "\n")
                    counter += 1
            except StopIteration:
                break
        file_object.close()
        gcp_sentiment_analysis.analyze("tweets.txt")
