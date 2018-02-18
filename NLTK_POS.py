import nltk
nltk.download('averaged_perceptron_tagger')

from twit import twit
def makeSentence(listOfWords, keyword):
    nouns = list()
    adjectives = list()
    verbs = list()
    adverbs = list()
    print(list(keyword))
    keyPOS = nltk.pos_tag([keyword])
    print("------------")
    print(keyPOS)
    print("------------")
    keyPOS = keyPOS[0]
    POS_tweet = nltk.pos_tag(listOfWords)
    print(POS_tweet)
    for words in POS_tweet:
        print(words)
        if words[1][0] == "N":
            nouns.append(words[0])
        elif words[1][0] == "J":
            adjectives.append(words[0])
        elif words[1][0] == "V":
            verbs.append(words[0])
        elif words[1][0] == "R":
            adverbs.append(words[0])
        if len(nouns) >= 1 and len(adjectives) >= 1 and len(verbs) >= 1 and len(adverbs) >= 1:
            break
    if keyPOS[1][0] == "N":
        return ([keyword,  verbs[0], " very " , adjectives[0]])
    elif keyPOS[1][0] == "J":
        return (["A ", keyword, nouns[0], " can just go ", adverbs[0], verbs[0]])
    elif keyPOS[1][0] == "V":
        return (["The ", nouns[0], " really should ", keyword])
    elif keyPOS[1][0] == "R":
        return ([nouns[0], " is a ", adjectives[0], " thing and always ", keyword, verbs[0]])
