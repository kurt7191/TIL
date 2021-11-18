# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:58:22 2021

@author: USER
"""

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)  # quote_plus가 한글 변환


driver = webdriver.Chrome(executable_path=r'D:/kjw/lecture/bda_21_2_대학원공통과목/week12/chromedriver_win32/chromedriver.exe')
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

v = soup.select('div.yuRUbf')

for i in v:
    print(i.select_one('h3.LC20lb.DKV0Md').text)
    print(i.a.attrs['href'])
    print()

driver.close()
