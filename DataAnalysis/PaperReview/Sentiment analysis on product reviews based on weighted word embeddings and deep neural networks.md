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



각각의 word embedding 방식과 각각의 weighted function 에 따른 예측 성능 전통적인 딥러닝 방식과 함께 평가한다.

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

3. fastText :

4. LDA2vec :

5. Doc2vec

   



### Weighting funcitions



1. idf : 
2. tf :
3. TF - IDF :
4. SIF :



### Vector aggregation functions



1. The weighted sum :
2. center-based aggreagtion :
3. Delta rule :



















