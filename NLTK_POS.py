import nltk

def makeSentence(listOfWords):
    nouns = list()
    adjectives = list()
    verbs = list()
    adverbs = list()
    for word in listOfWords:
        POS_tweet = nltk.pos_tag(word)
        if POS_tweet == "N":
            nouns.append(POS_tweet[0])
        elif POS_tweet == "J":
            adjectives.append(POS_tweet[0])
        elif POS_tweet == "V":
            verbs.append(POS_tweet[0])
        elif POS_tweet == "R":
            adverbs.append(POS_tweet[0])

        if len(nouns) >= 1 and len(adjectives) >= 1 and len(verbs) >= 1 and len(adverbs) >= 1:
            break


