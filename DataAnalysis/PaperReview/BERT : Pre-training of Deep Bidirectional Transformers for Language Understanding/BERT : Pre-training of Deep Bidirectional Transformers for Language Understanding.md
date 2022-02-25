# BERT : Pre-training of Deep Bidirectional Transformers for Language Understanding







## Abstract



BERT : **B**idirectional **E**ncoder **R**epresentation **T**ransformer



문장의 양방향 context 를 고려한 사전학습 모델로, Transformer 의  encoder 를 활용한 모델.

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

"feature based", "fine tunning"  방법.



- "feature based " 

  - 특징 기반 방법

  - 사전 학습된 특징을 하위 문제의 모델에 부가적인 특징으로 활용하는 방법.

  - "특징 기반 방법" 의 "특징" 이란 모델 중간에 나오는 특징값.

  - Elmo, word2vec.

    

- "fine tunning"

  - 미세 조정 방법
  - 사전 학습된 모델의 가중치를 그대로 사용하면서 최소한의 하위 태스크 특화적인 매개변수(가중치) 들을 추가해서 하위 태스크에 맞게 추가로  학습(미세조정) 하는 것.
  - 특정 목적 함수에 맞게 사전 학습된 모델의 가중치를 하위 태스크 작업을 할 때 그대로 사용하면서 하위 태스크를 위한 최소한의 가중치를 추가해서 추가 학습하는 방법.
  - GPT version 들이나, Transformer





### 연구진들의 문제 의식



지금까지의 언어 모델들은 모두 단방향 모델들이다.

GPT 같은 경우에도 단방향인데 (left - to - right) 학습을 할 때, 트랜스포머의 셀프 어텐션 layer 에서 이전의 토큰들만 참고할 수 있다. 



단방향적인 모델들은 문장 단위의 작업들을 수행하는데 있어서 최적합적이지 않고, 

단방향적 모델을 기반으로 사전 학습된 모델들을 토큰 단위의 하위 태스크에 적용하면 성능이 좋지 않을 수 있다. (질의 응답 태스크 같은)



그래서 연구진들이 내놓은 모델이  BERT : **B**idirectional **E**ncoder **R**epresentation **T**ransformer.

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

후에 Melamud et al.가  single 단어에 대해서 LSTM 을 사용해서 양쪽 context 를 활용해 예측하자고 주장한다. 이는 ELMo 방식과 닮았다.

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



버트가 다른 모델들과 구분되는 특징 중 하나는,  다양한 다운스트림 태스크에 걸쳐서 하나로된 아키텍처를 사용하는 성향을 가지는 것.

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

     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - ㅇ
     - 

   - mlm 작업은 필수적으로 으로 pre-train 과 fine-tunning 사이에 mismatch 가 발생하게 된다.🥲 왜냐하면, fine-tuning 에서는 mask 토큰이 존재하지 않기 때문에.

     즉 mask 토큰을 예측하면서 사전 학습된 bert 모델은 다른 다운 스트림 태스크에 적용할 때, 다운 스트림 태스크의 토큰들은 mask 가 존재하지 않기 때문에 서로 mismatch 가 발생하게 된다.

   - 이런 점을 완화하기 위해서 무작정 지정한 비율대로 token들을 maksing 하지 않는다. 대신에 (80 - 10 -10) rule 을 적용한다.

     지정한 비율로 선택된 토큰들 중에서 80%는 본래의 목적대로 masking 을 하고, 10%는 다른 단어로 대체하고 10%는 본래의 토큰으로 남긴다.

     만일 i th 번째 토큰이 masking 대상으로 선정됐다면 위의 80- 10- 10 rule 을 거치게 되고 본래의 token 값과 t_i 에 대한 예측값의 손실(cross entropy loss)을 구해서 모델에 대한 학습을 진행한다. (appendix 참고) 

2. Next Sentence Prediction
   - ㅇ
   - ㅇ
   - 















































