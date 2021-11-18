# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 21:59:08 2021

@author: USER
"""
from selenium import webdriver
import pandas as pd
import time
 
url = "https://play.google.com/store/apps/details?id=kr.co.zumo.app&showAllReviews=true" 
driverPath = 'D:/kjw/lecture/bda_21_2_대학원공통과목/week12/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(driverPath) 
driver.get(url)

# 개별 리뷰 살펴보기

# 리뷰
review = driver.find_element_by_xpath("//span[@jsname='bN97Pc']") 
review.text

# 날짜
date = driver.find_element_by_xpath("//span[@class='p2TkOb']") 
date.text

# 좋아요 수
like = driver.find_element_by_xpath("//div[@aria-label='이 리뷰가 유용하다는 평가를 받은 횟수입니다.']") 
like.text

# 별점 데이터

star = driver.find_element_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']") 
star.get_attribute('aria-label')

# 전체 리뷰 살펴보기
reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']") 
len(reviews)

# 스크롤 내리기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 10번 스크롤 내리기
for i in range(10): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    time.sleep(2)

# 더보기 누르기
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()

## 스크롤과 더보기 합하기
SCROLL_PAUSE_TIME = 3 
last_height = driver.execute_script("return document.body.scrollHeight") 
while True: 
    # (1) 4번의 스크롤링 
    for i in range(4): 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        time.sleep(SCROLL_PAUSE_TIME) 
    # (2) 더보기 클릭 
    try:
        driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
    except:
        break
    # (3) 종료 조건 
    new_height = driver.execute_script("return document.body.scrollHeight") 
    if new_height == last_height: 
        break 
    last_height = new_height

# Just One Loof
for i in range(4): 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(SCROLL_PAUSE_TIME) 
    # (2) 더보기 클릭 
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()

## Data Collection

reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']") 
len(reviews)
# 날짜
dates = driver.find_elements_by_xpath("//span[@class='p2TkOb']") 
len(dates)
# 좋아요 수

likes = driver.find_elements_by_xpath("//div[@aria-label='이 리뷰가 유용하다는 평가를 받은 횟수입니다.']") 
len(likes)
# 별점 데이터

stars = driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']") 
len(stars)

# Make a dataframe
res_dict = [] 
for i in range(len(reviews)): 
    res_dict.append({ 
        'DATE' : dates[i].text, 
        'STAR' : stars[i].get_attribute('aria-label'), 
        'LIKE' : likes[i].text, 
        'REVIEW' : reviews[i].text })
res_df = pd.DataFrame(res_dict) 
res_df

import os
save_file_path = 'D:/kjw/lecture/bda_21_2_대학원공통과목/week12'
os.chdir(save_file_path)
res_df.to_csv('lifeplus_review.csv', index=False, encoding='utf-8-sig')

