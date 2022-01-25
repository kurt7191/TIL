# 자연어 처리 관련 EDA



먼저 EDA 분석할 데이터 가져오기



```python
import os
import re

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import utils

data_set = tf.keras.utils.get_file(
fname = 'imdb.tar.gz',
origin='http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz',
extract = True)

def directory_data(directory):
    data = {}
    data['review'] = []
    for file_path in os.listdir(directory):
        with open(os.path.join(directory, file_path),"r", encoding = 'UTF-8') as file:
            data['review'].append(file.read())
            
            
    return pd.DataFrame.from_dict(data)    
    
def data(directory):
    pos_df = directory_data(os.path.join(directory,"pos"))
    neg_df = directory_data(os.path.join(directory,"neg"))
    pos_df['sentiment'] = 1
    neg_df['sentiment'] = 0
    
    return pd.concat([pos_df,neg_df]) 


train_df = data(os.path.join(os.path.dirname(data_set),"aclImdb","train"))
test_df = data(os.path.join(os.path.dirname(data_set),"aclImdb","test"))
```



1. 문장열 문장 리스트를 tokenizing
   - i like banana 를 [i, like, banana] 로 토크나이징.
2. tokeinizing 된 각 리스트들의 길이
3. tokenizing 된 음절의 길이를 저장



```python
#문장열 문장 리스트를 토크나이징

tokenized_reviews = [review.split() for review in reviews]

#토크나이징된 리스트에 대한 각 길이를 지정

review_len_by_token = [len(t) for t in tokenized_reviews]

#토크나이징된 것을 붙여서 음절의 길이를 저장

review_len_by_eumjeol = [len(s.replace(" ","")) for s in reviews]
```



tokenizing 된 각 리스트들의 길인 단어의 개수라고 할 수 있고

음절의 길이는 알파뱃의 개수라고 할 수 있다.

이 둘의 분포를 시각화하기.



```python
import matplotlib.pyplot as plt

plt.figure(figsize = (12,5))

plt.hist(review_len_by_token, bins = 50, alpha = 0.5, color = 'r', label = 'word')
plt.hist(review_len_by_eumjeol, bins = 50, alpha = 0.5, color = 'b', label = 'alphabet')
plt.yscale('log',nonposy = 'clip')

plt.title('Review Length Histogram')
plt.xlabel('Review Length')
plt.ylabel('Number of Reviews')

```



두 분포에 대한 기초통계값 얻기



```python
import numpy as np

print('문장 최대 길이 : {}'.format(np.max(review_len_by_token)))
print('문장 최소 길이 : {}'.format(np.min(review_len_by_token)))
print('문장 평균 길이 : {:.2f}'.format(np.mean(review_len_by_token)))
print('문장 길이 표준편차 : {:.2f}'.format(np.std(review_len_by_token)))
print('제 1사분위 길이 : {}'.format(np.percentile(review_len_by_token, 25)))
print('제 3사분위 길이 : {}'.format(np.percentile(review_len_by_token, 75)))
```



두 값에 대한 분포를 boxplot 을 그려서 얻기



```python
plt.figure(figsize = (12,5))
plt.boxplot([review_len_by_token],
           labels = ['token'],
           showmeans = True)


plt.figure(figsize = (12,5))
plt.boxplot([review_len_by_eumjeol],
           labels = ['Eumjeol'],
           showmeans = True)
```



wordcloud 로 단어의 개수를 나타내기



```python
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
%matplotlib inline

wordcloud = WordCloud(stopwords = STOPWORDS, background_color = 'black', width = 800,
                     height = 600).generate(' '.join(train_df['review']))

plt.figure(figsize = (15,10))
plt.imshow(wordcloud)
plt.axis = ('off')
plt.show()
```



감정값의 value_counts 에 대한 시각화



```python
import seaborn as sns
import matplotlib.pyplot as plt

sentiment = train_df['sentiment'].value_counts()

fig, axs = plt.subplots(ncols = 1)
fig.set_size_inches(6,3)
sns.countplot(train_df['sentiment'])

```



위의 과정들이 기초적인 NLP 의 EDA 과정



