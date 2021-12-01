#!/usr/bin/env python
# coding: utf-8

# # 과제1

# ★ 오늘의 과제
# 
# 1. 단어 분포 살펴보기 Lab  
# 1) imdb의 ‘coco’ 영화에 대한 리뷰들을 이용해서 앞의 단계들을 수행하시오.  
# 2) daum 영화에 ‘자산어보’ 영화의 리뷰들을 이용해서 앞의 단계들을 수행하시오.   
# 
# 

# ## imdb coco

# In[71]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

review_df = pd.read_csv('C:\\study\\workspace_python\\pdsample\\datasets\\mydata\\imdb_coco.csv')
review2_df = pd.read_csv('C:\\study\\workspace_python\\pdsample\\datasets\\mydata\\daum_jasanubo.csv')


# In[72]:


word_counts = review_df['comment'].apply(lambda x : len(x.split(" ")))


# In[73]:


word_counts.head()
word_counts.describe()


# In[76]:


plt.figure(figsize = (12,5))
plt.hist(word_counts, alpha = 0.5, bins = 200, color = 'r', label = 'word')
plt.legend
plt.title('Histogram of length of review')
plt.xlabel('Length of review')
plt.ylabel('Number of review')


# In[79]:


sns.distplot(word_counts, bins = 200,kde = False, color = 'red')


# In[82]:


plt.figure(figsize = (15, 4))
plt.boxplot(word_counts,
           labels = ['counts'],
           showmeans = True)
plt.figure(figsize = (15,4))
sns.boxplot(word_counts)


# In[86]:


from wordcloud import WordCloud

cloud = WordCloud(width = 800, height = 600).generate(" ".join(review_df['comment']))
plt.figure(figsize = (20,15))
plt.imshow(cloud)
plt.axis('off')


# In[88]:


sns.countplot(review_df['rating'])


# ## 다음 자산어보

# In[93]:


word_counts = review2_df['comment'].apply(lambda x : len(x.split(' ')))


# In[94]:


word_counts.head(15)
word_counts.describe()


# In[95]:


plt.figure(figsize = (12,5))
plt.hist(word_counts, alpha = 0.5, bins = 200,color = 'r', label = 'word')
plt.legend()
plt.title('Histogram of length of review')
plt.xlabel('Lenght of review')
plt.ylabel('Number of review')
plt.show()


# In[96]:


sns.displot(word_counts,bins = 200, color = 'red', kde = False)


# In[97]:


plt.boxplot(word_counts,
           labels = ['counts'],
           showmeans = True)



# In[99]:


# plt.rc('font', family='Arial.ttf')
# [출처] 파이썬 : 그래프(matplotlib 등), 워드클라우드 등에서 한글 폰트 깨짐 문제 해결|작성자 지잉



font_path = 'C:\Windows\Fonts/'
cloud = WordCloud(font_path = font_path + 'Arial.ttf',
                 width = 800, height = 600).generate(" ".join(review2_df['comment']))

plt.figure(figsize = (20,15))
plt.imshow(cloud)
plt.axis('off')


# In[ ]:





# 

# # 과제2

# 2. 데이터 전처리 Lab  
# 1) imdb의 ‘coco’ 영화에 대한 리뷰들을 이용해서 앞의 단계들을 수행하시오.  
# 2) daum 영화에 ‘자산어보’ 영화의 리뷰들을 이용해서 앞의 단계들을 수행하시오.   

# ## imdb coco

# In[ ]:


import pandas as pd

review_df = pd.read_csv('C:\\study\\workspace_python\\pdsample\\datasets\\mydata\\imdb_coco.csv')
review2_df = pd.read_csv('C:\\study\\workspace_python\\pdsample\\datasets\\mydata\\daum_jasanubo.csv')


# In[33]:


review_df['comment_n'] = review_df['comment'].apply(lambda x : x.lower())


# In[34]:


import re

p = re.compile('[0-9]+')
review_df['comment_n'] = review_df['comment_n'].apply(lambda x : p.sub(" ",x))

p = re.compile("\W+")
review_df['comment_n'] = review_df['comment'].apply(lambda x : p.sub(" ",x))


# In[35]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# In[36]:


stop_words = set(stopwords.words('english'))


# In[37]:


review_df.info()


# In[38]:


review_df['comment_n'] = review_df['comment_n'].apply(lambda x : word_tokenize(x))


# In[39]:


def remove_stopwords(word_tokens):
    result = []
    for w in word_tokens:
        if w not in stop_words:
            result.append(w)
    return result


# In[41]:


review_df['comment_n'] = review_df['comment_n'].apply(lambda x : remove_stopwords(x))


# In[42]:


from nltk.stem import WordNetLemmatizer


# In[43]:


n = WordNetLemmatizer()
review_df['comment_n'] = review_df['comment_n'].apply(lambda x : [n.lemmatize(w) for w in x ])


# In[49]:


review_df.loc[0,'comment_n']


# In[50]:


total_word = []
for i in range(len(review_df)):
    total_word.extend(review_df.loc[i, 'comment_n'])


# In[55]:


pd.Series(total_word).value_counts().head(15)


# In[61]:


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (15,4))
pd.Series(total_word).value_counts().head(15).plot(kind= 'bar')

plt.figure(figsize = (15,4))
pd.Series(total_word).value_counts().head(15).plot(kind = 'barh')

plt.figure(figsize = (15,4))
pd.Series(total_word).value_counts().head(15).plot(kind = 'barh').invert_yaxis()


# ## 다음 자산어보

# In[62]:


review2_df


# In[105]:


from pykospacing import Spacing

spacing = Spacing()
review2_df['comment_fix'] = review2_df['comment'].apply(lambda x : spacing(x))


# In[110]:


import kss


review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : kss.split_sentences(x))


# In[119]:


review2_df['comment_fix'][0]


# In[124]:


import re

p = re.compile("[0-9]+")

review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : [p.sub(" ",sentence) for sentence in x])


r = re.compile("\W+")
review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : [r.sub(" ", sentence) for sentence in x])

# review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : r.sub(" ",x))


# In[126]:


from hanspell import spell_checker


review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : [spell_checker.check(sentence).checked for sentence in x])
# spell_checker.check(r)


# In[131]:


from konlpy.tag import Okt

okt = Okt()
review2_df['comment_fix'] = review2_df['comment_fix'].apply(lambda x : [okt.pos(sentence) for sentence in x])


# In[196]:


#명사, 형용사, 동사만 꺼내기
result = []
for i in range(len(review2_df)):
    review1_tokens1 = []
    for sentence in review2_df.loc[i,"comment_fix"]:
        new_sent = []
        for token in sentence:
            if (token[1] == "Noun" or token[1] == "Adjective" or token[1] == 'Verb'):
                new_sent.append(token)
        review1_tokens1.append(new_sent)
    result.append(review1_tokens1)

review2_df['comment_fix'] = pd.Series(result)


# In[207]:


#표제어

from soylemma import Lemmatizer

lemmatizer = Lemmatizer()
result = []
for i in range(len(review2_df)):
    review1_tokens1 = []
    for sentence in review2_df.loc[i,"comment_fix"]:
        new_sent = []
        for token in sentence:
            if (token[1] == "Adjective") | (token[1] == "Verb"):
                stem_result = lemmatizer.lemmatize(token[0])
                if len(stem_result) != 0:
                    new_sent.append(stem_result[0])
            else:
                new_sent.append(token)
        review1_tokens1.append(new_sent)
    result.append(review1_tokens1)
    
review2_df['comment_fix'] = pd.Series(result)
            


# In[212]:


#불용어 제거
stopwords=[('이','Noun'), ('거','Noun'),('오','Noun'), ('것','Noun')]
result = []

for i in range(len(review2_df)):
    review1_tokens1 = []
    for sentence in review2_df.loc[i,"comment_fix"]:
        new_sent = []
        for token in sentence:
            if token not in stopwords:
                new_sent.append(token)
        review1_tokens1.append(new_sent)
    result.append(review1_tokens1)


# In[214]:


review2_df['comment_fix'] = pd.Series(result)


# In[217]:


#pos 태그 제거

result = []

for i in range(len(review2_df)):
    review1_tokens1 = []
    for sentence in review2_df.loc[i,"comment_fix"]:
        new_sent = []
        for token in sentence:
            new_sent.append(token[0])
        review1_tokens1.append(new_sent)
    result.append(review1_tokens1)

review2_df['comment_fix'] = pd.Series(result)


# In[222]:


result = []

for i in range(len(review2_df)):
    review1_tokens1 = []
    for sentence in review2_df.loc[i,"comment_fix"]:
        review1_tokens1.extend(sentence)
        
    result.append(review1_tokens1)


# In[226]:


review2_df['comment_fix'] = pd.Series(result)


# In[227]:


review2_df

