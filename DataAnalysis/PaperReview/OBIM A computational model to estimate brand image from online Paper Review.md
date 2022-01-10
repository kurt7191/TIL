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

aspect1(Performance)	ㅡ ㅡ	aspect3(Camera)



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
7. 

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

