## Lilleth Snavely (lls4abt)
## Source: https://www.tutorialspoint.com/create-word-cloud-using-python

## import libraries
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

## add more stopwords
STOPWORDS.add("billy")
STOPWORDS.add("billie")
STOPWORDS.add("yeah")
STOPWORDS.add("um")
STOPWORDS.add("whatever")
STOPWORDS.add("billy eilish")
STOPWORDS.add("billie eilish")
STOPWORDS.add("eilish")
STOPWORDS.add("really")
STOPWORDS.add("yep")
STOPWORDS.add("oh")
STOPWORDS.add("got")
STOPWORDS.add("blank blank")
STOPWORDS.add("blank")
STOPWORDS.add("put")
STOPWORDS.add("though")

## pick a file for Word Cloud creation
dataset = open("VanityFair2021.txt", "r").read()

## create World Cloud creation function
def create_word_cloud(string):
    maskArray = npy.array(Image.open("cloud.png"))
    cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wordCloud.png")

## Create the Word Cloud
dataset = dataset.lower()
create_word_cloud(dataset)


