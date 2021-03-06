# Transformer - Attention is all you need review





## Abstract



과거의 주요 시퀀스 모델들은 RNN(LSTM),CNN.

가장 성능이 좋은 모델도 seq2seq 모델.



논문에서 제안하는 아키텍처는 실험을 통해서 우수한 성능을 보이는 모델로 나타났다.

이 아키텍처는 **병렬화** 가능하고, 모델을 학습시키는데 걸리는 시간이 다른 모델에 비해서 **짧다**.



데이터는 English -> Germany, English -> French 를 사용했다.

Transformer 아키텍처는 언어 번역 이외의 다른 task 에도 잘 적용된다.







# Introduction





기존 전통적인 시퀀스 모델인 RNN 은 히든 스테이트(hidden state) h_t, 그 이전 단계의 히든 스테이트 h_t-1 그리고 시각 t의 입력값 x를 가진다.

RNN 아키텍처의 간단한 학습과정을 보면, h_t-1, t시각 입력값x를 활용해서 현 상태의 출력값 h_t를 반환한다.

이전 계층의 출력을 다음 계층으로 반환하기 위해서 h_t-1은 가중치 Wh를 가진다.

마찬가지로 출력값을 가지기 위해서 시각 t의 입력값은 가중치 Wx를 가진다.



모델 RNN의 출력값(Ht) 계산식은 다음과 같다.



`Ht = tanh(Ht-1 * Wh + Xt * Wx + b)`



하지만 RNN은 시퀀스의 길이가 길면 메모리 문제가 발생한다.

두 가지 문제가 발생하는데 아래와 같다.



- 기울기 소실
- 기울기 폭발



1. 기울기 소실

   - 딥러닝 모델 같은 경우, 역전파를 통해서 모델의 가중치들을 업그레이드 하는데, 목적 함수에 따라서 역전파에 거쳐가는 함수들이 달라진다.

     예를 들어서 RNN같은 경우 역전파가 거쳐가야할 함수는 matnul 함수와 tanh 함수다.

     역전파는 미분을 통해서 손실값이 최저가 되는 지점을 찾게 되는데, tanh 함수 같은 경우 미분을 하면 할수록 값이 작아지는 성질이 있다.

     따라서 T번 tanh 함수를 거치게 되면 T번 미분이 진행되면서 기울기가 작아지기 때문에 기울기 값이 학습을 제대로 할 수 없을 정도로 작아지게 된다.

2. 기울기 폭발

   - 기울기 폭발은 역전파 과정 중에서 matmul 함수에 의해서 발생한다. matmul 함수가 t번 발생하면 기울기가 너무 커지게 된다.



RNN의 기울기 소실이나 폭발과 같은 문제를 해결하기 위해서 LSTM 모델도 등장했지만 여전히 완벽히 해결되지 않았다.

트랜스포머는 시퀀스를 순차적으로 넣는 게 아니라 한꺼번에 집어넣기 때문에 병렬 처리가 가능하고, 번역 질을 높인다(최소 12시간 학습)



# Background



이전에도 Sequential 계산을 감소시키기 위한 노력들이 있었다.



1. Neural GPU
2. ByteNet 
3. ConvS2S



이것들은 모두 conv 뉴런 네트워크를 사용하며 모든 input, output 은닉 상태들에 대해서 병렬적으로 계산한다.

근데 여전히 position 들의 distance 에 따라서 연산이 증가한다. (Conv뉴런은 선형적 증가, ByteNet는 로그적으로 증가)

따라서 거리가 먼 포지션들간의 의존성을 학습하기가 어렵다. (위에서 말한 기울기 소실 혹은 폭발)



트랜스포머는 이를 보완해서 수많은 operations 들을 일정한 수의 operations으로 줄여준다.

하지만 effective 는 감소한다. -> 이를 해결하기 위해서 Multi-head-attention 을 제안한다.



Self-attention 은 자기 자신의 표현을 계산하고 얻기 위해서 다른 sequence 내의 single senquence 들과 관계를 맺는 방법이다.

이 방법은 여러 task 에서도 효과적으로 사용됐다.



우리가 제안하는 transformer 는 최초로 rnn 과 cnn 방식을 사용하지 않고 전적으로 셀프 어텐션에 의존해서 iuput 과 output들의 표현을 계산하는 모델이다. 





# Model architecture



sequence 변환 모델들은 **encoder 와 decoder 구조**를 가진다. (Ex, seq2seq)

간단하게 살펴보면 encoder 는 기본적으로 LSTM 모델을 사용하고 입력 문장 x = (x1 ....xn) 을  z = (z1 ... zn) 으로 바꾼다.

이러한 encoder 의 작동은 입력 문장을 고정 길이의 벡터로 변환하는 것과 같다.



여기서 z를 받은 decoder는 각 시각마다 (y1...yn) 을 출력하고 다음 값을 계산한다.

여기서 출력 (y1 ... yn)은 입력값 다음 단어에 대한 예측 값이라고 할 수 있다. (피드포워드 계층도 존재하기 때문에)

간단하게 정리하면 디코더는 언어모델로서 입력값 다음에 나올 단어를 예측하게 되는데, 이때 그 시각의 입력값 x 와 이전 시각의 출력값을 참조한다.



Seq2seq 또한 학습 과정 중에 오차 역전파를 통해서 가중치들을 업데이트 한다. 이때 **교사 강요(Teaher forcing) ** 를 사용한다.

디코더가 예측한 문장과 실제 문장간의 오차를 최소화 하는 방향으로 모델은 학습을 하게 되는데, 이때 디코더의 입력값을 강제로 조정하게 된다.

본래는 이전 시각의 출력이 현재 시각의 입력값으로 들어가면서 다음 시각의 단어에 대해서 예측하고 다음 단어의 실제값과 비교해서 오차를 구하게 되는데, 

이전 시각의 **실제값(출력값이 근사하려고 했던)** 을 현재 시각의 입력값으로 넣고 그 값을 바탕으로 예측한  다음 시각의 값을 다음 시각의 실제값과 비교해서 오차를 구한다.



만일, 학습 과정 중에 이전 시각의 출력값을 현재 시각의 입력값에 넣었을 경우 현재 시각에서 잘못 예측할 가능성이 커지게되며 이러한 과정은 연쇄적으로 일어나게 되면서 훈련 과정이 길어지게 된다. 이를 교사 강요를 통해서 어느 정도 해결할 수 있다.



### Encoder and Decoder Stacks



기본적으로 트랜스포머는 encoder, decoder 둘 다 self-attention 의 중첩으로 되어 있다.

그리고 fully connected layers 를 가지고 있다.



트랜스포머의 encoder, decoder 의 구성을 살펴보자.



1.  ***Encoder*** : 
   - 논문에서는 encoder 를 6개 쌓았다.
   - 각각의 encoder 는 sub layer 를 2개 가지고 있다.
   - 1. Multi-head self-attention mechanism
     2. Simple,position-wise fully connected feed-forward network
   - 각각의 sublayer 들은 잔차 연결(residual connection) 을 가진다.
     - LayerNorm(x + Sublayer(x))
     - 입력값 x와 sublayer 를 통과한 출력값을 더하고 normalization 했다.
     - 잔차 연결을 수월하게 하기 위해서 모든 sublayer의 출력 차원은 512
2. ***Decoder***
   - 논문에서는 decoder 또한 6개 쌓았다.
   - 디코더는 encoder와 다르게 3개의 sub-layrer 를 가진다.
   - 추가한 sub_layer는 encoder의 출력값 전체에 대해서 multi-head-attention을 적용한다. (decoder의 입력값이 아니라)
   - encoder 와 마찬가지로 잔차 연결을 가진다. (LayerNorm(x + Sublayer(x)))
   - decoder 는 또한 self-attention 을 수정하는데, masking된 self-attention을 사용한다.
   - 위치 i에 대한 예측이 위치 i미만의 것들에만 의존한다.



### ATTENTION



attention function 은 query 그리고 key, value 쌍으로 묘사된다.

query, key, value 그리고 output는 모두 벡터다.



- output 계산
  - output은 가중합으로 계산된다.
  - 이때 각 값에 할당된 가중치들은 key  와 일치하는 query의 **호환성 함수**에 의해서 계산된다.
  - key와 query를 이용해서 가중치 값을 구하게 되고 이 가중치들을 value에 가중합하게 된다.



셀프 어텐션은 문장 내 특정 단어에 대해서 표현하려고 할 때, 그 단어 이외의 문장 내 다른 모든 단어들과 연결하는 과정을 거친다는 것을 살펴봤다.

그 단어가 문장 내 다른 모든 단어들과 어떤 연관을 가지고 있는지 파악하면 그 단어에 대해서 훨씬 더 좋은 표현을 할 수 있기 때문이다. 

그렇다면 특정단어와 문장 내 모든 단어들과 연결짓는 방법은 무엇인가?

**이때 Q,K,V 행렬을 사용해서 특정 단어와 문장 내에 있는 모든 단어를 연결할 수 있다.**



- 1단계
  - 쿼리 Q 행렬과 키 K 행렬의 내적 연산을 수행한다.(한 쿼리는 행렬곱을 하기 위해서 transpose 한다.)
  - 내적을 하게 되면 각 단어간의 유사도를 측정할 수 있다.
  - 예를 들어서 (3,4) 형태의 쿼리 행렬과 키 행렬이 있다고 가정해보자. 둘의 곱을 위해서 키 행렬은 전치 해주고 곱하면 다음과 같은 형태일 것이다. (3 X 4) * (4 X 3). 그럼 최종 형태는 3X3의 형태일 것이다. 
  - 쿼리 행렬의 행들은 각 문장 내 단어들을 의미하고, 전치된 키 행렬은 열이 이를 의미한다. 행렬곱의 계산 형식을 살펴보면 쿼리 행렬의 각 행은 키 행렬의 모든 열들과 곱해짐을 알 수 있다. 이 곱이 의미하는건 쿼리 행렬의 단어 벡터 한 개와 키 행렬의 단어 벡터 3개 각각이 곱해진것을 의미한다. 
  - 벡터간 곱은 두 벡터의 유사도를 의미한다. 따라서 쿼리 행렬과 키 행렬의 내적을 진행하면 위의 예시 I am good 에서는 I단어와 (i,am,good) 단어들간의 유사도, am 단어와 (i,am,good) 단어들간의 유사도, good 단어와 (i,am,good) 단어들의 유사도를 측정하는 것과 같다.
  - 결국 어떤 특정 단어가 문장 내의 다른 각각의 모든 단어들과 **얼마나 유사한지 파악**하는데 도움을 준다.(문장 내 다른 모든 단어들과 연결지었다고 볼 수 있다.)
- 2단계
  - 앞서 계산한 쿼리 Q행렬과 키 K행렬의 내적 QK^t 의 키 행렬의 벡터 차원의 제곱근으로 QK^t 행렬을 나눈다.
  - 예시로 키 벡터의 차원 64 가정. 키 벡터 차원의 제곱근은 8이다.
  - 위에서 구한 8을 QK^t 행렬에 나눠준다.
  - 이와 같은 방법을 적용하면 안정적인 경삿값(gradient) 를 얻을 수 있다.
- 3단계
  - 2단계의 결과값은 비정규화된 값이다.
  - 따라서 정규화 시켜주기 위해 Softmax 함수를 적용한다.
  - 전체 값의 합은 1이 되고 각각의 원소는 0에서 1사이의 값을 가진다.
  - 이러한 행렬을 스코어 행렬(score matrix) 라고 부른다.
  - 이 %를 활용해서 문장 내의 특정 단어가 다른 단어와 %로 관련있는지 확인할 수 있다.
- 4단계
  - 어텐션 Z 행렬을 계산하는 것.
  - 3단계에서 구한 softmax 를 적용한 행렬에 밸류 행렬 V를 곱하면 어텐션 Z 행렬을 구할 수 있다.
  - 즉 어떤 단어 x의 셀프 어텐션은  밸류 벡터값의 가중치 합으로 계산된다.
  - 여기서 가중치는 3단계에서 구한 soft맥스 행렬이다. 이 행렬에는 각 단어에 대한 가중치 정보가 담겨 있다.



이를 scaled-dot-product attention 이라고 부르기도 한다.



가장 일반적으로 사용되는 attention 은 additive attention 과 dot-product attention

Dot product attention 은 우리가 위에서 봤던 attention 에서 정규화를 거치지 않은 것.

Additive attention 은 single hidden layer 가 있는 feed forward 를 사용해서 계산한다.



하지만 dot product attention 은 고도화된 곱셉 매트릭스가 있기 때문에 dot product attention 이 훈련에서 더 빠르고 공간 효율적이다.



두 개의 attention 모두 작은 d_k값을 사용한다는 점은 동일하지만, additive attention 은 dk의 큰 값을 scaling 하지 않아도 dot product 을 능가한다.

그래서 연구진들은 dot product가 d_k의 value를 증가시키고 그게 sofmax의 값이 작아지게끔 한다고 생각했다. 이를 방지하기 위해서 정규화 과정을 거치는 것. 따라서 scaled-dot-product-attention 이 된 것.

#### 

#### multi-head-attention



d_model(차원의 수) 의 차원을 가지는 key, value,queries 와 함께하는 하나의 attention 함수 보다는 여러 개의 attention을 하나로 묶는 게 성능이 더 좋다.

각각의 어텐션에서 출력값을 산출하고 이것들을 결합한다. 이게 multi-head-attention의 최종 출력값.

논문에서는 8개의 layer 를 쌓았다.



나중에 각각의 attention을 concatenate 해야되기 때문에 본래의 차원 d_model을 헤드의 개수로 나누어준다.

만일 d_model이 1000 이라고 한다면 각 attention단 125 차원을 가지게 된다.

후에 각각의 attention들은 출력값을 얻게 되는데 이를 다 합치게 되면 125 * 8 로 인해서 본래의 single attention 차원을 가지게 된다.



#### Application of Attention in our Model



1. encoder -decoder 구조

   - Query는 이전의 디코더 레이어로부터 가져오고 Key, Value는 encoder의 출력으로부터 가져온다.

   - key와 value를 인코더의 출력에서 가져오기 때문에 디코더의 모든 위치가 인코더의 모든 값을 참조할 수 있게 해준다.

     (마스크  멀티 헤드 어텐션 다음에 진행

2. 인코더는 셀프 어텐션 레이어를 포함한다. 셀프 어텐션의 query, key, value는 이전 인코더의 output으로부터 온다. 이를 통해서 각각의 인코더 위치는 이전 레이어 안에서 모든 위치에 참여할 수 있다.

3. 디코더도 마찬가지긴 한데,  우리는 leftward information이 흐르는 걸 방지해야 한다.

   - 언어 모델에서 각 시각마다 예측한 단어들이 있을텐데, 어텐션은 시각을 무시하고 시퀀스 전체를 입력값으로 집어넣기 때문에, 그 시각에 해당하지 않은 입력값도 포함하게 된다. 따라서 각각에 따라서 해당하는 입력값만 포함하고 나머지는 masking 해준다.





### Position-wise Feed-Forward Networks.



인코더, 디코더는 각각의 레이어에 fully connected feed forward network 를 가지고 있다.

선형 변환은 포지션마다 같은 값을 가지는 반면에 그들은 layer마다 다른 파라미터를 가진다.



두 개의 선형변환 with ReLU



### Embedding and Softmax



토큰들을 벡터로 만들기 위해서 사전 학습된 임베딩을 사용한다.

또한 다음 단어를 예측하기 위해서 학습된 선형 변환과 소프트맥스 함수를 사용한다.

논문은 두 개의 임베딩은 동일한 가중치를 가지고 softmax 이전의 선형  변환 또한 동일한 가중치를 가진다.



임베딩 레이어에서는 차원의 제곱근을 곱한다.



### Positioning Encoding



rnn 모델과 다르게 우리 모델은 시퀀스의 순서에 대한 정보가 없다.

모델이 시퀀스의 순서를 사용하기 위해서 토큰의 위치에 대한 정보를 벡터에 집어넣는다.

(앞서서 임베딩 레이어에서 각 토큰에 대해서 벡터화 했는데 그 값에 위치에 대한 정보를 집어넣는다.)



이를 위해서 positional encoding 을 추가한다.

positional encoding 도 임베딩의 차원과 동일한 차원을 가진다. 따라서 그 둘 값을 합할 수 있다.



sin과 cos 을 이용해서 위치 정보를 넣으려고 한다.



## Why Self-Attention





1. 계산 복잡도
2. 최소한의 sequential 한 작업 수로 측정할 수 있는 총 계산량.
3. 장거리 종속성 사이의 경로 길이
   - 경로의 길이가 중요하다.
   - 길이가 짧을수록 의존성을 학습하는데 좋다.
   - 따라서 다른 레이어 유형으로 구성된 네트워크의 두 입력 및 출력 위치 사이의 최대 경로 길이를 비교(장기 의존성을 학습할 수 있는)



Self attention 과 다르게 rnn 은 순차 작업이 필요하다.



셀프 어텐션이 rnn layer 보다 빠르다.(시퀀스 길이 n 이 임베딩 차원 d보다 작으면)

장기 의존성을 타파하면서 성능을 높이기 위해서 특정 윈도우 사이즈 r을 정해서 이웃들만 고려하게끔 할 수 있다.

이렇게 하면 최대 시퀀스 길이를 늘릴 수 있을 것으로 보인다 (후의 작업에서 할 수 있을 듯.)



이래서 Attention 을 사용한다.

## 

## Traning





사용 데이터 셋1 : WMT 2014 English-German dataset, 4.5m 개 sentence pair, tokenizer vocab : 37000 token

사용 데이터 셋2 : WMT 2014 English-French dataset, 37m 개 sentence pari, tokenizer vocab : 32000



Optimizer : learning rate 를 고정적으로 사용하는 게 아니라 초반 warm up step 은 크게 나중에는 적게 준다.





















### 







 







































