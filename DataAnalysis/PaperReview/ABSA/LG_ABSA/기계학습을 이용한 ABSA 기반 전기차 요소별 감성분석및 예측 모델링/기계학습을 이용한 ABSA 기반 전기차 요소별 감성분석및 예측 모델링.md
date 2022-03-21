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
    - 사용자 감성에 영향력 있는 aspect 파악 / Contributing factor 파악

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

    - ##### 따라서 비지도 방법(Unsupervised Method) 를 통해 Aspect 를 추출하고 이에 대해 감성 분석 시행.

    

- 전통적인 방식에서는 document 전체에 대한 감성 극성을 구했다면 최근에는 더 정교하고 세분화된 감성 분석을 요하고 있다.

  - 1. ##### document 에서 토픽(topic)을 추출 

  - 2. ##### 제품의 특성(attribute) 를 추출 (HOW???)

  - 3. 부품 요소(part) 를 추출 [appendix 4,10]

  - 위의 세 가지는 해당 추출에 대한 감성 분석을 통해 더 정교하고 세분화된 감성 분석을 수행한다.

    - 추출된 주요 요소들에 대한 사용자들의 감성을 파악하기 위해 paragraph, sentence 단위 감성 분석 수행
    - *해당 추출된 요소들이 포함된 문서 및 문장*이 어떤 감정을 나타내는지 파악함.

    

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

                  - >  웹페이지 유입의 c 만큼은 링크에 의한, 1−c 만큼은 임의적인 유입이라 가정하여 아래와 같은 식을 기술합니다. 이 임의 유입(1-c)은 PageRank 계산의 안정성을 가져오는 역할도 합니다. => 이게 d인듯?

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



감성 분석(Sentiment Analysis) 를 위한 접근 방식



1. 지식(사전) 기반 감성 분석(Knowledge(Lexicon)-based Approaches)
   - 감성 어휘 또는 문법 기반의 분류 => Happy, Sad, Boring 과 같은 분명한 감성 어휘들의 존재에 따라 텍스트 분류, 어휘간 문법적인 관계성을 통해 분류
2. 기계학습 기반 감성 분석(Statistical & Machine Learning based Approaches)
   - 통계&기계학습 기반 감성 분석 => Navie Bayes or Supprot Vector Machines (전통적 방식)
   - Deep Learning
3. Hybrid Approaches
   - 기계학습 방식 + 지식(사전) 기반 방식



기본적으로 ABSA 에서 감성 분석은 bag or words(빈도기반 방식) , linguistic features(문법적 방식) 등을 이용해서 전통적인 기계학습 분류기를 통해 학습시키는 모델링에 중점을 둔다.

최근에 딥러닝의 발전으로 딥러닝을 사용하는데, CNN, LSTM 기반의 다양한 모델이 적용됐다. (이마저도 전통적)

특히나 딥러닝의 분야에서는 Neural Attention Mechanism, 즉 Attention is all you need 논문에서 보인 attention 메커니즘을 많이 사용한다.



ABSA Task 에 적용된 attention 기반 모델은 IAN[appendix 28], MemNet[appendix 29],

BILSTM-ATT-G[appendix 30], RAM[appendix 31] 이후 MGAN(Multi-Grain Attention Network)[appendix 32] 의 성능이 제일 좋았다.



### 기계학습 기반 감성 분석



기계학습 기반 감성 분석(Statistical & Machine Learning Based Sentiment Analysis) 란, 

기계학습 기반 알고리즘으로 텍스트에서 추출한 특징을 학습시킨 모델을 바탕으로 문장, 문단, 문서 단위의 감성 분류/예측하는 것.



1. CNN(Convolutional Neural Network)

   - 이미지 또는 텍스트를 1차원 텐서인 벡터로 변환하고 다층 퍼셉트론의 입력층으로 사용하면 **공간적인 정보가 유실된 가능성이 크다.**(단어간 위치, 계층적인 구조와 같은 정보) => CNN 이 이미지 또는 텍스트의 공간적인 구조 정보를 보존하면서 학습할 수 있게끔 해준다.
   - ![스크린샷 2022-03-18 오후 1.05.32](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 1.05.32.png)

2. 어텐션 기반 양방향 장단기 메모리 네트워크 (Bidirectional-Lon Shot Term Memory with Attention)

   - 기존 RNN 의 기울기 소실 문제를 해결하기 위해서 만든 LSTM 모델을 활용

   - RNN 기반의 시퀀스 모델들은 직전 패턴을 기반으로 수렴하는 경향을 보이기 때문에 단방향성의 특징만을 가지는 단점이 있다. 따라서 이를 보완한 양방향 순환 신경망(bi-rnn) 이 등장한다.

   - 기존 순방향에 역방향 은닉층을 추가하여 성능 향상

   - 이 모델을 분류 task 에 적용하여 좋은 성능을 냈다.

   - ![스크린샷 2022-03-18 오후 1.09.29](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 1.09.29.png)

     

3. Hierarchial Attention Newtwork(HAN)

   - 기본적으로 하나의 문서는 단어 -> 문장 -> 문서 순으로 이어지는 Hierarchial Structure  를 가지고 있는데, 이러한 특징을 학습할 수 있는 네트워크가 문서를 학습하고 분류하는데 적합한 네트워크이며 HAN 이 아주 부합하는 모델로 평가되고 있다.
   - ![스크린샷 2022-03-18 오후 1.13.02](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 1.13.02.png)

4. 준지도학습(Semi-Supervised Learning)

   - 머신러닝 모델은 정답(Label) 이 꼭 있어야만 학습이 가능한데, 준지도학습은 이를 보완한 모델이다.
   - 정답 label 이 있는 데이터로 모델을 학습시켜 Teacher model 을 탄생시킨다.
   - Teacher Model 에 Non-label 데이터를 넣어서 예측값을 구한다.
   - 이 예측값들 중에서 높은 확률 값이 나오는 데이터 위주로 "Pseudo Label" 을 부여하는 방법으로 Label 전파를 진행
   - 새롭게 부여된 Label 의 데이터와 기존의 정답 Label 이 있는 데이터를 모두 사용하여 새로운 모델을 재학습 시키면서 분류 성능을 향상 => 셀프 트레이닝(Self-Training) => 준지도학습의 가장 간단한 방법
   - 아래 그림과 같은 도식을 따른다.
   - ![스크린샷 2022-03-18 오후 1.46.59](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 1.46.59.png)

5. Lexicon 기반 접근 방법

   - 사전에 정의된 긍정/부정 단어를 이용하여 텍스트에 포함된 단어의 감성 극성(Sentiment Polarity) 을 이용해서 텍스트의 긍정과 부정을 판별하는 rule-based 방식
   - 문장 내에 있는 단어들의 감성 사전 내 점수 기반으로 문장의 감성을 판별한다.
   - Label 이 없는 데이터에도 사용할 수 있어서 기계학습 기반의 감성 분류 이전에는 널리 활용됐다.



<hr>
## 연구 방법



해당 논문은 Aspect Based Sentiment Analysis 기술을 사용해서 전기차 사용자 리뷰 내의 **주요 Aspect 선정** 및 **해당 Aspect 과 관련된 의견 식별 및 감성 극성 추출** 하고자 한다.





![스크린샷 2022-03-18 오후 1.56.07](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 1.56.07.png)





먼저 주요 Aspect (major aspect) 를 추출해서 A라고 칭했다고 가정해보자.

그런 다음 aspect A에 포함되는 문장들을 모두 선별해서 ML 모델 또는 Lexicon 기반으로 각각에 감성을 부여한다.(판별한다.)

그리고 주요 aspect 의 상세 스펙과 aspect 에 대한 사용자의 감성 간의 상관관계를 확인한다.



그 다음으로 주요 aspect 의 상세 스펙(factor라고 칭하겠다.)과 Aspect 에 대한 사용자의 감성 간의 상관관계를 확인해보고,

**회귀분석** 을 통해서 **영향력 있는 변수**가 무엇인지 탐색한다.

ex) Aspect : 차량의 Size, 차량 Size 에 관련된 주요 변수(factors) : wheel base의 크기, 옆면 길이, 후면 길이, 차량 높이 등

factors들을 crawling 으로 추출.

(변수와 차량 size) 에 대한 사용자의 긍정/부정 감성 간의 관계를 확인하는 것.



### 데이터 수집



내가 연구를 할 때, 데이터를 얻을 수 있는 방법을 참고하면 좋을 거 같다.



1. Labe Data
   - 자동차 포럼 상의 리뷰 별로 사용자 만족도 Label 이 존재하는 리뷰 텍스트 Dataset
2. Non-Label Data
   - Youtube.com 의 사용자 만족도 Label 이 없는 Comment Dataset



#### Label 데이터 수집



자동차 포럼(Car Forums)에서 수집 => 가능한 많은 사용자 리뷰를 보유하고 있는 website 참고

Edmunds.com, Edmunds.com => 에서 수집

**By using Beautiful Soup** => 각 자동차 포럼 내 주요 정보를 추출하고 Query 시 효과적으로 정보를 추출하기 위한 양식의 데이터 프레임을 별도 구축하여 이에 저장.



152개의 차종에 대해, 총 5,065 건의 Label 이 있는 사용자 리뷰를 수집.



#### Non Label 데이터 수집



사용자의 만족도 Label 이 존재하지 않는 리뷰. sns나 웹에서 쉽게 접할 수 있는 텍스트 리뷰를 의미한다. => youtube 리뷰들을 대상으로 했다.



대상 차량은 Label 데이터에 존재하는 차량 list 들을 참조했다.

by using Selenium API => 자동 검색 및 Scroll Down 하여 Crawling 했다.



"제조사 - 모델명 – 생산 년도" => 미리 저장.

=> "제조사명 + 모델명 + 생산 년도 + Review" 자동 조합(예를 들면 “Tesla + model-s + 2018 + review”)



저장 Data Frame은 Label Data와 동일



 Youtube.com으로부터 얻는 Non-labeled 사용자 의견들을 모두 사용할 수는 없기 때문에 연구 목적에 맞게 UX 관련 내용의 Comment만 선별. (UX Keyword가 있는 Comment만 선별)



> UX Keyword = {I bought", “I ordered", “I buy", "my experience", “I experienced", “I choose", “I chose", "ve chosen", "driven", “I drove", “I purchased", “I own", "ve own", “I am owner", “I use", "ve used", “I used", “I was satisfied", "ve been satisfied"}



=> 전기차 Model 명이 반드시 들어가는 리뷰만 선별 -> comment 에서 사용자 경험이 해당 스트리밍 제목의 차종의 Model 일 가능성을 높였다.





label 데이터와 non label 데이터의 감성값 분포를 확인해보면 다음 아래와 같은 결과를 얻는다. (Lexicon 기반 감성 분석 값의 분포)



![스크린샷 2022-03-18 오후 2.21.57](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 2.21.57.png)





포럼 웹사이트를 통해서 획득한 label 데이터의 경우 부정 323, 중립96, 긍정 4,637rjs

중립과 부정의견의 비율이 8.4%에 불과. 데이터 불균형.





Non Label 의 경우 총 6,488개 중, 부정 881건, 중립 566건 긍정 5,041건

중립과 부정의견의 비율이 22.4%(1,447건)

sns상 자유롭게 게재하는 의견이 자동차 포럼상의 사용자 경험보다 덜 편향.

sns review 를 함께 사용하면 긍정으로 치우친 제품 리뷰의 편향성을 극복할 수 있을 것으로 보인다.

=> label 데이터보다는 낫다지만, 절대적으로는 불균형한게 맞으므로 데이터 불균형 문제를 꼭 해결해야만 한다.





### 데이터 전처리



수집된 텍스트들을 대상으로 **삭제(Remove)** 및 **교체(Replace)** 작업을 진행한다.

이와 관련된 skill

![스크린샷 2022-03-18 오후 2.28.26](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 2.28.26.png)



- 필요 없는 어휘와 불용어를 삭제하고 어휘를 표준화하는 작업
- 텍스트를 단어 단위로 토크나이징하기 -> 품사 태깅(Part of Speech Tagging) -> 표제어 추출(Lemmatization) -> 주로 명사와 형용사가 중요한 entitiy



By using nltk library of python



![스크린샷 2022-03-18 오후 2.31.24](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 2.31.24.png)



전처리 후 추출한 표제어(Lemma) 들을 **빈도수 순서**대로 나열한 그래프.



Car, Drive, Mile, Charge 와 같은 단어가 가장 많이 나왔다.

car를 비롯해서 쉽고 흔하게 등장하는 어휘나 텍스트 분석에 크게 중요하지 않은 단어들을 stopwords 리스트에 넣었다.

(자동차 모델 간 관련성 및 유사성을 파악하는 논문이 아니기 때문에 제조사명, 모델명은 전부 stopwords 로 집어 넣음.)



### Aspect-Based Sentiment Analysis 수행



1. Aspect Extraction
   - 각 리뷰에서 내재된 모든 제품 Component와 Attribute 를 찾는다.
2. Sentiment Analysis
   - **sentence 단위** 감성 예측 모델을 위한 Sentiment Analysis 과정 



> 텍스트트 언어학적으로 계층적 구조로 이루어져 있다. -> Document, paragraph, sentence, word (Hierarchical Structure)
>
> ABSA 수행 시 어느 수준 (Level) 에서 감성 분석을 진행할지 결정하는 것.



현 논문에서는 ASPECT 단위로 사용자의 감성을 분류한다. =>( 명사와 형용사 단어들을 기준으로 감성을 분류하는 거 같은데, 왜 위에서는 sentence 단위라고 했을까? 이 단어를 포함하는 sentence 에 대한 감성 분석이기 때문에 sentence level 의 감성 분석이라고 한건가?)



다른 데이터 셋을 이용해서 내가 ASPECT 감성 분석을 연습하고 싶을 때, 사용하는 공동 데이터들이 있는데 이 데이터들은 보통 문장 또는 문서 단위로 aspect 정답 label 들이 존재한다. (label 이 문장 또는 문서) => 이때는sentiment analysis 를 문장 또는 문서 단위로!



#### 요소 추출(Aspect Extraction)



1. TextRank

   - N-grams 및 Collocation을 얻기 위한 목적
   - 1. TextRank 는 그래프 기반 모델이므로 그래프를 만들어야 한다.
        - 각 어휘는 그래프의 Vertext(node 라고 이해했음) 역할
        - weighted edge matrix 는 모든 vertex 들 사이의 edge 연결 정보를 모두 포함하고 있다.
        - Weighted_edge[i] [j] 는 어휘 인덱스 i로 표현되 단어 vertex 와 어휘 j로 표현된 단어 vertex 사이의 연결 Edge. weight 값을 저장. (Ex Weighted_edge[i] [j] == 0, edge 연결이 없음)
        - text 에서 window size의 window 내에서 단어가 공존하는 경우, 단어 간에 연결이 있다. (true/false)
        - Weighted_edge[i] [j]  의 connection edge 값은 text 내의 서로 다른 위치에서 동일한 단어 사이에서 발견된 모든 연결에 대해 "1/i와 j의 거리" 만큼 증가한다.
        - covered_co_occurence 목록을 생성해서 pairs of absolute positions 목록을 생성하여 동일한 위칭 ㅔ 있는 동일한 두 단어가 반복적으로 계산되지 않도록 했다.
     2. Vertext의 TextRank 점수를 매기고 Key Phrases 의 순위를 확인하는 과정
        - ![스크린샷 2022-03-18 오후 3.04.44](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 3.04.44.png)
        - vertext i 에 대해 연결되어 있는 vertex j에 대한 scoring 은 위와 같이 계산된다.

2. Naive Method

   - 존재하는 모든 독립 어휘(명사)를 추출하는 데 조금 더 주안점을 두었다

   - 형용사와 (Adject) 와 명사(Noun) 에  한하여 연속적으로 등장하는 모든 단어 조합을 수집한 후, Redundancy Pruning을 거쳐 명사구(Noun Phrase) 와 연어(collocation) 을 얻는 방법.

     > 연어=> 형용사 + 명사 조합의 연어라고 이해했다.

   - 연속적으로 등장하는 명사(명사구) 수집을 통해 **전기차의 부품 용어** 나 **사용자들이 자주 사용하는 전기차 관련 용어**를 얻고자 했다.

   - 형용사를 통해서는 전기차에 대해 느끼는 주요 감성 어휘를 얻을 수 있을 것으로 기대했다.

   - 의미론적으로나 단어 위치 기반으로 count 하는 게 아니고 모든 명사(1개 이상 연속적으로 등장하는)를 고려하는 방법이기 때문에 Naive Method 라고 이름을 붙였다.

   - Redundancy Pruning

     - 추출된 명사구 및 연어에 대해 공통 단어(common word) 의 비중이 50% 이상인 경우 Redundancy(중복성) 가 높다고 판단하여 제거했다.

     - 공통 단어의 기준은 해당 단어가 나타나는 빈도가 전체의 10%를 넘을 경우로 정의했다.

     - > 10%의 빈도수를 넘는 단어는 공통 단어로 지정이 되고 공통 단어의 비중이 50%이상인 경우 제거했다.

       

   - 일정 Threshold 이상 어휘만을 선별했다.(frequency 기반)

     - 5번 이상 등장할 경우



#### 감성 분석(Sentiment Analysis)



논문에서 다루는 데이터셋은 문단 또는 문장 별 aspect 정답 label 이 존재하지 않는 데이터. => **aspect가 포함된 "문장(sentence)" level 의 감성 극성(sentiment polarity) 를 파악했다.**



기계학습 모델 기반으로 Aspect 가 포함된 문장 단위 긍정/부정 예측 모델링을 수행하고자 했다.

=> label 데이터가 충분하지 않아 문장의 감성이 정확하게 분류되지 않을 수 있다는 점을 고려해서 Lexicon based 감성 분석을 병행하여 보완했다.



##### 기계학습 기반 감성 분석

review 단위로 사용자 만족도 label이 있는 **텍스트를 학습시킨 기계학습 모델** 기반으로 문장의 감성을 예측했다.



> 논문에서는, 리뷰의 첫 한 두 문장과 리뷰 단위 평점 데이터를 학습 데이터로 사용하고, Aspect가 포함된 문장에 대한 추론을 진행했다.



리뷰 단위로 **만족도 label 이 있는 데이터**를 대상으로 **기계학습 모델에 학습**시키는 과정

1. 임베딩을 위한 전처리 과정 (input 값 전처리?)
   - 전처리가 완료된 리뷰 텍스트들의 평균 길이보다 약간 작게 문장의 길이를 제한했다.
   - 절단된 리뷰(Truncated Review) => 문장 길이를 약 150 단어로 제한하여 절단했다.
   - 150개 이상일시 잘라내고, 150개가 안되면 zero-padding 을 하여 길이를 맞췄다.
2. 문장 임베딩 과정 (representation 획득)
   - 단어를 밀집 벡터(Dense Vector) 의 형태로 표현하는 방법
   - 1. TF-IDF(Term Frequency-Inverse Document Frequency)
        - 희소표현(Sparse Representation) 인 문서 단어 행렬 DTM 으로 만들고 그 후 TF-IDF 가중치를 부여하는 방법
     2. Glove
        - 모든 단어가 100차원의 밀집 벡터 형태로 표현될 수 있도록 했다.
        - 논문의 연구는 텍스트 전체 말뭉치 내에서 동시 등장확률을 고려하고자 하는 컨셉
        - 두 단어벡터의 내적이 말뭉치 전체에서의 동시 등장확률의 Log scale값이 되도록 목적함수를 정의한 Glove 사용.
     3. Random Initialization => 나는 word2vec 으로 봤다.
        - 단어벡터의 초기값으로 무작위의 Index 값을 부여하는 방법.
        - index 값은 사용자가 지정한 단어벡터 차원의 수 중 하나.
        - 텍스트 분류를 가장 잘하는 방식으로 초기값을 없데이트 한다.
3. Data Augmentation(불균형 데이터 극복 위한)
   - 불균형 데이터의 경우 정확도는 높아도 재현율 및 f1 score 가 급격히 떨어진다.
   - 언더샘플링(Under sampling) 과 오버샘플링(Over Sampling)
   - 언더샘플링
     - Minority Class 의 개수에 맞추기 위해 Majority Class 에 있는 데이터의 일부를 샘플링
     - 즉 크기가 작은 class의 숫자에 맞추기 위해서 크기가 큰 class들의 데이터를 일부만 샘플링
     - 데이터가 지나치게 작아진다. => 본 논문에서는 사용하지 않는다.
   - 오버샘플링
     - 1. 무작위로 소수 데이터를 복제하는 무작위 추출
          - 과적합(overfitting) 문제를 야기한다.
       2. 사전에 기준을 정해서 소수 데이터만 복제하는 방식
          - 과적합(overfitting) 문제를 야기한다.
       3. 합성 데이터를 생성하는 방식 (노션 블로그 참조)
          - SMOTE(Synthetic Minority Oversampling TEchnique)
            - 데이터의 개수가 적은 클래스의 표본을 가져온 뒤, 임의의 값을 추가해 새로운 합성데이터를 생성하여 데이터에 추가하는 방식 => SMOTE 를 활용한 **Borderline-SMOTE** 방법을 적용
          - Borderline-SMOTE
            - SMOTE 알고리즘이 단순이 개수가 적은 클래스의 표본을 랜덤하게 샘플링했다며 이 모델은 다른 class와의 경계에 있는 샘플의 수를 증가시켜서 분류하기 어려운 부분에 집중했다.
4. 기계학습 모델 선정
   - 로지스틱 회귀분석 분류기를 기본으로 둔다. (기본적으로 긍정/부정의 binary 분류기 때문에)
   - 추가적으로 svm, naive bayes 그리고 로지스틱 회귀분석을 사용했다.
     - 1. Support Vector Machine(SVM)
          - 클래스 사이의 Margin을 최대화하는 초평면(Hyperplane) 을 찾는 방법
          - 해당 초평면에 걸쳐서 이를 지지하는 관측치들을 Suppor Vector 라고 한다.
          - 커널트릭을 사용해서 주어진 데이터를 고차원 특징 공간으로 사상한다.(projection)
            - Non_linear 문제를 linear 문제로 변환하여 고차원 공간의 데이터를 선형 분리할 수 있다.
          - 고차원의 데이터를 다중공산성 문제를 회피하여 원활하게 분류할 수 있다.(텍스트와 같은 고차원 인풋에 효과적으로 작동할 수 있다고 판단)
          - 이 논문에는 RBF Kernel 사용
       2. Naive Bayes(NB)
          - 텍스트 분류에 준수한 성능을 보여주는 알고리즘
          - 베이즈 이론(Bayes theorem) 의 확률 모델 기반.
          - 전체 corpus 내 각 단어의 빈도 수를 count, 사전확률과 우도를 모두 구하는 방법으로 학습
          - 사전확률과 우도의 곱을 계산하는 방식으로 예측
          - 단, 단어 간 서로 독립이라는 가정하에 등장확률을 계산한다. 또한 단어의 등장 순서를 무시하고 문서 내 빈도수만을 따져서 문서를 표현(bag or words) 기법과 잘어울린다.
       3. Convolutional Neural Newwork(CNN)
          - 텍스트에 내재된 공간적인 구조 정보를 보존하면서 학습할 수 있는 방법 (단어나 표현의 등장 순서 고려)
          - 각 단어가 벡터로 변환된 문장 행렬을 입력으로 받는 1D CNN 모델을 설계
       4. 양방향 LSTM 과 어텐션 메커니즘 (Bi-LSTM with Attention)
          - 밑바닥부터 시작하는 딥러닝 LSTM 개선 부분 참조
       5. 준지도학습(Semi-Supervised Learning)
          - Self-training 을 활용했다.
          - 위의 준지도학습 관련 그림 참조
          - 처음 학습된 teacher model 의 확률이 높은 데이터의 threshold 는 85%로 지정했다.
            - 분류기가 85%이상의 확률로 확신하는 분류 결과만 Label 부여.
          - 데이터 불균형 문제를 조금이나마 해소하고자 했기 때문에 사용.
       6. 절단된 리뷰(Truncated Text) 를 학습한 모델 간 성능 비교
          - 가장 나은 모델에 대하여 준지도학습을 통해 분류 성능 개선.
       7. 지금까지 학습된 모델에 Aspect 가 포함된 문장을 input 으로 넣어 감성 예측.
          - 리뷰의 도입부 150길이를 학습한 모델에, 문장 단위 텍스트를 입력해 감성 예측
          - 단, 데이터가 부족하여 감성 분류를 제대로 못할 것을 대비해서 Lexicon Based 감성 분류도 병행했다.
   - 전통적인 기계학습 모델의 분류 성능과 딥러닝 기반의 모델 예측 성능을 비교하는 방법으로 진행





##### Lexicon 기반 감성 분석



머신러닝 기반 접근 방식과 비교해보기 위해서 Lexicon base 로 input 문장에 대한 감성 분석을 시행했다.

(nltk 의 textblob을 사용)



#### A Framework for UX Analysis



1. 요소 추출(Aspect Extraction)
   - TextRank 와 Naive Method 적용
2. 감성 분석 (Sentiment Analysis)
   - 기계학습 기반의 감성 분석과 Lexicon 기반 감성분석을 병렬적으로 진행해 비교
   - 1. 기계학습 기반
        - 리뷰의 첫 한 두 문장만을 잘라낸 Truncated Text 를 학습
        - 텍스트 분류에서 적합한 SVM, NB 및 신경망 모델을 사용한다.
        - 학습된 모델을 활용해서 높은 확률을 보이는 class들에 대해서 label을 부여하는 준지도 학습의 한 형태인 Self Training 방법을 사용
        - 추출된 Aspect 가 포함된 문장을 불러와 학습된 모델로 긍정/부정 감성을 예측=> aspect 단위 감성 분석 진행
     2. Lexicon 기반



논문에서 사용한 Frame work 도식화.



![스크린샷 2022-03-18 오후 4.48.45](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 4.48.45.png)



## 연구 결과



### 요소 추출(Asapect Extraction) 결과





![스크린샷 2022-03-18 오후 4.52.40](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-18 오후 4.52.40.png)

 



전기차의 major Aspect(구성 부품 요소(component)와 사용자 특성(Attribute) 요소) 추출 완료된 그림.

> 8개의 component
>
> 8개의 Attribute 확인



사용자들의 불만 사항 및 니즈를 직접적으로 추출할 수 있는 단어들의 카테고리도 얻을 수 있었다.

사용자 맥락과 관련된 단어들도 얻을 수 있었다.



=> 만약 내가 aspects 들을 추출했으면 나타낸 aspects 들의 유형을 확인해서 직접 카테고리화 해야할듯 하다.



### 감성 분석(Sentiment Analysis) 을 위한 모델링 결과



#### 기계학습 기반 감성 분류 결과에 대한 모델 별 성능 비교



총 6개의 모델을 적용.

**리뷰 단위** 로 긍정/부정 Label 이 있는 데이터를 학습한 감성 분류 모델링 결과.

CNN 이 가장 좋은 성능 보였고 예상 외로 attention 기반의 모델들이 좋은 성능을 보이지 않았다.

=> 논문 저자는 데이터셋이 충분하지 못하여 단어 간의 배열 순서 정보나 단어-문장으로 이어지는 계층 구조에 대해서 학습하지 못했기 때문에 나타난 현상이라고 이해한다.



성능 지표로는  정확도(Accuracy) 를 사용하지 않고 Recall, Precision 의 산술 평균인 F1-Score 를 사용했다.



![스크린샷 2022-03-21 오전 9.54.20](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 9.54.20.png)



#### 준지도학습(Semi Supervised Learning) 실험 결과



![스크린샷 2022-03-21 오전 9.57.29](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 9.57.29.png)



왼쪽의 그림은 준지도학습 전의 Label 데이터를 학습한 CNN 모델의 테스트 결과.

오른쪽 그림은 준지도학습을 마친 CNN 모델의 테스트 결과.

Loss 는 늘었지만 F1 SCORE 는 0.1 증가 => 이를 통해서 준지도학습을 이용한 ABSA 방법의 타당성 증명



> NON-LABEL 되어 있던 데이터를 teacher model 을 이용해서 확률이 높은 class 에 Label 을 붙여 데이터를 보강한 이후, labeled(?)_NON-LABEL 데이터와 label 데이터를 함께 이용해서 만든 model 의 성능을 비교





### Aspect-Based Sentiment Analysis 결과



#### 기계학습 모델 기반 ABSA 결과

![스크린샷 2022-03-21 오전 10.01.26](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.01.26.png)

Aspect 추출 이후, Aspect 에 대해서 감성 분석을 한 결과.

빈도수와 감성 분석 결과값을 동시에 보여준다.



추출된 Aspect 가 포함된 문장 level 에 대한 감성 분석 결과를 최종 Model 이 return 할텐데, 이때 모델의 성능을 평가하기 위해서 문장 단위의 감성에 대한 정답 데이터가 필요하다.

어쩔 수 없이 **휴먼 라벨링(Labeling)** 을 시행하는데, 이때 sample 의 수가 많은 건 라벨링 하기에 시간과 비용이 많이 들기 때문에 평가하고자 하는 aspect 의 sample 의 개수가 적은 것을 선택하여 휴먼 라벨링을 진행한다.



논문에서는 "Ergonomic" aspect (sample = 51) 을 선택했으며 positive : 38, negative : 13 개다.

휴먼 라벨링과 모델의 예측을 비교해서 성능을 출력한 결과 "Ergonomic" aspect 가 포함된 문장 Level 감성 분류 정확도는 **약 92.1%**  를 보였다.



#### Lexicon 기반 ABSA 결과



![스크린샷 2022-03-21 오전 10.10.27](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.10.27.png)





Lexicon 기반으로 aspect를 포함한 문장에 대해서 감성 분석을 실행하게 되면 negative -1 ~ positive 1 사이의 값을 가지게 된다.

위 그림의 상단 Boxplot 을 확인해 보면 asepct 별 사용자의 긍정/부정 감성의 밀집도 및 편차를 확인할 수 있다.

(boxplot 으로 해당 aspect를 포함한 문장의 감성 값들의 분포를 확인할 수 있다. )

위 그림의 하단 분포 그래프를 확인해보면, 점 하나는 해당 aspect의 감성 값이라고 할 수 있고, 이 값들을 y축을 기준으로 찍어서 나타내면 분포 모양을 확인할 수 있다. 확인 결과 부정적인 aspect에 대해서는 y축 값 0을 기준으로 0 하단에 찍히는 것들을 확인할 수 있고, 긍정적인 aspect 에 대해서는 y축 값 0 을 기준으로 상단에 찍히는 경향을 볼 수 있다.

> positive : Room, Interior, Acceleration, Visibility, Safety
>
> negative : Charge, Battery, Power, Ice, Noise



![스크린샷 2022-03-21 오전 10.14.49](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.14.49.png)



기계학습 기반의 감성 예측 결과와 Lexicon 기반의 감성 분석 결과는 3개 항목(Noise, Winter, Ice) 을 제외한 14개 항목에서 긍정/부정 *예측 방향성*이 일치했다.

대부분 aspect에 대한 감성 분류 예측이 유사했기 때문에 안정적이라고 판단.



> 예측 방향성이 일치한다 => 하나의 Aspect 에 대한 긍정/부정 감성 분류 비율이 Lexicon 기반 모델과 ML 기반 모델이 서로 유사한 것을 의미한다.
>
> Noise 에서 Lexicon 은 부정으로 다수 예측한 반면에 ML 기반 모델은 긍정으로 다수 예측하여 불일치.





### 사용자 긍/부정 경험에 영향을 미치는 Contributing Factor



특정 Aspect 에 대한 차량의 상세 스펙(X) 와 사용자의 감성(y) 간의 관계를 *"상관관계분석"* 과 *"다중회귀분석"* 을 통해 확인.



“Leg Room” Aspect 의 상세 스펙인 Front leg room 의 실제 치수 X와 Leg Room 에 대한 Lexicon 기반 감성 점수 y 간의 상관 관계를 나타낸 그래프

=> 유의미한 결과를 얻지 못했다.

![스크린샷 2022-03-21 오전 10.26.12](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.26.12.png)





 Room 은 다양한 상세 스펙들을 가지고 있는데, 이 상세 스펙들을 모두 변수로 취급해서 Room 대한 사용자 감성 극성(y) 과 상세 스펙들(x) 간 다중회귀분석을 실행.

=> R^2 값이 0.096 으로 의미있는 결과를 얻지 못했으며 다른 Aspects 들에 대해서도 동일한 결과를 얻었다.



![스크린샷 2022-03-21 오전 10.28.39](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.28.39.png)



<hr>





## 결론



### 결론



위의 과정을 통해서 얻은 몇 가지 결론점.



- 전기차의 사용자 리뷰로부터 형용사와 명사 중심의 명사구 추출을 통해 차량 요소를 추출한 결과(Navied method..?) , 전기차의 다양한 구성 요소(Components) 들 뿐만 아니라, Human Factor 특성(Attribute) 를 추출할 수 있음을 확인
- Aspect 단위의 감성분석을 통해 Review 단위 감성 분석 대비 더욱 다양한 의견을 얻을 수 있다.

(review-wise 그래프를 보면 class 한쪽에 치우쳐져 분석하고 있음을 볼 수 있다.

aspect-wise 경우 다양한 분포를 확인할 수 있다.)

![스크린샷 2022-03-21 오전 10.32.45](/Users/jang-eunjun/Desktop/TIL/DataAnalysis/PaperReview/ABSA/LG_ABSA/기계학습을 이용한 ABSA 기반 전기차 요소별 감성분석및 예측 모델링/이미지/스크린샷 2022-03-21 오전 10.32.45.png)

- Minority Class 에 대해 오버생플링(Over-sampling)을 통해 데이터의 불균형 문제를 극복할 수 있음을 확인.

- 준지도학습(Semi Supervised Learning) 을 통한 분류 성능 개선을 확인. Label 이 없는 데이터에 대한 활용 방법을 제시(Youtube 크롤링 자료 같은 것들)

- 리뷰의 도입부 감성 극성이 전체 리뷰의 감성을 결정한다는 전제하에 **절단된 리뷰 학습을 통한 문장 분류가 효과적일 수 있음** 을 확인.(Truncated Text 활용)

- 기계학습을 이용한 ABSA 기반으로 UX 를 분석해 전기차의 긍정적 요소와 부정적 요소를 확인할 수 있었다.

  - 부정적 요소의 경우 동시 출현(Co-occurrence) *빈도수 기반 연관 어휘*와 함께 *해석*을 통해 사용자의 니즈를 발굴할 수 있었다.

    



### 연구 기여(Contribution)



이 논문은 ASPECT 별 사용자 긍정/부정 감성 분포를 통해서 부정적인 의견이 많은 aspect 탐지를 쉽게 할 수 있는 UX 분석 프레임워크를 개발했다.



문장별 감성 분석 및 사용 목적에 맞게 추가적인 분석을 진행할 수 있는 시스템을 개발하여 세분화된 사용자/고객 조사가 필요한 관련 분야에 기여했다.



### 한계점(Limitation)



지도학습 기반의 문장의 감성 예측 모델링을 구현하고자 했으며, 문장 level 에 대한 감성 Label 값이 존재하지 않기 때문에 사용자 리류 서두의 1~2문장을 학습한 모델을 활용해서 문장단위 감성 분석을 진행했다.

데이터가 더욱 많아지면 연구 정확도가 더 높아질 것으로 예상되는데, Label 데이터가 부족한 상황에서는 양질의 Non-label 데이터의 수를 많이 얻어 보강한다면 성능이 더 높아질 것으로 예상된다.



Non-label 데이터들 중에서 UX를 나타내는 텍스트만 선별해내는 기술이 강화되면 더 나은 모델을 만들 수 있을 것으로 예상된다.

aspect의 상세 스펙과 사용자의 감성의 상관 관계 파악을 할 때 잘 수행이 되지 않았는데, 더 많은 변수들이 고려가 되면 상관 관계를 잘 파악할 수 있을 것으로 보인다.

=> 사용자의 키와 몸무게, 팔다리 길이 등의 신체적 조건을 독립 변수로 활용 가능할 때 더욱 의미 있는 결괄 얻을 수 있을 것으로 예상한다. (추가적인 변수들)

































