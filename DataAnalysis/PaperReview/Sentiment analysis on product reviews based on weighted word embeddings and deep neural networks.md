# Sentiment analysis on product reviews based on weighted word embeddings and deep neural networks





# Summary



감성 분석은 자연어 처리 분야에서 굉장히 중요한 분야다.

감성 분석은 특정한 주제에 대한 소비자들의 태도, 생각, 의견들 또는 판단들이 추출된다.

이러한 감성 분석은 기업 조직의 의사 결정에 도움을 줄 수 있다.



우리는 상품 리뷰들에 대한 딥러닝 기반의 감성 분석을 진행한다.

우리가 주장한 아키텍쳐는 weighted Globe word embedding with CNN_LSTM 이다.

CNN-LSTM 의 층은 5개의 층이다.



1. weighted embedding 층
2. cnn층(1,2,3)
3. max-pooling 층
4. LSTM 층
5. dense 층



각각의 word embedding 방식과 각각의 weighted function 에 따른 예측 성능을 전통적인 딥러닝 방식과 함께 평가한다.

다 시도를 해본 결과 우리가 제안한 방식이 전통적인 딥러닝 방식의 성능을 압도한다.



<hr>

## Introduction





감성 분석은 개인이나 조직에 이익을 가져다주게 사용될 수 있다.

감성 분석의 방식은 두 가지로 구분이 된다.



1. Lexicon 기반 방식 : 긍정단어와 부정단어와 관련된 단어 사전을 사전에 만들고 새로 문서가 들어오면 그 문서를 token 화 해서 문서에 나온 단어들의 긍정, 부정을 파악하여 감정을 분석. 
2. 머신러닝 기반 방식 : 정답을 가지고 있는 데이터를 사용함. 이 데이터를 사용해서 지도기반 머신러닝 분류 모델을 만들 수 있음. (나이브 베이즈, SVM, K최근접 이웃 알고리즘, 랜덤포레스트 등등)



최근 NLP 작업에서 Neural network 를 사용하여 텍스트 처리를 하면 예측 성능을 향상시킬 수 있다는 연구가 많음.

그 중에 딥러닝 도구 RNN, CNN, GRU, LSTM 등이 사용될 수 있다.



또한 텍스트 문서를 표현하는 방법은 꽤 중요하다. 머신러닝을 기반으로한 NLP 업무의 성능에서.

전통적인 문서 표현 방법은 bag of words 방법인데 이 방법은 syntax, 단어 랭킹, 문법 규칙을 무시한다. 그리고 고차원의 문제가 발생하고 희소행렬 문제를 가지게 된다.



그래서 다양한 word embedding 방식이 나오는데, 이게 성능 향상을 도와줬다.

그리고 이게 고차원 문제와 희소행렬 문제를 없애줬다.

고전적인 방법으로는 word2vec 방식이 있다.

word2vec 은 문장안에 있는 각각의 단어에 동등한 weight를 부여했다.

근데, 최근 NLP연구는 Word embedding 에 weight를 부여하면 성능을 향상할 수 있다고 제안한다.



그래서 우리는 위에서 말한 것들을 고려해서, weighted word embedding with cnn-lstm 을 사용할 예정이다.



cnn-lstm 의 층은 다음과 같이 5층이다.



1. weighted embedding 층 
2. cnn층(1,2,3)
3. max-pooling 층
4. LSTM 층
5. dense 층



이제 각 기술마다의 예측성능 비교할건데,

- embedding skill : (word2vec, fastText, Glove, LDA2vec, and DOC2vec) 사용
- weight function : (TF-IDF, SIF, IDF) 사용

위와 같은 기술들과 함수들을 이용한 예측 성능들을 비교해볼 것. CNN-LSTM 은 물론 전통적인 딥러닝 네트워크에서도 (CNN, LSTM, RNN 등등)



<hr>

## Methodology



### Twitter product reviews corpus



기술적인 상품과 관련된 키워드들의 범주만 고려했다.



93,000 개의 영어로 쓰여진 트윗을 얻었다.

자동 필터를 적용해서 중복된 글이나 쓸모없는 것들을 제거했다.

그리고 각각의 트위터 포스트의 감정 상태에 대해서 알기 위해 긍정, 부정 label을 달았다.



네 명의 전문가가 기록을 했고, Fleiss's kappa (k) metric을 계산했더니 0.81 k를 얻었다.

이 수치를 통해서 괜찮다고 판단한 거 같다.



50,000개의 긍정 데이터, 43,000 개의 부정 데이터를 얻었다.

최종적인 우리 데이터는 43,000 긍정, 43,000 부정 데이터를 가진다.



그리고 전처리를 거쳤다.



우리가 제안한 방법의 예측 성능을 조사해야하기 때문에 target_dependent twitter corpus 를 사용했다.

이 데이터는 세 개의 레이블로 이루어져 있는데, 부정, 중립, 긍정으로 이루어져있다.

트레이닝 데이터는 6248개, 테스트는 692개다.



### Neural language model



neural language model은 단어의 의미론적 특색을 담은 vector 를 준다.

우리는 5개의 embedding 방식을 살펴볼건데 아래와 같다.



- embedding skill : word2vec, fastText, Glove, LDA2vec, and DOC2vec





1. word2vec : input layer, hidden layer, output layer 로 이루어져 있다.

   - 두 가지 방식으로 나뉜다.
     - CBOW :  맥락 단어들을 Input으로 넣어서 target 단어들을 예측하는 방식을 사용한다.
     - SG(SKIP-GRAM) : 반대로 target 단어로부터 맥락단어를 추론하는 방식을 사용한다.
   - 추론을 잘하는 신경망을 학습을 통해서 만들고, 그 때 입력 가중치 매개변수의 행을 각 단어의 분산 표현으로 지정하고 벡터로 선정한다.

2. GloVe :

3. fastText : 기존 embedding 모델들은 비슷한 구조를 가지고 있는 단어들에 대해서 각각 다른 벡터를 출력했다. 근데, 단어의 형태가 일정한 룰을 따르고 있으니 철자 단위 정보, n-gram을 활용해서 더 좋은 단어 표현을 만들려고 했다.

   - n-gram을 length(n) 을 각기 달리하여 각각의 character n-gram 을 만든다 => "<", ">" 있는거,
   - n-gram 내부에 단어들이 존재할텐데, 이 단어들을 word2vec 으로 변환하고 이 벡터들의 총합을 구한다.
   - 그 벡터 값이 바로 단어의 벡터 표현.

4. LDA2vec :

5. Doc2vec : word2vec 을 이용해서 문장이나 문서 전체에 대한 vector 를 얻어보자는 아이디어에서 나온 embedding 기술. word2vec 의 원리와 비슷하지만 word2vec 에 사용되는 입력값에 문장ID를 추가해서 개선한다.

   - 모든 문장에 ID를 부여해서, 문장ID를 얻는다.

   - 이를 똑같이 벡터화 해서 input 값으로 넣는다. 그 문장의 모든 맥락 단어들을 전부 사용할 때까지 똑같은 문장id 를 입력값으로 넣어주면서, 문장 id 벡터를 수정한다.

     

   



### Weighting funcitions



우리는 세 개의 weighted function 들을 살펴볼 것. 바로 TF-IDF, IDF, SIF.



1. IDF : 

   - 전체 문서의 수 / i단어를 포함하는 문서의 수이다. 
   - 해당 단어가 문서에 드물게 나올수록 값이 커진다. 
   - IDF 값이 커질수록 해당 단어가 중요한 단어임을 의미한다.

2. TF: 

   - 이 문서에 해당 단어가 등장한 횟수 / 문서내의 전체 단어 수
   - 단어가 얼마나 자주 등장하는지를 드러내는 수치.

3. TF - IDF : 

   - 문서에 많이 나온 단어 + 전체 문서에서 얼마나 희귀하게 나왔는지 같이 고려하는 방법

   - tf * idf

     

4. SIF :



### Vector aggregation functions



1. The weighted sum :
2. center-based aggreagtion :
3. Delta rule :



### Deep neural network architectures



딥러닝은 text 마이닝에 많이 사용된다.



1. CNN:
   - Convolution 사용
     - input, output, hidden layer가 있다.
   - hidden layer 는 몇몇의 다른 layer들로 구성되어 있음
     - convolution layer : 출력 feature map 은 입력 feature map 에 대한 합성곱 연산에 의해서 얻어진다.
     - activation function  : ReLU 활성화 함수 사용.
     - pooling layer : 맥스 풀링, 평균 풀링 등등이 존재, 데이터의 차원을 줄여준다. 그 중에 맥스 풀링 사용.
     - fully connected layer : 최종적인 결과를 얻기 위한 Affine 층.
2. RNN:
   - 시퀀스 데이터에 사용하기 위해 만들어진 모델
   - RNN 계층은 그 계층으로부터의 입력(Xt)과 그 전 시각으로부터의 출력(Ht-1)을 받는다. 그리고 이 두 정보를 바탕으로 현 시각의 출력을(Ht) 계산한다. 출력값(Ht)은 위로 다음 계층으로도 나아가지만 시계열 방향으로도 나아간다.
   - 장기 의존 관계를 잘 학습할 수 없다.
     - 기울기 소실 문제, 기울기 폭발 문제
3. LSTM:
   - RNN 의 기울기 소실 문제를 보완하기 위해 만들어짐.
   - RNN 에 게이트를 추가
     - 정보를 잊을지, 추가할지 조절
     - input, output, forget
4. GRU:
   - RNN 기반
   - LSTM 과 달리 두 개의 게이트 존재.



### proposed CNN-LSTM architecture



제안한 모델은 TF-IDF weighted GloVe word embedding scheme with CNN-LSTM architecture.



1. CNN-LSTM

   - 구조 : weighted embedding layer - 

     1. weighted embedding layer
        - TF-IDF, GloVe, center-based aggregation 이 성능 제일 좋게 나와서 weighted embedding layer 에 이 방법 사용.
        - 미리 훈련한 word vector 사용
        - vector 의 길이는 300.

     2. dropout
        - overfitting 방지하기 위해서 사용

     3. convolution layer
        - 3중으로 쌓음
        - 필터 개수 80개

2. text matrix

   - 모든 input text 들은 word vector 들의 결합이 된다.
   - input text 는 vector 들의 시퀀스가 된다. V = [v1, v2, v3, ... v_n]
   - vector sequence는 matrix 가 된다.
     - matrix의 행과 열은 word embedding 차원의 수와 input text의 길이와 관련있다.

3. extract feature

   - 특징을 추출하기 위해서 합성곱 연산을 진행한다.

   - convolution layer 의 필터가 matrix 의 행방향으로 진행된다.

   - 필터의 넓이는 word embedding width 와 같다.

   - convolution layer out put 도출

     - 1번째 식은 내가 이해하기로는 필터가 아래로 이동하면서 계산하며 나오는 1x1 벡터 하나를 의미.
     - 2번째 식은 bias 를 그 1x1벡터에 더해준 추출된 특징,그니까 모든 연산을 다 하면 수직으로 벡터 하나가 다 도출, 그게 C_i, 이 C_i 가 여러 필터 종류 중 하나의 결과값.
     - ReLU 활성화 함수 사용

     

4. MAX POOLING

   - 3개의 Convolution 에서 도출된 값들을 max pooling

5. dense

   - feed forward 신경망
   - L2 정규화 방식
   - drop out 사용해서 overfitting 방지
   - binary cross entropy 손실 함수 사용
   - optimizer adam 사용



## Experiments and results



1. 평가 척도로 분류에서 사용되는 정확도 척도를 사용
2. 각각 다른 word embedding 방식과 weighted function 방법을 전통적인 딥러닝 방식에 사용해서 평가
3. 최적의 하이퍼 파라미터를 찾을 때 베이지안 최적화 사용.
4. word2vec, fastText embedding 방식으로 CBOW, SG 사용, SG 방식이 더 좋은 성능을 보임.(벡터 사이즈 300)
5. LDA2vec parameter 도 설정
6. 4.2 표는 test set 에 대한 성능(정확도)



### result



conventional neural language 모델과 CNN+LSTM 모델이 있음.

그리고 word embedding 방식에도 padding 을 준 word embedding 인지, 그리고 weight를 부여한 word embedding인지 구분해뒀음.



table1 result

1. conv 모델에서는 lstm 근데 cnn+lstm 이 훨씬 좋음 (weight 안준 순수 embedding 때)
2. unweighted embedding 기술 중에선 GloVe가 성능이 제일 좋았음.
3. sentence padding 이 들어간게 unweighted embedding 보다 더 성능이 좋았다. 근데 weighted 된거랑 비교하면 안좋다.



table2 result

1. weight function, vector aggregation function, architecture 고려됐다.
2. 결과를 요약한 그래프가 있다.
   - tf-idf 가 제일 우수
   - center based aggregation 이 그 다음 우수
   - 
3. ㅇ
4. ㅇ
5. 























