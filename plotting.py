import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
from collections import Counter



stop_words = set(stopwords.words("english"))

lemmatizer = WordNetLemmatizer()

additional_stop_words = {"plot","crash","plane","fllight","flight","crashed" ,
                         "miles"," ", "pilot","aircraft","crew","cargo",
                         "approach","fly", "cause"}

stop_words = stop_words | additional_stop_words

def add_stop_words(stop_words,x):
    [stop_words.update(i) for i in x]
    return stop_words

def to_lammetize(x):
    return [lemmatizer.lemmatize(j.lower(),  pos='v') for j in x ]

def remove_stop_word(x):
    return [i.lower() for i in x if i.lower() not in stop_words and i != ""]

def plot_word_cloud(dfValues):
    width = 12
    height = 12
    plt.figure(figsize=(width, height))
    #text = 'all your base are belong to us all of your base base base'
    wc = WordCloud().generate(" ".join([ i for j in dfValues for i in j]))
    plt.imshow(wc)
    # wordcloud = WordCloud(font_path='/Library/Fonts/Gotham-Bold.otf',width=1800,height=1400).generate(str(hr1_filter))
    # plt.imshow(wordcloud)
    plt.axis("off")
# plt.show()
def word_count(dfValues):
    return Counter([i for j in dfValues for i in j ])