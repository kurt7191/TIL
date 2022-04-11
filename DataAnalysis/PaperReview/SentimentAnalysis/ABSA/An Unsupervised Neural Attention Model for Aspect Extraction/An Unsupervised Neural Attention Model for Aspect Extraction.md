# An Unsupervised Neural Attention Model for Aspect Extraction



Aspect 추출을 위한 비지도 뉴럴 어텐션 모델



## Abstract



Aspect 추출의 경우 aspect based sentiment analysis 에서 중요한 일.

현존하는 aspect 추출 모델의 경우 다양한 topic model(LSA, LDA) 등을 사용하고 있다.

이러한 방법은 매우 성공적이긴 하지만 coherent, 일관되지 못하다.

이 논문에서는 일관된 aspects 들의 추출에 대한 neural 접근을 제안한다.



Neural word embedding(단어 vector화를 통해서) 의 분포를 이용하면서 일관성을 향상시킨다.

자주적으로 산출된 words들을 가정하는 topic models 들과 달리, word embedding 모델들은 embedding space 에서 유사한 contexts 에서 나타나는 단어들이 서로 가깝게 위치하게 만든다.

게다가, 논문의 저자들은 학습을 하는 동안에 덜 관계있는 단어들을 덜 강조하기 위해서 attention 모델을 사용한다. 그리고 aspect의 일관성을 더욱 개선한다.



> keyword : 
>
> 일관성있는 aspect 추출 시도
>
> word embedding 사용
>
> attention 모델로 덜 중요한 단어들을 배제



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



<hr>



## Related Work



- Aspect 를 추출하는 과정은 최초로 Rule 기반이었다.

  - HU 와 LIU 는 빈번하게 등장하는 명사들과 명사구를 찾는 것을 통해 상품들의 특징들을 추출하기를 제안했다.

  - 그들은 또한 WordNet을 통해 opinion seed words 의 동의어 반의어를 찾음으로써 opinion term 들을 추출했다.

  - 이를 따라서(규칙 기반), 상품의 aspects들을 추출하기 위해서 수많은 방법들이 빈번한 item mining과 의존성 정보에 기반해서 제안되어왔다.

  - 이러한 방법들은 사전 지정 규칙들에 꽤 의존하고 있는데, 이 사전 지정 규칙들은 aspect terms들이 명사들의 작은 그룹으로 제한되어져 있을 때 잘 작동한다.

  

- 지도 학습 접근법은 일반적으로 표준 시퀀스 레이블링 문제로 aspect extraction을 모델링한다.

  - rule based 기반은 추출된 aspect term 들을 충분히 범주화 하는데 세련되지 못하다.
  - 반면에 지도학습 방법은 많은 양의 labeling 데이터를 요하게 된다.

- 비지도학습 방식으로는 label data 에 의존하는걸 피하기 위해서 topic model 이 제안되어져 왔다.

  - topic model 의 output 은 각 aspect 에 대한 단어 분산 표현이거나 랭킹이다.
  - 최근의 작업들은 LDA 의 연장선이라고 할 수 있다.
  - 2015년의 wang et al 은 주어진 문장의 aspect와 관련 sentiment를 동시에 추출하여 aspect 와 sentiment를 RBM에서 별도의 숨겨진 변수로 취급하는 제한된 볼츠만 기계(RBM) 기반 모델을 제안했다.
  - 동시 발생 단어쌍을 산출하는 biterm topic model(BTM) 이 제안됐다.
    - 논문에서 여러 업무에 걸쳐서 ABAE와 BTM 을 비교할 예정

- Attention 메커니즘

  - 어텐션 메커니즘은 모든 정보를 사용하는 게 아니라, task 에 가장 관련이 있는 정보에 집중하여 작업을 수행한다.
  - 논문에서는 attention mechanism 을 적용
  - asepct extraction task의 비지도 학습 세팅에서, 논문에서 제안한 어텐션 기반의 실험 결과는 효과적이다.





## Model Description



ABAE 모델을 이 section 에서 제안한다.

궁극적인 목적은 embedding space에서 가장 가까운 단어들을 관찰함으로써 해석될 수 있는 각각의 aspect의 집합을 학습하는 것이다.



- vocabulary 안에 있는 단어 w를 feature vector e_W에 연관짓는다.

- 우리는 word embedding을 **feature vector**를 위해서 사용한다. 왜냐하면 word embedding 들은 종종 문맥안에서 동시 발생하는 단어들을 embedding space 내에서 가깝게 위치한 point에 매핑하기 위해서 설계되어져 있기 때문이다.

- word embedding matrix E(V x d) 의 행에 일치하는 단어들과 feature vectors 들은 연관되어있다. (vocabulary size)

- d

- d

- d

- d

- d

- d

- 

  









