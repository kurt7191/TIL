# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:16:07 2021

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

review_df=pd.read_csv("imdb_minari.csv")

#word count
temp=review_df.loc[0,'comment']
print(temp)
temp1=temp.split(' ')
print(temp1)
word_list = review_df['comment'].apply(lambda x: x.split(' '))
word_counts = review_df['comment'].apply(lambda x:len(x.split(' ')))
word_counts.head()
word_counts.describe()

# 그래프에 대한 이미지 사이즈 선언
# figsize: (가로, 세로) 형태의 튜플로 입력
plt.figure(figsize=(12, 5))
# 히스토그램 선언
# bins: 히스토그램 값들에 대한 버켓 범위
# range: x축 값의 범위
# alpha: 그래프 색상 투명도
# color: 그래프 색상
# label: 그래프에 대한 라벨
plt.hist(word_counts, bins=200, alpha=0.5, color= 'r', label='word')
plt.legend()
# 그래프 제목
plt.title('Histogram of length of review')
# 그래프 x 축 라벨
plt.xlabel('Length of review')
# 그래프 y 축 라벨
plt.ylabel('Number of review')
plt.show()


sns.distplot(word_counts)
sns.distplot(word_counts,kde=False)

plt.figure(figsize=(12, 5))
ax = sns.distplot(word_counts,kde=False,bins=200,color='r')
ax.set_xlabel('Length of review')
ax.set_ylabel('Number of review')
ax.set_title('Histogram of length of review')
ax.legend(labels=['word'])
plt.show()

# 박스플롯 생성
# 첫번째 파라메터: 여러 분포에 대한 데이터 리스트를 입력
# labels: 입력한 데이터에 대한 라벨
# showmeans: 평균값을 마크함

plt.boxplot(word_counts,
             labels=['counts'],
             showmeans=True)

sns.boxplot(word_counts)


# pip install wordcloud
from wordcloud import WordCloud
temp1=review_df.loc[0,'comment']
temp2=review_df.loc[1,'comment']
temp3=" ".join(review_df.loc[[0,1],'comment'])
temp5=" ".join(review_df['comment'])

cloud = WordCloud(width=800, height=600).generate(" ".join(review_df['comment']))
plt.figure(figsize=(20, 15))
plt.imshow(cloud)
plt.axis('off')

# rating distribution

sns.countplot(review_df['rating'])
review_df['rating'].value_counts().sort_index()
