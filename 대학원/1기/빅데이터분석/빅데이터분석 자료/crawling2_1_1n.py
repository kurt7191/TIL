# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 02:22:07 2021

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:02:57 2021

@author: USER
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv
import os
import time
import random

save_file_path = 'D:/kjw/lecture/bda_21_2_대학원공통과목/week12'
#save_file_path = '크롤링 파일 저장 위치'

url = 'https://search.shopping.naver.com/best/category/click?categoryCategoryId=50000151&categoryChildCategoryId=&categoryDemo=A00&categoryMidCategoryId=50000151&categoryRootCategoryId=50000003&period=P1D'
result = requests.get(url)
#result.encoding = 'utf8'

# 제품명 가져오기
a = result.text
soup = BeautifulSoup(a, 'html.parser')


name = soup.select('div.productList_title__1nYWw')

for i in name :
    print(i.text)
    
# Top-5
print('='*20+'\nTop-5 제품\n'+'='*20)
for i in range(5) :
    print(name[i].text)


# save to a csv file
    
os.chdir(save_file_path)
save_file_name = 'naver_best_title1.csv'    
columns_list=['제품명']
f=open(save_file_name, 'w+', newline='')
cw = csv.writer(f)
cw.writerow(columns_list)

for i in name :
    temp_text=[]
    temp_text.append(i.text)
    cw.writerow(temp_text)
    
f.close()
print('\n!!!! Best Product Title Web Crawling Complete !!!!\n')



## to get detail product information
# to get urls

product_page_urls = []
for cover in soup.select('li.productList_item__2qOiU'):
  link=cover.select_one('a').get('href')
  if link == '#': continue
  product_page_urls.append(link)
print(product_page_urls)
len(product_page_urls)

save_file_name = 'naver_best_product_inf1.csv'    
columns_list=['랭킹','제품명','최저가','판매처']
f=open(save_file_name, 'w+', newline='')
cw = csv.writer(f)
cw.writerow(columns_list)


for index, product_page_url in enumerate(product_page_urls):
    html=urlopen(product_page_url)
    bsObject=BeautifulSoup(html,"html.parser")
    product_inf=[]
    title=bsObject.select('div.top_summary_title__15yAr > h2')[0].text
    product_inf.append(title)
    try:
        score=bsObject.select('div.top_grade__3jjdl')[0].text
    except:
        score=''
    product_inf.append(score)
    min_price=bsObject.select('em.lowestPrice_num__3AlQ-')[0].text
    product_inf.append(min_price)
    delivery_inf=bsObject.select('div.lowestPrice_delivery_price__3f-2l')[0].text
    product_inf.append(delivery_inf)    

    print(index+1,title, score, min_price, delivery_inf)
    cw.writerow(product_inf)
    time.sleep(random.uniform(1,3)) # 1~3 초 사이의 랜덤한 시간으로 쉬어 진행
    
f.close()
print('\n!!!! Product Information Web Crawling Complete !!!!\n')
