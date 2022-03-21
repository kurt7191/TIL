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

이 중에 뉴럴 모델들은 데이터의 특징들에 대해서 세세함 엔지니어링 없이도 text의 표현을 잘 배울수 있는 능력이 좋아지고 있다.(svm과 비교해서)



이러한 뉴럴 데이터의 발전에도 불구하고, 전통적인 LSTM 과 같은 전통적인 뉴럴 모델들은 암묵적인 방식으로 context 의 정보를 파악하고, 명시적으로 중요한 context 의 단서를 나타낼 수 없다.

논문 저자들은 aspect 에 대한 감성을 추론하기 위해서는 몇몇 context words 들의 하위 집합이 필요하다고 생각한다.

ex) "great food but the service was dreadful!".

=> 여기서 service aspect 에 대한 감성을 분석하고 싶다면, "dreadful" 단어가 중요한 단서가 될텐데, 이때 "great" 같은 단어는 감성을 추론하는데 있어서 필요 없다.



표준 LSTM 은 순차적으로 작업하며 똑같은 작동으로 각각의 context word에 대해서 조작한다. 그래서 각각의 context word 의 중요성을 명시적이게 드러낼 수 없다.

바람직한 해결책은 명시적이게 context words 들의 중요성을 포착하고 aspect word가 주어진 이후에 문장의 특징을 형성하기 위해서 정보를 사용할 수 있어야 한다. (LSTM 이 그렇지 못한데, 이래야만 한다!)



이러한 목표들을 위해서 논문의 저자들은 명시적인 기억과 attention 메카니즘을 이용해서 aspect level의 sentiment 분류 deep memory network 를 발전시킨다. (aspect level 의 감성을 예측하는 딥러닝을 발전시킨다 by using *attention* 사용)

논문에서 사용한 방식은 데이터 중심적이고 계산 효율적이며 **구문 분석기(syntactic parser)** 나 **sentiment lexicon(감정 어휘)** 에 의존하지 않는다.



이 방식은 multi 계산 layer 로 구성되어져 있고, 각각의 layer들은 attention 아키텍처에 기반한다. 

각 계층은 내용 및 위치 기반 attention 모델이며, (encoder를 쌓은건가?) 먼저 각 context 의 중요도와 가중치를 학습한 다음에, 이 parameter 를 사용해서 연속 text representation 을 계산한다.

이 text representation 은 sentiment 분류의 특징으로 간주된다.

오차 역전파를 진행하고, loss function 은 cross entropy error 를 사용한다.



=> 마찬가지로 이 모델은 svm, lstm, lost with attention 모델의 성능을 정확도와 계산 속도 측면에서 압도한다.





















