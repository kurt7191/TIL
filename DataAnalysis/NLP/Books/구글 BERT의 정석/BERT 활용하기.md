# BERT 활용하기



이 장에서는 사전 학습된 BERT 를 사용하는 방법을 알아볼 것.

1. 구글에서 오픈 소스로 제공한 사전 학습된 BERT 모델의 다양한 구성을 살펴본다. (구성)
2. 사전 학습된 BERT 모델을 특징 추출기로 사용하는 방법 확인.
3. 허깅페이스의 트랜스포머 라이브러리, 이를 활용해 사전 학습된 BERT에서 임베딩 추출 방법
4. BERT의 모든 인코더 레이어에서 임베딩을 추출하는 방법
5. 다운스트림 태스크를 위한 BERT 파인 튜닝 방법
   - "텍스트 분류 작업"을 위해 사전 학습된 BERT를 **파인튜닝**하는 방법
   - "감정 분석 작업''을 위해 BERT를 **파인튜닝**하는 방법

*파인튜닝 : 사전 학습된 가중치 값을 원하는 태스크에 적용하고, 가중치를 그 태스크에 맞게 조정하는 작업



<hr>

## 사전 학습된 BERT 모델 탐색



우리는 앞선 2장에서 MLM 과 NSP 로 BERT를 사전학습하는 방법을 배웠다.

하지만 BERT를 사전학습 시키려면 많은 계산 비용이 든다.

따라서 사전 학습된 BERT 모델을 다운로드해 사용하는 게 효과적이다.



1. BERT - cased
   - 토큰 대문자 보존
2. Bert - uncased
   - 토큰 소문자로 변환



사전 학습된 BERT를 이용해서 무엇을 할 수 있을까?

1. 임베딩을 추출해 "특징 추출기"로 사용.
2. 텍스트 분류, 질문-응답 등과 같은 다운스트림 태스크에 맞게 파인 튜닝



## 사전 학습된 BERT에서 임베딩을 추출하는 방법



임베딩을 얻기 위한 간략한 처리 과정을 다음과 같다 with BERT

문장이 있으면 토큰 단위로 나누고, 그 값들을 BERT의 입력값으로 넣어 토큰 단위 표현 벡터인 임베딩을 얻는다.

이때 토큰 수준에서 임베딩을 얻는 것뿐만 아니라 문장 수준의 임베딩도 얻을 수 있다.

이 장에서 토큰 수준 및 문장 수준 임베딩을 얻는 법을 살펴보자.



먼저 하려고 하는 TASK 에 대한 예시를 들어보자.

텍스트 감정 분석을 하려고 한다고 해보자.

우리는 텍스트 원본을 그대로 입력값으로 받아들일 수 없고, 벡터화 해야지만 입력값으로 받아들일 수 있다.

지금까지 NLP를 배우면서 토큰, 단어에 대한 벡터화 방법 여러 가지를 살펴봤다. 

우리는 지금까지 TF-IDF 방법과 word2vec 을 사용해서 텍스트를 벡터화 했다.

하지만 TF-IDF 방법이나 word2vec 은 문맥을 고려하지 못한다는 문제점이 있음을 살펴봤다.

BERT는 이런 단점을 보완하며, 토큰이나 단어를 벡터화할때 문맥 정보를 담을 수 있다.



먼저 예시 문장 "I love Paris" 가 있다고 해보자.

이를 토큰화 하면 다음과 같이 담길 수 있다.



tokens = [I, love, Paris]



이제 자연어 처리를 하기 위해서 문장의 시작과 끝에 태깅을 하도록 하자. 그러면 아래와 같은 결과를 얻는다.



tokens = [[cls],I, love, Paris, [sep]]



자연어 처리를 할 때, 모든 문장의 길이는 각각 다르기 때문에 입력값의 len 값도 모두 다르다.

학습을 시키고 예측을 하기 위해서는 입력값의 shape 을 통일해줄 필요가 있다. 따라사 입력 shape 을 고정시키고 미달인 문장에 대해서는 PAD를 주어 길이를 맞춘다.

예를 들어서 토큰 길이를 7로 고정했다고 하면, 위의 tokens 리스트는 길이가 5이기 때문에 pad 2개를 줘야한다.

따라서 아래와 같은 결과를 얻게된다.



tokens = [[cls],I, love, Paris, [sep],[pad],[pad]]



이때 중요한 점은 컴퓨터 pad에 대해서 실제 토큰의 일부가 아님을 깨닫게 해야한다는 점이다.

따라서 컴퓨터가 알아들을 수 있게 인덱스로 이를 설명한다.

따라서 새로운 리스트 attention_mask 를 만든다. 모든 어텐션 마스크 값을 default 로 1을 할당하고, pad인 토큰 인덱스에는 0값을 할당한다.

그러면 위의 예시는 아래와 같은 결과를 얻게 된다.



attention_mask = [1,1,1,1,1,0,0]



다음으로 얻었던 토큰을 토큰 ID로 매핑한다.

그럼 다음과 같은 결과를 얻을 수 있다.



token_ids = [101,1045,2293,3000,102,0,0]



이렇게 토큰을 얻고 마스크 값을 얻었으면 이 두 값을 BERT의 입력값으로 넣어준다.

사전 학습된 BERT에 입력값이 들어가면 값이 BERT 의 인코더 레이어들을 거치게 되고 최종 출력값을 도출하게 된다.

각각의 토큰은 특정 차원의 표현 벡터를 가지게 되는데 사전 학습된 BERT의 은닉층이 768개면 단어 표현 벡터의 차원도 768이다.



사전 학습된 BERT를 통해서 토큰 단위로 표현 벡터를 얻는 것 뿐만 아니라 문장 단위로 표현 벡터를 얻을 수 있다.

CLS 태그는 기본적으로 모든 문장의 집계 표현을 보유하고 있다.

따라서 각 문장의 CLS 태그를 문장에 대한 표현 벡터로 사용할 수 있다.

위와 같은 방식으로 모든 문장 각각에 대해서 표현 벡터를 얻고 이를 입력값으로 제공하고 분류기를 학습해 감정 분석 작업을 진행할 수 있다.



여기까지 사전 학습된 BERT를 이용해서 임베딩(표현) 을 추출하는 방법을 살펴봤다.

이제 트랜스포머로 알려진 라이브러리를 활용해서 이러한 작업을 수행하는 방법을 확인하자.



### 허깅페이스 트랜스포머



허깅페이스는 자연어처리의 민주화를 추구하는 조직이다.



### BERT 임베딩 생성하기



본래 나는 jupyter 를 이용하지만 구글 코랩을 이용해서 진행했다.



```python
import torch
from transformers import BertModel, BertTokenizer
```



트랜스포머 모델을 다운로드 하기 위해서 패키지를 가져온다.



```python
model = BertModel.from_pretrained('bert-base-uncased')
```



사전 학습된 BERT 모델을 가져오는데 토큰이 소문자로 변환된 걸 사용한다.



```python
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
```



BERT , bert-base-uncased 를 사전 학습 시키는데 사용된 토크나이저를 다운로드 한다.



##### 입력 전처리 하기



이제 문장을 BERT에 입력하기 전에 전처리하는 방법을 살펴보자.



```python
sentence = "I love Paris"

tokens = tokenizer.tokenize(sentence)
print(tokens)

tokens = ['[CLS]'] + tokens + ['[SEP]']
print(tokens)
```



임의의 문장을 생성하고 tokenizer 로 token화 한 이후에

문장의 시작과 끝에 "CLS, SEP" 을 넣어준다.



```python
tokens = tokens + ['[PAD]'] + ['[PAD]']
print(tokens)
```



문장의 길이를 7로 고정한다고 가정하고 위의 임의의 문장에 대해서 "pad" 를 넣어줘서 길이를 맞춰주자.



```python
attention_mask = [1 if i != '[PAD]' else  0 for i in tokens]
```



컴퓨터가 pad가 본래 토큰에 속한 값이 아니란걸 깨닫게 하기 위해서 attention mask 를 만든다.

pad에 해당하는 값을 0을 넣어주고 그렇지 않은 값은 1을 넣어준다.



```python
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(token_ids)
```



앞서 문장을 토큰화하면서 사용했던  tokenizer 객체를 이용해서, 토큰에 id를 매핑한다.

이제 사전 학습된 BERT를 이용해서 문장의 표현 벡터 혹은 임베딩을 얻기 위한 준비물인

attention mask 와 token id로 매핑된 토큰들을 얻게 되었다.

이제 사전 학습된 BERT에 이 준비물들(입력값)을 넣어서 임베딩값을 얻어보자.



##### 임베딩 추출하기



BERT모델은 두 값으로 구성된 튜플로 출력을 반환한다.

**첫 번째 값은 은닉 상태 표현인데, 이는 최종 인코더에서 얻은 모든 토큰의 표현 벡터로 구성되어있다.**

**두 번째 값인 cls_head 는 CLS 토큰의 표현으로 구성된다.**

(최종 인코더에서 얻은 모든 토큰의 표현 벡터, CLS 토큰의 표현 벡터) = (은닉 상태 표현, cls_head)



```python
hidden_rep, cls_head = model(token_ids, attention_mask = attention_mask, return_dict = False)

```



여기서 중요한 점은 책에는 안나와 있지만 return_dict 파라미터다.

bert모델이 업데이트 되면서 model 을 통한 반환 값이 달라지게 되었다.

따라서 retur_dict = False 를 해줘야 온전한 튜플 형태의 array가 반환된다.



여기서 hidden_rep 의 shape 을 살펴보면 [1,7,768] 이 나온다.

1은 batch 사이즈고, 7은 토큰의 길이이며, 768 은 각 토큰에 벡터 차원을 의미한다.

따라서 hidden_rep[0] [0] 은 cls의 벡터 표현이 [0] [1] 은 i의 벡터 표현이 그리고 [0] [2] 는 love 의 벡터 표현이 나온다.



```python
cls_head.shape
```



cls_head 는 cls 토큰의 표현 벡터가 담겨져 있음을 확인했다.

앞서 우리는 cls 토큰이 문장에 대한 표현 벡터로 사용될 수 있음을 살펴봤다.

즉 cls_head 를 "I love Paris" 의 문장 표현 벡터로 사용할 수 있다.



그렇다면 모든 인코더 레이어 계층에서도 임베딩을 추출할 수 있을까?

(최종 인코더 레이어 계층에서 벡터, 임베딩을 추출하는 게 아니라 각각의 인코더 레이어 계층에서 임베딩 혹은 벡터를 추출할 수 있을까?)

그럴 수 있으며 다음 장에서 살펴보려고 한다.



### BERT의 모든 인코더 레이어에서 임베딩을 추출하는 방법



최종 인코더 레이어에서 얻은 벡터만을 사용하는 것보다

여러 인코더 레이어의 임베딩을 속성으로 사용해 실험해보니 더 좋은 결과를 얻었다.

(F1 SCORE)



### 임베딩 추출하기



모든 인코더 계층에서 임베딩을 가져오기 위해, 모델을 정의하면서 output_hidden_state = True 로 설정한다.



```python
from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained('bert-base-uncased',
                                  output_hidden_states = True)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
```





먼저 위의 과정과 같은 전처리 과정을 거진다.



```python
sentence = 'I love Paris'
tokens = tokenizer.tokenize(sentence)
tokens = ['[CLS]'] + tokens + ['[CLS]']
print(tokens)

tokens += ['[PAD]'] + ['[PAD]']
print(tokens)

tokens_id = tokenizer.convert_tokens_to_ids(tokens)
attention_mask = [1 if i != '[PAD]' else 0 for i in tokens]
print(attention_mask)

token_ids = torch.tensor(token_ids).unsqueeze(0)
attention_mask = torch.tensor(attention_mask).unsqueeze(0)
```



그리고 임베딩을 가져오는데, output_hidden_state = True 기 때문에 3개의 값이 있는 튜플이 반환된다.

(최종 인코더 계층에서만 얻은 모든 토큰의 표현 벡터, 최종 인코더 계층의 cls 토큰 표현 벡터, 모든 인코더 계층에서 얻은 모든 토큰의 표현 벡터 )



```python
last_hidden_state, pooler_output, hidden_states = model(token_ids,
                                                        attention_mask = attention_mask)

```



다시 정리하면 

- last_hidden_state : 최종 인코더의 모든 토큰들 단어 표현 벡터
- pooler_output : 최종 인코더의 cls 토큰 단어 표현 벡터 (선형 및 tanh 활성화 함수에 의해 계산된다.)
- hidden_states : 모든 인코더 레이어 계층에서 얻은 모든 토큰의 표현 벡터



근데 여기서 error 가 발생한다. output_hidden_state = True 로 설정했지만, 이게 업데이트 돼서 인코딩의 모든 레이어에서 나오는 표현 벡터를 못얻고 있다. 다음에 한 번 오류를 수정해보자.



<hr>

## 다운 스트림 태스크를 위한 BERT 파인 튜닝 방법



지금까지 사전 학습된 BERT모델을 사용하는 방법을 배웠다.

사전 학습된 모델을 다운스트림 태스크에 맞춰서 파인 튜닝 하는 방법을 배워볼 것.



- 텍스트 분류
- 자연어 추론(NLI)
- 개체명 인식(NER)
- 질문 - 응답



### 텍스트 분류



사전 학습된 BERT 모델을 텍스트 분류 태스크에 맞춰 파인 튜닝하는 방법.



먼저 데이터 셋을 가정해보자.

각각의 문장에 대해서 긍정의 감정인지 혹은 부정의 감정인지에 대한 데이터 셋이 있다고 가정해보자.

그 데이터 셋에 "I love Paris" 가 있다고 가정해보자.

I love Paris 를 토큰화하고 전처리 과정을 거친다. 시작 부분에는 "[cls]" 를 추가하고, 문장의 끝에는 "[sep]" 를 추가한다.

그리고 사전 학습된 BERT 에 전처리된 문장을 집어 넣어서 모든 토큰의 벡터 표현을 얻는다.



다음으로 모든 토큰의 임베딩을 무시하고 R_cls 인 [cls] 토큰의 임베딩만 취한다.

cls토큰 임베딩을 분류기(소프트맥스 함수가 있는 피드포워드 네트워크)에 입력하고 학습시켜 감정 분석을 수행한다.



그렇다면 주목해야할 점이 있는데

사전 학습된 BERT 모델을 파인 튜닝하는 게, 사전 학습된 BERT를 특징 추출기로 사용하는 것은 어떻게 다른가?

사전 학습된 BERT 모델을 **파인 튜닝**하면  **분류기 가중치와 함께 사전 학습된 BERT 모델의 가중치를 업데이트** 하는 것.

반면 사전 학습된 BERT 모델을 특징 추출기로만 사용하면, 사전 학습된 BERT 모델의 가중치는 업데이트하지 않고, 분류기의 가중치만 업데이트 하게 된다.



그럼 정리해서 감정 분석 태스크를 위해서 사전 학습된 BERT 모델을 파인 튜닝하는 과정을 살펴보자.

먼저 입력 문장을 전처리 해서 "CLS, I, love, Paris, SEP" 와 같은 형식으로 입력값을 만든다.

이 입력값을 사전 학습된 BERT 모델에 집어 넣어서 각 토큰에 관한 표현 벡터, 임베딩을 얻는다.

이때 r_cls 임베딩만 참고해서 softmax 함수를 이용해 피드 포워드 네트워크에 집어 넣는다.

이 값을 참고해서 긍정과 부정을 분류한다.



##### 감정 분석을 위한 BERT 파인 튜닝



IMDB 데이터 셋을 사용할건데, IMBD 데이터 셋은 영화 리뷰와 그 리뷰에 관한 감정 레이블을 가진다.



```python
%%capture
!pip install nlp==0.4.0
!pip install transformers==3.5.1
```



```python
from transformers import BertForSequenceClassification, BertTokenizerFast, Trainer, TrainingArguments
from nlp import load_dataset
import torch
import numpy as np


#데이터셋과 모델 불러오기

!gdown https://drive.google.com/uc?id=11_M4ootuT7I1G0RlihcC0cA3Elqotlc-
dataset = load_dataset('csv', data_files='./imdbs.csv', split='train')

dataset = dataset.train_test_split(test_size=0.3)

train_set = dataset['train']
test_set = dataset['test']

model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')

#데이터셋 전처리

tokenizer('I love Paris')
tokenizer(['I love Paris', 'birds fly','snow fall'], padding = True, max_length=5)

def preprocess(data):
    return tokenizer(data['text'], padding=True, truncation=True)

train_set.set_format('torch', columns=['input_ids', 'attention_mask', 'label'])
test_set.set_format('torch', columns=['input_ids', 'attention_mask', 'label'])

#모델 학습
batch_size = 8
epochs = 2

warmup_steps = 500
weight_decay = 0.01


training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=epochs,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    warmup_steps=warmup_steps,
    weight_decay=weight_decay,
    evaluate_during_training=True,
    logging_dir='./logs',
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_set,
    eval_dataset=test_set
)


trainer.train()
trainer.evaluate()
```



### 자연어 추론



자연어 추론 (NLI) 모델은 가정이 주어진 전제에 참인지 거짓인지 중립인지 여부를 결정하는 태스크.

BERT 를 파인 튜닝해서 NLI를 수행하는 방법을 알아보자.



데이터셋은 전제에 해당하는 문장과 가설에 해당하는 문장이 있고 이에 대한 (참, 거짓, 중립) 레이블이 존재한다.

우리가 만들려고 하는 모델의 목적은 전제와 가설 문장의 쌍에 관해서 참,거짓,중립 여부를 결정하는 것이다.



1)두 문장을 token화 시킨다. 그리고 문장의 시작엔 cls를 넣고 문장 중간 중간에는 sep 을 넣는다.

2)데이터를 사전 학습된 BERT 에 넣어서 각 토큰 마다의 임베딩 값을 얻는다.

3)문장 전체에 대한 임베딩 정보값은 cls 토큰 임베딩값에 들어가 있다. 따라서 r_cls 임베딩값을 분류기에 입력해서 참, 거짓, 중립일 확률을 반환한다.

4)학습 초기에는 결과가 좋지 않지만 학습할수록 결과가 좋아진다.



### 질문 - 응답



question-answering task 에서는 질문에 대한 응답이 포함된 단락과 함께 질문이 제공된다.

태스크의 주 업무는 주어진 질문에 대한 단락에서 답을 추출하는 것이다.



그러니까 질문 문장이 한 개 있고, 단락 문장이 하나 있는데, 이 단락 글의 내용 안에는 질문의 응답에 관한 내용이 포함되어 있다.

우리 모델을 질문에 대한 응답을 단락의 내용 안에서 찾아서 출력해야 한다.

이 과정을 수행하기 위해서 우리 모델은 주어진 단락의 답을 포함하는 텍스트 범위의 시작과 끝의 인덱스를 이해해야 한다. 시작 인덱스부터 끝 인덱스가 질문에 대한 응답일 것이다.



단락 내의 시작 인덱스와 끝 인덱스를 알기 위해서 시작 벡터 S와 끝 벡터 E라는 2개의 벡터를 사용한다.(이 두 벡터는 학습이 되는 값.)

각각의 문장 내의 토큰 임베딩과 시작 벡터S와의 내적을 구하고, 그 값을 소프트맥스 함수에 집어 넣는다.

그리고 시작이될 확률이 가장 큰 토큰을 시작 토큰으로 선택한다.

끝 인덱스 선정도 마찬가지다.











