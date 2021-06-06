import numpy as np
import pandas as pd
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
import string

df = pd.read_csv('D:/aplikasiku/naivebayes/bayes/myapp/sampel_data.csv')
data = "Piford Technologies is a Software Development company. Piford also provide trainings."
stopwords = set(stopwords.words('english'))


# data = "Piford's Technologies, Piford is in Mohali !."
data_1=[char for char in data if char not in string.punctuation]
print(data_1)

data_1=''.join(data_1)
print(data_1)


data_1=data_1.split()  #word_tokenize(data)
print(data_1)

# data_1 = ["Piford Technologies Piford is in Mohali."]


# create the transform
vectorizer = CountVectorizer()

vectorizer.fit(data_1)

print(vectorizer.vocabulary_)  

"""encode document"""
vector = vectorizer.transform(data_1)
print(vector)


def text_cleaning(a):
 remove_punctuation = [char for char in a if char not in string.punctuation]
 #print(remove_punctuation)
 remove_punctuation=''.join(remove_punctuation)
 #print(remove_punctuation)   
 return [word for word in remove_punctuation.split() if word.lower() not in stopwords.words('english')]


# df.head()


print(df.iloc[:,0].apply(text_cleaning))#data after removing punctuation and stop words


bow_transformer = CountVectorizer(analyzer=text_cleaning).fit(df['TITLE']) 
  
#print(len(bow_transformer.vocabulary_))   
bow_transformer.vocabulary_


title_bow = bow_transformer.transform(df['TITLE'])

print(title_bow)


X = title_bow.toarray()
print(X)

 
X.shape  # 77,257  # 257 seperate words in our dataset and 77 rows

# TF-IDF Algo -term frequency-inverse document frequency to know the most significant words

tfidf_transformer=TfidfTransformer().fit(title_bow)
print(tfidf_transformer)

title_tfidf=tfidf_transformer.transform(title_bow)
print(title_tfidf)# got tfidf values for whole vocabulary
print(title_tfidf.shape)   #(77, 257)


model = MultinomialNB().fit(title_tfidf,df['CATEGORY'])			# PROSES TRAINING DATA DENGAN MENGGUNANAN MULTINOMIALNB



all_predictions = model.predict(title_tfidf)   # PREDKSI BEBERAPA VARIABEL
print(all_predictions)


#Printing the confusion matrix of our prediction

confusion_matrix(df['CATEGORY'], all_predictions)    # PENGUJIAN METRIX


