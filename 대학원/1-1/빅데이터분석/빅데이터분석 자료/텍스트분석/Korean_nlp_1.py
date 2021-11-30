# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:33:55 2021

@author: USER
"""

review1="""
죄송한데 이영화 도데체 어느 포인트에서 감동을 하라는 거죠?
진짜 모르겠어서 그래요 알려주세요 제발...
그래미는 외국어 영화상은 왜 준거지?
정말 미나리로 감동 받고 싶으면
이 미나리말고 다른 미나리 추천드릴께요
미나리로 대박 눈물뽑은 헬로 고스트가 훨 낫음...
헬로고스트 미나리가 백번 감동 줌...
미나리신드롬은 마치 동화 벌거벗은 임금님 같다
기생충이 아카데미 올라왔으니 금년에도 한국꺼 뭐 없나?
어 미나리? 어라 미국 자본이야? 오 한류랑 미국 자본의 콜라보영화 
이거 이슈 되겠는데?
그래서 매스컴에서 연신 띄워서 환상을 현실로 만들어준 영화
재미없는데 일단 이슈는 되었으니 상은 줘야겠고...
그렇게 상탔다니까 아 재미있는거야라고 
스스로 셀프최면 거는거지...
마치 벌거벗은 임금님처럼
"""


review2="""
초보 감독의 미숙한 연출로 흐름이 이어지지 못하는 
아쉬움이 많은  영화네요.   
시대를 잘 타고 나와서 아카데미 후보에 오르는 
운빨이  90%랄까 ~~   
마더같은 영화가  지금 나왔다면 아카데미상을 휩쓸건데,,,  
아무튼 후보에 거론되는것도  살짝 민망한 정도 ~~
"""

# 띄어쓰기
# pip install git+https://github.com/haven-jeon/PyKoSpacing.git

from pykospacing import spacing

review1_space=spacing(review1)
print(review1_space)
print(review1)

review2_space=spacing(review2)
print(review2_space)
print(review2)

# 문장 분리
import kss
review1_split=kss.split_sentences(review1_space)
review2_split=kss.split_sentences(review2_space)

# 숫자 제거

import re

p=re.compile("[0-9]+")
review1_n_remove=[]
for sentence in review1_split:
    review1_n_remove.append(p.sub(" ", sentence))
print(review1_n_remove)

review2_n_remove=[]
for sentence in review2_split:
    review2_n_remove.append(p.sub(" ", sentence))
print(review2_n_remove)


# 문장부호, 특수문자 제거

p=re.compile("\W+")

review1_p_remove=[]
for sentence in review1_n_remove:
    review1_p_remove.append(p.sub(" ", sentence))
print(review1_p_remove)

review2_p_remove=[]
for sentence in review2_n_remove:
    review2_p_remove.append(p.sub(" ", sentence))
print(review2_p_remove)

# 맞춤범 검사
# pip install hanspell 또는

#git clone https://github.com/ssut/py-hanspell.git
#cd py-hanspell
#python setup.py install
# 이후에 spyder 종료 후 다시 열면 import 가능

from hanspell import spell_checker

spell_checker.check(review1_p_remove[0])

review1_spell=[]
for sentence in review1_p_remove:
    review1_spell.append(spell_checker.check(sentence).checked)

review2_spell=[]
for sentence in review2_p_remove:
    review2_spell.append(spell_checker.check(sentence).checked)


# 형태소 분석기를 이용한 토큰화
from konlpy.tag import Okt  
okt=Okt()  

review1_tokens=[]
for sentence in review1_spell:
    review1_tokens.append(okt.pos(sentence))

review2_tokens=[]
for sentence in review2_spell:
    review2_tokens.append(okt.pos(sentence))

#review1_tokens=[]
#for sentence in review1_spell:
#    review1_tokens.append(okt.morphs(sentence))

#review2_tokens=[]
#for sentence in review2_spell:
#    review2_tokens.append(okt.morphs(sentence))

# 명사, 동사, 형용사만 추출
review1_tokens1=[]
for sentence in review1_tokens:
    new_sent=[]
    for token in sentence:
        if (token[1]=='Noun' or token[1]=='Adjective' or token[1]=='Verb'):
            new_sent.append(token)
    review1_tokens1.append(new_sent)

review2_tokens1=[]
for sentence in review2_tokens:
    new_sent=[]
    for token in sentence:
        if (token[1]=='Noun' or token[1]=='Adjective' or token[1]=='Verb'):
            new_sent.append(token)
    review2_tokens1.append(new_sent)

# 표제어 추출
# pip install soylemma 
from soylemma import Lemmatizer

lemmatizer = Lemmatizer()
lemmatizer.analyze('차가우니까')
lemmatizer.lemmatize('차가우니까')
lemmatizer.analyze('한국어') #명사는 결과가 empty
lemmatizer.lemmatize('몰라서') # 결과가 여러 개 나올 수 있음
lemmatizer.lemmatize('그래요')

review1_stems=[]
for sentence in review1_tokens1:
    new_sent=[]
    for token in sentence:
        if (token[1]=='Adjective')|(token[1]=='Verb'):
            stem_result=lemmatizer.lemmatize(token[0])
            if len(stem_result)!=0:              # 빈 리스트가 반환되는 경우 제외
                new_sent.append(stem_result[0])  # 결과 중 맨 앞에 것만 추가
        else:
            new_sent.append(token)
    review1_stems.append(new_sent)
            

review2_stems=[]
for sentence in review2_tokens1:
    new_sent=[]
    for token in sentence:
        if (token[1]=='Adjective')|(token[1]=='Verb'):
            stem_result=lemmatizer.lemmatize(token[0])
            if len(stem_result)!=0:              # 빈 리스트가 반환되는 경우 제외
                new_sent.append(stem_result[0])  # 결과 중 맨 앞에 것만 추가
        else:
            new_sent.append(token)
    review2_stems.append(new_sent)


# Stopwords 제거

stopwords=[('이','Noun'), ('거','Noun'),('오','Noun'), ('것','Noun')]
review1_stop=[]
for sentence in review1_stems:
    new_sent=[]
    for token in sentence:
        if token not in stopwords:
            new_sent.append(token)
    review1_stop.append(new_sent)

review2_stop=[]
for sentence in review2_stems:
    new_sent=[]
    for token in sentence:
        if token not in stopwords:
            new_sent.append(token)
    review2_stop.append(new_sent)

# pos 태그 제거
review1_final=[]
for sentence in review1_stop:
    new_sent=[]
    for token in sentence:
        new_sent.append(token[0])
    review1_final.append(new_sent)

review2_final=[]
for sentence in review2_stop:
    new_sent=[]
    for token in sentence:
        new_sent.append(token[0])
    review2_final.append(new_sent)

# one list로 만들기
review1_final1=[]
for sentence in review1_final:
    review1_final1.extend(sentence)
print(review1_final1)

review2_final1=[]
for sentence in review2_final:
    review2_final1.extend(sentence)
print(review2_final1)

