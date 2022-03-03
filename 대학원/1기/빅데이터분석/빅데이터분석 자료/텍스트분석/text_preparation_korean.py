# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:00:00 2021

@author: USER
"""

import pandas as pd

review_df=pd.read_csv("daum_minari.csv")

# 띄어쓰기
# pip install git+https://github.com/haven-jeon/PyKoSpacing.git

from pykospacing import spacing

review_df['comment_n']=review_df['comment'].apply(lambda x: spacing(x))

# 문장 분리
import kss

review_df['comment_n']=review_df['comment_n'].apply(lambda x: kss.split_sentences(x))

# 숫자 제거

import re

def remove_num(sent_list):
    p=re.compile("[0-9]+")
    sent_n_remove=[]
    for sentence in sent_list:
        sent_n_remove.append(p.sub(" ", sentence))
    return(sent_n_remove)

review_df['comment_n']=review_df['comment_n'].apply(lambda x: remove_num(x))


# 문장부호, 특수문자 제거

def remove_punc(sent_list):
    p=re.compile("\W+")
    sent_n_remove=[]
    for sentence in sent_list:
        sent_n_remove.append(p.sub(" ", sentence))
    return(sent_n_remove)

review_df['comment_n']=review_df['comment_n'].apply(lambda x: remove_punc(x))


# 맞춤범 검사
# pip install hanspell 또는

#git clone https://github.com/ssut/py-hanspell.git
#cd py-hanspell
#python setup.py install
# 이후에 spyder 종료 후 다시 열면 import 가능

from hanspell import spell_checker

def spell_checking(sent_list):
    sent_spell=[]
    for sentence in sent_list:
        sent_spell.append(spell_checker.check(sentence).checked)
    return(sent_spell)
    
review_df['comment_n']=review_df['comment_n'].apply(lambda x: spell_checking(x))


#### 명사만 추출 <- 형태소 사용부터 변경
from konlpy.tag import Okt  
okt=Okt()  

def noun_selection(sent_list):    
    sent_tokens=[]
    for sentence in sent_list:
        sent_tokens.append(okt.nouns(sentence))
    return(sent_tokens)

review_df['comment_n']=review_df['comment_n'].apply(lambda x: noun_selection(x))

# Stop word 제거

def rem_n_stopwords(sent_list):
    stopwords=['이','거','것','저','또','도','나','더','그','일','말','제','수','안','줄','게','좀','듯','님','점','등','고','영화']
    sent_stop=[]
    for sentence in sent_list:
        new_sent=[]
        for token in sentence:
            if token not in stopwords:
                new_sent.append(token)
        sent_stop.append(new_sent)
    return(sent_stop)

review_df['comment_n']=review_df['comment_n'].apply(lambda x: rem_n_stopwords(x))


# 빈 리스트 제거(문장에 빈 경우)

def remove_empty_list(sent_list):
    removed_list = []
    for sentence in sent_list:
        if sentence: # sentence가 빈 경우가 아니면
            removed_list.append(sentence)    
    return removed_list

review_df['comment_n']=review_df['comment_n'].apply(lambda x: remove_empty_list(x))

review_df.to_csv('daum_minari_result.csv',index=False, encoding='utf-8-sig')

# one list로 만들기

def one_word_list(sent_list):
    one_list=[]
    for sentence in sent_list:
        one_list.extend(sentence)
    return(one_list)

review_df['comment_n']=review_df['comment_n'].apply(lambda x: one_word_list(x))

# Word Frequency 

total_word=[]
for i in range(len(review_df)):
    total_word.extend(review_df.loc[i,"comment_n"])

pd.Series(total_word).value_counts().head(15)


# 한글 폰트 사용
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

pd.Series(total_word).value_counts().head(15).plot(kind='bar')
pd.Series(total_word).value_counts().head(15).plot(kind='barh')
pd.Series(total_word).value_counts().head(15).plot(kind='barh').invert_yaxis()

