from credentials import *
import tweepy
import gcp_sentiment_analysis

class twit:

    @classmethod
    def writeToText(cls, keywords):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        file_object  = open("tweets.txt", "w")
        counter = 0
        results = tweepy.Cursor(api.search,q= keywords, lang = 'en', rpp = '100', pages= '1').pages()
        for page in results:
            if counter > 100:
                break
            try:
                for tweets in page:
                    file_object.write(str(tweets.text) + "\n")
                    counter += 1
            except StopIteration:
                break
        file_object.close()

    @classmethod
    def search(cls):
        return gcp_sentiment_analysis.analyze("tweets.txt")

    @classmethod
    def frequency(cls):
        file_object = open("tweets.txt","r")
        wordList = file_object.read().split()
        wordCount = {}
        for word in wordList:
            word = word.lower()
            if word in wordCount and word != "rt":
                wordCount[word] += 1
            else:
                wordCount[word] = 1
        file_object.close()
        print(wordCount)
        highestFreq = []
        for items in wordCount.keys():
            highestFreq.append((wordCount[items],items))
        print(sorted(highestFreq))
