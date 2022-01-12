# OBIM: A computational model to estimate brand image from online Paper Review



## Abstract



이 논문은 소비자 리뷰들로부터, 브랜드 이미지를 수치로 정량화 할 수 있는 모델 OBIM 을 소개하려고 함.





브랜드 이미지는 3개의 주요 brand associations 와 관련있다.

"favourability", "strength", "uniqueness"



따라서, 우리는 브랜드 이미지를 알아내기 위해서 이 associations 들을 알아내야만 한다.

이 글은 NLP 기술을 이용해서 리뷰 데이터로부터 associations 들을 추출하려고 한다.





이 추출된 3개의 associations 들은 sentiment, co-word network analysis 로 계산된다.

최종적으로 이 계산된 수치들(OBIM VALUE)의 합이 OBIM SCORE 이다.

이렇게 구해진 OBIM SCORE는 소비자들의 관점을 측정하는데 사용되어지고, 시간이 지남에 따라서 브랜드에 대한 associations 들이 어떻게 변하는지 알려준다.



그리고 OBIM SCORE 이 응용되는 분야가 있는데 바로, SWOT 분석과 숨겨진 Concept을 찾는 Senti Concept Mapper technique => 이 두 가지 기술이 어떻게 마켓팅에 OBIM SCORE 가 도움이 되는지 보여준다.



<HR>

## Introduction





브랜드 이미지는 마켓팅 전략에 굉장히 중요하게 작용한다.

이 브랜드 이미지는 소비자의 기억 속에 있는 brand association 네트워크에 따라 만들어진다.

즉 소비자들이 브랜드를 생각하면 떠오르는 연상들로 브랜드 이미지가 정의 내려진다.



특히,  소비자들이 브랜드에 대해 가지는 favourability, strength, unique 연상들로 브랜드 이미지가 만들어진다.

따라서 브랜드들은 소비자들로 하여금 브랜드에 대해서  강력하고 독특하고 호의적인 연상을 심어주려고 한다.



따라서 마켓터들은 소비자들의 이러한 연상들을 파악하고 탐구해야 하는데, 소비자들이 브랜드에 관해서 가지는 연상들을 파악하기란 쉽지 않다.



그러나,

이 논문은 소비자들의 "리뷰 text" 를 이용하면 소비자들의 연상을 파악할 수 있다고 생각했다.

왜냐하면 리뷰가 소비자들이 제품에 대해서 가지는 생각이나 연상들을 담고 있기 때문이다.

그래서 논문은 리뷰 text 를 이용해서 소비자 연상을 추출하는 법을 소개하려고 한다.



논문은 OBIM 모델을 사용해서 favourability, strength, unique 를 정량화, 수치화 하려고 한다

먼저 favourability 측정법은 두 가지 step을 거친다.

1. Aspects 을 double propagation technique을 이용해서 추출한다.
   - (이 Aspect 를 brand association 으로 간주한다.)
2. 사전 기반 감성 분석을 이용해서 각 Aspect 에 관한 점수를 매긴다.



Strength 와 unique 수치를 구할 때 가장 기초가 되는 건 co-word network 다.

co-word network는 review corpus 안에 있는 단어들을 이용해서  만들며 각 link 에 weight를 부여한다.

이 weight 들은 단어 동시 발생을 정규화한 수치다.

Strength 는 이 노드들의 간선(edge) 수치들의 평균이다.



aspect2(Phone)



|

|



aspect1(Performance)	 ㅡ ㅡ	a spect3(Camera)



Phone 과 Performance 가 동시 발생한 횟수가 1이라고 했을 때, 이 1을 정규화해서 Phone 과 Performance 노드간 link 에 weight 를 부여한다. 이 방식으로 Phone 과 연결된 모든 노드 링크에 weight 를 부여한다음, 이 값들에 평균 값을 내면 Phone 과 관련된 Strength 연상 수치.



unique 수치는 선의 수치와 선의 중요성을 연장해서 도출된다.(DIL 기법)



이렇게 구해진 세 개의 수치화된 연상을 이용해서 OBIM SCORE 를 구한다.



이렇게 구해진 OBIM SCORE 는 회사의 ASSOCIATIONS 기반 SWOT 분석에 사용이 되는데, 회사의 강점, 약점, 기회, 위협을 도출한다. 그리고 회사의 숨겨진 Concept 을 찾는 Senti-Concept Mapper 에 사용이 된다. (co-word 네트워크 서브 그래프로부터 브랜드 연상들과 관련된 개념들을 발견)



(OBIM SCORE 가 구해지는 과정을 보면, 주요 이론 기반이 Aspect 기반의 sentiment 와 co-words 임을 알고 있자.)



##### Specific Contribution



1. Aspect 를 온라인 리뷰로부터 추출할건데, 이 Aspect 를 brand association 으로 간주한다. 그리고 이미 존재하는 감성 lexicon 을 사용하여 브랜드 brand associations을 찾는다.
2. 비정형 자료에서 association 을 계산할거라 그 이전과는 다르다.
3. 이전 연구자와는 다른데, 상품에 관련된 단어들을 고려하고 strength 를 구했기 때문에 다르다. DIL 방법을 사용해서 uniqueness 수치를 구한다.
4. OBIM SCORE 를 세 개의 주요 brand association 을 결합해서 구한 최초의 사례.
5. OBIM SCORE 를 SWOT 분석에 사용할 것.
6. Senti - Concept Mapper 을 사용해서 숨겨진 Concept 을 찾을 것.

   

<hr>



## Literature Review



이 파트에서는 주로 브랜드 이미지를 추정하는 기술들을 리뷰할 것.



Aspect Based sentiment analysis, 

Co-word  network 



1. favourability 를 text sentiment 분석을 통해서 구한다.
   - 문서 전체에 대해서 감성분석을 하는 게 아니라 Aspect 기반으로 감성 분석을 한다. (Aspect Based sentiment analysis 사용)
   - Aspect는 제품의 특정 기능인데, 이 기능은 브랜드에 해당하는 연상을 인식한다.
   - Aspect 를 추출하는 방법은 크게 3가지로 구분이 된다.
   - 1. Frequency-based
     2. Supervised Machine Learning based :
        - label 을 붙인 데이터를 사용하는데, 이는 비용이 너무 많이 드는 문제가 발생.
        - 딥러닝을 이용해서 Aspect 를 추출하면 좋은데 비용적인 문제가 있다.
     3. Syntax-based
        - 문장 구조를 이용해서 Aspect 를 추출한다.
        - 알려진 opinion word 를 이용해서 aspect 를 추출한다.
2. Strength 와 Unique 를 Co-word 네트워크를 분석하여 도출
   - associative memory 는 굉장히 중요
   - co-word 는 association network 를 만듬.
   - co-word 내에서, 노드의 의미적 연결성을 의미한다.



<hr>

## Methodology





1. 전처리

   - HTML TAG, 특수문자 등의 TEXT에서 분석에 불필요한 내용을 지우기.
2. Favourability 수치 계산하기

   - Aspect 를 brand association 으로 정함
   - 그러나 리뷰의 모든 단어들을 Aspect로 정하지 않음. 왜냐하면, 모든 문서로 정할 경우 상품에 관련된 aspect 가 아니라 브랜드와 관련 없는 단어들이 aspect 가 될 가능성이 있음.
   - Nice phone with amazing performance. 를 모든 단어로 aspect 취한다면, "Nice", "phone","with", "amazing","performance", 하지만 nice는 phone과의 연관성이고 amzaing 은 performance와의 전체 연관성이다. 소비자들은 상품의 중요한 측면을 분석한다.
   - 따라서 상품의 aspect 를 brand association 으로 간주하자고 제안한다.다시 말하자면 모든 단어들을 aspect 로 정한는 게 아니라 상품과 관련된 명사 -> aspect들만 brand association 으로 간주.
   - Vader 방식 사용해서 aspect 를 추출한다.
   - 그 다음 문장의 구문론적 구조를 사용하는데, 수식어가 붙은 명사를 aspect로 지정한다.
   - 여기서 우리는 aspect를 추출할 때, double propagation approach 를 사용한다. 여기서 우리가 사용할 규칙은 두 가지.
     - 만일 opinion word 가 target  word에 형용사나 명사 수식을 하면 target word 는 aspect로 받아진다.
     - 형용사나 명사수식과 직접적인 관련이 있는 opinion word가 있고 target word가 똑같이 그 단어에 연관 있으면 target word로 채택 (예, The phone has the best camera)
     - opinion 과 aspects 간의 조합은 감성분석을 하기 위해서 남겨둔다.
   - 비지도 방식의 vader 기법을 사용하는데, opinion 에 대해서 분석한다. 분석을 한 값은 -1 ~ 1 을 갖고, -1에 가까울수록 부정 1에 가까울수록 긍정이다. 출력된 값들을 opinion과 aspects 쌍에 적용해서 aspect의 감성 수치를 구한다. 이 값들의 평균이 favourability 점수다.
3. Strength 점수 계산하기

   - aspect 차원에서  strength 점수를 계산할거기 때문에 favourability 점수를 구할 때처럼 똑같이 aspect를 추출한다.
   - co-occurrence matrix 를 만든다. C(i,j), C(i,j) 는 i와 j가 동시에 출현한 빈도를 가진다.
   - wc(i) 는 i단어가 전체 문서에서 등장한 횟수를 의미한다.
   - V = corpus 내에서 unique 단어들의 개수를 의미한다.
   - C(i,j) 를 일반화 해서 NC(i,j) 를 만든다.
     - NC(i,j) 의 값은 i노드와 j노드의 간선 weight 로 간주된다. 이 값은  0 ~ 1 사이의 값을 가진다.
     - 근데, 식에 보면 C(i,j) 의 i, j 가 각각 한 번만 출현하면 C(i,j) 의 값은 1이 된다. 둘이 동시 출현한 횟수가 적음에도 높은 수치를 보이기 때문에 패널티를 부여해서 가중치를 평탄화 시키고 모든 V에 C(i,j) 값을 분배한다. 즉 1/V 를 한다.
     - i단어와 붙어있는 모든 단어들의 NC(i,j) 값을 더하고  노드 n_i 값으로 나누면 S_i 값 즉, Strength 수치가 도출된다.
4. uniqueness 점수 계산하기

   - 다른 제품과 구분되는 특수성을 uniqueness 로 본다. (co-word network 에서)

   - DIL 방법을 사용.

     - local data 사용, neighborhood node, (degree, weight(노드의 중요도를 확인하기 위해서))
     - 두 단계를 사용
       1. 간선의 중요도를 계산
       2. 간선이 붙어있는 노드의 공헌도를 
     - weight 가 붙어있지 않은 그래프 사용.
     - 간선의 weight 를 구하는데, 이 weight 는 importance 를 구하는데 사용된다., 이 weight 를 노드의 contribution 으로 정함. 근데 만일 n_i노드가 1번만 나오면 식이 0이 되고, n_i, n_j 둘다 한 번 나오는데 하필 둘이 관계를 맺어도 값이 0 이된다.
     - 위의 문제를 해결하기 위해서 그냥 노드간 weight 를 contribution 으로 정한다.

     - 이 구해진 N(i,j) , weight 즉, contribution 을 이용해서 그 노드의 중요도를 구한다. 이 값이 바로 uniqueness.
     - 식은 다시 보고 

5. 브랜드 이미지 점수 구하기
   - OBIM VALUE : Favourability * Strength * Uniqueness 를 곱한 값.
   - OBIM SCORE : 모든 OBIM VALUE 를 더한 값, (N번째 OBIM VALUE 까지)
   - N은 CORPUS 내에서 추출한 ASPECTS 들의 개수임.



<HR>

## Demonstration of the proposed framework



1. Description of the dataset
   - Samsung, Coolpad, Lenovo, Motorola and Huawei from Amazon 핸드폰 리뷰 사용
   - 1월부터 오월까지 데이터 사용
   - 이 데이터들 내에서 3~4개 이상의 문장들로 구성된 리뷰들만 채택 
   - Standard 한 Preprocessing 과정을 거침
2. Computing favorability, strength, and uniqueness scores
   - 먼저 단일 명사든 복수 명사든 모두 잠재적인 aspect로 간주한다.
   - double propagation 알고리즘(두 개의 규칙을 사용한) 으로 구문론적 방법을 사용해서 opinion - aspect pair 들을 생성한다.
   - 이 opinion - aspect 쌍으로 각 aspect 에 대한 positive , negative 를 추출하는데, 값이 0 에 가까울수록 negative, 1에 가까울수록 positive 로 배정한다. 그래서 aspect에 대한 감정 값을 평균내면 그게 "Favourability" (먼저 Favourability 구했음)
   -  이제 데이터로부터 "Strength" 구함.
   - co-word 네트워크를 사용하기 위해서 co-word matrix C 를 만듬. C(i,j) 즉, i단어와 j단어가 동시에 출현한 횟수를 Normalization 하면 NC(i,j) 가 되는데 이 값은 i노드와 j노드의 weight 로 간주된다.
   - NC(i,j) 의 모든 값들, 즉 i단어와 붙은 모든 j에 대한 NC(i,j) 값을 더하고, i단어의 degree로 값을 나누면 strength 값이 도출된다.
   - 이제 데이터로부터 "Uniqueness" 를 구한다.
   - 앞서 구한 NC(i, j)는 단어의 importance를 구하는데 사용됨. NC(i,j)의 contribution 을 계산하는 식은 논문에 나와있는 식과 같은데, 만일 단어가 1번만 나온다거나, 두 단어가 한번 나온게 co-occurence를 한 경우에는 그냥 NC(i,j) 를 contribution 으로 간주한다.
   - 이와 같은 방식으로 i와 붙어있는 모든 노드들의 집합 j에 대해서, contribution을 계산하고 모두 더한 후, i단어 노드의 degree 를 일반화한 값을 더해준다. 이 값이 바로 "Uniqueness" 값
   - association network 에 포함된 aspect 들은 모두  "favourability" 값을 구할 때 승인된 aspect들 뿐.
3. Comparision based on brand imagpe attributes
   - 월별로 favourability, strength, uniqueness 를 속성으로 두고 scatter 를 찍으면 각 브랜드들을 시간대별로 performance를 비교할 수 있다.
   - 그리고 그래프로 scatter 를 확인할 수 있지만, 각 속성별로 표를 만들어서 그것대로 비교해도 유의미하다.
4. Calculation of OBIM score
   - OBIM SCORE 로 브랜드를 비교하면 편리하다.



<HR>

## Application of OBIM scores



OBIM SCORE 는 브랜드의 강점 약점,을 친민감, 강점, 독특함 연상들로부터 알려준다.



1. Association based SWOT analysis: A technique for market positioning

   - SWOT(Strength, Weaknesses, Opprotunities, and Threats) 전략에 OBIM SCORE 사용

   - SWOT은 회사의 강점을 탐구하고, 기회들을 탐구하고, 약점을 최소화하면서 위협에 대책한다.

   - OBIM VALUE (각 ASPECT에 대한) 를 오름차순으로 정렬. 그러면 상위 5개 하위 5개의 OBIM VALUE 에 관한 ASPECT 추출 가능하다. 상위 5개는 강점으로, 하위 5개는 약점으로 선정.

   - OBIN VALUE 가 낮은 ASPECT에 대해서 향상 시키는 것이, 브랜드의 내부 강점과 외부 기회에 좋다.

   - 그리고 나브랜드의 위협은 브랜드의 약점으로부터 올 수 있는데, 다른 브랜드에서는 약점이 아니지만 그 브랜드에서는 그 ASPECT 가 약점인 경우에는 그게 브랜드의 위협이 될 수 있다.

     

2. Senti-Concept Mapper : A technique to analyze the sentiment of hidden concepts

   - Senti-Concept Mapper 는 구조화된 컨셉을 brand association 들의 연결로 본다.
   - Senti-Concept Mapper는 숨겨진 concept 을 발견하거나, 이미 드러난 concept 의 감정 수치를 계산한다.
   - 컨셉의 감정이 시간이 변화감에 따라서 어떻게 변화는지 분석할 수 있게 해준다.
   - Concept identification
     1. Camera의 performance 를 중심으로 개념을 채굴하는데 "resolution","performance","battery" 를 고려해서 채굴할 수 있다.
     2. concept 에 새로운 association 을 집어 넣는데 제약이 없다. association "resolution" 은 새로운 연상인 "screen" 을 추가할 수 있다.

3. Sentiment of identified concepts.

   - concepts 의 구성물로 채택된 association 각각의 favourability 값들의 평균이 컨셉의 감정값으로 본다.

<hr>

## Conclusion



1. 한계
   - 지금 현재 product review 에 대해서만 obim score를 적용했는데, online review 에 대해서 적용을 하면 obim score 가 수정될 수 있을 것이다.
   - 수동적인 swot분석과 senti concept mapper 방식인데, 나중에 자동화된 모델이 나올 수 있다.
   - 만일 문장에 감정에 영향을 주는 외부적 요소가 들어간다면, obim score 에 영향을 줄 수 있다.(단어사전대로가 아니라.)
   - 마지막으로, 소비자 관점들은 마켓팅과 같은 프로모션에 의해서 편향되어질 수 있는데, 그러한 편향을 잡는게 모델의 발전을 이루어낼 수 있다.
