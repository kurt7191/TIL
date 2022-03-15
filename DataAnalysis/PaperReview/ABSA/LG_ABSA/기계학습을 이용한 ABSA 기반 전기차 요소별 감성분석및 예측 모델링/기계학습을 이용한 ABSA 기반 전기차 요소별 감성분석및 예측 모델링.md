# 기계학습을 이용한 Aspect-Based Sentiment Analysis 기반 전기차 요소별 사용자 감성 분석 및 예측 모델링



## 초록



- 분석 대상 : 전기차

- ##### 사용 방법론 : 기계학습, absa

  - 순서

    - 데이터 수집

      - 대표적인 자동차 포럼에서 사용자 만족도가 5점 척도로 평가된 Label 데이터 5065개
      - Youtube에서 Non-label 데이터 약 21만개 수집
      - 수집된 Youtube 데이터 중,  User Experience 관련 어휘가 포함된 리뷰로 한정 6,488개 선별

    - 전처리 및 Feature 생성

      - 분산 표현(distributio representation) 을 통한 임베딩 과정을 통해 특징(Feature) 추출

    - 요소 추출(Aspect Extraction) 을 위한 모델링

      - TextRank
      - Naive Method

    - 감성 분석(Sentiment Analysis) 을 위한 모델링

      - 지도학습(Supervised Learning) 기반 (Label 이 있는 리뷰 데이터 사용 (일부 절단해서))

    - ##### 요소 별 사용자 감성 분석

      - 요소 추출과 감성 분석 모델을 만들었으면 이를 바탕으로 aspect가 포함된 문장에 대한 감성 분석을 실시 => 요소별 감성 분석을 진행

    - ##### 특정 요소와 사용자 감성의 관계 분석

      - 사용자 감성에 영향력 있는 차량 세부 스펙(aspect)를 찾아 Contributing Factor 를 발굴

- ##### 목적 : 차량의 주요 요소들을 추출한 이후에 그 요소들에 대한 사용자들의 감성을 예측하고 특정 요소에 대한 특정 감정의 관계성에 대해서 분석

- 사용 데이터 : label이 없는 데이터 (사용자 리뷰 부족 문제를 해결하기 위해)



##### 결과



- 추출된 요소(Aspect Extraction)

  - *총 16개 카테고리* 의 주요 *Aspects 가 추출*됐다.(8개 : 전기차 구성 요소, 8개 : Human Factor)
    - positive : “Acceleration / Room / Interior / Power / Safety / Ergonomics / Price / Power”
    - negative : “Seat / Battery / Charge / Noise / Winter / Ice”

- 감성 분석(Sentiment analysis) method

  - ##### *리뷰 단위*(text or document?) 감성 분류에 있어 *CNN 모델*이 가장 높은 성능을 보임

  - CNN을 활용한 준지도학습(semi-Supervised Learning)

    - Non-label data 중 80% 이상의 분류 확률이 높은 데이터 위주 (youtube 데이터인듯?)로 Pseudo Label(매 가중치 업데이트 마다 확률이 가장 높은 클래스를 true label 로 사용) 부여 (**https://deep-learning-study.tistory.com/553**)참조
    - 즉, non-label 데이터에 대해서 레이블을 부여하는데, 매 가중치 업데이트마다 각각의 class에 대한 확률값이 도출이 될텐데, 80% 이상의 확률을 기록하는 class를 label 로 사용한다.

- 추출된 요소(Extracted aspect) 가 포함된 *문장 단위* 감성 분류

  - 기계학습 모델 기반

  - Lexicon 기반 감성 분류

  - ##### 17개 Aspect 중 14개가 예측 방향성이 일치 => 이를 통해 기계학습 감성분류 모델의 타당성 간접적으로 확인

- 샘플 검증 (모델 평가로 이해)

  - 논문에서 학습된 딥러닝 모델의 **높은 분류 정확도** 확인(높은 성적을 보인다.)

  - ##### 딥러닝 모델이 단어 의미 이상으로 문장 문맥을 파악하여 긍정/부정 분류

  

  > 결론 :
  >
  > 1. Aspect 기반의 문장 단위 분석을 통해 보다 더 다양한 토픽과 편향되지 않은 의견을 추출할 수 있음을 보였다.
  >
  > 2. 리뷰 데이터를 over sampling 해서 data inbalancing 문제를 극복(긍정 편향성)
  >
  > 3. 준지도학습을 통한 nonlabel data 활용 방법을 통해 사용자 평가가 부족한 제품에 대해 보다 효과적으로 분석 (Pseudo Label 이야기 하는 듯)

  

=> 정리하면 데이터 수집 , 데이터 전처리 및 임베딩, 요소 추출 method 사용, 감성 분석 모델 학습, 추출된 요소를 포함하는 문장 단위(sentence level) 감성 분석-> 평가



<hr>

## 서론



### 연구 배경



- 사용자 경험 분석을 위한 기초적인 프레임워크(framework) 는 Aspecet Based Sentiment Analysis(ABSA) 다.

  - 사용자가 생성한 *review text* 에서 제품 및 서비스에 대한 *특정 개체*와 *특징*에 대한 의견을 얻는 것.
  - 리뷰 단위 감성 분석과는 얻을 수 있는 정보의 질에 차이가 있다.
  - ex) 특정 구성 부품(component), 개체, 사용자와 제품간의 상호작용적 특성에 관한 단어 => 요소(aspect) 로 채택
  - 각 aspect 에 대한 감성 파악 => ABSA 완성
  - 이 논문은 기계학습 기반의 asba
    - 주요 aspect
    - 해당 aspect 에 대한 사용자의 감성
    - 사용자 감성에 영향력 있는 aspect 파악 / Contributiong factor 파악

- 사용자 리뷰 데이터는 한쪽 label 로 편향된 데이터셋이다.

  - 긍정적인 경험을 얻은 사용자만 긍정적인 의견을 남긴다는 사용자 행동 성향 때문임.
  - 제품에 대해서 전반적으로 긍정일지라도 제품의 모든 aspect 에 대해서 긍정적이진 않을 것.

  

  

> 제품의 **주요 aspect 를 추출(major aspect)** 하고, 각각 **사용자의 긍정/부정 감성을 확인**하고 **제품 aspect의 상세 스펙**(aspect 에서 멈추지 않고 그 aspect 의 상세 스펙 확인) 과 사용자가 느끼는 감성 극성간의 **상관관계** 파악.



### 연구 대상



전기차 => 국제적인 환경 규제 정책들에 의해서 점점 소비가 많아질 예정



<hr>



## 연구 목표



### 연구 목표



- 성장 초기 단계의 향후 수요가 폭발적인 증가가 예상되는 제품에 대해 전기 자동차를 선정

- 주요 Aspects(major aspect) 발굴

  - 차량 내의 구성 요소(component) aspect
  - 사용자-차량 간 인터랙션 특성 aspect

- 주요 Aspect 에 대한 사용자 감성 파악

- 주요 요소(aspect) 의 여러 요소(factor) 중에서 사용자의 감성에 영향력 있는 요소(Contributing Factor)를 파악

- > 구조 : major aspect(factor1, factor2, factor3, ... Strength factor ... ,factorN) 

- 사용자 리뷰 부족 issue 발생

  - Non label 데이터 함께 활용하는 방법 도출 => 보다 견고한 감성 예측 모델 만들 수 있음
    - 사용자 리뷰가 부족한 차세대 제품에 대한 *더 다양한 토픽*을 얻을 수 있음

- 데이터 불균형 issue 발생

  - Non label 데이터 함께 활용하여 불균형 해소

- Aspect Based Sentinment Analysis(ABSA) 방법을 적용





> 주요 목표 : 주요 aspect(차량 내의 구성 요소 (component) aspect , 사용자-제품 간 인터랙션 특성 aspect) 를 찾고, 주요 aspect 에 대한 사용자 감성 분석을 적용한 후, 주요 요소(asepct) 중에서 사용자의 감성에 영향력 있는 factor 를 파악한다.
>
> 하위 목표 : 사용자 리뷰 부족 문제와 데이터 불균형 문제를 해소
>
> 프레임워크 제안 : 사용자의 감성에 영향력 있는 차량 요소(factor)가 무엇인지 확인할 수 있는 새로운 UX(User experience)  분석 프레임워크 제안 => 주요 aspect 내의 영향력 있는 factor 를 발견 함으로써!
>
> ex) 주요 aspect으로 "엔진"=> "엔진"에 대한 감성분석 => 긍정 출현 가정 => 엔진에 대해서 긍정적이게 생각하게 하는 주요 factor 추출 => 어떤 x 부품이 선정 => 도출된 정보 활용





![스크린샷 2022-03-15 오후 6.25.56](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-15 오후 6.25.56.png)





<hr>

### 선행 연구(literature review)



#### Aspect-Based Sentiment Analysis



ABSA 란 대상의 *하위 요소* 및 *특성과 관련된 용어*를 고려해서 각각에 대한 감정을 식별하는 기술이다.

##### 대개(전통적으로) 단락(paragraph)에 대한 감성을 긍정/부정으로 분류 또는 예측하는데, 주어진 텍스트가 하나의 감성 극성만 있다는 가정으로 진행하지만 absa 는 corpus 내의 각각의 aspect 에 관련된 감성을 예측한다.



- 초기 연구

  - 주요 어휘가 자주 반복된다라는 전제.

    - *자주 출현하는 명사를 기준*으로 aspect 를 추출하고 추출된 aspect에 대한 감성 분석을 진행한다.
    - [appendix 4번]

    

- 최근 연구

  - 3가지 Subtask를 통한 방법

    - ##### Aspect  추출

    - ##### Aspect 카테고리 탐지

    - ##### Aspect에 대한 감성 극성(Sentiment Polarity) 추출 [appendix 5번]

    - 위의 세 가지를 하기 위해서는 corpus 에서 "aspect 카테고리", "카테고리에 해당하는 aspect 용어", "정답 감성 label" 가 필요하다.

  

- ABSA 를 활용한 주요 과제

  - 문서 내 주요 Aspect 를 발굴하고, 해당 Aspect 의 감성을 분석한다.
  - 연구자가 설계한 기계학습 모델을 기반으로 aspect와 이에 대한 감성 극성에 대한 예측 정확도를 높이려고 시도한다.

  

- ABSA 의 주요 데이터셋

  - 초기 ABSA 연구는 대부분 "제품"에 대한 웹 사용자 리뷰
  - 최근에는 제품에 대한 사용자 리뷰뿐만 아니라 서비스에 대한 리뷰도 사용되고 있다

  

- ABSA 활용 workshop

  - SemEval(International Workshop on Semantic Evaluation)

  - 논문 읽어야 겠네...

  - 참가자들 끼리 모여서 모델을 뽐내는데, 각각의 도메인 데이터셋에 대해 참여자들의 모델을 사용해서 정확도를 평가한다.(그런 workshop.......)

    - Aspect 와 그에 대한 감성 레이블이 있다.

    - 현실 산업에서는 aspect에 대해 레이블이 달린 경우는 거의 없다.

    - ##### 따라서 비지도 방법(Unsupervised Method) 를 통해 Aspect 를 추출하고 이에 대대 감성 분석 시행.

    

- 전통적인 방식에서는 document 전체에 대한 감성 극성을 구했다면 최근에는 더 정교하고 세분화된 감성 분석을 요하고 있다.

  - 1. ##### document 에서 토픽(topic)을 추출 

  - 2. ##### 제품의 특성(attribute) 를 추출 (HOW???)

  - 3. 부품 요소(part) 를 추출 [appendix 4,10]

  - 위의 세 가지는 해당 추출에 대한 감성 분석을 통해 더 정교하고 세분화된 감성 분석을 수행한다.

    - 추출된 주요 요소들에 대한 사용자들의 감성을 파악하기 위해 paragraph, sentence 단위 감성 분석 수행
    - 해당 추출된 요소들이 포함된 문서 및 문장이 어떤 감정을 나타내는지 파악함.

    

- ##### 주제 단위 감성 분석

  - ABSA 이외의 주제 단위 감성 분석 = LARA. [appendix 11]
  - LARA
    - 전체 리뷰의 *평가 점수* 를 바탕으로 리뷰 내 aspects에 대해 평가 점수를 산출.
    - 전체 리뷰평점과 aspects 간의 weight를 Linear Regression 기반으로 산정 (Linear Regression weight 를 사용해서 각 aspect 에 대한 평가 점수를 도출)
    - 전체 평점과 관계 있음
  - ABSA
    - 전체 평가 점수와는 무관하게 각 주제(aspect 로 이해해도 될라나?) 의 문장이나 단락의 감성 극성을 구한다.
    - 이때 Lexicon 또는 기계학습 기반으로 독립적으로 계산하는 방법으로 접근한다.(전체 평점과 관련 x)

- ##### ABSA 의 워크플로우(Pontiki et al. 이 최초로 제안한 3가지 중요한 Subtask)

  - 1. Aspect Term 추출

    2. Aspect Term 들을 서로 다른 카테고리로 묶는 것 (top2vec으로 토픽 벡터를 찾고 그 주변의 단어들을 aspect로 해도되겠는데?)

    3. Aspect Term 별 감성 극성을 추출하는 것
       - aspect term은 보통 sentence 내부에 존재하기 때문에 해당 문장 내의 aspect term 에 대한 감성 극성을 판정하는 방법을 취한다.(sentence 의 감성 값을 취하라는 건지 헷갈림)
       - 초기에는 감성 값을 취하는 방식을 Lexicon-based methods 를 취했다 [appendix 6, 12]
       - 최근에는 기계학습 기반의 감성 분석을 진행하고 있다. [appendix 13]





#### 요소 추출(Aspect Extraction)



- 도대체가 Aspect aspect 거리는데, aspect 가 뭐야?

  - Aspect(요소) 는 크게 "구성 부품(Component)"과 "특성(Attribute)"로 정의 가능하다.
    - 구성 부품 : 제품 or 서비스의 구성 요소 및 부품
      - ex) 전기차 => 배터리, 소프트웨어, 사운드 시스템(Sound system)
    - 특성(Attribute) : **사용자가 느끼는** 제품의 특성
      - ex) 가속감(Acceleration), 안정성(Safety), 사용 편의성(Ease of Use)

- 초기 aspect 추출(Asoect Extraction) 접근 방식

  - 출현 빈도의 명사 또는 명사구 추출
    - 주요 토픽은 반복해서 등장한다는 전체하에 시행
    - 빈도수가 높은 명사는 그 document 의 주제라고 생각하고, 그 주제를 aspect로 삼았던 거 같다.
  - Rule-based Linguistic Pattern 기반으로 추출하는 연구 => obim 에 등장했던걸로 기억한다.
    - 문법적인 관계를 활용하여 문장의 구조를 파악하고 *구문적 특성을 활용하여 감성 어휘와 연관된 Aspect 를 추출*하는 방법 [appendix 14,15]
  - LDA(Latent Dirichlet Allocation) 기반의 토픽 모델링(Topic Modeling) 을 통한 토픽 추출 방법.
    - LDA 를 통해서 추출된 토픽들이 주요 aspect로 채택되는 거 같다.

- 최근 aspect 추출 접근 방식

  - 딥러닝 기반의 Aspect 추출 

    - But, 지도 학습 기반으로 Label이 있는 데이터 셋에 한하여 사용하는 경우가 많다. [appendix 19,20,21]

  - 텍스트 요약 기법 (Text Summarization)

    - document를 텍스트 요약 함으로써 document 의 주요 키워드(keyword) 또는 주제를 발견

      1. 추상적 접근(Abstractive Approach) => 요약을 통한 주요 단어나 어구 발견

         - ##### corpus 또는 document 의 내용을 기반으로 요약문 생성 (seq2seq or attention mechanism)

         - 그러나 seq2seq 는 기본적으로 지도학습이기 때문에 리뷰 텍스트별 요약(정답) 이 있어야만 한다.

         - 이 논문은 그러한 데이터를 찾지 못해 추상적 접근에 실패한다.

      2. 추출적 접근(Extractive Approach) => **구글링으로 보완 필수**

         - 주어진 문서 집합 내에서 이를 대표할 수 있는 단어들이나 문장들을 선택 (문서내 대표 단어 선택)

           - 가장 존재력이 높은 어구(Informative Pharase) 또는 문장 선택

           - 실제 원문의 내용 및 맥락과 동떨어진 요약 결과를 낼 가능성이 적음

           - 그러나 원문 내 표현으로 한정됨 (가능한 표현 제한)

           - 1. TextRank[appendix 23] => 키워드 추출과 핵심 문장 추출 제공

                - **Graph-based Ranking 알고리즘 기반**의 PageRank를 활용(Graph-based Ranking 알고리즘 기반)

                - PageRank 가 높은 웹페이지는 다른 웹사이트로부터 링크를 받거나 다른 사이트가 많이 참조한 것. => 이를 문서 내에 적용해서 중요 단어, 주요 어구, 문장의 중요도에 따른 가중치 부여 => TextRank 의 핵심.

                - > 중요한 페이지는 많은 점수를 가지고 있습니다. Backlinks 가 적은 링크라 하더라도 중요한 페이지에서 투표를 받은 페이지는 중요한 페이지가 됩니다. (블로그)

                - **핵심 단어 선정**을 위한 점수 산정

                  - TextRank 는 두 단어 간의 유사도를 측정

                  - 분포 가설에 근거해서 두 단어가 동시 출현한 빈도수가 높으면 유사하다고 가정

                  - 여기서 말한 동시 출현 횟수는, 설정 값 window size 내에서의 동시 출현 횟수를 의미

                  - ##### 즉, window size내에서 두 단어가 동시 출현한 횟수가 많으면 두 단어는 유사하다고 가정 => 유사하면 핵심 단어일 가능성 높아짐(핵심단어 값이 커짐)

                  - Co-occurence matrix 생성

                  - > TextRank 는 문서 내의 중요한 단어(키워드) 를 동시발생횟수가 높은 단어들로 선택한다. => graph 내의 edge 로 선정 (동시 발생 횟수를 edge 로 선정.)
                    >
                    > 동시 발생 횟수가 높다고만 해서 키워드 단어로 선정하는 게 아니라, 명사, 형용사, 동사에 한해서 키워드 단어로 선정한다. (stopwords 지정 필요)

                  - TextRank 를 통해 단어, 어구, 또는 문장의 순위를 계산하는 식

                  - ![스크린샷 2022-03-15 오후 10.05.34](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-15 오후 10.05.34.png)

                  - 그림의 WS(V_i) 를 계산하고 값이 높은 순으로 order, "d" 는 "damping factor" => pageRank 에서 웹 사용자가 페이지를 이탈할 확률, TextRank 에서도 그 값을 그대로 사용

                  - >  웹페이지 유입의 c 만큼은 링크에 의한, 1−c1−c 만큼은 임의적인 유입이라 가정하여 아래와 같은 식을 기술합니다. 이 임의 유입은 PageRank 계산의 안정성을 가져오는 역할도 합니다. => 이게 d인듯?

                  - 각 그래프에 PageRank 를 학습해서 각 Vertex(단어 혹은 문장) 의 랭킹을 계산하여 가장 값이 높은 순으로 정렬 => 랭킹이 가장 높은 단어 또는 문장은 키워드와 핵심 문장으로 간주

                  - ##### 핵심 문장 선정의 원리? => 문장도 위 그림식을 통해서 중요 랭킹값 도출

                  - > - 문장 간 유사도를 기반으로 sentence similarity graph 를 만든다.
                    >   - 유사도가 큰 문장을 핵심 문장으로 선정.
                    >
                    > - 밑의 그림은 코사인 유사도 이외에 TextRank 논문이 제안한 유사도 식이다. 이를 이용해서 문장의 유사도를 나타낸다.
                    >
                    > - 두 문장에 공통으로 등장한 단어의 개수를 각 문장의 단어 개수의 log 값의 합으로 나눈 것
                    >
                    > ![스크린샷 2022-03-15 오후 10.39.32](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-15 오후 10.39.32.png)
                    >
                    > - 문장 길이에 log 를 부여하기 때문에 길이가 길어질수록 분모의 값의 증가분은 줄어들고 길이가 길어질수록 중복된 단어가 나올 확률이 높아지므로 분자가 커진다. 고로 유사도는 커진다. => TextRank 는 긴 문장을 선호
                    > - 한 문장이 여러 문장들과의 유사도가 높아지려면, 문서 내에서 자주 등장하는 단어를 많이 포함하고 있으면 된다. 
                    > - 따라서 유사도를 기준으로 핵심 문장을 선정한다면,  문서 내에서 자주 등장하는 단어들을 많이 포함한 문장은 다른 문장들과 똑같은 단어들을 많이 공유할 확률이 높아져서 유사도가 높기 때문에 핵심 문장으로 선택될 가능성이 크다. (단, stopwords 들 제외)
                    >
                    > 
                    >
                    > 
                    >
                    > co-occurence graph 와 sentence similarity graph 각각 PageRank 를 학습하여 각 마디(단어 혹은 문장)의 랭킹을 계산한다. (PageRank 의 graph edge 방식에 착안해서 랭킹값 계산)



![다운로드](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/다운로드.jpeg)



> 이로써, PageRank 방식에 착안한 TextRank 를 이용해서 문서 내의 키워드 단어와 핵심 문장들을 추출했다.(통계 기반)



#### 감성 분석(Sentiment Analysis)













<hr>











































