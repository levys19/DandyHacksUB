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
    def wordCount(cls):
        file_object = open("tweets.txt","r")
        wordList = file_object.read().split()
        wordDictionary = {}
        counterWords = {"if", "is", "the", "that", "rt", "at", "not", "is", "or", "will", "by", "to", "be", "after"}
        for word in wordList:
            word = word.lower()
            if word in wordDictionary and word != "rt" and word not in counterWords:
                wordDictionary[word] += 1
            else:
                wordDictionary[word] = 1
        file_object.close()
        return wordDictionary

    @classmethod
    def frequency(cls , wordCountDictionary):
        highestFreq = []
        for items in wordCountDictionary.keys():
            highestFreq.append((wordCountDictionary[items],items))
        highestFreq = reversed(sorted(highestFreq))
        reversedFreq = []
        for items in highestFreq:
            reversedFreq.append(items[1])
        return reversedFreq
