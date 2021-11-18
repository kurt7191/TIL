#!/usr/bin/env python
# coding: utf-8

# ### BeautifulSoup LAB

# In[108]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


url = 'https://movie.naver.com/movie/point/af/list.naver'
res = requests.get(url)
bs = BeautifulSoup(res.text, 'html.parser')


# In[109]:



numbers = bs.findAll('td',{'class' : 'ac num'})
titles = bs.findAll('td',{'class':'title'})
stars = bs.find('tbody').findAll('div',{'class':'list_netizen_score'})
# for number in numbers:
#     print(number.text)
    


# In[117]:


#2번

for number in numbers:
    print(number.text)
    
for title in titles:
    print(title.find('a',{'class':'movie color_b'}).text)

for star in stars:
    print(star.text)


# In[121]:


#3번

review_number = []
movie_title = []
star_list = []


for number in numbers:
    review_number.append(number.text)

for title in titles:
    movie_title.append(title.find('a',{'class':'movie color_b'}).text)
    
for star in stars:
    star_list.append(star.text)
    
number_sr = pd.Series(data = review_number)
title_sr = pd.Series(data = movie_title)
star_sr = pd.Series(data = star_list)

df = pd.concat({'number':number_sr,'title':title_sr,'star':star_sr},axis = 1)

import os
save_file_path = 'C:\\study\\workspace_python\\pdsample\\datasets\\mydata'

os.chdir(save_file_path)
df.to_csv('naver_review.csv', index=False, encoding='utf-8-sig')


# In[164]:


#4번

def get_review(url):

    
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    numbers = soup.findAll('td',{'class' : 'ac num'})
    titles = soup.findAll('td',{'class':'title'})
    stars = soup.find('tbody').findAll('div',{'class':'list_netizen_score'})
    
    review_number = []
    movie_title = []
    star_list = []

    
    for number in numbers:
        review_number.append(number.text)
    
    for title in titles:
        movie_title.append(title.find('a',{'class':'movie color_b'}).text)
    
    for star in stars:
        star_list.append(star.text)
    
    
    number_sr = pd.Series(data = review_number)
    title_sr = pd.Series(data = movie_title)
    star_sr = pd.Series(data = star_list)
    
    df = pd.concat({'number':number_sr,'title':title_sr,'star':star_sr},axis = 1)
    
    return df


# In[191]:


#5번

import time
import random


url = 'https://movie.naver.com/movie/point/af/list.naver'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
div = soup.find('div',{'class':'paging'})
a_list = div.findAll('a')

all_review = pd.DataFrame()
for a in a_list:
    if a.string == '다음':
        continue
    else:
        page_url = 'https://movie.naver.com/' + a['href']
        
        review = get_review(page_url)
        all_review = all_review.append(review,ignore_index=True)
        time.sleep(random.uniform(1,2))
        
        
save_file_path = 'C:\\study\\workspace_python\\pdsample\\datasets\\mydata'

os.chdir(save_file_path)
all_review.to_csv('naver_10_review.csv', index=False, encoding='utf-8-sig')


# ### 셀레니움 LAB

# In[192]:


from selenium import webdriver
from bs4 import BeautifulSoup
import time


# In[227]:


#2번
#기사제목 css selector 로 추출해보시오


url = 'https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=001&aid=0012306531&rankingType=RANKING'

driver_path = 'C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = driver_path)
driver.get(url)

article_head = driver.find_element_by_css_selector('#articleTitle')
print(article_head.text)


# In[208]:


#3번
#기사 제목을 xpath selector로 추출해보시오

article_head_xpath = driver.find_element_by_xpath('//*[@id="articleTitle"]')
print(article_head_xpath.text)


# In[212]:


#4번
#기사 작성일시를 css selector로 추출하시오 

article_date = driver.find_element_by_css_selector('#main_content > div.article_header > div.article_info > div > span')
print(article_date.text)


# In[215]:


#5번
#기사 작성일시를 xpath selector로 추출하시오

article_date_xpath = driver.find_elements_by_xpath('//*[@id="main_content"]/div[1]/div[3]/div/span')
print(article_date_xpath[0].text)


# In[229]:


#6번, 7번
import time

read_more_button = driver.find_element_by_css_selector('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_view_comment > a > span.u_cbox_in_view_comment')
read_more_button.click()


# In[231]:


#6번, 7번

while True:
    try:
        second_button = driver.find_element_by_css_selector('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_paginate > a > span > span > span.u_cbox_page_more')
        second_button.click()
        time.sleep(2)
    except:
        break

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
reviews = soup.findAll('span',{'class':'u_cbox_contents'})
all_reviews = [review.text for review in reviews]


# In[ ]:





# In[ ]:




