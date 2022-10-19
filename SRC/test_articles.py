# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
# Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
# polarity_scores method of SentimentIntensityAnalyzer
# oject gives a sentiment dictionary.
# which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("Sentence Overall Rated As", end = " ")
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
    else :
        print("Neutral")

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from textblob import TextBlob
from newspaper import Article

url = 'https://time.com/charlottesville-white-nationalist-rally-clashes/'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.text
#print(text)

blob = TextBlob(text)
sentiment_scores(blob)

url2 = 'https://people.com/pets/stolen-dog-reunited-with-owner-after-11-years-apart/'
article2 = Article(url2)

article2.download()
article2.parse()
article2.nlp()

text2 = article2.text
blob2 = TextBlob(text2)
sentiment_scores(blob2)