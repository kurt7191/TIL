# Aspect Level Sentiment Classification with Deep Memory Network



## Abstract



이 논문은 딥러닝 기반의 Aspect level 단위의 감성 분석 분류기 모델을 제안한다

특징 기반의 svm 모델과 LSTM과 같은 시퀀셜 뉴럴 모델과 달리 논문 방법의 접근은, aspect의 감성 극단을 추론할 때 명백하게 각각의 문맥 단어의 중요성을 포착한다.



멀티 계산 layer와 함께 중요 정도와 text representation 들은 계산되어진다.

각각의 레이어는 외부 memory 에 대한 신경망 attention 모델이다

##### Laptop 과 Restaurant 데이터셋에 관한 이 논문의 실험은 SVM 시스템, LSTM 그리고 attention 기반의 LSTM의 성능과 비교할만한 성능을 낸다.

(두 개의 데이터 셋에서 향상된 성능을 보여주면서 더 빠른 계산 속도를 보여준다..)

> deep memory network with 9 layer => 논문에서 제안한 architecture
>
> LSTM 과 비교했을 때, 15배 더 빠르다.



- 논문에서 제안한 The Deep Memory network with 9 layer => 이전의 모델들보다 성능이 더 좋다.



<hr>

## Introduction



Aspect 기반의 감성 분류는 감성 분류 분야에서 기초적인 분야이다.

문장이 주어지고 aspect 가 sentence 내에 주어지면, 이 task 는 감성 극단을 추론하는 것을 목적으로 한다.

예를 들어서, "great food but the service was dreadful" 이라는 sentence 가 있다면,

sentence 내의 aspect 인 food의 감성 극단은 긍정인 반면에 service 는 부정이다.



aspect 기반의 감성 분석을 위해서 전통적으로 지도학습 기반의 머신러닝 알고리즘과 감성 분류기를 사용한다.

=> 이런 이전 연구들은 SVM(Suppor vector machine) 과 뉴럴 네트워크 모델들을 포함한다.

이 중에 뉴럴 모델들은 데이터의 특징들에 대해서 세세한 엔지니어링 없이도 text의 표현을 잘 배울수 있는 능력이 좋아지고 있다.(svm과 비교해서)



이러한 뉴럴 데이터의 발전에도 불구하고, 전통적인 LSTM 과 같은 전통적인 뉴럴 모델들은 암묵적인 방식으로 context 의 정보를 파악하고, 명시적으로 중요한 context 의 단서를 나타낼 수 없다.

논문 저자들은 aspect 에 대한 감성을 추론하기 위해서는 몇몇 context words 들의 하위 집합이 필요하다고 생각한다.

ex) "great food but the service was dreadful!".

=> 여기서 service aspect 에 대한 감성을 분석하고 싶다면, "dreadful" 단어가 중요한 단서가 될텐데, 이때 "great" 같은 단어는 감성을 추론하는데 있어서 필요 없다.



표준 LSTM 은 순차적으로 작업하며 똑같은 작동으로 각각의 context word에 대해서 조작한다. 그래서 각각의 context word 의 중요성을 명시적이게 드러낼 수 없다.

바람직한 해결책은 명시적이게 context words 들의 중요성을 포착하고 aspect word가 주어진 이후에 문장의 특징을 형성하기 위해서 정보를 사용할 수 있어야 한다. (LSTM 이 그렇지 못한데, 이래야만 한다!)



이러한 목표들을 위해서 논문의 저자들은 명시적인 기억과 **attention 메카니즘을 이용**해서 aspect level의 sentiment 분류 deep memory network 를 발전시킨다. (aspect level 의 감성을 예측하는 딥러닝을 발전시킨다 by using *attention* 사용)

논문에서 사용한 방식은 데이터 중심적이고 계산 효율적이며 **구문 분석기(syntactic parser)** 나 **sentiment lexicon(감정 어휘)** 에 의존하지 않는다.



이 방식은 multi 계산 layer 로 구성되어져 있고, 각각의 layer들은 attention 아키텍처에 기반한다. (인코더 디코더 합쳐져 있는건가?)

각 계층은 내용 및 위치 기반 attention 모델이며, (encoder를 쌓은건가?) 먼저 각 context 의 중요도와 가중치를 학습한 다음에, 이 parameter 를 사용해서 연속 text representation 을 계산한다.

이 text representation 은 sentiment 분류의 특징으로 간주된다.

오차 역전파를 진행하고, loss function 은 cross entropy error 를 사용한다.



=> 마찬가지로 이 모델은 svm, lstm, lost with attention 모델의 성능을 정확도와 계산 속도 측면에서 압도한다.



> 논문에서 제안한 모델은 attention 기반의 multi layer 신경망 감성 분류기



## Background: Memory Network

> literature 들에 대해서 설명하는 거 같다.



이 논문은 논문이 쓰여질 당시의 질의 응답 memory network 에서 영감을 받았다.

그래서 Memory Network 에 대해서 설명한다.



예측의 목적으로 쓰여질 수 있고 학습될 수 있고 읽을 수 있는 long-term-memory component를 **추론**하는게 Memory Network 의 주요 목적이다.



이전에 memory network는 memory m 과 네 개의 구성요소들 I,G,O,R 로 이루어져 있다.

여기서 memory m은 벡터 array 와 같은 object 의 array 이다. (벡터라는 말인가? 그렇게 이해함)



네 개의 구성요소들 중에서

- I는 iuput 을 내부 특징 표현으로 변환한다.
- G는 오래된 memories 들을 새로운 input 과 함께 업데이트한다.

- O는  현재의 memory state 와 새로운 input과 함께 주어진 output representation 을 만든다.
- R은 출력 표현을 기반으로 응답을 만든다.



논문에서는 앞서 question answering task 에서 영감을 받았다고 했는데, 이 작업에 대해서 설명하려고 한다.

sentences 들의 list 들과 질문이 주어지면, task 는 이 문장들로부터 증거를 찾는데 목적을 두고 답을 찾는데 목적을 둔다.

1. 이 추론을 하는 동안에 I components 는 하나의 문장 s_i 를 읽는다. 그리고 그 문장 s_i 를 vector representation 으로 변환한다.

2. 그리고 G component는 현재의 문장 표현을 기반으로 해서 memory m_i 를 업데이터 한다.

3. 그 이후 모든 문장들은 가공이 되고 우리는 이 문장들의 의미성을 담고 있는 matrix m 을 얻게 된다.  각각의 행은 sentence 들을 나타낸다. (m matrix 겟또)
4.  q question 이 주어지면, network 는 마찬가지로 이를 vector representation 으로 변환한다.(e_q)
5. 그리고 O component는 질문관련 증거들을 찾기 위해서 e_q 벡터를 사용한다. 그리고 output vector o를 만든다.
6. 마지막으로 R component는 output vector o를 input 으로 간주한다. 그리고 응답(response) 를 output 한다.



> 여기서 O component는 하나 이상의 computational layer 로 구성될 수 있다.



여기서 computational layer 을 사용했을 때 드는 직관은, 더 **추상적인 증거**들을 이전의 추출된 증거들을 기반으로 해서 찾을 수 있다는 것이다.=> 더 추상적이게 찾을 수 있다.



> Sukhbaatar et al. (2015) 은 multiple hops 이 single hop 보다 더 추상적인 증거들을 찾을 수 있다고 이야기 한다. 그리고 질의응답 task, 언어 모델에서 더 나은 결과들을 창출할 수 있다고 이야기 한다.



##### 여기까지 memory network literature 에 대한 설명이였다.



![20170525175344](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/20170525175344.png)





## Deep Memory Network for Aspect Level Sentiment Classification



이 part 에서는 aspect 기반의 감성 분류를 위한 Deep Memory Network 를 보여줄 예정

1. 논문의 저자들은 task 에 대해서 먼저 정의를 내리고,

2. 접근법을 개관하고,

3. 각각의 계산 layer 에 있는 내용, 위치 기반의 attention model 들을 설명하고,

4. 마지막으로, 이 접근을 aspect 기반의 감성 분류에 사용하는걸 설명한다.



### Task Definition and Notation



s = {w1,w2,...,wi,...wn} sentence가 주어지면, 그 sentences 들은 n개의 words 들로 구성되어 있다.

그리고 s 내의 단어들 중 w_i 가 aspect word라고 가정하자.

##### 감성 분류 작업은 aspect w_i 에 대한 sentence s의 감성 극성을 결정한다. => task definition



Ex) "great food but the service was dreadful!" : S

S 문장(sentence)의 "food" word 에 대한 감성 극성은 긍정(positive)다.

반면에, S의 "service" word 에 대한 감성 극성은 부정(negative) 다.



우리가 text corpus 를 다룰 때, 우리는 각각의 word들을 낮은 차원의 것, 연속적인 것 그리고 값을 가지고 있는 vector 로 mapping 한다. 이는 word embedding 이라고 알려져있다.

모든 word vectors 들은 쌓일 수 있고 결국 matrix 가 될 수 있다.

예를 들어서 word embedding matrix 를 L 이라고 했을 때 L 은 **L ∈ R^d×|V |** 이다.

d는 dimension 을 의미하고 |v|는 vocabulary size를 의미한다.

그럼 word 하나에 대한 임베딩 표현 w_i 는 **ei ∈ R^d×1** 로 표현될 수 있다.

> vocabulary size 는 단어 1개에 대해서 이야기 하고 있으니 1이다.



### An Overview of the Approach



deep memory network for aspect level sentiment classification 에 대한 oveview



위에서 설명했듯이 s = {w1,w2,...,wi,...wn}가 주어지면, aspect  word는 w_i 라고 가정하고, 각각의 word들은 embedding vector로 변환된다.

이 word embedding vector 들은 두 부분으로 분리되는데, 바로 aspect representation과 context representation 이다.

> aspect representation or context representation

=> 아마 aspect word 에 대한 embedding vector 와 aspect 주변 cotext word들의 representation 으로 나눈 것 같다.



만일 aspect 가 문장 내에서의 단일 word인 service, food 라고 한다면 aspect representation 은 해당 단어들의 word embedding vector 라고 할 수 있겠다.

근데, aspect 가 multi word expression (복합단어?) 이라면 aspect representation 은 그것을 구성하고 있는 word vectors들의 평균이다.ex) "battery life"

논문에서는 해석을 단순화하기 위해서 aspect 를 단일 단어 w_i로 간주했다.



다른 한 파트인 context representation(context word vector) {e1 , e2 ... ei−1 , ei+1 ... en } 들은 쌓이게 되고 외재적인 memory m으로 여겨진다. (Matrix)

m은 다음 식과 같은 형식을 가진다. 

> m ∈ R^d×(n−1) 



내가 이해하기로는 aspect word vector 1개를 뻬고 context word들만 고려해야 하기 때문에 vacabulary size 가 들어갈 곳에 1을 빼주는 것 같다.  





> 정리하자면,
>
> sentence 가 주어지면 sentence 내의 words 에 대해서 모두 embedding 작업을 거치게 되는데 이 embedding 된 vectors 들은 두 파트로 구분이 되고, 한 파트는 aspect word에 대한 embedding vector이며, 다른 하나는 aspect word 를 제외한 context words 의 vector 들이며 context words들의 vector 들은 memory m matrix 로 만들 수 있고, 이 matrix 의 shape 은 aspect word 를 제외한 matrix 이기 때문에 vocabulary size 에서 1을 뺀다.



### ![스크린샷 2022-03-22 오후 2.30.51](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 2.30.51.png)



위의 그림은 qa task 에서 memory network를 사용한 것에 영감을 받은 논문 저자들의 접근법에 대한 설명을 그림으로 나타낸 것.

그림을 보면 알 수 있듯이 여러 computational layer(hop)들로 이루어져 있다.

각각의 hop들은 attention layer 와 linear layer 을 가지고 있다.



1. 어텐션 레이어를 통해서 memory m 에서 중요한 증거를 적응적으로 선택하기 위한 input 으로 aspect vector 를 취한다.

   - attention 이 중요한 부분에 대해서 가중치를 주기 때문에 쓰인 것 같다.

2. hop1 에서의 attention layer 의 output과 linear layer 의 output은 합쳐지고 hop1 의 output 으로 간주되는데, 이는 다음 hop layer 의 input으로 간주된다.

3. 이 과정을 똑같이 반복하는 layer들의 개수를 설정하고, 이 과정을 반복하면 반복할수록 추상적인 증거들이 외재적인 memory m 으로부터 선택될 수 있다.

   (참고로 memory m 은 context vectors 들의 matrix 다.)

4. 마지막 hop layer 의 output은 aspect 를 고려한 문장 표현으로 간주된다. 그리고 이는 aspect 감성 분류의 특징으로 사용된다.



> 알아두면 좋은 점
>
> attention과 linear의 parameters 들은 다른 hop layer 들과 공유되어진다.
>
> 따라서, 9개의 layer의 parameter의 숫자는 동일하다. 



### Content Attention



##### attention 을 aspect 에 대해서 고려한 sentence 의 representation 을 feature 로 추출하기 위해서 사용한다.



직관적으로, context words들은 평등하게 혹은 동일하게 문장의 의미에 대해서 기여하지 않는다는 점이다.

게다가 우리가 다른 aspect 에 초점을 두게 되면 context word의 중요도도 달라질 것이다.

(즉, aspect를 기준으로 context word 의 weight/importance 는 달라진다.)



> 따라서 aspect 별로 중요한 context 단어에 대해서 집중??을 해야 하는데, 이러한 메커니즘은 attention 메커니즘와 유사하다.



ex)

“*great food but the service was dreadful!*”

aspect 이 "food" 이면 context word "great" 이 context word "dreadful"  보다 더 중요한 단어일 것이다.

반대로 aspect가 "service" 면, context word "great" 보다 context word  "dreadful" 가 더 중요한 단어일 것이다.



<hr>

> ##### 잠시 attention 구조 복습



![어텐션 메카니즘](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/어텐션 메카니즘.png)





##### 어떤 계산을 통해서 필요한 정보만 Affine layer 에 전달한다.

위의 그림을 정리

LSTM 으로 구성된 seq2seq 의 아키텍처가 있다고 가정해보자.

seq2seq 의 encoder 가 sentence를 입력값으로 받았을 때, 내놓은 sentence 에 대한 vector matrx 가 있을 것이다. 이를 **hs**라고 해보자.

hs는 "어떤 계산" 에 이용되어지는데, "어떤 계산" 은 input 값으로 첫 번째 시각의 LSTM 이 output 으로 뱉은 값과 hs를 input으로 받는다. 이 계산을 통해서 decoder 의 lstm 첫 번째 시각의 input 의 특징을 잘 반영한 맥락 벡터(context vector) 가 도출된다. context vector 가 도출되는 과정은 아래 그림과 같다.

> 가중치 a는 첫 번째 시각 LSTM 의 output 과 hs matrix 간의 내적을 통해서 계산이 된다.
>
> 또한 맥락 벡터는 가중치 a와 hs matrix 간의 가중합이다.



![어텐션 맥락벡터](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/어텐션 맥락벡터.png)



<hr>



자, 위의 attention 메카니즘을 잘 기억하면서 논문을 설명하면

위의 seq2seq 가 내뱉은 sentence에 대한 vector matrix hs의 역할을 논문은 context vector 들의 matrix memory m 이 맡는다.

memory m의 각 행은 context word 들을 의미한다.



또한 seq2seq 의 decoder 의 각 시각마다의 input 은 논문에서 aspect vector 라고 할 수 있다.(일종의 정답? 같은 느낌)

attention 메커니즘과 똑같이 Memory m 과 가중치를 곱해야 하는데, 이 가중치 a는 input 인  aspect vector 들과의 내적을 softmax 함수에 집어넣어 0 ~ 1 사이의 값을 만든 값일 것이다.

Memory m 과 가중치 a를 곱한 가중치 합은 attention 메커니즘의 맥락 벡터(context vector)와 같은 벡터를 생성한다. 그 식은 아래와 같다. (이는 attention layer의 output임, vec으로 표현)



![스크린샷 2022-03-22 오후 3.14.09](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 3.14.09.png)





> aspect vector 와 유사성이 가장 큰 값을 가중치를 가장 크게 주어 만든 맥락 벡터.
>
> 결국 이 맥락 벡터는(attention 메카니즘의 용어를 빌려) aspect 를 잘 고려한 문장 표현으로 간주될 수 있다.



논문의 저자들은 attention 아키텍처의 장점으로 aspect 와의 의미론적 유사성에 따른 memory m 의 각각의 word들에 대한 중요도 점수를 적응적으로 부여할 수 있다는 점을 꼽는다.

또 다른 장점으로 attention 모델은 차별화가 가능하기 때문에 다른 구성요소와 함께 end-to-end(??무슨말이지 들어본거 같긴한데.._)로 쉽게 훈련할 수 있다.



### Location Attention



위에서 설명한 neural attention framework 는 **content based 모델**이다.

이 모델은 aspect word 와 context word 사이의 **위치 정보를 무시하는 단점**이 있다.

위치 정보는 attention 모델에 유익하게 사용될 수 있는데, 이는 직관적으로 aspect word 와 가까운 단어들은 그렇지 않은 단어들보다 더 중요하기 때문이다.



논문의 저자들은 context word의 위치를 본래의 sentence 시퀀스 내에서의 **aspect word와의 절대적인 거리**로 정의했다.

논문의 저자들은 위치 정보를 인코드 하는 4가지 전략을 수립했다.



- model1
  - ![스크린샷 2022-03-22 오후 4.06.56](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 4.06.56.png)
  - v_i =  word w_i 의 위치 벡터 (aspect word를 뜻하는 w_i 인 거 같은데?)
  - e_i = context vector e_i 의 vector
  - v_i를 구하는 공식
  - ![스크린샷 2022-03-22 오후 4.08.40](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 4.08.40.png)
  - k는 hop의 개수, n은 sentence의 길이, l_i는 w_i 의 위치
- model2
  - model1의 simple 버전
  - 다른 hop안에서 w_i를 위한 똑같은 v_i 벡터를 사용
  - v_i 구하는 공식
  - ![스크린샷 2022-03-22 오후 4.12.05](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 4.12.05.png)
- model3
  - location vector v_i를 parameter로 간주한다.
  - 모든 position vectors들은 position embedding matrix 에 쌓인다.
  - 기울기 하강과 함께 그것들은 함께 학습되어진다.
- model4
  - 마찬가지로 location vector을 파라미터로 간주한다.
  - 다른 점은, 얼마나 많은 word semantics의 부분이 memory 에 쓰여졌는지 컨트롤 하기 위해서 location representation 을 neural gate로 간주한다.
  - location vector을 시그모이드 함수의 input으로 주어 m_i 를 계산한다.
  - ![스크린샷 2022-03-22 오후 4.18.10](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 4.18.10.png)



### The Need for Multiple Hops



multiple layer을 가지고 있는 계산 가능한 모델들이 multi level에서의 데이터의 표현을 배울 수 있는 능력을 가지고 있다는 건 널리 알려진 사실이다.



이 작업에서, **one layer** 내의 attention layer는 본질적으로 가중화된 평균 구성 함수이다. 그리고 그것은 언어 내에서 형용사, 강화, 부정과 같은 정교한 계산 능력을 감당할 수 없을 정도로 강력하지 않다.



**Multiple computational layer** 는 deep memory network 가 text의 표현을 여러 수준의 추상화와 함께 배울 수 있게끔 한다.



각 layer/hop 은 중요한 context word를 검색하고, 이전 단계에서의 word 의 representation 을 더 추상적이게 바꾼다.(이전 단계걸(attention 메커니즘 내의 용어 맥락 벡터) 더 추상적이게!)

이런 변형과 같은 충분한 구성들과 함께,  aspect에 대한 문장의 매우 복잡한 representation은 학습될 수 있다.



> 즉, multi layer 로 문장의 매우 복잡한 representation 들을 계산하고 학습할 수 있음.

### 

### Aspect Level Sentiment Classification



layer의 마지막 hop 의 output 을 feature로 선정한다.

이 feature 를 aspect level의 감성 분류를 위해서 softmax layer 의 input으로 넣는다.

이 모델은 cross entropy loss 값을 최소화하는 방향으로 지도 학습 방식을 취해서 학습한다.

이때 word embedding 의 방식은 Glove 방식을 취했다.



## Experiment



### Experiment Setting



- data
  - from Se- mEval 2014
  - laptop
  - restaurant
  - 데이터 내에 conflict category 가 있는데, 이 항목은 pos, neg 가 하나의 sentence 내에 존재해서 conflict 될 때 나타낸다. => 논문은 conflict category 인스턴스들을 제거하고 불균형한 label의 더 적은 label 에 이를 추가한다.
  - 모델의 평가는 accuracy로 할 예정.







### Comparison to Other Methods



두 데이터셋에서 다음과 같은 방법들을 기본으로 해서 비교했다.



1. Majority
   - training data set에 있는 주요 label을 test set 의 각각으 instance 의 label로 부여하는 것
2. Feature-based SVM
   - 지금까지는 가장 높은 성능을 보이고 있는 것
3. LSTM
   - LSTM
   - TDLSTM
     - aspect에 대한 backward, forward lstm 사용
   - TDLSTM+ATT
     - hidden vector 전체에 대해서 attention 메커니즘을 합친 TDLSTM 을 확장한 것
4. ContextAVG
   - 논문에서의 접근의 간단화한 버전
   - context word vector 들은 평균지어지고 그 결과에 aspect vector 가 더해진다. => 이게 feature 로 채택되는 듯.
   - 그 output 은 softmax 함수에 input 으로 들어간다.





> 결과 : 기존의 전통적인 모델들은 성능이 그렇게 좋지 못했는데 svm 은 좋은 편이다.
>
> 논문에서 제안한 모델은 svm과 비빌만 하다.=> 엄청 압도하진 않음
>
> ㅇ
>
> 계산시간을 살펴봤는데, LSTM 기반의 모델들은 계산 비용이 높은 반면에 논문에서 제안한 모델들은 계산 비용이 낮았다.



### Effect of Location Attention



![스크린샷 2022-03-22 오후 5.20.06](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/Aspect Level Sentiment Classification with Deep Memory Network/이미지/스크린샷 2022-03-22 오후 5.20.06.png)



Table 4는 위치 정보가 들어가 있지 않은 경우, Table 5는 위치 정보가 들어간 경우.

Table 4(a)는service 같은 경우에는 hop 의 크기가 커지면서 점점 정확하게 attention 하게 되어 정답을 맞추었지만 

Table 4(b) 는 food aspect 에 대해 감성 분석을 진행할 때, 그 주변 context word 들에 대한 가중치(attention) 이 잘못 되고 있음을 알 수 있다. 똑같ㄷ이 dreadful 에 가중치가 커지고 있는 모습을 볼 수 있다.

결국 잘못 예측하여 food aspect 를 부정으로 판단하게 된다.



Table(5)는 위치 정보가 추가된 경우이며 table 4와 달리 context word 들에 대한 attention 이 잘 이루어지고 있음을 알 수 있다.



### Error Analysis



위치정보가 추가된 모델의 오류들을 아래와같이 열거할 수 있음.



- 구성적이지 않은 감정에 대한 표현
  - 이 모델은 single context word를 계산가능한 unit으로 간주한다.
  - "dessert was also to die for!" => die, for 각각으로 의미가 구성되면 안된다.
- 많은 단어들로 구성되어져 있는 복잡한 aspect 표현
  - "ask for the **round corner table next to the large window**"
  - 굵은 글씨가 aspect 라고 할 때, 이 구성 word들의 평균으로 aspect vector를 표현한다.
  - 좋지 않다.
- 부정, 비교, 조건과 같은 맥락 단어 사이의 감성적 관계
- 비교급이 사용이 될 때.





## Conclusion



context words 들의 중요도를 포착하는 deep memory network 를 aspect level 의 감성 분류를 하기 위해서 발전시켰다.

rnn 기반 모델들과 비교를 했을 때, 더 간단하고  더 빨랐다. => LSTM 아키텍처들보다 훨씬 낫다.

그리고 svm 과 비빌만한 성능을 냈다.(압도 x)



attention 기반의 전략을 짰는데 한 모델은 위치 기반 정보가 포함되어 있지 않고, 한 모델은 위치 기반 정보가 포함되어 있다.

그 결과 content 뿐만 아니라 위치 정보까지 활용해야 weight 와 text representation 을 잘 학습할 수 있었으며 성능이 더 좋았다.



그리고 multi layer 를 사용하는게 성능을 더 좋게한다.





> 한 문장으로 요약 :
>
> Attention 기반으로 context word들을 통해서 aspect 에 대한 문장 representation 을 얻고 이를 feature 로 사용해서 감성을 분류한다.

























