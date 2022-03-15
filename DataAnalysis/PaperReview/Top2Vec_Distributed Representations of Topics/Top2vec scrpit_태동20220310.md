> Topic Modeling
>
> : Technique of scanning a large corpus, detecting patterns & find groups of similar wards called Topics

- Topic Modeling
  - 많은 양의 텍스트를 구성, 검색 및 요약하는 기능은 NLP에서의 보편적인 문제
  - topic modeling은 다량의 텍스트 모음을 사람이 합리적으로 읽고 정렬할 수 없을 때 자주 사용
  - **토픽 모델링은 일반적으로 corpus라고 하는 대량의 문서 모음에서 latent semantic structure(잠재적 의미 구조)를 발견하는 데 사용**
- set of weighted words
  - topic의 combinations(결합) 및 variations(변형)는 고유한 가중치 단어 집합으로 설명할 수 있음
  - 따라서 topic을 나타내는 데 사용할 수 있는 가중치 단어의 조합이 무한히 많기 때문에 topic이 연속적이라고 가정
  - 또한 각 문서에는 해당 연속체에 값이 있는 고유한 topic이 있다고 가정
- Popular Methods 
  - LDA(Latent Dirichlet Allocation) 및 pLSA(Probabilistic Latent Semantic Analysis)
  - **LDA와 pLSA를 사용하려면 topic의 수, 불용어 목록, 형태소 분석 및 표제어가 필요한 경우가 많음**
  - 또한, 이러한 방법은 단어의 순서와 의미를 무시하는 문서의 단어 모음 표현에 의존
  - **LDA와 pLSA는 topic들의 숫자 t가 알려져 있다고 가정 : LDA를 만들 때 임의의 topic 숫자를 사용자가 직접 정의**
  - ex1) BOW표현에서 Canada와 Canadian은 의미론적 유사성에도 불구하고 다른 단어로 취급
  - ex2) 형태소 분석 및 표제어는 단어 어간을 공유하지 않는 big과 large와 같은 단어의 유사성 인식X
- A new approach

  - Top2vec : Simple and automatically finds the number of topics (created by "Dimo Angelov")
  - 문서 및 단어의 분산 표현은 단어 및 문서의 의미를 포착하는 능력으로 인해 큰 인기
  - topic vector를 찾기 위해 문서 및 단어의 semantic(의미론적) embedding을 활용하는 top2vec



> 단어와 문서의 분산 표현
>
> : Distributed Representations of Words and Documents

- 분산 표현
  - 분산 표현은 단어와 문서의 vector 표현을 학습하기 위한 NLP ML 기술의 핵심
  - **분산 표현은 단어를 vector로 표현하는 방법으로, 단어의 의미를 정확하게 파악할 수 있는 vector 표현**
  - 학습한 개념을 자동으로 일반화할 수 있음
- 분포가설
  - 단어의 의미는 주변 단어에 의해 형성된다는 가설
  - 단어 자체는 의미가 없고, 그 단어가 사용된 '맥락'이 의미를 형성
- 동시발생 행렬 
  - 어떤 단어에 주목했을 때, 그 주변에 어떤 단어가 몇 번이나 등장했는지를 세어 집계하는 방법
  - 즉, 모든 단어에 대해 동시발생하는 단어를 표에 정리한 것
- 통계 기반 기법 
  - 단어의 동시발생 행렬을 만들고 그 행렬에 SVD를 적용하여 **밀집벡터(단어의 분산 표현)**을 얻음 
  - 차원 감소 : '중요한 정보'는 최대한 유지하면서 벡터의 차원을 줄이는 방법
  - Truncated SVD : 특잇값이 작은 것은 버리는 방식으로 성능 향상
  - 대규모 corpus를 다룰 때 비용 및 시간 문제 발생
- 추론 기반 기법
  - 신경망을 이용하여 추론하는 기법으로 통계 기반 기법보다 더 강력한 분산 표현 가능
  - corpus의 어휘 수가 많아 SVD등 계산량이 큰 작업을 처리하기 어려운 경우에도 신경망 학습 가능



> word2vec - doc2vec - top2vec

- **(1)word2vec** 

  - skip-gram : 중앙의 단어(target)로부터 주변의 여러 단어(맥락)를 추측
  - 어떤 유사한 단어들끼리는 주변 맥락 단어들이 유사하게 등장할 것이라는 것을 전제하고 학습
  - word2vec은 동시발생하지 않는 단어 사이의 내적을 최소화하면서 동시에 발생하는 단어에 대한 단어 vector간의 내적을 최대화하는 것
  - 신경망을 이용한 분산 표현으로 context 단어에 대해 단일 학습 단계에서 모든 단어에 대해 동시 학습 
  - but 이러한 방법은 대규모 말뭉치로 확장할 수 있는 능력 부족

  

- **(2)doc2vec**

  ![image-20220307111835406](G:\내 드라이브\태동\연구실\Typora\image-20220307111835406.png)

  - doc2vec은 BOW 표현의 약점을 극복하고 모델을 확장하기 위해 distributed paragraph vector(분산 단락 벡터)를 제안
  - paragraph vector : 기존 word vector에 paragraph matrix를 합한 vector
  - PV-DBOW(Distributed Bag of Words version of Paragraph Vector) 
    - word vector를 제외하고 paragraph vector만을 이용해 학습을 진행하는 모델
    - 이 모델은 word vector(문맥 단어)를 고려하지 않고 paragraph vector만을 사용해 단어 예측 수행
  - **word2vec이 단어를 vector로 변경하는 word embedding 방식이라면, doc2vec은 문서를 vector로 변경하는 document embedding 방식**
  - **문서가 그 문서를 가장 잘 설명하는 단어와 가장 가깝고, 문서와 다른 단어와는 거리가 먼 의미 공간 생성**
  - 서로 다른 문서들은 다른 단어들에 의해 의미 공간의 다른 영역으로 이끌리기 때문에 멀리 떨어져 있을 것
  - word2vec : 2013년 / word vector / CBOS, Skip gram
  - doc2vec : 2015년 / word vector + paragraph vector / PV-DM, PV-DBOW

  

- Distributed Representations of Topics (topic의 분산 표현)

  - Semantic space : 거리가 의미적 연관을 나타내는 공간적 표현
  - doc2vec 모델은 동일한 공간에 embedding된 문서 및 word vector를 학습할 수 있음
  - embedding되거나 사전 훈련된 word vector를 사용하면 학습된 문서 벡터의 품질이 향상됨
  - 즉, **문서 벡터가 의미적으로 유사한 단어 벡터에 가깝도록 학습됨**
  - 또한 **문서와 가장 유사한 단어 또는 문서를 가장 대표하는 단어를 찾는 데 사용**할 수도 있음
  - semantic embedding : 문서 및 단어 embedding은 embedding된 공간의 거리가 문서와 단어 간의 semantic similarity(의미론적 유사성)을 측정

  

- Semantic embedding

  - 기존의 BOW 모델링 방법과 달리 semantic embedding은 단어와 문서 간의 의미론적 연관을 학습
  - embedding 문서 및 단어 semantic space에서 문서의 밀집된 영역은 유사한 topic을 가진 문서로 해석
  - 본 논문에서는 이러한 가정을 사용하여 문서 vector의 밀집된 영역에서 계산되는 distributed topic vector인 top2vec을 제안
  - **semantic space에서 발견되는 문서의 밀집된 영역의 수는 topic의 수로 가정하며, topic vector는 문서 vector의 밀집된 각 영역의 중심으로 계산됨**
  - 조밀한 영역은 매우 유사한 문서 영역이며 중심 또는 topic vector는 해당 영역을 가장 대표하는 평균 문서
  - **semantic embedding을 활용하여 각 topic vector에 가장 가까운 word vector를 찾아 각 topic vector를 가장 대표하는 단어를 찾음**

  

- **(3)top2vec : Distributed Representations of Topics**

  - **topic vector를 사용하면 각 문서 벡터의 가장 까가운 topic vector를 기반으로 topic size 계산 가능**

  - 또한 **topic vector에 대해 차원 축소를 수행하여 similar topic을 계층적으로 그룹화하고 발견된 topic 수를 줄일 수 있음**

  - top2vec과 확률적 생성 모델의 가장 큰 차이점은 topic을 모델링하는 방법
    - LDA 및 pLSA : topic을 단어 분포로 모델링하며, 이는 최소한의 오류로 원본 문서 단어 분포를 재현하는 데 사용 
    
    - top2vec : 문서 간에 공유되는 두드러진 topic을 나타내며, topic vector에 가장 가까운 단어는 topic과 그 주변 문서를 가장 잘 설명 
    
      ![image-20220307025542187](G:\내 드라이브\태동\연구실\Typora\image-20220307025542187.png)

  - topic modeling과 semantic search(의미 검색)를 위한 알고리즘

  - **텍스트에 있는 topic을 자동으로 감지하고, embedding된 topic 및 단어 vector를 함께 생성**

  - resulting topic vector는 semantic similarity(의미론적 유사성)를 나타내는 거리와 함께 문서 및 단어 vector와 함께 포함

  - topic vector에 document가 할당된 개수 = topic size

  - top2vec모델을 훈련하면 다음을 수행할 수 있음
    - Get number of detected topics : 감지된 수의 topic의 수를 가져옴
    - Get topics / Get topic sizes : topic 및 topic size를 가져옴
    - Get hierarchichal topics : hierarchichal(계층적) topic을 가져옴
    - Search topics by keywords : keyword별로 topic을 검색
    - Search documents by topic : topic별로 문서를 검색
    - Search documents by keywords : keyword별로 문서를 검색
    - Find similar words / Find similar documents : 비슷한 단어를 찾음 / 유사한 문서를 찾음
    - Expose model with [RESTful-Top2Vec](https://github.com/ddangelov/RESTful-Top2Vec)

  - Benefit
    - 자동으로 topic의 수를 찾음
    - 불용어 목록이 필요하지 않으며 stemming(형태소 분석) 및 표제어 추출(lemmatization)도 불필요
    - 짧은 텍스트에서 작동하며
    - embedding된 topic, 문서, 단어 vector를 만들며, 검색 기능 내장





> Model Description (Algorithm) 

top2vec 작동방식 : top2vec은 텍스트에 있는 topic을 자동으로 감지하며 stop words제거, 형태소 분석 등 전통적인 텍스트 사전 처리 필요 X

- **(1)  Create Semantic Embedding (시멘팅 임베딩 생성)**

  - Doc2vec - Convert each document & words to vectors (문서를 숫자 표현으로 변환)

  - Doc2vec 또는 Universal Sentence Encoder 또는 BERT Sentence Transformer를 사용하여 embedding된 문서 및 단어 vector를 만듦

  - 문서의 topic을 추출하기 위해서 특정 속성들을 갖고 있는 embedding document vector와 word vector 필요

  - 특히, **doc vector와 word vector 간의 거리가 의미적 연관을 나타내는 embedding하는 것이 필요**

  - **의미론적으로 유사한 document들은 의미론적 공간(embedding space)에서 서로 근접하게 위치** 

  - 단어는 가장 잘 설명하는 문서와 가장 가까움

    **↓ semantic space : 단어와 문서의 공간적 표현**

    - 의미론적으로 유사한 doc끼리는 semantic space에서 근접하게 나타남
    - word vector는 본인이 가장 잘 표현할 수 있는 doc에 가깝게 나타남
    - embedded doc vector와 embedded word vector를 이용하여 topic vector 계산 가능

  ![image-20220307091558707](G:\내 드라이브\태동\연구실\Typora\image-20220307091558707.png)

  

  ![image-20220307094304106](G:\내 드라이브\태동\연구실\Typora\image-20220307094304106.png)

  

  - 즉, **문서 목록이 주어지면 top2vec은 doc2vec 또는 사전 훈련된 모델을 통해 각 문서를 숫자 표현(또는 문서 벡터)으로 변환**

    - **본 논문에서는 word2vec과 doc2vec으로 생성된 의미론적 공간이 연속적인 topic들의 표현이라고 주장**
    - 각각의 고유한 단어는 또한 숫자 표현(단어 벡터)를 가질 것
    - 문서의 의미론적 내용이 캡처되고 유사한 단어가 서로 근접하도록숫자 표현이 생성
    - 보라점 : document / 초록점 : word

  - doc2vec의 DBOW 아키텍처

    - DBOW : context window에서 주변 단어를 예측하는 데 사용되는 document vector에 대한 context word를 교환하는 것 : embedded doc or word vector를 동시에 학습
    - doc2vec의 DBOW는 word2vec의 skip-gram과 매우 유사함
    - 차이점은 DBOW에서는 window 내 주변 단어들을 사용하는 대신  window 내에서 주변 단어를 예측하는 데 사용되어지는 doc vector를 사용

  - word2vec의 skip-gram model

    - skip-gram의 training objective는 문장이나 문서에서 주변 단어들을 예측하는 단어 표현을 찾는 것
    - words w1, w2 ... wt에 대해 log 확률의 평균을 최대화 하는 것
    - c는 training context의 크기를 나타낸 것으로, c가 클수록 training의 결과는 좋아지지만 훈련에 소요되는 시간이 더욱 커짐

    ![image-20220310022752369](G:\내 드라이브\태동\연구실\Typora\image-20220310022752369.png)

    - skip-gram model : vocabulary의 각 단어에 대한 input word와 context word vector를 학습

    - word2vec 모델은 input word vector에 대한 행렬 w_n,d로 구성

      - n = corpus vocabulary의 크기 / d = 각 단어를 학습하기 위한 vector의 크기
      - w_n,d의 각 행은 word vector를 포함

    - k 크기의 context window가 주어진 경우, 왼쪽과 오른쪽에 k 개의 context word가 있을 것

      - w를 둘러싼 각 2k개의 word에 대해, input word vector는 context word w의 context vector(문맥 상황 vector)를 예측하는 데 사용될 것
      - **각 주변 단어 w에 대한 예측은 softmax 함수 : 각 word가 context word (w_c)인 어휘에 대한 확률 분포 생성**

    - 학습은 후방 전파 및 확률적 경사 하강을 사용하여 w_n,d의 각 context word vector를 업데이트 

      - w_n,d에서 w로 구성되어 주변 단어 vocabulary에 대한 확률 분포에서 주어진 context vector의 확률이 가장 큼
      - 이 과정은 모든 n개의 word에 대해 모든 context window에 대해 반복

    - 이 학습 과정은 **의미론적으로 유사한 단어들이 서로 가까이 있는 context word vector를 갖는 반면, 다른 단어들은 멀리 있는 context word vector를 가짐**

    - 확률 P(w_c|w)를 최대화하기 위해서는 w x w_c의 값이 w x w_n,d의 최대값이 되어야 하기 때문 

      → 이 값은 w가 w_n,d의 모든 context vector에서 w_c에 가장 가까울 때 최대화됨

      → 따라서 학습 과정은 w와 w_n,d를 업데이트하여 w와 w_c가 더 가까워지도록 함

    - 이것은 embedding space에서 모든 유사한 context word를 끌어당기는 동시에 모든 유사하지 않은 context word를 밀어내는 것으로 해석될 수 있음

    - **즉, 의미론적으로 유사한 모든 word들이 서로 가깝고 서로 다른 모든 단어들이 멀리 떨어져 있는 context vector w로 표현되는 의미론적 공간을 만듦**

  - dec2vec의 DBOW model

    - DBOW model이 문서 벡터를 학습하는 방식은 skip-gram과 유사
    - DBOW는 행렬 D_c,d로 구성
      - c = corpus의 문서 수 / d = 각 문서에 대해 학습할 vector의 크기 
      - D_c,d의 각 행은 document vector를 포함
    - 학습 과정에서 document vector가 그 안에서 발생하는 word vector에 가까워야 하고, 그 안에서 발생하지 않는 word vector와 멀어지게 해야 함
      - 이는 각 word가 자신과 유사한 document를 유인하는 동시에 다른 document를 밀어내는 것으로 해석
      - 그 결과 문서가 문서를 가장 잘 설명하는 단어와 가장 가깝고, 문서와 다른 단어와는 거리가 먼 의미 공간 생성

  - 본 논문에서는 word2vec과 doc2vec에 의해 생성된 의미 공간이 topic의 연속적인 표현이라고 주장

    - 두 모델은 훈련되는 모든 n개의 단어에 대한 차원 d의 context word vector를 포함하는 행렬 W_n,d 학습
      - 이 행렬의 각 word vector만으로는 의미가 없으며, 행렬의 다른 word vector와의 상대적 유사성 제공
      - 행렬 W는 내장 공간으로부터 d차원 vector에 적용될 때 n차원 vector를 생성하는 선형 변환으로 볼 수 있음
    - d차원의 공간의 모든 점은 다른 topic을 나타냄
    - 각 word vector는 w_c의 확률이 가장 높은 d차원의 공간의 topic에 해당
    - 일반적으로 d차원 공간의 어떤 점 p는 가장 가까운 word vector에 의해 의미론적으로 가장 잘 설명

  - doc2vec의 성능에 큰 영향을 미치는 하이퍼파라미터

    - window size : context word의 왼쪽, 오른쪽 단어 수 → 15개가 최상의 결과
    - negative sampling or hierarchical softmax → 계층적 소프트맥스가 더 나은 document vector 생성
    - sub-sampling : 가장 중요한 하이퍼파라미터로, 주어진 context window에서 word 폐기 확률 결정 → 제안된sub-sampling 임계값 105
    - minimum count : 모형의 전체 빈도보다 작은 word를 폐기 → corpus와 vocabulary 크기에 크게 의존하며 본 논문에서는 50개의  count가 잘 작동
    - vector size : 학습할 document 및 word vector의 크기이며, 더 클수록 더 복잡한 정보 인코딩 → 제안된 벡터 크기는 300
    - epochs : 에포크 수 20~400 → 본 논문에서는 40~400

  

- **(2) UMAP : Dimensionality reduction (차원 축소)**

  - 차원 축소를 통해 축소된 공간에서 보다 정확한 document clustring을 찾음

    ![image-20220307092213475](G:\내 드라이브\태동\연구실\Typora\image-20220307092213475.png)

    

    ![image-20220307094235466](G:\내 드라이브\태동\연구실\Typora\image-20220307094235466.png)

    - UMAP을 사용하여 문서 벡터의 저차원 embedding 생성
    - 숫자 표현을 사용하면 문서를 clustering하여 topic를 찾을 수 있었지만 고차원 공간의 문서 벡터는 희소한 경향이 있음
    - UMAP(Uniform Manifold Approximation and Projection) : 차원 축소를 수행하여 밀집된 영역을 찾는 데 도움
    - 차원이 높은 vector는 정보가 드문드문(sparse) 나타남
    - 논문에서는 clustering의 downstream task에 대해 최상의 결과를 제공하는 5가지 차원을 찾음


  - UMAP(Uniform Manifold Approximation and Projection) : 서로 먼 데이터는 더 멀리, 가까운 데이터는 더 가깝게 하는 수학적 기반을 이용한 global한 데이터 분포 학습 방법

    - t-SNE : 고차원에서 각 두 점들에 대해 데이터가 비슷하면 높은 확률, 데이터가 다르면 낮은 확률 부여
      - 저차원으로 임베딩된 데이터에 대해서도 고차원의 확률 관계를 유사하게 맞추는 방식으로 학습
      - 우리가 두 데이터를 node로 볼 수 있고, 각 데이터 사이의 확률이 그 둘을 잇는 edge의 weigh
      - 즉, 우리는 각 데이터가 분포되어 있고, 각 데이터를 잇는 edge의 weight 확률인 weighted graph 형태로 생각할 수 있음

    - UMAP 또한 이러한 고차원에서 각 데이터의 graph관계를 저차원으로 임베딩 했을 때도 유사하게 잘 유지가 될 수 있도록 하는 학습
    - UMAP이 더욱 적절한 수학적 이론을 기반으로 제작된 알고리즘이기에 고차원 데이터 간의 graph 구조(global 구조)가 저차원에서 t-SNE에 비해 더 잘 유지

  - UMAP 그래프 형성 과정 - fuzzy simplicial complex

    ![image-20220310031108813](G:\내 드라이브\태동\연구실\Typora\image-20220310031108813.png)

    - extent 값이 커질수록, 각 데이터의 주변의 범위 즉 반지름이 커지는 것을 확인
    - n-nearest 값이 커질수록, 각 데이터가 연결된 다른 데이터의 수가 늘어나는 것을 확인
    - UMAP에서는 데이터를 감싸고 있는 원이 만나는 두 데이터는 연결되기 때문에 각 데이터를 둘러싼 원의 크기는 매우 중요한 역할을 함
      - 원이 너무 커지면 모든 데이터가 연결되고, 너무 작으면 고립된 데이터가 많이 생겨나기 때문
      - 따라서 적절한 원의 크기를 정하는 것이 중요

    - 각 데이터는 다른 반지름을 가진 원을 가지게 되고 이러한 원이 만나는 두 데이터가 연결되는 것
      - 하지만 여기서 모든 데이터에 대해 원이 커지게 되면 모든 데이터가 연결되는 문제가 발생하여 fuzzy 개념을 이용하여 해결
      - 즉, 원의 반지름이 너무 커지게 되면 경계를 모호하게 하여 각 데이터 간의 연결을 제한
      - 이러한 규칙 때문에 특정 데이터가 하나도 연결이 안되는 경우가 발생하는 것을 방지하기 위해 가장 가까운 두 데이터는 무조건 연결하도록 함

    - 마지막으로 이러한 규칙으로 데이터를 연결한 후, 가까운 데이터들은 연결된 정도가 강하게, 먼 데이터는 연결된 정도가 약하게 설정

  - UMAP이 빠른 이유

    - (1) fuzzy 이론에 의해 데이터 중심에서 멀리 떨어질수록 다른 데이터와의 결합확률은 0에 가까워짐
      - 따라서 데이터에 대해 가까운 몇 개의 이웃 데이터에 대해서만 계산을 수행해도 global 구조 학습

    - (2) negative sampling을 수행하여 모든 데이터 연결 고리에 대해 학습 하지 않음 
      - word2vec을 구현할 때 학습 시간을 줄이기 위해 사용된 기법
      - 유사하지 않은 수많은 단어 중 몇 개만 추려서 학습하는 것

    - (3) UMAP은 저차원 데이터에 대해서 각 데이터의 연결 정도를 계산할 때 실제 사용되는 함수가 아닌 근사 함수를 사용하여 미분 속도를 높임
    - (4) 저차원 임베딩 데이터를 초기화할 때 랜덤으로 하지 않고 spectral embedding 기술을 이용하여 학습이 더 빠름

  - UMAP의 단점
    - 하이퍼파라미터의 영향이 상대적으로 큼
    - 저차원으로 임베딩되어 가시화된 결과에서 각 데이터 간의 거리는 실제 데이터 간의 거리를 의미하지 않음. 또한 데이터들의 군집 크기 역시 의미가 없음
    - 저차원으로 임베딩되는 과정에 어쩔 수 없이 정보 손실이 발생하여 데이터 왜곡 현상 발생



- **(3) HDBSCAN : Clustering of documents (주제를 찾기 위한 문서 clustering)**

  - 문서의 밀집된 영역을 찾음

  ![image-20220307094224362](G:\내 드라이브\태동\연구실\Typora\image-20220307094224362.png)

  - HDBSCAN(Hierarchical Density-Based Spatial clustering of Applications with Noise) : 수치 표현을 저차원 공간으로 압축한 후 문서의 밀집 영역을 찾음
  - 위 다이어그램에서 각 점은 문서 vector를 나타내고 문서의 밀집된 영역은 색상이 지정되어 있으며 각 영역은 topic을 나타냄
  - 빨간점은 cluster에 속하지 않은 이상값
  - 각 밀집 영역에 대해 동일한 cluster에 있는 모든 문서 vector의 산술 평균을 취하여 topic(topic vector)의 숫자 표현을 얻음
  - 마지막, 각 문서에는 해당 문서 vector에 가장 가까운 topic vector를 기반으로 하는 topic 번호 할당

  

- **(4) Calculate "Topic vector" : centroid of document vectors**

  - 각 조밀한 영역에 대해 원래 차원에서 문서 vector의 중심을 계산 → 이것이 topic vector

    ![image-20220307094432878](G:\내 드라이브\태동\연구실\Typora\image-20220307094432878.png)

  - 빨간점은 이상값 문서이며 topic vector를 계산하는 데 사용되지 않음

  - 보라점(document vector)을 통해 topic vector를 산출함 : 즉, 보라점은 topic vector가 계산되는 밀집 영역에 속하는 문서 vector

    ![image-20220310000718799](G:\내 드라이브\태동\연구실\Typora\image-20220310000718799.png)

  - 의미 임베딩 공간에서 밀도가 높은 문서의 각 cluster에 대한 레이블이 주어지면 topic vector 계산 가능

  - centroid or vector mean을 활용한 topic vector로 활용 : "무게 중심"

    - 동일한 밀도 군집에 있는 모든 document vector의 산술 평균 계산
    - 가장 가까운 이웃의 word vector와 매우 유사한 topic vector를 생성 → 고차원 공간의 희소성 때문?

  - 중심은 밀도가 높은 cluster를 수행하는 각 document vector 집합에 대하 계산되어 각 집합에 대한 topic vector 생성 → 발견된 밀집 영역의 수는 corpus에서 식별된 prominent한 topic의 수

  

- **(5) Find n-closest word vectors to the resulting Topic Vector**

  - 의미 공간에서, 모든 점은 가장 가까운 word vector에 대해 의미론적으로 가장 잘 묘사되는 topic을 표현

    - 그러므로 topic vector에 대해 가장 가까운 word vector들은 의미론적으로 그것의 가장 대표적인 것
    - 각 word vector와 topic vector의 거리는 단어가 얼마나 의미적으로 topic과 유사한지 나타냄
    - topic vector에 가장 가까운 단어는 topic vector가 그 영역의 중심이기 때문에 밀도가 높은 영역에 있는 모든 문서와 가장 유사한 단어로 볼 수 있음
    - 이 단어들은 밀집 영역에 있는 문서의 공통적인 topic을 요약하는 데 사용

  - 일반적인 단어는 대부분의 문서에 나타나기 떄문에 모든 문서와 동등하게 멀리 떨어져 있는 의미 공간 영역에 있는 경우가 많음 → stopword 제거 필요 X

  - resulting topic vector에 대해 n-closet 가장 가까운 단어 vector를 찾음

    ![image-20220307094644210](G:\내 드라이브\태동\연구실\Typora\image-20220307094644210.png)

  - 근접성 순으로 가장 가까운 word vector가 topic words가 됨

  - 즉, topic vector의 뜻은 그 주변 word vector로 결정됨 : top2vec 완성



- Topic Size and Hierarchical Topic Reduction

  - topic vector와 document vector들은 topic size가 계산되게끔 만듦
    - topic vector는 각 document vector가 가장 가까운 topic vector에 속하도록 document vector를 분할하는 데 사용할 수 있음
    - 이는 각각의 document들을 특정 하나의 topic으로 연관짓게 만듦
    - 각각의 topic size는 그 topic vector에 속하는 document의 숫자로 측정

  - 계층적으로 topic size를 줄일 수 있음
    - 희망하는 숫자의 topic size에 도달할 때까지 반복적으로 가장 작은 topic size를 그것과 가장 유사한 topic에 합병하면서 진행
    - 가장 작은 topic size의 topic vector와 그것의 가장 가까운 topic vector 간의 가중 산술 평균을 취하면서 이루어지며 각각의 topic size에 따라 가중치 부여



> Result

- 모델 평가
  - topic model을 가장 잘 평가하는 자연스러운 방법은 topic이 문서를 얼마나 잘 설명하는지 점수 매기는 것
  - 이 평가는 topic이 사용자에게 얼마나 유용한지 측정

- 전통적인 topic modeling은 topic 공간을 이산화시키고 문서를 이러한 topic의 합성으로 설명
- top2vec은 topic을 지속적으로 표현하고 topic에 해당하는 문서를 해당 공간에 배치
  - top2vec에 의해 발겨된 topic vector는 문서 그룹에 공통적인 topic 또는 문서의 개별 topic에 대한 평균을 나타냄
  - topic set을 평가하기 위해 문서는 하위 집합으로 분할되며, 각 하위 집합은 가장 가까운 topic vector가 동일한 document vector에 해당
  - 따라서 각 문서는 정확히 하나의 topic에 할당
  - **이러한 topic을 평가하기 위해 topic vector에 가장 가까운 단어로 설명될 때, 각 문서의 하위 집합에 대해 얻은 총 정보가 측정**



> Topic Information Gain

![image-20220310023501790](G:\내 드라이브\태동\연구실\Typora\image-20220310023501790.png)(1)

- 모든 단어 w로 설명될 때 모든 문서 d에 대해 얻어진 총 정보 또는 상호 정보는 위와 같이 제공됨

  

  ![image-20220310023451007](G:\내 드라이브\태동\연구실\Typora\image-20220310023451007.png)(2)

- 문서 d와 단어 w 사이의 각 공존이 information gain 계산에 미치는 영향은 확률 가중치 정보량(PWI) d와 w가 정보 총량에 기여하는 것으로 볼 수 있음

  

  

  ![image-20220310023621767](G:\내 드라이브\태동\연구실\Typora\image-20220310023621767.png)(3)

- topic은 전체 어휘 w에 대한 분포

  - 그러나 사용자에 대한 유용성을 평가하기 위해, 항목의 상위 n개의 단어를 사용하여 평가

  - 각 문서가 하나의 topic에만 할당되는 평가의 경우 각 주제t는 n개의 단어 w 및 문서 d로 구성

    

![image-20220310023845884](G:\내 드라이브\태동\연구실\Typora\image-20220310023845884.png)(4)

- 방정식 (3)에서 p(w)는 모든 문서 D에 대한 단어 w의 한계 확률
  - 로그항을 계산하는 데 사용되며, 이 항은 w와 d 사이의 pointwise mutnal information
  - 우리가 측정하는 수량(quantity)은 이전과 같은 해당 topic word에서 얻은 각 문서에 대한 정보
  - 따라서 p(w)는 1이고 위와 같은 결과 발생



![image-20220310024215696](G:\내 드라이브\태동\연구실\Typora\image-20220310024215696.png)(5)

- 또는 각 문서가 여러 topic으로 표현되는 경우에 대해 방정식 일반화 가능
- 이 경우 p(w)를 p(t)로 대체
- p(t)는 문서 d를 topic t로 표현하기 위해 사용되는 단어의 비율



**→방정식 (4)와 (5)를 사용하여 서로 다른 topic 집합을 비교할 수 있음**

- **information gain이 많을수록 topic t가 해당 문서에 대해 더 많은 정보를 제공하는 것을 의미**
- topic이 'the', 'and', 'it'과 같은 단어 또는 직관적으로 정보를 제공하지 않는 word를 포함한다면, 더 낮은 information gain 값을 받게될 것
- 이것은 계산에서 p(d|w)항 때문인데, 이는 매우 일반적인 word가 주어진 특정 무서의 확률이 매우 낮기 때문
- 항목에 해당하는 문서의 하위 집합에 주로 있는 word는 해당 문서에 대한 정보를 제공하기 때문에 더 높은 정보를 얻을 수 있음
- 따라서 방정식 (4)와 (5)는 직관적으로 더 유익한 것에 해당하는 값을 제공
- **본 논문에서는 topic information gain(주제 정보 이득)이 topic model을 평가하는 데 좋은 척도라고 주장**



> Discussion

- semantic space
  - **semantic space**가 매우 유사한 문서, topic size의 밀도 높은 영역에서 topic vector를 계산하고 계층적 topic reduction(축소)을 가능하게 하는 **topic을 지속적으로 표현하는 것**을 보여줌
  - top2vec model은 의미 공간의 거리를 기준으로 단어, 문서 및 topic 간의 유사성을 비교할 수 있음

- 문서의 topic이 얼마나 유익한지를 계산하기 위해 mutnal information(상호 정보)을 사용하여 topic을 평가하는 새로운 방법을 제안
  - topic information gain은 문서의 topic word로 설명될 때 문서에 대해 얻은 정보의 양을 측정
  - 이렇게 하면 topic word의 품질이 측정되고 문서에 topic 할당 가능

- topc2vec이 다양한 크기의 topic과 상위 topic word 수에 대해 LDA와 pLSA보다 더 유익하고 corpus를 대표하는 topic을 일관되게 발견한다는 것을 보여줌
  - 전통적인 topic modeling에 비교하여, corpus를 나타내는 topic 수와 topic을 자동으로 파악
  - stop-word list를 필요로 하지 않음
  - 단어의 분산 표현을 사용하면 단어 의미론을 무시하는 BOW 표현의 몇 가지 문제 완화



- Challenges
  - UMAP & HDBSCAN
  - Execution time & crashes
    - Use small dataset for initial testing
    - Get more resources in order to use big dataset
    - 본 논문 외에서 본 data set 외에 다른 데이터에도 잘 적용될지 의문
  - Minimum topic 수는 직접 지정해주어야 함
    - 중간에 군집화 - HDBSCAN이 드렁가는데, 이 알고리즘에서는 min-topic 수를 지정해 주어야 함
- Personal Reflection
  - Easy to use and automatically finds number of topics
  - Does not loose semantics
  - Stop word removal, stemming/lemmatization not required
  - Search functions are built in
- Future Directions

  - Hyper-parameters Tunning
    - Doc2vec : vector size = 300, window = 15
    - UMAP : Default Nearest Neighbors = 15, metric = "cosine"
    - HDBSCAN : min cluster = 15, metric = "euclidean"

  - As a future direction, it would be interesting to play around with these and come up with findings for better optimization in Topic Modeling



