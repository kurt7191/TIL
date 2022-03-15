# sentence-BERT 및 domain-BERT 살펴보기



sentence-BERT 는 BERT의 파생 모델로 주로 문장의 표현을 얻는데 사용된다.



- sentence-BERT로 문장 표현에 대해 배우기
- sentence-transformers 라이브러리 탐색
- 지식 증류로 다국어 임베딩 학습
- ClinicalBERT 및 BioBERT 와 같은 domain-BERT 살펴보기



<HR>

## sentence-BERT 로 문장 표현 배우기



sentence-BERT는 고정 길이 문장 표현을 얻는 데 사용된다.

사전 학습된 BERT 또는 파생 모델을 이용한다.

vanila-BERT 또는 파생 모델을 직접 사용해서 문장 표현을 얻을 수 있다.

하지만 vanila-BERT는 유사도를 계산할 때 시간이 많이 걸리는데, 계산 시간이 오래걸리는 단점을 개선하기 위해서 sentence-BERT가 사용될 수 있다.

sentence-BERT는 **문장 쌍 분류** 혹은 **두 문장간의 유사도 계산** 등에 널리 사용된다.



sentence-BERT의 작동 원리를 살펴보기 전에 사전 학습된 BERT를 이용해서 문장 표현을 계산하는 법을 살펴보자.



### 문장 표현 계산



사전 학습된 BERT를 이용해서 문장 표현을 계산해보자.

Paris is a beautiful city 를 먼저 토큰화 한다.



[cls, Paris, is, a, beautiful, city, sep]



앞서 BERT 모델에서 R_cls 토큰이 문장의 표현을 담고 있다고 했었다. 따라서 Paris is a beautiful city 문장의 표현을 R_cls 토큰의 표현으로 정할 수 있다.



issue :

사전 학습된 BERT 모델에서 출력된 어떤 문장의 표현은 BERT 모델이 파인 튜닝되기 전이기 때문에 토큰의 문장 표현이 정확하지 않을 수 있다.



solution : 

따라서 모든 토큰의 표현을 풀링해서 문장 표현을 계산할 수 있다.(평균 풀링, 최대 풀링)



- 평균 풀링을 하게 되면 문장 표현은 본질적으로 모든 단어의 의미를 가진다.
- 최대 풀링을 하게 되면 문장 표현은 본질적으로 중요한 토큰의 의미를 가진다.



사전 학습된 BERT 모델을 통해서 문장의 표현을 얻는 방법들을 살펴봤는데, 다음으로 sentence-BERT 모델이 어떻게 문장의 표현을 얻는지 살펴보자.



### sentence-BERT 이해하기

(파인튜닝에 샴 및 트리플렛 네트워크 아키텍처를 사용)

=> 문장 유사함을 두 개의 레이블로 분류



기본적으로 sentece-BERT 는 사전 학습된 BERT를 택해서 문장 표현을 얻도록 파인 튜닝된 모델이다.

이 모델의 특별한 점은 사전 학습된 모델을 파인 튜닝하기 위해서 **샴 및 트리플렛 네트워크 아키텍처를 사용**해서 더 빠르고 정확한 문장 표현을 얻게 된다.



##### 샴 네트워크 sentence-BERT

##### (문장 쌍 분류 태스크를 위한 sentence-BERT)

문장 쌍 태스크를 위해서 사전 학습된 BERT를 파인 튜닝하기 위해 샴 네트워크 아키텍처를 사용한다.

문장 쌍 분류 태스크는 두 문장A,B 가 있을 때 두 문장이 유사하면 1 레이블을 유사하지 않으면 0 레이블을 반납한다.



예를 들어서 다음과 같은 문장 A,B가 있다고 해보자.



A = I completed my assignment

B = I completed my homework



주어진 문장 쌍에 대해서 각각 토큰화 한다.



A  = [cls,I, completed, my, assignment,sep]

B = [cls,I, completed, my, homework, sep]



사전 학습된 BERT 모델에 A,B를 집어 넣어서 각각 토큰들에 대한 표현을 얻는다.

단, 샴 네트워크는 동일한 가중치를 공유하는 2개의 동일한 네트워크로 구성된다.

따라서 2개의 동일한 사전 학습된 BERT 모델을 사용해서 A,B 문장 각각 따로 표현을 얻는다.

그 과정을 보면 입력값이 BERT모델을 지나쳐서 표현을 얻게되고 그 표현값이 풀링(평균 풀링 혹은 최대 풀링) 을 통해서 문장의 표현을 출력한다.



A,B 두 개의 문장 표현이 나올텐데 이 두 문장 표현을 결합하고 가중치를 곱한 후 소프트맥스 분류기를 넣어서 문장 쌍 분류 태스크에 sentence-BERT를 이용할 수 있다.



u,v 가 두 문장의 표현이라고 한다면, 밑의 식으로 두 문장 표현을 결합한다.



(Wt((u,v,|u-v|)))



그리고 소프트맥스 함수와 분류기를 집어넣어서 두 문장의 유사성이 0인지 1인지 분류한다.



Softmax(Wt((u,v,|u-v|)))



이때 교차 엔트로피 손실(cross-entropy-loss) 를 최소화하도록 Wt를 업데이트해 네트워크를 학습한다.



##### (문장 쌍 회귀 태스크를 위한 sentence-BERT)

=> 문장 간 유사도 수치 측정



문장 쌍 회귀 태스크의 목표는 주어진 두 문장 사이의 의미 유사도를 예측하는 것이다.

위의 문장 쌍 분류 태스크를 위한 sentence-BERT의 과정과 유사하다

동일한 사전학습된 BERT 모델을 사용해서 두 문장에 대한 표현을 각각 얻는다.

각각 문장의 표현을 u,v 라고 할 때, 이 두 문장에 코사인 유사도와 같은 유사도 척도를 사용해 두 문장 간의 유사도를 계산한다.



이때 평균제곱손실(mse) 를 최소화하게끔 모델의 가중치를 업데이트해 주어진 네트워크를 학습한다.

이런 식으로 문장 쌍 회귀 태스크에 sentence-BERT를 사용할 수 있다.



##### 트리플렛 네트워크 sentence-BERT



이제 sentence-BERT가 샴 네트워크 아키텍처를 사용한 게 아니라 트리플렛 네트워크 아키텍처를 사용하는 법을 알아보자.



- 기준 문장 : Play the game
- 긍정 문장 : He is playing the game
- 부정 문장 : Don't play the game



태스크 : 기준 문장과 긍정 문장의 유사도는 높아야 하고, 기준 문장과 부정 문장 사이의 유사도는 낮아야 한다.

문장이 세 개이기 때문에 sentenc-BERT는 트리플렛 네트워크 아키텍처를 사용한다.



먼저 3개의 사전 학습된 BERT를 이용해서 각각의 문장에 대한 표현을 얻는다. (S_p, S_a, S_n) => 각각 긍정, 기준, 부정 문장에 대한 표현을 얻는다.

그리고 세 개의 문장 표현을 이용해서 다음과 같은 트리플렛 목적 함수를 최소화한다.

max(||s_a - s_p|| - ||s_a - s_n|| + 입실론, 0)



|| .|| 는 거리 메트릭을 나타낸다. (유클리디안 거리), 입실론은 마진을 나타낸다.

기준 문장 s_a에서 긍정 문장 표현 s_p는 기준 문장 표현 s_a에서 부정 문장 표현 s_a보다 적어도 입실론 만큼은 가깝다.



트리플렛 손실 함수를 최소화하기 위해서 (긍정, 기준, 부정) 문장의 각각의 거리를 측정하고, 손실함수에 그 값을 집어넣어서 손실 값을 출력한다. 이때 손실 함수의 값이 최소가 되게끔 네트워크를 학습한다.



지금까지 sentence-BERT 의 두 가지 네트워크 (샴 네트워크, 트리플렛 네트워크) 를 살펴봤다.

다음을 sentence-transformers 라이브러리를 탐색하자.



## sentence - transformers 라이브러리 탐색



사전 학습된 sentence-BERT 의 종류는 아래와 같다.



- bert-base-nli-cls-token : 사전 학습된 BERT-base 를 가져와 NLI 데이터 셋으로 파인 튜닝했으며 cls 토큰 표현을 문장의 표현으로 간주한다.
- bert-base-nli-mean-token : 사전 학습된 sentence-BERT로 사전 학습된 BERT-base를 가져와 NLI 데이터 셋으로 파인 튜닝 했으며, 문장 표현을 구하기 위해서 평균 풀링 전략을 사용했다.
- roberta-base-nli-max-tokens : 사전 학습된 sentence-BERT로 사전 학습된 RoBERTa-베이스를 가져와 NLI 데이터셋으로 파인 튜닝했다. 문장 표현을 구하기 위해 최대 풀링 전략을 사용
- distilbert-base-nli-token : 사전 학습된 sentence-BERT, 사전 학습된 DistilBERT - base를 가져와 NLI 데이터셋으로 파인 튜닝했으며 문장 표현을 얻기 위해서 평균 풀링 전략을 사용했다.



사전 학습된 sentence-BERT라고 하면 기본적으로 사전 학습된 BERT를 가져와 샴 또는 트리플렛 네트워크에 맞춰 파인튜닝 했음을 의미한다.



### sentence-BERT를 사용한 문장 표현 계산



```python
from sentence_transformers import SentenceTransformer

#사전 학습된 sentence-BERT 모델을 가져온다.

model = SentenceTransformer('bert-base-nli-mean-tokens')

#문장 지정

sentence = "Paris is a beautiful city"

#enocder 함수로 사전 학습된 BERT 모델로 문장의 표현을 계산한다.

sentence_representation = model.encode(sentence)

#표현된 문장의 shape을 확인한다.
print(sentence_representation.shape)
```



사전 학습된 sentence-BERT 모델을 가져오는데, 이 모델은 사전 학습된 BERT-base 모델을 NLI 데이터셋에 맞춰서 파인 튜닝한 모델이며, 이 모델에서 산출된 토큰들의 평균값을 문장의 표현 값으로 간주한다.

enocder 함수로 사전 학습된 BERT 모델로 문장의 표현을 계산한다.



### 문장 유사도 계산하기



```python
import scipy
from sentence_transformers import SentenceTransformer, util

# 모델 불러오기
model = SentenceTransformer('bert-base-nli-mean-tokens')

#문장 정의
sentence1 = 'It was a great day'
sentence2 = 'Today was awesome'

#각 문장에 대한 표현을 얻기 (모델을 두 개 사용)
sentence1_representation = model.encode(sentence1)
sentence2_representation = model.encode(sentence2)

#코사인 유사도 산출
cosin_sim = util.pytorch_cos_sim(sentence1_representation, sentence2_representation)

#출력
print(cosin_sim)
```



역시 샴 네트워크를 이용해서 모델을 각각 두 개 이용하여 두 문자의 표현을 얻는다.

두 문장의 표현은 각 모델의 풀링에 의해서 구해진다.

두 표현의 유사도를 코사인 유사도로 구하게 된다.



### 커스텀 모델 로드



sentence_transformers 라이브러리에서 사용할 수 있는 사전 학습된 sentence-BERT 모델 외에도 자체(커스템) 모델을 사용할 수 있다.

본래는 사전 학습된 BERT-base 모델을 NLI 데이터 셋에 맞춰서 파인 튜닝한 모델을 통해 토큰들의 표현을 풀링을 통해서 얻었었다. 이 과정 자체를 주어진 모델이 정해줬었다. (그 이후에 코사인 유사도를 계산해서 두 문장간의 유사도를 계산했다.)



하지만 이 주어진 모델대로 진행하지 않고 개인이 커스터마이징 할 수도 있다.



사전 학습된 ALBERT 모델이 있다고 가정하자.

사전 학습된 ALBERT 모델을 단어 임베딩 모델로 설정한다.

코드로 주어진 문장에서 모든 토큰의 표현을 반환하는 단어 임베딩 모델을 정의한다.



```python
from sentence_transformers import models, SentenceTransformer
word_embedding_model = models.Transformer('albert-base-v2')
```



문장의 각 토큰들의 표현을 구했으면 이를 이용해서 그 문장의 표현 벡터를 구할 수 있다.

문장의 시작을 알리는 cls를 사용하거나, 맥스 풀링, 평균 풀링을 사용해서 문장을 표현하는 임베딩을 얻을 수 있다.



```python
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens = True,
                               pooling_mode_cls_token = False,
                               pooling_mode_max_tokens = False)

```



(사전 학습된 ALBERT 모델로 임베딩을 얻고 이를 평균 풀링한다는 파라미터 의미.)



```python
model = SentenceTransformer(modules = [word_embedding_model, pooling_model])
model.encode('Transformers are awesome')
```



SentenceTransformer 의 모듈값에 토큰 값을 얻는 모델을 우리가 위에서 지정한 word_embedding_model(ALBERT)로 지정하고 풀링 모델도 지정한다.

그리고 문장의 표현 벡터를 얻는다.



### sentence-BERT 로 유사한 문장 찾기



```python
from sentence_transformers import SentenceTransformer, util
import numpy as np

#사전 학습된 sentence-BERT 를 다운로드

model = SentenceTransformer('bert-base-nli-mean-tokens')

#마스터 사전을 정의

master_dict = [
               'How to cancel my order?',
               'Please let me know about the cancellation policy?',
               'Do you provide refund?',
               'what is the estimated delivery date of the product?',
               'why my order is missing?',
               'how do i report the delivery of the incorrect items?'
]

#입력 질문을 정의
inp_question = 'When is my product getting delivered'

#입력 질문의 표현을 계산
inp_question_representation = model.encode(inp_question,
                                           convert_to_tensor = True)
#질문 표현의 타입 확인하기
type(inp_question_representation)

#master dict 내부의 문장들 표현하기
master_dict_representation = model.encode(master_dict, 
                                          convert_to_tensor = True)
#질문 표현과 유사도 cos_sim 로 구하기
similarity = util.pytorch_cos_sim(inp_question_representation,
                                   master_dict_representation)
#최댓값 위치 인덱스 반환
np.argmax(similarity)

#master_dict[np.argmax(similarity)] 로 최대 가까운 언어 출력
print('The most similar question in the master dictionary to given input question is : ',
      master_dict[np.argmax(similarity)])
```



사전 학습된 sentence-BERT 모델을 가져오고(NLI 데이터셋에 맞춰서 파인 튜닝된...)

그걸로 질문을 표현하고 master dict 문장들도 표현해서 cos_sim 으로 문장간 유사도를 구하고 출력한다.



## 지식 증류를 이용한 다국어 임베딩 학습



단일 언어 임베딩에서 다국어 문장에 적용하는 법을 알아보자.

앞에서 알아본 M-BERT, XLM, XLM-R 모델들은 언어 간의 벡터 공간에서 정렬되어 있지 않다.

즉, 다른 언어로 된 동일한 문장의 표현이 벡터 공간에서 다른 위치로 매핑된다.

이제 다른 언어로 된 유사한 문장을 벡터 공간의 동일한 위치에 매핑하는 법을 알아보자.



> M-BERT, XLM, XLM-R 은 동일한 의미에 관한 서로 다른 언어의 두 문장이 벡터 공간에서 다르게 표현된다.
>
> 이제 동일한 의미면서 서로 다른 언어로 표현된 두 문장이 벡터 공간의 동일한 위치에 매핑되는 법을 알아볼 것.



sentence-BERT에서 생성된 단일 언어 문장 임베딩을 지식 증류를 통해 다국어로 만들어 다양한 언어에 sentence-BERT를 적용할 수 있다.

sentence-BERT의 지식을 XLM-R 과 같은 다국어 모델에 전달, 다국어 모델이 사전 학습된 sentence-BERT와 동일한 임베딩을 형성하도록 한다.



XLM-R 은 100개의 다른 언어에 대한 임베딩을 생성.

사전 학습된 XLM-R을 이용해 sentence-BERT의 다양한 언어에 대한 문장 임베딩을 형성하도록 XLM-R 모델을 가르친다.

sentence-BERT 를 교사로, 사전 학습된 XLM-R을 학생 모델로 사용.

지식 증류를 시키는 과정을 살펴보도록 하자.



영어로된 소스 문장과 한국어로 된 타깃 문장이 있다고 가정해보자.



"How are you, 지금 어떠니?"



영어로된 소스 문장을 sentence-BERT(교사) 모델에 입력해서 소스 문장의 표현 값을 얻는다.

동시에 영어로된 소스 문장을 XLM(학생) 모델에 입력해서 소스 문장의 표현 값을 얻는다.

당연히 sentence-BERT(교사) 모델과 XLM(학생) 모델에서 출력한 임베딩 값을 다르다.

학생이 생성한 소스 문장에 대현 표현과 교사가 만든 소스 문장에 대한 평균 제곱 오차(MSE) 를 최소화하도록 학생 네트워크를 학습시킨다.



또한 교사가 반환한 소스 문장 표현과 학생이 반환한 타깃 문장(한국어) 표현 간의 MSE를 계산한다.

타깃 한국어가 원본 영어 문장과 동일하기 떄문이다(의미)

교사의 소스 문장 표현과 학생의 타깃 언어 표현의 평균 제곱 오차(MSE) 값이 최소가 되게끔 학생 네트워크를 학습시킨다.

학습을 하면 할수록 학생 네트워크는 교사 네트워크와 동일한 임베딩을 생성하도록 학습한다.



### 교사 - 학생 아키텍처



위에서 예시를 든 것도 교사 - 학생 아키텍처와 같다.

[(s_1, t_1), (s_2, t_2), ... , (s_i, t_i), ...., (s_n, t_n)] 를 병렬 번역된 소스-타깃 문장 쌍이라고 가정하자.



s_t는 소스 언어로 된 원 문장, t_i는 타깃 언어로 번역된 문장이다.

예를 들어서 (s_i, t_i) 는 영어와 프랑스어가 될 수 있고, 영어와 독일어가 될 수 있다.



소스 문장에 대해서 교사 모델과 학생 모델이 표현 값을 얻게 된다.

타깃 문장에 대해서 학생 모델이 표현 값을 얻게 된다.

교사가 만든 소스 문장에 대한 표현 값과 학생이 만든 소스 문장에 대한 표현 값의 MSE 를 구하고 이 값이 최소가 되게끔 학생 네트워크를 학습시킨다.

또한 교사가 만든 소스 문장에 대한 표현 값과 학생이 만든 타깃 문장에 대한 표현 값의 MSE가 최소가 되게끔 학생 네트워크를 학습시킨다.



그 값에 1/B 를 해주는데 B는 배치 크기를 의미한다. 수학 식은 (294pg 에 있다.)

이런식으로 교사 네트워크와 동일한 임베딩을 형성하도록 학생 네트워크를 학습시킬 수 있다.

사전 학습된 어떤 모델이든 교사와 학생으로 이용할 수 있다.



### 다국어 모델 사용



앞에서는 지식 증류를 통해 단일 언어 모델을 다국어로 만드는 법.

지금부터는 사전 학습된 다국어 모델을 사용하는 법!

sentence-transformers 라이브러리를 통해 공개적으로 사용할 수 있도록 했다. 



사전 학습된 다국어 모델들



- distiluse-base-multilingual-cased : 아랍어, 중국어, 네덜란드어, 영어, 프랑스어, 독일어, 이탈리아어, 한국어, 폴란드어, 포르투칼어, 러시아어, 스페인어 및 터키어 지원
- xlm-r-base-en-ko-nli-ststb : 한국어와 영어를 지원한다.
- xlm-r-large-en-ko-nli-ststb : 한국어와 영어를 지원한다.



```python
from sentence_transformers import SentenceTransformer, util
import scipy

eng_sentence = 'thank you very much'
fr_sentence = 'merwci beaucoup'

eng_sentence_embedding = model.encode(eng_sentence)
fr_sentence_embedding = model.encode(fr_sentence)

similarity = util.pytorch_cos_sim(eng_sentence_embedding,
                                  fr_sentence_embedding)

print('The similarity score is : ', similarity)
```





## domain-BERT



이전에 위키피디아 말뭉치를 사용해 BERT를 사전 학습시키는 법과 이를 파인 튜닝해 다운스트림 태스크에 사용하는 법을 배웠다.

일반 위키피디아 말뭉치에서 사전 학습된 BERT를 사용하는 대신에, 특정 도메인 말뭉치에서 BERT를 처음부터 학습할 수 있다.

이런 작업을 거치면 일반 위키피디아에 없을 도메인들의 어휘를 학습시키는 데 도움이 된다.

domain-BERT의 두 가지 모델을 살펴보자.



domain-BERT 종류

- ClinicalBERT
- BioBERT



위의 모델들로 사전 학습 시키는 법과 다운스트림 태스크에서 파인 튜닝하는 법을 알아보자.



###  ClinicalBERT



ClinicalBERT 는 **대규모 임상 말뭉치에서 사전 학습된 임상 domain-BERT 모델**이다.

임상 노트나 진행 노트는 환자에 대한 매우 유용한 정보를 포함하는데, 전문 용어와 관련되어 난도가 높다. 따라서 임상 텍스트의 콘텍스트 표현을 이해하기 위해 많은 임상 문서로 ClinicalBERT를 사전 학습한다.



사전 학습이 끝난 ClinicalBERT는 재입원 에측, 체류 기간, 사망 위험 추정, 진단 예측 등과 같은 다양한 다운스트림 태스크에 사용된다.



##### ClinicalBERT 사전 학습



ClinicalBERT는 MIMIC-III 임상 노트를 사용해 사전 학습된다. (베스 이스라엘 디코니스 메이컬 센터에서 제공하는 데아터) => 4만명 이상의 환자를 관찰한 건강 관련 데이터셋을 포함.

ClinicalBERT 는 기본 BERT가 사전 학습했던 것처럼 MLM과 NSP 태스크를 이용해 사전 학습된다.

!!!(결국 데이터셋만 달라졌지 기본 BERT가 사전 학습했던 과정과 같다.)



##### ClinicalBERT 파인 튜닝



재입원 예측, 입원 기간, 사망 위험 추정, 진단 예측 등 다양한 다운스트림 태스크에 맞춰서 ClinicalBERT 를 파인 튜닝할 수 있다.



재입원 예측 태스크를 한다고 가정.

향후 30일 이내에 환자가 다시 재입원할 확률을 예측하는 것.

사전 학습된 ClinicalBERT 에 임상 메모를 입력하고 임상 메모의 표현을 반환한다.(R_cls)

R_cls 의 값을 분류기(피드포웓 + 시그모이드) 에 입력하고 분류기는 환자가 30일이내에 다시 입원할 확률을 반환한다.



여기서 한 가지 issue 에 대해서 생각해볼 수 있다.

BERT에서는 최대 토큰의 길이가 512이다.

근데 환자의 임상 기록이 512보다 더 많은 토큰으로 구성되어 있으면 어떻게 해야하나?

이 경우 임상 노트를 여러 시퀀스로 분할할 수 있다.

각 서브시퀀스를 모델에 입력한 후 모든 서브시퀀스를 개별적으로 예측한다.

그런 다음 마지막에 다음 식으로 점수를 계산한다.



P(readmit = 1 | h_patient) = (P^n_max + P^n_mean * n / c ) / 1 + n / c



- n은 서브 시퀀스의 수
- P^n_max 는 모든 서브시퀀스에서 재입원 확률의 최댓값
- P^n_mean은 모든 서브시퀀스에서 재입원 확률의 평균값
- c는 스케일링 팩터



이제 위의 식을 단계별로 이해해보자.



여러 서브 시퀀스가 있을 것이다. 근데 모든 서브 시퀀스가 예측에 중요한 정보를 가지고 있지는 않다. 

따라서 모든 서브시퀀스에서 확률이 가장 높은 것만 사용하면 된다.

따라서 식은 다음과 같다.



P(readmit = 1 | h_patient) = P_max



그런데 서브 시퀀스에 노이즈가 포함도어 있고 노이즈로 인해서 최대 예측 확률을 얻었다고 가정해보자. 이런 경우는 최종 예측으로 최대 확률을 선택하는 것은 잘못된 선택이다. 따라서 이를 방지하기 위해 평균 확률도 포함한다.



P(readmit = 1 | h_patient) = P_max + P_mean



환자가 임상 기록이 많거나 임상 기록이 더 길수록 서브시퀀스의 수(n) 가 많아진다.

이 경우에는 노이즈가 많기 때문에 P_max를 얻을 가능성이 높아진다. 따라서 P_mean에 더 많은 중요성을 부여해야 한다. 따라서 P^n_mean의 중요성을 더 주기 위해서 스케일링 벡터 C를 이용해 n/c를 곱한다.



P(readmit = 1 | h_patient) = P^n_max + P^n_mean * n / c



다음으로 최종 점수를 정규화하기 위해서 1 + n/c로 나누면 최종 식을 얻을 수 있다.



P(readmit = 1 | h_patient) = (P^n_max + P^n_mean * n ) /  (c / (1+n/c))



이 식은 환자의 재입원 확률을 산출한다.



정리하면 사전 학습된 ClinicalBERT 에 임상 메모를 넣어서 문장에 대한 표현 값을 얻고 이 값을 피드포워드 + 시그모이드로 이루어져있는 분류기에 집어 넣어서 재입원 확률값을 도출한다.

근데 임상 메모가 길게 되면 BERT의 512 토큰 개수를 초과할 수 있다. 이를 해결하기 위해서 여러 개의 서브 시퀀스로 나눌 수 있다.

각각의 서브 시퀀스마다 표현 값을 얻어서 분류기에 집어 넣어 재입원 확률을 산출한다.

이때 확률의 최댓값만 사용하려고 했으나, 노이즈가 있을 수 있으므로 재입원의 평균 확률을 더한다. 

하지만 데이터가 길면 길수록 MAX 가 나올 확률이 많아지기 때문에 재입원 평균 확률에 중요도를 더 부여해야 한다. 따라서 스케일링 팩터 C를 이용해서 n/c를 곱한다.



##### 임상 단어 유사도 추출



ClinicalBERT 에서 토큰간 유사한 것끼리 묶어보면 잘 묶임을 알 수 있다.



### BioBERT



BioBERT 는 대규모 생물 의학 코퍼스에서 사전 학습된 생물 의학 domain-BERT다.

사전 학습 후 생물 의학 질문-응답, 생물 의학 개체명 인식 등과 같은 많은 생물 의학 분야별 다운스트림 태스크에 맞춰 파인 튜닝 가능하다.



(생물 의학 텍스트에 특화되어 있음)



- PubMeb : 인용 데이터베이스, 생명 과학 저널, 온라인 서적 및 MEDLINE, 미국 국립 의학 도서관
- PubMed Central :  생의학 및 생명 과학 저널에 기재된 기사를 포함한 무료 온라인 저장소



1. 먼저 영어 위키피디아 및 토론토 책 말뭉치 데이터셋으로 구성된 일반 도메인 말뭉치를 사용해 사전 학습된 일반 BERT로 BioBERT의 가중치를 초기화.

2. 생체 의학 도메인 말뭉치를 사용해서 BioBERT를 사전 학습한다.(BioBERT는 일반 사전 학습된 BERT로 가중치 초기화됨)
3. 토큰화를 위해서 워드피스 토크나이저 사용





##### BioBERT 모델 파인 튜닝



개체명 인식 태스크를 위한 BioBERT 로 파인 튜닝할 수 있다.





## 마치며



sentence-BERT : 문장의 표현을 얻음.

문장의 표현을 얻기 위해서 파인 튜닝된 BERT



사전 학습된 BERT를 파인 튜닝하기 위해서 샴 및 트리플렛 네트워크 아키텍처를 사용해 파인 튜닝을 더 빠르게 하고 정확한 문장 임베딩을 얻음



지식 증류를 이용해 단일 언어 임베딩을 다국어로 만드는 법을 알아봤다.

교사가 학생에게 지식 가르쳐줌.

그리고 사전 학습된 다국어 모델을 사용하는 법 배움.



그 다음으로 domain-BERT를 배움. 의학과 생물과 관련된 DOMAIN 필요시 책을 찾아보면 될 듯.





















