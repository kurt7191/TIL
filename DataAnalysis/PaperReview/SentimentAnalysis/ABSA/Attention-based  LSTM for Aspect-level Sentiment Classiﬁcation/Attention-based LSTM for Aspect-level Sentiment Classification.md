# Attention-based LSTM for Aspect-level Sentiment Classification



## Abstract



논문의 저자들은 sentence 의 감성 극단이 오직 sentence의 content(내용) 에 의해서 결정되는 것 뿐만 아니라 관계하고 있는 aspect에 의해서도 결정된다고 주장한다.

예를 들어서 *The appetizers are ok, but the service is slow.* 가 있으면,

aspect "taste" 에 집중해서 sentence의 감성을 파악하면 긍정이 나오는 반면에 "service" aspect 에 집중을 해서 sentence 의 감성을 파악하면 부정이 나온다.

따라서 aspect 와 content 의 내용 사이의 연결을 연구해보는건 보람이 있다.

논문의 저자들은 aspect 기반 감성 분류를 위한 Attention-based Long Short-Term Memory Network 를 제안한다.



어텐션 메커니즘은 다른 aspects(aspect 별로)들이 input 으로 받아들여질때, 문장의 다른 부분들에 집중을 한다.

논문에서 제안한 모델의 성능을 SemEval2014 데이터 셋을 이용해서 진행한다. 그리고 논문에서 제안한 모델이 aspect 단위의 감성 분류 작업에서 높은 성능을 보임을 보여준다.



<hr>

## Introduction



논문에서는 sentence 의 감성 극성이 content와 aspect 둘 다에 꽤 높게 관련 있음을 발견했다. (위의 예시를 통해서도 확인할 수 있다.)

예를 들어서, "Staff are not the friendly, but the taste covers all" 문장은 "service" aspect 에 초점을 두어서 감성 분석을 하면 부정이 나오지만 만일 "food" aspect 에 중점을 두어서 감성 분석을 하면 긍정이 나올 것이다.

즉, 다른 aspect들이 고려가 되어 sentence에 대한 감성을 분류하면, 감성 극성은 반대의 결과가 도출될 수 있다.



neural 네트워크 작업은 nlp 에서 많은 발전을 이루었는데, sentiment analysis 를 다루기에는 아직 성숙하지 않은면이 있다.

몇몇의 작업들, target 의존 감성 분류는 target 정보를 고려함으로써 이익을 얻을 수 있다.

> ex) Target Dependent LSTM(TD-LSTM)
>
> Target- Connection LSTM(TC-LSTM)



이런 모델들은 target 만을 고려하고 aspect level 의 분류에 매우 중요하다고 입증된 aspect에 대해서는 고려하지 않는다.



논문의 저자들은 **특정 aspect에 대응하여 sentence의 중요한 부분**에 참여하기 위해서 attention 메커니즘을 사용한다. (attention 메커니즘은 관련있는 중요한 word 에 가중치를 크게 준다.)

논문은 **aspect 가 주어진 sentence의 중요 부분에 초점**을 둘 수 있는 aspect-to-sentence attention 메커니즘을 설계한다.

논문은 asepct level 의 감성 분류에서 감성 극성과 aspect의 잠재적인 상관관계를 연구한다.

> 주어진 aspect 에 대한 중요한 정보를 파악하기 위해서, attntion based LSTM 을 설계 (restaurants, laptop data 사용)





##### 논문의 Contribution

- attention-based Long Short Term 을 제안하고, 이는 효율적인 성능을 보였다.
- attention 동안의 aspect 정보를 고려한 두 가지 방법을 제안한다.
  - attention weights 들을 계산하기 위해서 sentence hidden representation 에 aspect vector를 합친다.
  - input word vector 에 aspect vector 를 합친다.
- 실험 결과는 논문의 접근 방식이 이전의 방식에 비해서 더 높은 성능을 보였음을 보여준다. 추가적으로 attention 메커니즘이 aspect level sentiment analysis 에 잘 적용됨을 보여준다.



## Related Work(literature?)



### Sentiment Classification at Aspect-level



현재의 접근의 주요 작업들은 언급된 entities들 또는 aspects들을 고려하지 않고 전체 문장의 감성 극성을 발견하는 시도들이다.

이때 lexicon 과 svm 모델을 사용했다. => 근데 비용이 많이 든다.





### Sentiment Classification with Neural Networks



word의 분산 표현에 대해서 얻을 수 있는 간단하고 효율적인 방법이 제안됐기 때문에 뉴럴 네트워크는 감성 분석에서 실질적으로 진전이 있었다.

지금까지 rnn 기반 모델들이 sentiment analysis 에 많이 사용됐다.

하지만 자료가 많이 없는 언어들의 경우에는 syntax parsing errors 들이 발생한다.



LSTM(TD-LSTM, TC-LSTM) 경우에 target dependent sentiment classification(target label 이 있는 감성 분류) 에서 높은 성능을 자랑했다. 



TC-LSTM 같은 경우 target 구에 포함되어 있는 word vector 들을 평균 냄으로써 target vector 를 구했다.

하지만 단순히 평균을 내는 것으로는 target 구의 의미론적 표현을 충분히 나타낼 수 없다.

>  target vector에 대해서 평균을 내는 작업은 최적 이하의 성능을 보였다.



위의 방법들의 강한 효율성에도 불구하고, 세분화된 aspect level 에서의 다른 감성 극성을 구별하는 것은 여전히 어렵다. 그러므로, 논문 저자들은 aspect 정보들을 완전히 사용할 수 있는 강한 뉴럴 네트워크를 디자인하려고 한다.



> LSTM 이 감성 분류에서 많이 사용되고 높은 효율을 보여왔다.



### Attention-based LSTM with Aspect Embedding



#### Long Short -term Memory(LSTM)



RNN 은 전통적인 피드포워드 뉴럴 네트워크 중 하나다. 하지만 전통적인 RNN 의 경우 기울기 소실 문제와 기울기 폭발 문제가 발생하기 때문에 사용하기 까다롭다.

 이를 극복하기 위해서 LSTM 모델이 탄생했다.

LSTM 모델에는 3개의 gates 들과 cell memory state 가 존재한다.

Cell momory state 는 c경로라고 불린다. c경로는 다음 계층으로 그 값을 넘기지 않고 LSTM 계층 내에서만 값을 주고 받는다. 반면에 h(hidden state) 는 다음 계층으로도 그 값을 보내고 자기 자신으로도 값을 보낸다.



> Ct = 현재 시각 t까지의 모든 기억들이 담겨있다.

![스크린샷 2022-03-24 오후 12.56.14](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 12.56.14.png)



Ct 까지의 기억을 바탕으로 현재의 h(hidden state) 를 도출한다. 이때 도출한 h 값은 기억셀 Ct의 모든 원소에 tanh 함수를 적용한 것과 같다.

이 사실을 토대로 Ct 와 h에 대해서 유추해보면, Ct의 각 원소에 tanh 함수를 적용한 값이 Ht 가 되기 때문에 둘은 원소 수가 동일하다.

다음 시각의 값들을 도출하기 위해서 Ct, ht 가 입력값으로 들어가서 어떤 계산을 거치게 되고 Ct+1 이 출력이 된다.

그리고 또 다시 Ct+1 의 각 원소 값에 tanh 을 적용해서 ht+1 을 출력한다.



> **여기서 등장하는 중요한 개념이 `게이트`** 
>
> 게이트란 우리말로 문을 의미한다. 문을 열거나 닫거나 하여 데이터의 흐름을 제어한다.
>
> 뿐만 아니라 게이트는 흑백 원리(0 or 1)로만 작용하는 게 아니라 데이터를 어느 정도만 흐르게 할지 결정할 수 있다.
>
> 즉, 게이트를 조금만 열어두거나, 많이 열어두거나 하여 다음 단계로 흘러갈 데이터의 양을 조절할 수 있다.
>
> 
>
> 게이트의 열림 상태는 0 ~ 1사이의 실수로 나타낸다. 만일 1이면 완전 개방하여 100%의 데이터를 흘러가게 한 것이고 0.2이면 20 %의 데이터만 흘러가게 한다.





##### output gate

LSTM 에는 **output 게이트**가 존재한다.

LSTM 의 은닉상태 ht는 메모리셀 Ct의 각각의 원소에 tanh 함수를 적용한 것과 같다.

즉, tanh(Ct) 가 ht 였다.

**tanh(Ct) 에 게이트를 적용**하는 걸 살펴보자. 이는 tanh(Ct) 의 각 원소에 대해서 그 원소가 다음 은닉 상태 ht에 얼마나 중요한가를 조정한다.

이 게이트는 다음 은닉 상태의 출력을 담당하는 게이트므로 **output 게이트**라고 부른다.



게이트 식은 다음과 같다.



`o = Sigmoid(Xt * Wx(o) + Ht-1 * Wh(o) + b(o))`



> 여기서 o는 Output 게이트를 의미하는 차원에서의 o이다. 식을 해석하면 t시각의 입력층에 가중치 매개변수 행렬을 곱해주고 그 이전의 은닉상태 값에 가중치 매개변수 행렬 값을 곱해준 값들을 더한 후 바이어스를 더하고 그 값에 시그모이드 함수를 적용한 값이 게이트 값이다.
>



이렇게 구한 게이트 행렬 값 o를 tanh(Ct) 행렬과 곱해주어 Ht 값을 구한다.

이때 게이트 값과의 곱이란 `아다마르 곱(Hadamard product)` 라고도 한다. 이 곱은 행렬의 각 원소별 곱을 의미한다.



> tanh 함수의 출력값은 -1.0 ~ 1.0 사이다. 이 값은 그 안에 인코딩된 정보의 강약 정도를 나타낸다. 그럼 본래 tanh(Ct) 를 하게 되면 각각의 t 시각의 정보의 강약 정도가 나타난다.
>
> 한편 sigmoid 함수는 값은 0.0 ~ 1.0 을 지니며 데이터를 얼마만큼 통과시킬지를 정하는 비율을 뜻한다. 따라서 주로 게이트에는 시그모이드 함수가, 실질적인 정보를 지니는 데이터는 tanh 함수가 활성화 함수로 적용된다.
>
> 실질적인 정보 지닌 데이터 : tanh, 게이트 : sigmoid



##### forget gate

우리가 다음에 해야 할 일은 무엇을 잊을까 결정하는 일이다.

망각을 담당하는 게이트를 **forget gate** 라고 부른다.

식은 다음과 같다.

`f = Sigmoid(Xt * Wx(f) + Ht-1 * Wh(f) + b(f))`

f값을 구하게 되면 그 이전의 기억 셀 Ct-1과 f를 아다마르 곱, 원소별 곱을 진행하여 Ct 값을 구한다.



##### 새로운 기억 셀

(이전의 기억 셀과 더하기 과정을 거친다.)

forget 게이트를 이용해서 기억 셀에세 잊는 것 밖에 하지 못한다.

새로운 정보를 잊었으면 추가해야 하는데, 새로운 정보를 추가하는 작업은 tanh 노드를 이용한다.



> 이 tanh 노드는 게이트가 아니다. 새로운 정보를 기억 셀에 추가하는 것이 목표다. 따라서 simoid 함수가 아니라 tanh 함수가 사용된다. (simoid 함수는 데이터를 얼마만큼 통과시킬지에 관한 비율 수치)
>



tanh 노드에서 수행하는 계산식은 다음과 같다.

`g = tanh(Xt * Wx(g) + Ht-1 * Wh(g) + b(g))`

tanh 노드에서는 t시각의 입력값과 그 이전의 은닉 상태를 받아서 매개변수값과 바이어스를 고려해 계산을 수행한다. 이 결과값인 g는 **f게이트를 거친 Ct-1 과 "더하기" 과정을 거쳐서 새로운 기억을 추가**한다.



##### input 게이트



마지막으로 input 게이트가 존재한다.

input 게이트는 g게이트에 들어온 새로운 정보가 얼마나 가치가 큰지를 판단한다.

즉, 새로 추가되는 정보를 무비판적으로 받아들이는 게 아니라 적절히 취사선택하는 게 input 게이트의 역할이다.

`i = Sigmoid(Xt * Wx(i) + Ht-1 * Wh(i) + b(i))`



하단은 위에서 설명한 게이트 수식들을 모안둔 것이다.



![스크린샷 2022-03-24 오후 1.01.35](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 1.01.35.png)



![fig 6-18](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/fig 6-18.png)



#### LSTM with Aspect Embedding



Aspect 정보는 aspect 가 주어진 하나의 문장의 감성 극성을 분류할 때 중요하다.

우리는 다른 apsect 들이 고려된다면 반대의 극성들을 얻게될 것이다.

(aspect 에 따라서 감성 극성이 달라진다.)



논문의 저자들은 aspect 정보를 최대한 잘 사용하기 위해선, 각각의 aspect 의 embedding vecotr 를 학습하는걸 제안한다.



#### Attention based LSTM(AT-LSTM)



전통적인 LSTM 모델은 aspect level 감성 분석을 위해 어떤 부분이 중요한지 발견하지 못한다.

이 문제를 해결하기 위해서, 논문의 저자들은 주어진 aspect 에 대응하는 중요한 부분을 포착할 수 있는 attention 메커니즘을 설계하는걸 제안한다.



밑의 그림은 attention 기반의 LSTM (AT-LSTM) 의 아키텍처를 보여준다.



![스크린샷 2022-03-24 오후 2.07.42](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 2.07.42.png)



그림상에 보이는 H는 hidden state의 벡터들의 집한인 matrix로 만든다. (이 h 들은 LSTM 모델이 만든 히든 스테이트다.)

H ∈ R^d*N => d는 dimension 을 의미하고 N은 주어진 sentence의 length 즉, 단어의 개수를 의미한다.

그리고 v_a 는 aspect 임베딩을 나타내고 e_N은 1s의 벡터를 의미한다. (이게 그림상에도 어디 있는 거지??)



##### attention mechanism 은 attention weight(어텐션 가중치) 를 생성하고 이를 이용해서 representation r을 생성한다.

a는 attention weight 들로 구성된 vector 이고, r은 주어진 aspect가 있는 sentence의 가중치된 표현이다.



어텐션 메커니즘은 다른 aspects들이 고려될 때, 모델이 문장의 가장 중요한 부분을 포착하게끔 해준다.

h* 은 input aspect 가 주어진 sentence의 특징 표현으로 간주된다. (sentence representation 최종)

논문 저자들은 linear layer 를 h* vector를 e vector 로 바꾸기 위해 추가한다. 이 e vector 는 class number |c| 의 개수와 동일한 길이를 가지는 vector 이다.

그리고 softmax layer 를 조건 확률 분포를 만들기 위해 e 뒤에 추가한다.



#### Attention-based LSTM with Aspect Embedding(ATAE-LSTM)



AE-LSTM 에서 aspect 정보를 사용하는 방법은 aspect embedding을 attention weight 를 계산하는 역할로 사용하는 것이다.

> aspect embedding 으로 attention weight 를 계산한다.



논문의 저자들은 aspect 정보를 활용하기 위해서 input aspect embedding을 각각의 word input vector 에 추가한다.



![스크린샷 2022-03-24 오후 3.47.34](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 3.47.34.png)



이 경우 output hidden representation (h1, h2, h3, .....hn) 은 input aspect 으로부터의 정보를 가질 수 있다. 

이를 통해서 words들과 input aspect 간의 의존선을 가지는 모델을 만들 수 있다.



#### Model Training



모델은 오차역전파를 통해서 학습될 수 있다.

손실 함수는 cross-entropy loss 함수를 사용한다.

y는 문장의 target(감정) 분포로 가정하고, y^는 예측된 감성 분포로 가정한다.

학습의 목표는 모든 sentence의 y와 y^간의 cross-entropy-loss를 최소화하는 것이다



사용되는 parameter 들은 LSTM 에서 사용했던 parameter 들과 유사하게 게이트에 관련된 파라미터들이 사용된다. 게다가 word embedding 들도 파라미터 사용된다.

(W_i, W_f, W_o, W_c)

주목할만한 점은, LSTM 의 게이트들의 가중치 파라미터들은 제각각 다른 모델들에 따라서 dimension 이 달라진다.

만일 aspect embedding 이 LSTM의 cell unit의 input 에 추가된다면, 게이트들의 dimension 은 그에 따라 확대된다.



논문은 각 모델들의 parameter 들을 아래와 같은 리스트로 정리했다.



- AT-LSTM
  - Aspect embedding 은 parameter set 에 자연스럽게 추가된다.
  - Wh, Wv, Wp, Wx, w 들이 attnetion 의 파라미터다.
  - 추가적인 파라미터들은 aA, WH, Wv, Wp, Wx, w 다.
- AE-LSTM
  - parameter로 aspect embedding A 를 추가한다.
  - 게이트 파라미터들도 확장된다.
- ATAE-LSTM
  - aspect embedding 의 concatenation과 함께 게이트 parameter 들의 dimension 은 확장된다.
  - word embedding 과 aspect embedding 들은 학습하는 동안에 최적화된다.



논문은 optimizer 방식으로 AdaGrad를 사용한다.



### Experiment



논문은 위에서 제안한 모델들의 aspect level 의 sentiment analysis 의 성능을 평가한다.

Glove 방식을 이용해서 word embedding 을 시행했다.

(vector 의 dimension 은 300)

attention weight들은 sentence의 길이와 동일하다.



#### Dataset

우리는 SemEval 2014 Task 의 데이터 셋을 사용한다.

semEval 데이터 셋은 aspects 들의 list들을 포함하고 각각에 aspect에 해당하는 문장의 감성 극성을 가지고 있다.



#### Task Definition



이미 결정된 aspect set이 주어지면, 이 task  는 각각의 aspect 의 감성 극성을 결정한다.

예를 들어서, "The restaurant was too expensive" 문장이 주어지면, 이 문장의 aspect 로 부정적인 감성 극성을 가지고 있는 price 가 존재한다.

이 문장의 aspect set 은 food, price, service, ambience, anecdotes, miscellaneous 이다.

semeval 데이터에는 aspect 특징된 감성 분석을 가진 데이터는 restaurant 데이터 뿐이다.



모델의 결과는 아래와 같다.



![스크린샷 2022-03-24 오후 4.10.12](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 4.10.12.png)



##### Aspect-Term-level Classification



sentence 내에 aspect term 이 주어지면 이 작업은 어떤 aspect term 의 감성 극성이 긍정인지 부정인지 혹은 중립인지 결정한다.

aspect term 의 각각의 발생에 감성 극성과 위치가 나타나 있다 (restaurant, laptop of semeval)

예를 들어서어서 aspect "fajitas" 는 "i loved their fajitas" 문장 내에서 negative 감성 극성을 가진다.



#### Comparision with baseline methods



모델들의 성능을 비교하는 part

- LSTM
  - standard 한 LSTM 은 문장내에서 어떠한 aspect 의 정보들도 포착할 수 없다.
  - aspect 의 정보들을 포착할 수 없기 때문에 aspect 가 다르게 주어져도 똑같은 감성 극성을 내뱉는다.
- TD-LSTM
  - TD-LSTM 은 aspect 를 target 으로 다룸으로써 sentiment classifier 의 성능을 높였다.
  - Td lstm 은 attention 메커니즘을 사용하지 않기 때문에 어떤 단어들이 주어진 aspect 에 대해서 중요한 단어들인지 알 수 없다.
- TC-LSTM
  - traget(sentiment 가 아니라 aspect를 의미하는 듯) 을 sentence의 representation 에 결합시키면서 TD-LSTM 을 확장시킨 모델.
  - TC-LSTM 은 TD-LSTM 과 LSTM 의 성능보다 더 낮다는 점에 유의해야 한다.
  - TC-LSTM 은 단어 벡터로부터 얻어진 target representation을 LSTM cell unit의 input에 추가한다. (lstm 의 input 에 target representation 을 추가)



논문의 저자들은 aspect 를 다른 vector space 로 embedding 한다.

aspect 의 embedding vector 는 training 과정에서 잘 학습될 수 있다.

##### Ate-lstm 은 word vector 와 aspect embedding 벡터의 부적합의 결점을 설명하는 것뿐만 아니라, 주어진 aspect에 대한 가장 중요한 정보를 포착할 수 있다.



또한 ATAE-LSTM 은 다른 aspects 들이 주어졌을 때,  문장의 다른 부분과 중요성을 포착할 수 있다.



#### Qualitative Analysis



aspect 가 주어진 문장의 감성 극성을 어떤 단어들이 결정하는지 분석하는건 계몽적인 일이다.

(attention 을 통해서 파악)

attention 메커니즘은 attention weight 들을 통해서 attention 모델이 어떤 단어에 주목했는지 시각화 할 수 있다.



![스크린샷 2022-03-24 오후 4.57.52](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/SentimentAnalysis/ABSA/Attention-based  LSTM for Aspect-level Sentiment Classiﬁcation/이미지/스크린샷 2022-03-24 오후 4.57.52.png)



색깔이 진한건 attention vector 의 값의 크기를 나타낸다. (더 짙어질수록 더 중요하다.)




#### Case Study



LSTM 으로는 잘 작동하지 않았던 감성 분류 작업을 논문에서 제안한 모델로 구현하여 성능 비교를 해보려고 한다.

문장 "The appetizers are ok, but the service is slow" 라는 문장이 있을 때, aspect food 와 service 가 존재한다.

논문에서 제안한 모델은 단순히 이 문장의 감성 극성을 판별하는 게 아니라 aspect 에 따른 이 문장의 감성 극성을 판단한다.



EX)

“*I highly recommend it for not just its superb cuisine, but also for its friendly owners and staff.*”

여기에는 부정적인 단어 not 이 있는데 이 문장의 감성은 부정이 아니다. 논문에서 제안한 모델은 not 단어 자체에 영향을 받지 않고 올바른 감성 극성을 판단할 수 있다.





EX)

“*The service, however, is a peg or two below the quality of food (horri- ble bartenders), and the clientele, for the most part, are rowdy, loud-mouthed commuters (this could ex- plain the bad attitudes from the staff) getting loaded for an AC/DC concert or a Knicks game.*”,



이 문장은 길고 구조가 복잡하다.

기존 parser 는 힘들게 올바른 parssing tree 를 얻을 수 있을 것이다. 따라서 tree-based 뉴럴 네트워크 모델들은 감성 극성을 올바르게 판단하기에 매우 어렵다.

반면에 논문에서 제안한 attention 기반의 LSTM 은 attention 메커니즘과 aspect embedding 의 도움으로 이 문장들에 잘 적용될 수 있다.



### Conclusion and Future Work



지금까지 논문에서 제안한 모델의 중요 포인트는 aspect embedding 을 학습하고 aspect를 attention weights를 계산하는 과정에 참여하시키는 것이다.

그래서 다른 aspect 들이 문장에 주어졌을 때 올바른 sentence 의 감성을 분류할 수 있게 된다.

우리가 제안한 모델들 중에서 AE-LSTM 과 ATAE-LSTM 이 기존의 모델들보다 더 우수한 성능을 얻었다.

##### 지금까지 작업 이후의 작업으로, attention 메커니즘과 함께 두 가지 이상의 aspect 를 모델링하는 것이다. (우리가 연구할 것 혹은 이미 나왔겠지?) => sentence 내에 aspect food 가 등장하면 food 에 집중해서 sentence의 감성을 판별했는데, 다음 연구로는 food와 service aspect 를 고려해서 sentence 의 감성을 분류하는 작업을 연구할 수 있을 것으로 논문은 이야기하고 있다.





<hr>




































