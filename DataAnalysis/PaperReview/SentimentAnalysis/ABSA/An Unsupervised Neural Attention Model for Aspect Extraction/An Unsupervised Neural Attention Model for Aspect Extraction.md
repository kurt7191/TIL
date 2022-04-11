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

  표현된 opinions (review 같은 것) 에서 entity aspect 를 추출하는 것이다.

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

  - HU 와 LIU(사람임) 는 빈번하게 등장하는 명사들과 명사구를 찾는 것을 통해 상품들의 특징들을 추출하기를 제안했다.

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

##### 궁극적인 목적은 embedding space에서 가장 가까운 단어들을 관찰함으로써 해석될 수 있는 각각의 aspect의 집합을 학습하는 것이다. (위에서 살펴봤듯이 aspect term 들의 군집 개체 하나를 하나의 aspect 로 간주한다.)



- vocabulary 안에 있는 단어 w를 feature vector e_W에 연관짓는다.
- 우리는 word embedding을 **feature vector**를 위해서 사용한다. 왜냐하면 word embedding 들은 종종 문맥안에서 동시 발생하는 단어들을 embedding space 내에서 가깝게 위치한 point에 매핑하기 위해서 설계되어져 있기 때문이다.(word2vec)
- word embedding matrix E(V x d) 의 행에 일치하는 단어들과 feature vectors 들은 연관되어있다. (V는 vocabulary size를 의미한다.)
- 다른 words 들과 똑같은 embedding space(차원 동일) 를 공유하고 있는 aspects 들의 embedding 을 얻는게 목적.
- aspect embedding matrix T를 만들 수 있는데 이는 k x d의 shape 을 가진다. k는 정의된 aspect 의 개수를 의미하고, d는 차원을 의미한다. 당연스럽게 본래 vocabulary 에서 aspect 들을 추출하는 것이기 때문에 k는 V보다 적다.(k < V)
- aspect embedding들은 aspect word들에 근사하는데 사용되어진다. 여기서 asepct word 들은 attention mechanism 에 의해서 필터링된다.

- ABAE 에 대한 각각의 input sample 은 review 문장에 있는 단어들에 대한 index들의 리스트이다. (정확하게 무슨 말이지?) => input 이 주어지면 두 단계들이 수행된다.
  - attention mechanism을 통해서 aspect words들이 아닌 단어들에 대해 weight를 낮게 주면서 non_aspect 단어들을 걸러낸다. 그리고 weighted 된 word embeddings 들을 통해서 문장 임베딩 Z_s를 구조화한다. (sentence embeiddng인 Z_s를 만들었는데, attention mechanism 을 통해서 덜 중요한 단어들에 대해서 낮은 weigh를 준 sentence embedding임 ) => 문장 임베딩 Z_s 생성
  - T matrix(aspect embedding들의 matrix) 로부터의 aspect embeddings의 선형 결합으로써 문장(sentence) embedding 을 다시 구조화(re-construct) 하는 것을 시도한다.
    - 이 re-constructions(r_s)과 차원 축소는 (ABAE가 첫번째로 필터링된 문장들의 embedding인 Z_s를 최소한의 축소를 수행한 re-construct된 r_s embedding으로 전환하는걸 목표로 하는) k 임베드 space 안에서 aspect 단어들의 최대한의 정보를 보존한다. (Z_s -> r_s 로 re-construct 하는데, 이 작업을 통해 aspect 단어들의 최대한의 정보를 보존한다는 것 같음)
      - 더 자세한 과정은 논문의 밑의 세부적인 설명을 들어야 하는 듯.







### Sentence Embedding with Attention Mechanism



- ABAE 모델은 첫 번째 step으로 input sentence (s) 에 대해서 vector 표현 z_s 를 만든다.

  - ![스크린샷 2022-04-11 오전 10.43.22](/Volumes/GoogleDrive-116207538797775600332/내 드라이브/타이포라_source/스크린샷 2022-04-11 오전 10.43.22.png)

  - 논문의 저자들은 sentence의 aspect(topic) 와 최대한 관련된 정보들을 포착한 sentence의 vector 표현을 구하려고 한다.
  - 이때 논문의 저자들은 z_s는 sentence 내의 n개의 문장들의 word embedding 의 가중합으로 정의한다. (e_w_i)
  - 이때 가중치를 a_i (i는 sentence내의 word의 index) 라고 표현한다. 이는 i번째 단어 w_i가 sentence 의 주요 topic을 잘 포착하는 것에 중점을 둔 올바른 단어일 확률이다.
    - a_i는 sentence의 topic을 word가 잘 표현할 확률을 의미하는데, attention mechanism을 활용해서 계산된다. 
    - attention model 은 sentence의 전체적인 맥락 뿐만 아니라 단어 e_w_i에 조건을 둔 attention model 이다.
    - ![스크린샷 2022-04-11 오전 10.53.35](/Volumes/GoogleDrive-116207538797775600332/내 드라이브/타이포라_source/스크린샷 2022-04-11 오전 10.53.35-9642039.png)
    -   y_s는 word_embeddings들의 평균 값이다. 논문 저자들은 y_s가 sentence의 권역 맥락을 가장 잘 고려했다고 믿는다.
    - M(dxd) matrix 는 권역 맥락 embedding y_s 와 word embedding e_w 사이를 매핑한 matrix다. 그리고 학습 과정의 부분으로서 학습된다. (나는 sentence 내의 word representation의 평균 값인 y_s와 sentence 내의 각각의 word embedding 과의 유사도 매핑으로 이해했다. 이게 맞나??)
    - 논문의 저자들은 attention mechanism 을 두 개의 step process로 간주했다.
      - sentence 가 주어지면 sentence에 대한 표현을 sentence 내의 모든 word representation 의 평균으로 계산한다.
      - 그 다음 두 가지를 고려하여 word의 weight이 할당된다.
        - 첫 번째로, k aspects들과 관련있는 word를 포착할 수 있는 변형 M을 통해서 word를 걸러낸다.
        - 그리고 sentence에 대해 필터링된 word와의 관련성을 포착한다. (전역 context y_s에 대해서 필터링된 word의 내적을 취함으로써)
    - ㅇ
    - 
    - 

- ㅇㅇ

- 

