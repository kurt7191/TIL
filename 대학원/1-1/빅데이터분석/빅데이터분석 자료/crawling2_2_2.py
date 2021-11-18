# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:22:25 2021

@author: USER
"""

import time

from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'D:/kjw/lecture/bda_21_2_대학원공통과목/week12/chromedriver_win32/chromedriver.exe')
browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

tag_names = browser.find_element_by_css_selector("ul.rank_top1000_list").find_elements_by_tag_name("li")

tag_names[0].text
tag_names[0].text.split("\n")


for tag in tag_names:
    print(tag.text.split("\n"))
