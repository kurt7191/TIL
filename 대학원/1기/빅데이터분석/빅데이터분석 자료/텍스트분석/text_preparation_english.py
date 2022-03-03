# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:00:00 2021

@author: USER
"""

import pandas as pd

review_df=pd.read_csv("imdb_minari.csv")

# 대소문자 처리

review_df['comment_n']=review_df['comment'].apply(lambda x: x.lower())

# 숫자, 문장부호, 특수문자 제거
import re
p=re.compile("[0-9]+")
review_df['comment_n']=review_df['comment_n'].apply(lambda x: p.sub(" ", x))

p=re.compile("\W+")
review_df['comment_n']=review_df['comment_n'].apply(lambda x: p.sub(" ", x))

# 불용어 제거

from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords  

stop_words = set(stopwords.words('english')) 

review_df['comment_n']=review_df['comment_n'].apply(lambda x: word_tokenize(x))

def remove_stopwords(word_tokens):
    result = []
    for w in word_tokens: 
        if w not in stop_words: 
            result.append(w) 
    return result

review_df['comment_n']=review_df['comment_n'].apply(lambda x: remove_stopwords(x))

# 어간 추출
from nltk.stem import WordNetLemmatizer
n=WordNetLemmatizer()

review_df['comment_n']=review_df['comment_n'].apply(lambda x: [n.lemmatize(w) for w in x])

review_df.to_csv('imdb_minari_result.csv',index=False)

# Term Frequency

total_word=[]
for i in range(len(review_df)):
    total_word.extend(review_df.loc[i,"comment_n"])

pd.Series(total_word).value_counts().head(15)

pd.Series(total_word).value_counts().head(15).plot(kind='bar')
pd.Series(total_word).value_counts().head(15).plot(kind='barh')
pd.Series(total_word).value_counts().head(15).plot(kind='barh').invert_yaxis()
