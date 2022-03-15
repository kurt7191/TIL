# 사전 학습 모델



사전 학습(Pre-training) 에 대해서 알아볼 것.

기존에 자비어(Xavier) 등 임의의 값으로 초기화하던 모델의 가중치를 다른 문제(task) 에 학습시킨 가중치들로 초기화하는 방법(사전 학습 했던 모델의 가중치를 다른 태스크의 가중치로 활용)



이때 사전 학습한 가중치를 활용해 학습하고자 하는 본 문제를 다운스트림 태스크(downstream task) 라고 한다.

만일 감성 분석 문제로 학습한 가중치를 유사도 문제의 가중치 초깃값으로 사용하게 되면

다운스트림 태스크는 텍스트 유사도가 되고 사전 학습 태스크(pre-training task)는 감성 분석이 된다.



- 사전 학습 태스크(pre-training task)
- 다운스트림 태스크(downstream task)



사전 학습 문제로 여러 가지가 나올 수 있지만 BERT나 GPT등 사전 학습 문제로 언어 모델을 많이 사용하고 있다.

언어 모델을 간략하게 살펴보면, 특정 단어가 주어졌을 때, 다음 단어가 어떤 단어가 나올지 예측하는 것을 해결하는 문제다.



왜냐하면 감성 분석 같은 경우에는 라벨이 있어야만 가능한 학습 즉 지도 학습 방식이며 따라서 해당하는 데이터를 구하기 어렵기 때문이다. 더군다나 감성 분석 같은 경우에는 특정 언어의 전반적인 이해라기 보다는 특정 태스크에 더 특화되어 언어를 이해하기 때문에 다운 스트림 태스크의 성능이 떨어질수도 있다.



반대로 언어 모델 같은 경우 비지도 학습이며, 태스크의 특성상 특정 언어의 일반적인 특성을 학습하기 때문에 다운스트림 태스크의 성능을 향상시킬 수 있다.



그럼 여기까지 사전 학습의 전반적인 개념을 살펴봤고,

사전 학습된 가중치를 활용하는 방법에 대해서 알아보자. 

그 방법은 두 가지로 나뉘나.



1. 특징 기반 (feature-based) 방법 : 
   - 사전 학습된 특징을 하위 문제의 모델에 부가적인 특징으로 활용하는 방법
   - 모델 중간에 나오는 특징 값 : 특징
   - 예를 들어서 단어에 대한 임베딩 벡텉가 단어에 대한 특징 값이다.
   - word2vec 이 대표적인 특징 기반 사전 학습 활용 방법의 예이다.
   - 학습한 임베딩 특징을 우리가 학습하고자 하는 모델의 임베딩 특징으로 활용하기 때문
2. 미세 조정(fine-tuning) 방법 , 파인 튜닝: 
   - 사전 학습한 모든 가중치와 더불어 하위 문제(downstream task)를 위한 최소한의 가중치를 추가해서 모델을 추가로 학습(미세 조정) 하는 방법.
   - 감정 분석 문제에 사전 학습 시킨 가중치와 더불어 텍스트 유사도를 위한 부가적인 가중치를 추가해 텍스트 유사도 문제를 학습하는 것.(그러면 사전 학습시킨 가중치와 부가적으로 추가한 가중치가 업데이트 된다.)



여기 까지 사전 학습(pre-training), 다운스트림 태스크(downstrea task), feature based, 파인 튜닝에 대해서 살펴봤다.



## BERT(버트)



기존의 사전학습 모델인 GPT, ELMo 등의 모델과 비교해서 높은 성능을 보여준다.

그 이유로 BERT는 양방향성(bidirectional) 을 띠기 때문이다.



GPT : 단방향성

ELMo : 양방향성 이지만 단방향성 모델 두 개를 붙여놓은 것.

BERT : 모델 하나로도 양방향성



BERT모델이 양방향성일 수 있는 이유는 BERT의 사전 학습 문제인 마스크 언어 모델(Masked language modeling) 덕분이다.



### BERT의 사전 학습 문제



언어 모델 : 단어들의 시퀀스에 대한 확률, 단어들의 모음이 있을 때 해당 단어의 모음이 어떤 확률로 등장할지를 나타내는 값

(시퀀스에 대한 확률)



word2vec (CBOW모델), 특정 위치 주변의 단어가 주어졌을 때, 특정 위치 단어를 예측하는 것.



언어 모델은 자연어 처리 분야에서 활발하게 사용되어 왔는데, 언어 모델이 비지도 학습이기 때문이다.

또한 언어에 대한 일반적이고 전반적인 지식을 학습할 수 있기 때문이다.



BERT는 2개의 문제를 사전 학습한다.(두 개의 사전 학습 태스크를 가진다.)



- 마스크 언어 모델링 (MLM)

  - 양방향성
  - 입력 문장이 주어지면 일부 단어들을 MASKING 해서 마스킹된 단어가 무엇인지 예측하게 한다.
  - 기존의 언어 모델 같은 경우 앞의 단어들을 사용해서 다음 단어를 예측하는 방식이다.
  - 하지만 마스크 언어 모델링은 앞뒤 상관없이 문장 안의 단어들을 모두 사용해서 가려진 단어들을 에측한다. 따라서 양방향의 단어들을 모두 사용하게 된다.
  - 15% 마스킹
    - 80 - 15 -15
    - 80%는 MASK, 15%는 다른 단어로 교체, 15%는 그대로

- 다음 문장 예측 (next sentence prediction)

  - 주어진 두 문장이 이어진 문장인지 이어지지 않은 문장인지 판별
  - 데이터 셋 구성은 50%의 확률로 한 텍스트에서 이어지게 데이터를 추출
  - 50%의 확률로 두 개의 텍스트에서 각각 문장을 가져옴.
  - cls, sep 특수 토큰 추가
  - NSP 사전 학습 문제도 추가한 이유는, BERT의 다운스트림 태스크 중에 두 문장 간의 관계를 예측하는 문제에 도움을 주기 위해서임.

  

  ##### BERT의 모델

  

  트랜스포머의 인코더 부분만 활용한다.

  트랜스포머와 다른 점은 기존 트랜스포머의 포지션-와이즈 피드포워드 네트워크에서 사용됐던 ReLU 함수를 사용하는 게 아니라 GELU 함수를 사용한다는 점이다.

  

  GELU : ReLU보다 0주위에서 부드럽게 변화해 학습 성능을 높인다.

  

  BERT모델은 트랜스포머의 크기에 따라서 나뉜다.

  

  1. BERT-base(layer : 12, hidden state : 768, 멀티헤드어텐션의 헤드의 수 A : 12)
  2. BERT-LARGE

  

  (미세 조정 즉 파인튜닝과 같은 거 할 때도 모델의 크기는 사전 학습 모델의 크기와 맞춰야 한다.)

  



## BERT를 활용한 미세조정 학습



구글에서 공개한 BERT모델은 학습한 데이터에 따라 여러 형태로 공개돼 있는데, 대부분 영어 데이터로 학습했다.

한글 데이터를 활용한 문제에 BERT 문제를 활용할 것.

BERT를 활용하기 위해서 가져와야 할 도구 두 가지는 토크나이저와 가중치를 가지고 있는 모델이다.



##### 버트 파일 불러오기

(토크나이저 가져오기)

```python
from transformers import *

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
```



##### 버트 문장 전처리 진행하기



BERT 모델은 입력 값 3개를 받게 되는데 요약하면 다음과 같다.



1. input_ids : 문장을 토크나이즈해서 인덱스 값으로 변환한다. 일반적으로 BERT는 토크나이저를 **워드 피스 토크나이저**(하위 단어 토큰화 알고리즘)를 사용한다.
2. attention_mask : 패딩된 부분에 대해서 학습에 영향을 받지 않기 위해 처리해주는 입력값(어텐션 마스크 기본값:1, 패딩 토큰 : 0)
3. token_type_ids : 두 개의 시퀀스를 입력으로 활용할 때 0과 1로 문자의 토큰 값을 분리한다.



버트에 필요한 입력값의 형태로 Tokenizer 라이브러리를 활용하면 조금 더 손쉽고 빠르게 BERT의 입력값을 구현할 수 있다.

이 라이브러리에서 encode_plus 기능을 활용할 예정.

**encode_plus는 특정 문장을 버트에 필요한 입력 형태로 변환해주고 문장을 최대 길이에 맞게 패딩도 해주며 결과값을 딕셔너리 형태로 반환한다.**



1. 문장은 토크나이징한다.
2. add_special_tokens를 True로 지정하면 토큰의 시작점에 'cls' , 토큰의 마지막에 'sep' 토큰을 붙인다.
3. 각 토큰을 인덱스로 반환한다.
4. max_length에 MAX_LEN 최대 길이에 따라 문장의 길이를 맞추는 작업을 진행한다. MAX_LEN 길이에 미치지 못하는 문장에 패딩을 준다.
5. 컴퓨터가 패딩된게 본래의 값이 아니게 인지해주게끔 attention_mask를 생성한다.
6. 토큰 타입은 문장이 1개인 경우 0, 두 개인 경우 0과 1로 구분해서 생성한다.



```python
def  bert_tokenizer(sent, MAX_LEN):
    
    encoded_dict = tokenizer.encode_plus(
    text = sent1,
    text_pair = sent2,
    add_special_tokens = True, #Add 'cls','sep'
    max_length = MAX_LEN, # Pad & trucate all sentences
    pad_to_max_length = True,
    return_attention_mask = True,
    trucation = True
    )
    
    input_id = encoded_dict['input_ids']
    attention_mask = encoded_dict['attention_mask']
    token_type_id = encoded_dict['token_type_ids']
    
    return input_id, attention_mask, token_type_id

```

**encode_plus는 특정 문장을 버트에 필요한 입력 형태로 변환해주고 문장을 최대 길이에 맞게 패딩도 해주며 결과값을 딕셔너리 형태로 반환한다.**



### 버트를 활용한 한국어 텍스트 분류 모델



##### 네이버 영화 리뷰 데이터 전처리



```python
import os
import re
import numpy as np
from tqdm import tqdm

import tensorflow as tf
from transformers import *

from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import pandas as pd
import matplotlib.pyplot as plt

# 시각화

def plot_graphs(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_'+string], '')
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_'+string])
    plt.show()
    
#random seed 고정
tf.random.set_seed(1234)
np.random.seed(1234)

BATCH_SIZE = 32
NUM_EPOCHS = 3
VALID_SPLIT = 0.2
MAX_LEN = 39 # EDA에서 추출된 Max Length
DATA_IN_PATH = 'data_in/KOR'
DATA_OUT_PATH = "data_out/KOR"

tokenizer = BertTokenizer.from_pretrained("bert-base-multilingual-cased", cache_dir='bert_ckpt', do_lower_case=False)
```



### 토크나이저 테스트



```python
test_sentence = "안녕하세요, 반갑습니다."

encode = tokenizer.encode(test_sentence)
token_print = [tokenizer.decode(token) for token in encode]

print(encode)
print(token_print)
```



