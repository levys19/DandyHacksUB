import nltk
import random
from twit import twit
def makeSentence(listOfWords, keyword):
    nouns = list()
    adjectives = list()
    verbs = list()
    adverbs = list()
    keyPOS = nltk.pos_tag(keyword)

    for word in listOfWords:
        POS_tweet = nltk.pos_tag(word)
        if POS_tweet[1][0] == "N":
            nouns.append(POS_tweet[0])
        elif POS_tweet[1][0] == "J":
            adjectives.append(POS_tweet[0])
        elif POS_tweet[1][0] == "V":
            verbs.append(POS_tweet[0])
        elif POS_tweet[1][0] == "R":
            adverbs.append(POS_tweet[0])

        if len(nouns) >= 1 and len(adjectives) >= 1 and len(verbs) >= 1 and len(adverbs) >= 1:
            break
    if keyPOS[1][0] == "N":
        print(keyword + " is " + adverbs[0] + " " + verbs[0])
    elif keyPOS[1][0] == "J":
        print("A " + keyword + " " + nouns[0] + " can just go " + adverbs[0] + " " + verbs[0])
    elif keyPOS[1][0] == "V":
        print("The " + nouns[0] + " really should " + keyword)
    elif keyPOS[1][0] == "R":
        print(nouns[0] + " is a " + adjectives[0] + " thing " + " and always " + keyword + " " + verbs[0])
