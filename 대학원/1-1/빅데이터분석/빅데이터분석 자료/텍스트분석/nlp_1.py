# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 20:40:46 2021

@author: USER
"""

from nltk.tokenize import word_tokenize

sentence = "Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."

print(word_tokenize(sentence))

from nltk.tokenize import sent_tokenize

paragraph = "Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data. Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation."

print(sent_tokenize(paragraph))

import konlpy

from konlpy.tag import Okt

okt = Okt()

text = "한글 자연어 처리는 재밌다 이제부터 열심히 해야지ㅎㅎㅎ"
print(okt.morphs(text))
print(okt.morphs(text, stem=True)) # 형태소 단위로 나눈 후 어간을 추출

print(okt.nouns(text))
print(okt.phrases(text))

print(okt.pos(text))
print(okt.pos(text, join=True)) # 형태소와 품사를 붙여서 리스트화

