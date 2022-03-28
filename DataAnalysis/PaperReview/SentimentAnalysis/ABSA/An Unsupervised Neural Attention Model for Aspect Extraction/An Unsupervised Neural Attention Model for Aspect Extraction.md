# An Unsupervised Neural Attention Model for Aspect Extraction



Aspect 추출을 위한 비지도 뉴럴 어텐션 모델



## Abstract



Aspect 추출의 경우 aspect based sentiment analysis 에서 중요한 일.

현존하는 aspect 추출 모델의 경우 다양한 topic model(LSA, LDA) 등을 사용하고 있다.

이러한 방법은 매우 성공적이긴 하지만 coherent 일관되지 못하다.

이 논문에서는 일관된 aspects 들의 추출에 대한 neural 접급을 제안한다.



Neural word embedding(단어 vector화를 통해서) 의 분포를 이용하면서 일관성을 향상시킨다.

자주적으로 산출된 words들을 가정하는 topic models 들과 달리, word embedding 모델들은 embedding space 에서 유사한 contexts 에서 나타나는 단어들이 서로 가깝게 위치하게 만든다.

게다가, 논문의 저자들은 학습을 하는 동안에 덜 관계있는 단어들을 덜 강조하기 위해서 attention 모델을 사용한다. 그리고 aspect의 일관성을 더욱 개선한다.





## Introduction



- 우리가 sentiment analysis based on aspect 를 할 때 가장 중요한 것 중 하나는 분석할 aspect 를 추출하는 것이다.

  그 작업을 표현된 opinions (review 같은 것) 에서 entity aspect 를 추출하는 것이다.

  예를 들어서 문장 "The beef was tender and melted in my mouth" 이 있다고 하자.

  그럼 여기서 aspect term 은 beef 이다.

  두 가지 sub-tasks들이 aspects extraction 에 사용되는데,



1. 모든 aspects term 들을 review corpus 에서 추출한다.

2. aspects term 들을 군집화해서 비슷한 의미를 가지고 있는 것끼리 카테고리화하는데, **각  카테고리가 단일 aspect 를 나타내는 범주로 분류한다.**

   > 하나의 군집은 여러 개의 aspect term 들로 이루어져 있지만, 군집 하나는 단일 aspect 를 나타내는 걸로 이해했다.
   >
   > ex) cluster  'beef','pork', 'pasta' , 'tomato' 는 food aspect 라고 할 수 있다.



- 이전의 aspect 추출 작업들은 세 개의 접근 방식으로 분류될 수 있다.

  - Rule based
    - rule based 방식은 extracted 된 aspect term 들을 카테고리화 하지 않는다.
  - supervised
    - supervised 방식은 data anntotation 을 요구한다.
    - supervised 방식은 domain 적응 문제를 겪는다.
  - unsupervised
    - 비지도 방법들은 labeled 되지 않은 데이터를 사용할 수 있다.

- LDA

  - 최근에 비지도 extrack 방식으로 LDA 가 주목받고 있다. 

  - LDA는 corpus 를 topics(aspects) 들의 혼합체로 간주한다.

  - 그리고 topics들을 단어들의 혼합체로 간주한다.

  - 논문의 저자들은 LDA 에 의해서 발견된 aspects 들의 혼합체들이 corpus 를 꽤 잘 설명하는 반면에, 개별 aspects 들은 꽤 낮은 성능을 보임을 발견했다.

    > 나는 이 말을 topics 들(aspects) 이 corpus 는 잘 설명하는 반면에 개별 topic(aspect) 자체만을 살펴보면, 그것을 구성하고 있는 단어 혹은 개념들이 그 topic or aspect 를 잘 설명하고 있지 못하다고 이해했다. 

  - aspects 들은 종종 관련이 전혀 없거나 느슨하게 관련된 개념으로 구성되어져 있다.

  - 이러한 문제는 두 가지 reason 이 존재한다.

    - 전통적인 LDA 모델들은 topic 의 일관성을 유지할 수 있는 가장 중요한 자원들인 단어 동시 발생 행렬을 직접적으로 인코딩하지 않는다.

    - 각 단어가 **독립적**으로 생성된다고 가정하고, 문서 수준에서 단어 속성을 모델링하여 이러한 패턴을 암묵적으로 포착한다. (LDA 가 n 번째 단어를 생성하는 과정을 보면 왜 독립적인지 이해가 가능하다.)

    - LDA 모델은 기본적으로 document 의 topic 의 분포를 가정하는데, review document 들은 짧은 경향이 있는데, 이 때문에 topic의 분포 추정은 더 어렵다.

      

      

      

- novel neural approach

  - LDA 모델의 약점을 다루는 새로운 neural approach 를 제안한다.

  - 논문은 neural word embedding 을 먼저 시작한다.이 임베딩은 단어들을 mapping 하는데, 보통 embedding space 에서 같은 맥락에서 주변 지점들에서 동시 발생하는 단어들을 매핑한다.

  - 논문 저자들은 문장 내에 존재하는 word embeddings 들을 attention mechanism 을 이용해서 걸러낸다.

  - > 아마 attention mechanism 으로 aspect 와 관계가 깊은 word embedding 들만 걸러낸다는 말이 아닐까?

  - 그리고 걸러낸 word embedding 들을 aspect embedding을 조립하기 위해 사용한다.

  - > 앞서 aspect 들을 모두 추출하고, 군집화한 이후에, 그 군집 하나당 single aspect 를 나타낸다고 이야기 했는데, 그 이야기가 아닐까?

  - aspect embedding의 training 과정은 autoencoder 와 유사하다. 

    차원 축소를 사용하는데, 임베딩된 문장(sentence)과 재구조화된 각각의 문장들 중에서 공통된 요소를 추출하기 위해 사용한다.(aspect embedding들의 선형 결합을 이용해서 )

    > LSA 를 살펴보면 임베딩된 문장의 차원을 축소하면 숨겨져 있던 중요한 정보들이 나옴을 살펴봤는데, 그런 이야기를 더 발전시킨 이야기가 아닌가 싶다.

  - 사용하는 attention mechanism 은 어떠한 aspect 에도 포함되지 않은 단어들을 덜 강조한다. 그리고 이는 모델이 aspect word 에 초점을 두게끔 만든다.

  - 논문의 저자들은 위에서 설명한 novel neural approach model 을

  - > Attention-based Aspect Extraction (ABAE) 라고 칭한다.!
    >
    > LG 프로젝트 코드가 이 코드인가??싶다.



LDA based model 과 대조적으로, 우리가 제안한 방법은 명시적으로 단어 발생 통계를 word embeddings 에 인코드한다.

