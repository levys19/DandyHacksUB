from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def compute_sentiment(annotations):
    sentiment_list = list()
    positive_sentiments = 0
    negative_sentiments = 0
    mixed_sentiments = 0
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Tweet: \n{} \nSentiment Score: \n{}'.format(
            sentence.text.content, sentence_sentiment))
        if sentence_sentiment > 0.15:
            sentiment_list.append(1)
            positive_sentiments += 1
        elif sentence_sentiment < -0.1:
                sentiment_list.append(-1)
                negative_sentiments += 1
        else:
            sentiment_list.append(0)
            mixed_sentiments += 1
    print("Total tweets:" + str(len(sentiment_list)))
    print("Number of Positive Tweets:" + str(positive_sentiments))
    print("Percentage of Positive Tweets:" + str(positive_sentiments/len(sentiment_list)) + "%")
    print("Number of Negative Tweets:" + str(negative_sentiments))
    print("Percentage of Negative Tweets:" + str(negative_sentiments / len(sentiment_list)) + "%")
    print("Number of Mixed/Neutral Tweets:" + str(mixed_sentiments))
    print("Percentage of Mixed/Neutral Tweets:" + str(mixed_sentiments / len(sentiment_list)) + "%")
    avg_sentiment_value = sum(sentiment_list)/len(sentiment_list)
    print("Overall Sentiment Value:" + str(avg_sentiment_value))
    if avg_sentiment_value > 0.15:
        return "Overall Positive Sentiment"
    if avg_sentiment_value < -0.1:
        return "Overall Negative Sentiment"
    return "Overall Mixed Sentiment"


def analyze(filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(filename, 'r') as readfile:
        # Instantiate a plain text document
        content = readfile.read()

    document = types.Document(
            content=content,
            type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print results
    print("Sentiment:")
    print(compute_sentiment(annotations))

