# Lilleth Snavely (lls4abt)
# Source: https://www.tutorialspoint.com/create-word-cloud-using-python

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


dataset = open("VanityFair2021.txt", "r").read()

def create_word_cloud(string):
    maskArray = npy.array(Image.open("cloud.png"))
    cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wordCloud.png")

dataset = dataset.lower()
create_word_cloud(dataset)


