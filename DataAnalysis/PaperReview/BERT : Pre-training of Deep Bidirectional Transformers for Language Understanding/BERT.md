

# BERT : Pre-training of Deep Bidirectional Transformers for Language Understanding

## Abstract

BERT : **B**idirectional **E**ncoder **R**epresentation **T**ransformer

문장의 양방향 context 를 고려한 사전학습 모델로, Transformer 의 encoder 를 활용한 모델.

사전 학습 모델은 파인 튜닝될 수 있고 다양한 다운스트림 태스크에서 높은 성능으로 활용될 수 있다.

사용되는 다운스트림 태스크(Downstream task)

- 질의 응답 문제
- 자연어 추론 문제(NLI)
- 태깅 문제

> 다운스트림 태스크란?
>
> 사전 학습(pre-train) 모델을 이용해서 구체적으로 풀고 싶은 문제들을 의미한다.
>
> 사전 학습된 모델을 이용해서 원하고자 하는 태스크를 파인 튜닝(fine tuning) 방식을 통해 모델을 업데이트 하는 방식을 사용하는데 이때 태스크를 다운스트림 태스크 라고 부른다.

## Introduction

BERT 모델은 문장 단위의 작업도 포함한다. 물론 문장 단위의 작업을 진행하면서 토큰 단위의 작업도 진행한다.

문장 단위의 작업들은 예를 들어서 자연어 추론(nli), 의역, 요약 등등이 있다.

토큰 단위의 작업들은 예를 들어서 개체명 붙이기, 질의 응답 등등이 있다.

사전 학습 언어 모델을 다운 스트림 태스크에 적용하는 두 가지 전략이 있다.

"feature based", "fine tunning" 방법.

- "feature based "
  - 특징 기반 방법
  - 사전 학습된 특징을 하위 문제의 모델에 부가적인 특징으로 활용하는 방법.
  - "특징 기반 방법" 의 "특징" 이란 모델 중간에 나오는 특징값.
  - Elmo, word2vec.
- "fine tunning"
  - 미세 조정 방법
  - 사전 학습된 모델의 가중치를 그대로 사용하면서 최소한의 하위 태스크 특화적인 매개변수(가중치) 들을 추가해서 하위 태스크에 맞게 추가로 학습(미세조정) 하는 것.
  - 특정 목적 함수에 맞게 사전 학습된 모델의 가중치를 하위 태스크 작업을 할 때 그대로 사용하면서 하위 태스크를 위한 최소한의 가중치를 추가해서 추가 학습하는 방법.
  - GPT version 들이나, Transformer

### 연구진들의 문제 의식

지금까지의 언어 모델들은 모두 단방향 모델들이다.

GPT 같은 경우에도 단방향인데 (left - to - right) 학습을 할 때, 트랜스포머의 셀프 어텐션 layer 에서 이전의 토큰들만 참고할 수 있다.

단방향적인 모델들은 문장 단위의 작업들을 수행하는데 있어서 최적합적이지 않고,

단방향적 모델을 기반으로 사전 학습된 모델들을 토큰 단위의 하위 태스크에 적용하면 성능이 좋지 않을 수 있다. (질의 응답 태스크 같은)

그래서 연구진들이 내놓은 모델이 BERT : **B**idirectional **E**ncoder **R**epresentation **T**ransformer.

GPT 모델 같은 경우도 tramsformer 를 사용했었는데 bert 도 마찬가지로 transformer 를 사용한다.

추가적으로 bert는 단방향성을 포기하고 양방향성을 선택한다.

그래서 bidirectional 한 encoder representation transformer 인 것.

그럼 양방향성을 어떤 방식으로 연구진들이 만들었는지 알아보자.

그들은 새로운 목적 함수를 고안하는데, 바로 MLM(Masked language model) 목적함수다.

입력 시퀀스가 존재할 때 입력 시퀀스의 토큰을 랜덤하게 일정 비율로 masking 한다.

mlm의 최종 목적은 masking 된 토큰들의 본래 word context 기반으로 예측하는 것이다.

이때 word context 는 양방향의 토큰들을 사용하게 된다.

연구진들은 MLM 뿐만 아니라 다음 문장 예측 NSP(Next sentence prediction) 을 사용한다.

이 논문의 contribution 은 다음과 같다.

- 언어 표현을 위해서 양방향성 사전 학습(pre-train) 의 중요성을 설명한다.
  - 주의할점은 독립적으로 left-to-right 를 학습한 것과 right - to - left 를 학습한 것과는 결이 다르다.
- 특정 태스크들에 맞게 무겁게 설계되어진 아키텍처들을 능가한다.
  - 문장 단위, 토큰 단위의 큰 태스크들에서 bert 모델은 다른 모델들을 압도한다.
- bert 는 11개의 NLP 태스크들을 발전시킨다. (사전 학습된 모델들을 구글은 제공한다!!)

## Related Work

사전 학습 languager model 의 고된 역사가 존재....

이를 논문은 짧게 리뷰하고 있다.

#### 비지도 특징 기반 접근 (Unsupervised feature based approach)

비지도 특징 기반 접근은 어떤 모델에서 학습한 특징을 하위 태스크 작업에서 부가적으로 사용하는 것을 의미한다.

대표적인 비지도 특징 기반 접근은 단어 임베딩을 얻기 위해서 학습한 word2vec 모델이라고 할 수 있다.

nlp 작업 역사적으로 단어의 임베딩 표현 값을 얻기 위한 노력을 수십년간 지속되어왔다.

제일 먼저 단어의 표현을 얻기 위해서 "left-to-right" 모델이 사용됐다.

이 작업은 단어(토큰) 단위에서 끝나지 않고 문장 단위로 발전하게 되는데,

토큰에 대한 표현 벡터를 얻는 거 뿐만 아니라 문장에 대한 표현 벡터를 얻기 위한 연구가 진행됐다.

그래서 다음 단어들이 될만한 문장 후보들을 랭크 시키기 위한 목적 함수를 사용해왔다.

이떄도 마찬가지로 left-to-right 방향의 학습을 진행했다.

(이전 문장 표현이 담겨진 다음 문장들의 단어들)

그리고 보완되서 나온게 left-to-right + right-to-left 모델이다.(ELMO 탄생.)

문맥에 민감한 단어의 벡터 표현을 만든다.

이런 ELMo 는 질의 응답 태스크, 개체명 인지 태스크, 감성 분석 등등을 발전시킨다.\

후에 Melamud et al.가 single 단어에 대해서 LSTM 을 사용해서 양쪽 context 를 활용해 예측하자고 주장한다. 이는 ELMo 방식과 닮았다.

하지만 논문의 저자들은 이는 근본적으로 deep biodirectional 하지 못하다고 말한다.

(빈칸채우기 task 가 nlp 발전을 이룰것,)

#### 비지도 미세 조정(Unsupervised fine-tuning)

마찬가지로 위에서 설명했지만, 미세 조정(파인 튜닝) 은 이전에 사전 학습했던 모델의 가중치들을 그대로 다운 스트림 태스크에 사용하면서, 다운스트림 태스크에 최소한으로 필요한 가중치만 추가해서 다운 스트림 태스크에 맞춰 학습(미세 조정) 하는 방법을 말한다.

파인 튜닝의 장점은 처음부터 배움이 필요한 매개변수들이 많이 필요없다는 점이다.

이로 인해서 bert 이전의 gpt 모델은 높은 성능을 자랑했다.

## BERT

버트와 그것의 상세한 구현에 대해서 살펴볼 것.

버트의 구현은 크게 두 개로 나뉜다.

1. Pre-training
   - 특정 pretrain-task 가 주어짐.
   - unlabeld data 를 사용
2. Fine-tuning
   - Labeled data 를 사용
   - Pre-train 에서 만들어졌던 매개변수(가중치) 를 그대로 사용.
   - 그 파라미터들은 모드 특정 다운스트림 태스크 안에서 파인 튜닝됨.

버트가 다른 모델들과 구분되는 특징 중 하나는, 다양한 다운스트림 태스크에 걸쳐서 하나로된 아키텍처를 사용하는 성향을 가지는 것.

즉, 다양한 다운스트림 태스크안에서 사용되는 버트들은 서로 큰 차이가 없다는 점.

왜냐하면, 각 다운스트림 태스크마다 최소한의 가중치만을 추가했기 때문이다.

##### model architecture

BERT는 양방향적인 트랜스포머 인코더의 멀티 layer 이다.

이때 말하는 트랜스포머는 Attention is al you need 의 저자인 Vaswani et al. (2017) 의 오리지널 트랜스포머 모델을 의미한다.

따라서 bert 모델의 종류는 인코더 개수와 은닉 상태의 크기에 따라서 결정된다.

bert 모델의 구조를 이해하기 위해서 연구진들은 기호에 관한 약속을 정한다.

L은 layer 의 개수

H는 hidden state 의 크기

A는 self-attention 의 head의 개수를 의미한다. (멀티 헤드 어텐션을 기억해보라)

L,H,A 에 따른 bert 의 대표 모델 두 개를 살펴보겠다.

- BERT base :
  - L : 12
  - H : 768
  - A : 12
- BERT large
  - L : 24
  - H : 1024
  - A : 16

이 두 개의 모델의 구조를 잘 기억해두는 게 좋다.

왜냐하면 다양한 다운스트림 태스크에서 base 모델이나 large 모델을 다운 받아서 사용하기 때문이다.

Bert base 같은 경우는 gpt 와의 비교를 위해서 gpt 와 크기를 같게 만들었다.

하지만 gpt 는 한정되게 왼쪽의 context 만 사용한 self-attention 을 사용했고 bert 는 양방향성 context 를 고려한 self-attention 을 사용했다. (이걸 계속 강조한다. gpt 와 경쟁을 하는건가?)

##### Input/output Representation

Bert 모델의 input 은 single sentence, dual sentence 모두 하나의 token sequence로 representation 가능하다. (question, answer 데이터)

bert의 작업을 통해서, sentence 는 실제 언어적인 의미이기 보다는, 임의의 인접한 text의 범위이다.

여기서 sequence 는 bert 에 대한 input token sequence 를 의미한다. 그리고 이 sequence는 single 일 수도 있고 pair sentence 일수도 있다.(packed together)

Bert 는 input 시퀀스에 대한 전처리 작업을 진행한다.

bert 는 WordPiece embeddings(30,000 vocabulary) 로 시퀀스를 토큰화 한다.

시퀀스를 토큰화 할 때 일반적인 규칙이 존재하는데, 시퀀스의 첫 토큰은 항상 "cls" 토큰이다.

cls 토큰은 시퀀스의 시작을 알리는 토큰으로, 문장의 정보를 담고 있는 토큰으로 활용되기도 한다. (sentence classification 에서)

sentence 가 두 개일때도 위와 같은 과정을 똑같이 거치는데, 차이점은 두 개의 문장을 packed 한 이후에 토큰화 작업을 시작한다는 점.

여전히 cls 토큰을 첫 문장의 시작에 붙여주는건 똑같다.

두 문장을 구별할 때 사용하는 special token 은 sep 토큰이다. sentence 가 끝날 때마다 sep 토큰을 추가해준다.

그리고 각 토큰들이 a sentence 문장 내의 토큰인지 b sentence 문장 내의 토큰인지 구별하는 embedding 을 추가해준다.

bert에서는 임베딩을 E로, cls 토큰의 최종 representation 을 C 그리고 i번째 토큰의 최종 representation 을 T_i로 정했다.

최종적인 input 토큰들의 값은 positioning token + segment token, token 값을 더한 값이다.

##### Pre-traininmg BERT

역시 앞에서 설명한 것과 같이 gpt 와 다르게 단반향으로 학습하는 게 아니라 양방향으로 학습한다.

두 가지의 사전 학습 목적 함수가 있는데, 이 두 가지를 통해서 양방향 학습이 가능해진다.

1. Masked Language Model(MLM)

   - 우리는 직관적이게 양방향성의 context 를 고려한 학습이 한쪽(left-to-right or right-to-left) 로 학습한 것보다 더 성능이 좋을 것이라 생각한다.

   - 하지만 양방향성의 context 고려는 단어에 대해서 간접적이게 스스로를 보게 하고(see itself), 따라서 word에 대한 예측 성능이 떨어질 수 있다.

   - 이런 issue 에 직면해서 등장한 deep bidirectional train 방식이 mlm 이다.

   - 랜덤하게 일정 비율로 시퀀스 내의 토큰들을 masking 한다.

   - mlm 의 기본적인 원리는 다음과 같다.

     - 랜덤하게 일정 비율로 시퀀스 내의 토큰들을 masking 한다.
     - 그리고 우리는 masking 된 토큰이 본래 어떤 단어였는지 예측한다.

   - mlm 의 과정은 다음과 같다.(내일 구글 BERT의 정석을 통해서)

   - mlm 작업은 필수적으로 으로 pre-train 과 fine-tunning 사이에 mismatch 가 발생하게 된다.🥲 왜냐하면, fine-tuning 에서는 mask 토큰이 존재하지 않기 때문에.

     즉 mask 토큰을 예측하면서 사전 학습된 bert 모델은 다른 다운 스트림 태스크에 적용할 때, 다운 스트림 태스크의 토큰들은 mask 가 존재하지 않기 때문에 서로 mismatch 가 발생하게 된다.

   - 이런 점을 완화하기 위해서 무작정 지정한 비율대로 token들을 maksing 하지 않는다. 대신에 (80 - 10 -10) rule 을 적용한다

     지정한 비율로 선택된 토큰들 중에서 80%는 본래의 목적대로 masking 을 하고, 10%는 다른 단어로 대체하고 10%는 본래의 토큰으로 남긴다.

     만일 i th 번째 토큰이 masking 대상으로 선정됐다면 위의 80- 10- 10 rule 을 거치게 되고 본래의 token 값과 t_i 에 대한 예측값의 손실(cross entropy loss)을 구해서 모델에 대한 학습을 진행한다. (appendix 참고)

2. Next Sentence Prediction

   - 질의 응답, 자연어 추론과 같은 많은 다운 스트림 태스크들은 두 문장들간의 관계에 대한 이해에 바탕을 두고 있다.
   - 두 문장의 관계에 대한 이해를 학습하기 위해서 우리는 next sentence prediction task 를 시행한다. (단일 언어 corpus 로부터)
   - 두 문장 A.B를 선택할 때, 50%의 B는 실제 A문장 뒤에 나오는 문장으로 선택하고 나머지 50%는 corpus로부터 랜덤하게 가져온다. 실제 A문장 뒤에 나오는 문장의 label 은 (isNext) 이고 그렇지 않은 문장의 label 은 (notNext)
   - 이때 문장의 cls 토큰의 벡터 표현인 C가 next sentence prediction 에 사용된다.



### Fine tuning BERT



파인 튜닝은 간단하다.

transformer 의 self attention 메카니즘이 sentence 가 single sentence 든 pair sentence든 상관없이 다운 스트림 태스크에서 bert 가 모델을 만들 수 있게 해준다.

본래, text pair 를 사용하기 전에, text pair 에 대해서 인코딩하고 bidrectional cross attention 를 해주어 양방향성 맥락을 넣어준다. 근데 bert 모델은 self attention 을 통해서 이 두 가지의 단계를 통합한다.



각각의 다운 스트림 태스크에 대해서 우리는 태스크 특화적인 input과 output 을 넣어준다.

Input : 

input 데이터를 살펴보면, 사전 훈련된 중의 문장 a와 b는 paragrahing 에서의 문장 쌍, 수반 문제에서의 가설과 전제의 문장 쌍, 질의 응답 문제에서의 question 과 passage 문장쌍 과 유사하다.



output:

token representation 들은 token level task 들 예를 들어서 시퀀스 태킹과 질의 응답과 같은 것들을 위해서 output layer 에 들어가게 된다.

그리고 cls 표현 C는 classification 문제, 예를 들어서 수반과 감성분석 문제를 위해서 output layer 에 들어가게 된다.

파인 튜닝은 사전 훈려에 비해서 비용이 저렴하다. (시간 등등)

왜냐하면 사전 훈련은 모델의 임의의 초깃값부터 업데이트 하는 반면에 파인 튜닝은 사전 학습된 매개변수들에 최소한의 필요한 가중치만 추가해서 학습하기 때문이다.



## Experiment



각종 다운 스트림 태스크들을 살펴볼 예정.





### The General Language Understanding Evaluation (GLUE)



GLUE 는 다양한 자연어 이해 태스크들의 collection 이다.

앞서 시퀀스 내의 token 들을 토큰 임베딩, 세그먼트 임베딩, 포지션 임베딩에 넣어서 얻게된 벡터 표현들을 이용한다.

그때 시퀀스의 맨 처음 special token 이었던 cls 토큰 즉, C 토큰을 이용해서 classification 문제를 해결한다.

이때 C토큰의 shape H이다.

사전 학습된 bert 모델을 이용하는데, 파인 튜닝할 때 사전 학습에 사용됐던 매개변수를 그대로 사용하되 추가적으로 classification layer weight인 W를 추가해서 학습하게 된다. 이때 W의 차원 shape 은 K x H 가 된다.

참고로 K는 label 의 개수를 의미한다.

우리는 학습을 위해서 손실 함수를 계산해야 하는데, 전통적인 분류 문제의 손실 함수를 구하는 방법을 사용한다.

C x W(transpose) 를 하고, softmax 함수와 log 함수를 취한다.

C x W를 하게 되면 (1 * H) x ( H * k) 가 되고, 결국 1 * k가 되는데, 이는 label 의 logit [a,b,c,...k] 가 나온 것과 같다. 여기에 softmax 와 log 함수를 취해줘서 각 label들이 나올 확률을 구하는 것.

 

bert 모델에  따른 task 들 성능이 표로 정리되어 있다.

표에서 주목해야할 점은 OpenAI GPT 와는 모델 구조가 똑같은데 성능이 더 좋다는 점이다. 그 이유는 양방향성 맥락을 참조할 수 있게끔 bert 모델은 사전 학습을 할 때 MLM 목적함수를 사용했기 때문이다.

또한 Bert base 와 Bert large 둘 다 모두 다른 모델들의 성능을 능가했다.

그리고 large 모델이 base 모델보다 성능이 좋았다.

#### 

### SQuAD v1.1(The Stanford Question Answering Dataset)



question 과 answer text 의 pair 로 이루어진 데이터 셋이다.

question 과 question 에 대한 정답이 포함되어 있는 passage 가 존재한다.

태스크의 목적은 passage 안에서 question 에 대한 정답의 범위 혹은 span 을 찾는 것이다.



모델에 input으로 집어 넣을 때, pair 를 하나의 시퀀스로 합쳐서 넣는다.

question a는 A임베딩을 적용하고 passage 는 B임베딩을 적용한다.



우리는 파인 튜닝 하는 동안에 오직 start vector S(H) 와 end vector(H) 만 사용한다.

이때 단어 i가 정답의 시작 단어가 될 확률은 T_i 와 S의 dot product 를 한 후에 softmax 함수에 집어넣어서 구한다.

즉, sequence 내의 모든 토큰들과 시작 단어 s와의 내적후 softmax 함수에 넣게된다.

그 후에 시작이 될 확률이 가장 높은 단어를 선정하기 위해서 softmax 한 값들 중에서 가장 큰 값을 단어의 시작 단어로 선정한다.

시작 단어 뿐만 아니라 끝 단어 선정도 이와 마찬가지다.



이때 position i 부터 position j까지  정답의 span 을 정할 때, (j >= i)

S ·Ti + E ·Tj 의 예측 값이 가장 큰 값을 prediction 으로 선정한다.

결국 학습할 때 목적 함수는 올바른 시작 단어와 끝 단어의 가능성의 합이다.



정리하면, 먼저 질문과 질문에 대한 정답이 포함된 passage를 pair 쌍으로 해서 embedding 작업을 거치게 된다.

이로써 passage pair 내의 토큰들의 벡터 값(임베딩)을 얻게 된다.

passage 시퀀스 내의 토큰들 중에 질문의 정답이 될 시작 단어와 끝 단어 인덱스를 구해야 한다.

이때 시작 벡터 s와 끝 벡터 e를 사용한다.

passage 시퀀스 내의 토큰들과 시작 벡터 s와의 내적을 하게 되고 소프트 맥스 함수를 취해서 시작 벡터가 될 확률이 가장 높은 토큰을 선정한다. end토큰도 마찬가지다.

시작 단어 인덱스와 끝단어 인덱스를 도출했으면 이 인덱스들을 이용해서 답을 포함하는 텍스트 범위를 선택한다.



(질문-응답을 위한 사전 학습된 bert 파인 튜닝 그림 찾기)



### SQuAD v2.0



SQuAD v1.1 버전을 확장한 것.

2.0 버전에서는 질의 응답 문제를 더 real 하게 만든다.

1.1 버전에서는 질문에 대한 정답이 paragraph 내에 속해 있었다. 하지만 현실에서는 그렇지 않을 가능성이 크다. 따라서 paragraph 에 정답이 없는데 정답을 예측하는 문제를 2.0 버전에서는 다룬다.



2.0에서는 정답이 없는 question 을 cls 토큰이 시작과 끝의 span 정답을 가진 것으로 다룬다.

시작 및 끝 위치의 확률 공간은 cls 토큰을 포함하도록 확장된다.

우리는 답이 없는 스팬의 점수 : s_null = S * C + E * C

를 null 이 아닌 span (non null answer) 의 최고 점수 sˆ = max S·T + E·T   와 비교한다.

우리는 non null answer 가 s_null 보다 높을 때 정답이 있는 거라고 확정하고 non null answer 을 예측한다.





### SWAG(The Situations With Adversarial Generations)

113k 의 sentence pair 는 근거가 있는 상식 추론을 평가하는 문장 쌍 완성 예제다.

주어진 문장에서 가장 그럴 듯한 문장을 네 개의 선택지들 중에서 선택하는 게 이 데이터 셋을 이용한 task 다.



swag 데이터 셋에 우리가 파인 튜닝할 때, 우리는 input 값으로 네 개의 sequence 를 집어 넣는다.

이 각각의 input 들은 주어진 문장 A와 가능한 연속 문장 B를 concatenation 한 값이다.



파인 튜닝 중에 추가된 매개변수는 어떤 벡터인데, 문장의 cls벡터인 c벡터와 곱하는 벡터이다.

c벡터는 올바른 추론 문장인지 판단하기 위해서 각각 softmax 와 정규화를 거치게 되고 파인 튜닝의 추가 파라미터와 곱해지게 된다.



## Ablation Studies



bert 의 여러 측면에 대한 절제 실험을 진행한다.



### Effect of Pre- training Tasks



사전 학습에서 사용된 목적 함수들의 종류에 따른 평가를 진행.



##### No NSP

앞서 bert 의 사전학습은 두 개의 목적 함수에 따라 진행됨을 살펴봤다.

바로 mlm 과 nsp 이다.

nsp 목적함수를 제거하고 오직 mlm만으로 사전 학습을 진행한 목적 함수를 No NSP 라고 부른다.



##### LTR & No NSP



left context only model 

지금까지 양방향성 context 를 활용한 걸 살펴봤는데

(mlm을 활용해서), gpt 에서 사용하던 것처럼  left-to-right 로 학습하는 것.

이건 mlm학습을 할 시, 사전 학습과 파인 튜닝의 mismatch 를 해소한다.

추가적으로 nsp 과정도 거치지 않는다.



이건 OPEN AI GPT 와 비슷한데, 더 큰 training dataset 과 input representation 그리고 우리의 파인 튜닝 스케마가 다르다.

 

우리는 nsp 함수를 제거해서 사전 학습 했을 시 성능을 비교해볼텐데,

nsp 를 제거하면 QNLI, MNLI with SQuAD data 태스크에서 낮은 성능을 가졌다.

그 다음 우리는 양방향성을 제거해서 사전 학습하게 되면 어떤 성능을 보일지 살펴볼텐데,

mlm보다 ltr 을 수행했던 사전 학습된 모델들이 성능이 더 낮게 나왔다.

그래서 biLSTM 을 집어 넣어서 양방향성 context 를 추가하려고 했지만 여전히 사전 학습시에 bidirectiomal model 을 사용한게 성능이 더 좋았다.



그래서 우리는 ELmo 처럼 LTR + RTL 을 합치려고 했는데 비용이 두 배로 사용될 뿐만 아니라, 질의 응답 태스크에서 직관적이지 않다. 왜냐하면 RTL 이 도무지 질문에 대한 정답의 상태가 될 수 없기 때문이다.



### Effet of Model Size



위에서는 사전 학습에 사용되는 목적 함수에 따른 모델의 성능을 살펴봤는데, 

모델 사이즈에 따른 모델의 성능은 어떻게 될까?

즉, 파인 튜닝 작업을 할 때 정확도가 모델의 크기에 따라서 어떻게 달라질까?



layer 의 개수 은닉 상태의 차원의 수, attention head 의 개수별 차이를 살펴볼 예정

(우리가 지금까지 사용했던 model 사이즈와 그것과 다르게 설정한 model 사이즈별 성능 차이를 살펴볼 예정)



실험 결과 더 큰 model 일수록 정확도가 높았다.

그리고 기존의 bert 모델이 현재까지 나온 transformer 들 중에서 가장 높은 성능을 자랑했는데

현재까지 나온 거대한 사이즈의 transformer 들보다  BERT-base 모델이 더 높은 성능을 자랑했다.



- Vaswani et al. (2017) : (L = 6, H = 1024, A = 16) with 100M

- (Al-Rfou et al., 2018) : (L = 64, H = 512, A = 2) with 235M



- BERT base :
  - L : 12
  - H : 768
  - A : 12
- BERT large
  - L : 24
  - H : 1024
  - A : 16





지금까지 모델 사이즈의 크기를 증가시키면 large scale tasks들에서 성능 향상을 보였다고 알려져 있는데,

bert는 모델 사이즈 크기를 증가시키면 small scale tasks 들에서도 성능 향상을 보일 수 있다.



기본적으로 모델 사이즈의 크기를 증가시키면 성능이 좋아지는건 맞지만, 일정 임곗값을 초과하게끔 모델 사이즈가 커지게 되면 성능 향상이 없는 것으로 알려져 있다.

이런 작업들은 보통 fine-tuning 했을 때가 아니고 feature-based 기반의 사전 학습 모델을 사용했을 경우다.

하지만 bert와 같이 fine-tuning approach 를 사용한 사전 학습 모델의 사용의 경우,

태스크 특화적인 모델이 더 커지고 더 표현들을 깊게 학습할수록 성능이 좋아지는데, 다운 스트림 태스크의 크기가 작아도 성능이 좋게 작용한다.



### Feature-based Approach with BERT



지금까지의 모델들은 모두 fine-tuning approach 를 사용했고, 분류 작업에서는 simple classification layer 를 추가했으며 모든 parameter 가 다운스트림 태스크에 맞게 파인 튜닝 됐었다.



하지만 feature-based approach 가 이득이 되는 경우도 있다.



1. 모든 태스크들이 트랜스포머 인코더 아키텍처로 쉽게 표현되는건 아니다.

   그러므로 태스크 특화적인 모델이 추가되는걸 요구한다.

2. 미리 비싼 학습 데이터의 표현들을 사전 학습하는 건 이득이다. 이 표현들을 여러 다운스트림태스크에 사용하면 이득.



BERT로 문장을 임베딩하고 그 값을 태스크에서 사용. 이때, 사전 학습된 bert의 파라미터를 다운스트림 태스크에서는 사용하지 않는다.



## Conclusion



최근 언어 모델과 함께한 전이 학습에 의해서 발전한 경험적인 발전은 사전 학습이 많은 언어 이해 시스템에서 중요한 부분이라는걸 설명해오고 있다.



단방향성 모델이 심지어 low resource 에서 좋은 성능을 보였다.

우리의 주요 contribution 은 위의 작업을 bidirectional architecture 에 일반화 시키는 것.