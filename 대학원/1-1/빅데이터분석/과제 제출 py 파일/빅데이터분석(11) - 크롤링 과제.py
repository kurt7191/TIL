#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

#1번
url = 'https://ko.wikipedia.org/wiki/%ED%95%9C%EC%96%91%EB%8C%80%ED%95%99%EA%B5%90'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser',  from_encoding='utf-8')
# print(bs)


# In[12]:


#2번
#위키 문서의 제목을 가져오세요 

bs.find('h1').get_text()


# In[15]:


#3번

number_three = bs.findAll(text = '한양대학교')
print("이 문서에 '한양대학교'는 {}번 나온다.".format(len(number_three)))


# In[27]:


#4번
#목차의 제목들을 추출하시오

index = bs.find('div',{'class':'toctitle'}).get_text()
print(index)
a = bs.find('div',{'class':'toc'}).find('ul').findAll('li')
for i in a:
    print(i.get_text())


# In[31]:


#5번
#웹 페이지 내에 포함된 전체 링크들의 텍스트들을 추출하시오

links = bs.findAll('a')
for link in links:
    print(link.get_text())


# In[35]:


#6번
#위키 본문내에 포함된 링크만 뽑아주세용

main_links = bs.find('main',{'class':'mw-body'}).findAll('a')
for link in main_links:
    print(link.get_text())


# In[61]:


#7번
#전체 웹 페이지 내에 있는 이미지 파일명들을 추출하시오
img_names = bs.findAll('img')

for name in img_names:
    if len(name['alt']) > 0:
        print(name['alt'])
    else:
        print(name['src'])
    
    
#파일명이 없고 src 만 있는 경우가 있어서 src는 따로 뽑았습니다.

    


# In[64]:


#8번
#위키 본문내에 포함된 이미지 이름만 뽑아주세용

main_img = bs.find('main',{'class':'mw-body'}).findAll('img')
for img in main_img:
    if len(img['alt']) > 0:
        print(img['alt'])
    else:
        print(img['src'])
    


# In[71]:


#9
#본문 내에 소제목들을 추출하시오.

for i in bs.find('div', {'id':'bodyContent'}).findAll({'h3','h2'}):
    print(i.get_text())


# In[79]:


#10
#본문 내에 위키 문서로의 링크들만 추출하시오
import re

wiki_links = bs.find('main',{'class':'mw-body'}).findAll('a',{'href':re.compile('^\/wiki\/.*')})

for link in wiki_links:
    print(link['href'])


# In[ ]:





# In[ ]:





# In[ ]:




