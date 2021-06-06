import numpy as np
import pandas as pd
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import string

df = pd.read_csv('D:/aplikasiku/naivebayes/bayes/myapp/sampel_data.csv')
data = "Piford Technologies is a Software Development company. Piford also provide trainings."
datanya = set(stopwords.words('english'))
data_1=[char for char in data if char not in string.punctuation]
data_1=''.join(data_1)
data_1=data_1.split()  #word_tokenize(data)

# proses transform
vectorizer = CountVectorizer()
vectorizer.fit(data_1)
vector = vectorizer.transform(data_1)

def text_cleaning(a):
    remove_punctuation = [char for char in a if char not in string.punctuation]
    remove_punctuation=''.join(remove_punctuation)
    return [word for word in remove_punctuation.split() if word.lower() not in stopwords.words('english')]

df.iloc[:,0].apply(text_cleaning)

bow_transformer = CountVectorizer(analyzer=text_cleaning).fit(df['TITLE'])

bow_transformer.vocabulary_
title_bow = bow_transformer.transform(df['TITLE'])

X = title_bow.toarray()

tfidf_transformer=TfidfTransformer().fit(title_bow)

title_tfidf=tfidf_transformer.transform(title_bow)

model = MultinomialNB().fit(title_tfidf,df['CATEGORY'])   # PROSES TRAINING DATA DENGAN MENGGUNANAN MULTINOMIALNB

all_predictions = model.predict(title_tfidf)   # PREDKSI BEBERAPA VARIABEL
