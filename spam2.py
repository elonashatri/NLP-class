from __future__ import print_function, division
from future.utils import iteritems
from builtins import range

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from wordcloud import WordCloud

df = pd.read_csv('spam2.csv',encoding='ISO-8859-1')

# drop unnecessary columns
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)

# rename columns
df.columns = ["labels", "data"]

# create binary labels
df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})
Y = df['b_labels'].values

CountVectorizer = CountVectorizer( decode_error='ignore')
X = CountVectorizer.fit_transform(df['data'])

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size = 0.33)

model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print("train score: ", model.score(Xtrain, Ytrain))
print("test score: ", model.score(Xtest, Ytest))


# data vizualisation 
def visualize(label):
    words = ' '
    for msg in df[df['labels'] == label]['data']:
        msg = msg.lower()
        words += msg + ' '
    wordcloud = WordCloud(width=600, height = 400).generate(words)
    plt.imshow(wordlcoud)
    plt.axis('off')
    plt.show()

    visualize('spam')
    visualize('ham')