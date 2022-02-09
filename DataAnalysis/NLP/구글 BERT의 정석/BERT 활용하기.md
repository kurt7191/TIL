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

이때 토큰 수준에서 임베딩을 얻는 것 뿐만 아니라 문장 수준의 임베딩도 얻을 수 있다.

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





근데 여기서 error 가 발생한다. output_hidden_state = True 로 설정했지만, 이게 업데이트 돼서 인코딩의 모든 레이어에서 나오는 표현 벡터를 못얻고 있다. 다음에.