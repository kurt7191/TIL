# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 16:50:47 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup

url='https://movie.naver.com/movie/bi/mi/review.nhn?code=187310'
res=requests.get(url)
soup=BeautifulSoup(res.text,'html.parser')

# 리뷰 리스트
ul=soup.find('ul',class_="rvw_list_area")
lis=ul.find_all('li')

#리뷰 제목 출력
for li in lis:
  print(li.a.text)
  
# 리뷰 제목과 날짜를 크롤링해서 파일에 저장하기
import pandas as pd
import os
import time
import random

df = pd.DataFrame(columns=["review","date"])
for li in lis:
  df = df.append({'review':li.a.text,
                 'date':li.span.em.text}, ignore_index=True)
print(df)

save_file_path = 'D:/kjw/lecture/bda_21_2_대학원공통과목/week12'

os.chdir(save_file_path)
df.to_csv('naver_review.csv', index=False, encoding='utf-8-sig')

# 함수로 만들기

def get_review(url):
  res=requests.get(url)
  soup=BeautifulSoup(res.text,'html.parser')

  ul=soup.find('ul',class_='rvw_list_area')
  lis=ul.find_all('li')
  df = pd.DataFrame(columns=["review","date"])
  for li in lis:
    df = df.append({'review':li.a.text,
                 'date':li.span.em.text}, ignore_index=True)
  return df

# 여러 페이지 크롤링하기

url='https://movie.naver.com/movie/bi/mi/review.nhn?code=187310'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser') 
div = soup.find('div',class_='paging')
a_list = div.find_all("a")
for a in a_list:
    print(a.string)

all_review = pd.DataFrame()
for a in a_list:
  print(a['href'],a.string)
  if a.string=='다음' or a.string=='이전':
    continue
  else:
    page_url='https://movie.naver.com'+a['href']
    print(page_url)

    review = get_review(page_url)
    print(review)
    all_review = all_review.append(review,ignore_index=True)
  time.sleep(random.uniform(1,2)) # 1~2 초 사이의 랜덤한 시간으로 쉬어 진행

print(all_review)
all_review.to_csv('naver_all_review.csv',index=False,encoding='utf-8-sig')
