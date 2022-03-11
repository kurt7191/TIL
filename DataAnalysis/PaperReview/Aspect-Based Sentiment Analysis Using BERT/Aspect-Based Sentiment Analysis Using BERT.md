# Aspect-Based Sentiment Analysis Using BERT



# Abstract



표준적인 감성 분석은 텍스트의 감성 전반을 분류하는 것을 다룬다.

감성이 텍스트 내에서 어떤 entity, aspect 혹은 topic 에 향하는지에 관한 중요한 정보를 포함하지 않는다.

(다차원 감성 분석을 할 수 없다.)



Aspect-based sentiment analysis (ABSA) 는 기존의 표준적인 감성 분석보다 훨씬 더 복잡한 task 다.

왜냐하면 sentiment 뿐만 아니라  aspects 도 찾아내기 때문이다.



이 논문은 잠재적인 문맥(contextual) word 표현 사용을 보여준다.

여기서 잠재적인 문맥 단어 표현은 사전 학습된 bert 모델로부터 나온다.

그리고 이 사전 학습된 bert 모델을 파인 튜닝한다.



aspect 분류를 위해 도메인 밖의 absa 에 대한 다른 기존 작업은 수행되지 않았었지만 이 논문에서 첫 시도한다.



> 사전 학습된 bert 모델을 이용해서 다운 스트림 태스크에 맞게 파인 튜닝하여 word representation 을 얻는다.





<hr>



## Introduction



NLP 작업에서 opinion mining으로도 알려져 있는 Sentiment analysis는 research 나 산업에서 많이 사용된다.

예를 들어서 소셜 미디어 와 상품 리뷰들에 대해서 감성 분석하는 작업을 실행한다.

기업들이 이러한 작업을 많이 수행한 이유는 고객들의 브랜드와 상품, 이념 그리고 특정 주제에 대해서 어떻게 생각하는지는 회사에게 아주 값진 정보이기 때문이다.

하지만 고객 정보를 담고있는 docs 들을 분석하는건 꽤나 어렵고 복잡한 일이다.

(자연어(natural language)는 정보의 자동 추출을 복잡하게 만드는 모호하고 비유적인 표현들을 담고 있다.)



전통적인 sentiment analysis 는 text 전반에 대한 감성 분석에 초점을 두고 있는데, 이는 고객이 기업의 무엇에 대한 감정인지를 밝혀내지는 않는다.

만일 text 가 동시에 다른 토픽과 entities(aspect) 를 담고 있는 경우 다른 aspects들에 대해서 다른 감정들을 표현하는 걸로는 충분하지 않을 수 있다.

text 내에서의 특정한 aspect 와 연관하여 감정들은 밝혀내는 것은 더 복잡한 작업이고 이는 aspect-based-sentiment analysis(ABSA) 로 알려져 있다.



> 전통적인 sentiment analysis 와 다르게 이 논문에서는 text 내의 특정 aspect 에 맞게 sentiment 를 분석하고 싶은 거 같음



지금까지 absa 영역에서의 중요 논문들은 SemEval-2014, SemEval-2015, SemEval-2016 등등이 있다. 



NLP 에서 다양한 사전학습 언어 모델의 발전들이 있어 왔다. (Ex. ELMo 그리고 BERT)

근데 absa 영역에서 사전 학습된 모델을 이용한 경우는 없었다.

논문에서는 BERT 를 기본 모델로  제약없는 ABSA 모델 발전을 위해서 사용할 것이다. 

그 발전은 추가적인 외재적인 훈련 데이터들을 사용하게 해주는 것.

이는 사전 학습된 언어 모델 덕이다.



더 정확하게 이 논문의 contribution 은 다음과 같다.



- 도메인 외 분류를 위한 문장과 text 레벨에서의 새로운 ABSA task 를 제안한다.
- 위의 task 를 해결하기 위해서, 일반적으로 사용되어지는 분류 모델이 제안된다. 그리고 그 모델은 사전 학습 모델인 BERT 를 문맥 단어 표현을 얻기 위해서 사용한다. 그리고 이 모델은 문장 쌍 분류 모델을 text 와 aspect 사이의 의미적 유사성을 찾기 위해서 사용한다. 이 모델은 지금까지의 absa 모델들의 성능을 능가한다.
- aspect 분류와 감성 분류 문제를 동시에 해결하기 위해서, BERT 로부터 하나의 문장 쌍 분류 모델을 사용하는 합쳐진 모델을 제안한다. (aspect 분류와 감성 분류를 동시에 진행하는데 기본적인 모델로 bert를 사용한다고 이해했다.)



## State of the art



state of the art 챕터는 이 논문의 나머지 부분에서 사용되어질 최첨단의 기술들과 모델들에 대해서 review 한다.

2.1 섹션에서는 이 논문에서 사용될 사전 학습 모델에 대해서 다루는데 모델의 아키텍처와 주요 특징들에 대해서 다룬다.

2.2 섹션은 SemEval-2016 에서 다뤘던 absa task 를 다룬다.

사전 훈련된 모델의 유무와 관계 없이 섹션 2.3 과 2.4에서 이전 absa 작업들은 간략하게 다룰 것이다.



### BERT



사전 학습된 언어 모델들은 word 에 대한 문맥을 제공한다. 그 문맥은 이전에 label 되지 않은 훈련 데이터로부터 단어들의 포현과 발생을 학습했다.

bert 모델은 bidirectional encoder representation transformer 이름 그대로 word 의 단어 표현을 양방향성의 문맥을 고려하여 얻는 사전 학습 모델을 의미한다.

bert 는 더 elmo 와 같은 모델들보다 더 문맥적인 특징들을 고려해서 단어의 문맥 특징들을 추출했다.



그렇다면 BERT 는 어떻게 양방향성 문맥을 고려해서 단어의 의미를 얻을 수 있었을까?

그건 바로 MLM(masked language model) 덕택이다.

즉, bert 는 사전 학습 당시 모델의 task 로 mlm task 를 부여한다.

mlm task는 문장 내의 랜덤한 단어에 대해서 masking 을 하고 그 단어에 대해서 예측하는 작업을 수행한다.

먼저 모델이 단어를 masking 할 때, 마스킹 토큰에 대해서 [mask] 로 표현을 한다.

그리고 모델은 mask 토큰의 왼쪽 오른쪽 단어들을 이용해서 masking 단어에 대해 예측한다. (트랜스포머)

mlm을 사용한 왼쪽 오른쪽 문맥 추출 작업 이외에도 bert는 next-sentence prediction(nsp) 작업도 수행하여 왼쪽 오른쪽 문맥에 대한 정보를 습득한다.



##### Previous work



이전에도 왼쪽의 문맥과 오른쪽의 문맥을 사용해서 word의 표현을 얻는 모델이 존재했다.

바로 ELMo 다. ELMO 는 LSTM 모델을 사용했는데, 왼쪽에서 오른쪽으로의 학습을 진행하는 LSTM 모델과 오른쪽에서 왼쪽으로 작업을 진행하는 LSTM 모델을 합친 모델이다.

왼쪽에서 오른쪽으로 진행하면서 얻은 단어 표현과 오른쪽에서 왼쪽으로 진행하는 단어 표현을 concatenate 한다.



하지만 BERT 는 더 이상 RNN 기반의 모델로 시퀀스 데이터에 대해서 학습하지 않는다. bert는 transformer 기반의 encoder 를 사용하여 word의 단어 표현을 얻는다.



##### Input Representation



BERT 모델의 input 은 어떤 형태일까?

먼저 bert 모델의 input 은 wordpiece tokenization 이라는 작업을 거친다.

Wordpiece tokenization 작업을 통해서 token set 을 얻을 수 있다.

(worpiece tokenization 의 작업이 어떤 식으로 이루어져서 토큰 set을 얻는지 알고 싶다면 장은준의 맥킨토시를 훔쳐서 til 폴더를 훔쳐봐라!)



tokenizing 을 진행한 후에 얻게 되는 두 개의 특별 토큰이 있는데 바로 cls 토큰과 sep 토큰이다.

Cls 토큰은 문장이 시작할 때 붙이는 토큰이고 sep 토큰은 문장이 끝날 때마다 붙이는 토큰이다. cls 토큰은 첫 문장이 시작할 때만 붙이고 그 이후에는 붙이지 않는다.

이렇게 특별 토큰까지 붙게 되면 최종적인 input token set 이 완성이 된다.



최종 input token sets 은 각기 다른 input layer (3개) 에 의해서 또 가공이 된다.(same 차원을 가짐)

그리고 3개의 layer 를 거치고 나중에는 각각 합산하게 된다.

1. token embedding layer
2. Segment embedding layer
3. position embedding layer



(이 또한 작동 원리가 궁금하다면 장은준의 맥킨토쉬에서 til 폴더를 훔쳐봐라! 하하하하하)



##### Transformers



seq2seq => encoder, decoder 아키텍처 사용

이때 rnn 기반의 기술들을 사용한다.

하지만 transformer 는 attention is all you need 라는 논문 제목에서 알 수 있듯이 **rnn 을 사용하지 않은 모델** 이다.

각 계산 단계에서 어떤 시퀀스가 중요한지 계산하는 attention 만을 사용한다.

encoder는 input을 고차원 공간 벡터에 매핑할 뿐만 아니라 디코더에 대한 추가 입력으로 중요 키워드를 사용한다.

이는 decoder 의 성능을 향상시키는데 어떤 시퀀스들이 중요한지에 대한 정보가 담겨 있기 때문이다.



##### Sentence Pair Classifier Task



bert 는 모델과 파라미터의 주요 변화가 없이, 특정한 태스크를 위해서 모델을 파인튜닝하는 걸 더 쉽게 만들기 위해서 word embedding 을 얻기 위해 모델을 사전 학습한다.

> 쉽게 말해서 파인 튜닝할 떄 사용한 word representation 을 얻기 위해서 사전 학습을 통해 word representation 을 얻는다.

일반적으로 output layer 는 모델을 더 특화시키기 위해서 모델의 꼭대기에 추가된다



그 문장 쌍 분류(sentence pair classifier) task 는 *두 문장간의 의미론적 관계들을 결정하는 것을 다룬다.*

이 모델은 두 개의 text 를 iuput 으로 받고, output 으로 문장들간의 관계를 표현하는 label을 가진다.

이러한 종류의 작업은 모델이 자연 언어에 대한 포괄적인 이해와 완전한 추론을 수행할 수 있는 능력에 대해 얼마나 좋은지 평가한다.



##### Pre-training tasks



일반적인 언어 모델의 목적은 label 되지 않은 규모가 큰 text들을 사용하는 것이다. 그리고 언어 모델의 일반적인 목적은 맥락적인 단어들의 표현을 배우는 것이다.



언어 모델이 nlp 영역에서 label되지 않은 데이터에서 단어의 발생이나 단어 예측 패턴을 학습하는데 주요 키 포인트다.

언어 모델은 벡터 공간에서 단어를 표현하는 벡터들을 사용하는 단어 임베딩과 같은 기술들을 사용하여 문맥을 배운다.

언어 모델은 단어에 대한 표현을 얻게되고 유사한 단어들은 유사한 벡터 표현을 가지게끔 만든다.



주요 사전 학습 tasks 들은



- masked languaged model bert
- next sentence prediction
  - 두 문장들간의 관계를 이해하는데 사용된다.
  - bert는 두 문장들간의 관계를 예측하기 위해서 사전학습한다.
  - a,b 두 문장이 있을 때, 학습할 때 절반은 a뒤에 b문장이 온거고 NextSentence 레이블이 붙고, 나머지 절반은 랜덤으로 b문장이 들어오고 IsNotNextSentence 레이블이 붙는다.
  - 



### Aspect-Based Sentiment Analysis



ABSA 는 전통적인 text 차원의 감성 분석보다 더 복잡하다.

ABSA는 text에서 언급되어진 entity의 aspect들과 attributes들을 밝혀내는데 초점을 둔다.



지금까지의 ABSA 의 논문들은 대표적으로 세 개가 있는데 다음과 같다. 그리고 쓰인 데이터셋은 각기 다른데

2014에서는 식당과 노트북에 관한 label된 리뷰들을 사용했고 full review 를 사용하지 않았다.

2015도 마찬가지로 full review 를 사용하지 않았다.

2016도 바뀐거 없는건 매한가지인데 추가적인 test 데이터를 제외하고는 바뀐게 없다.

- SemEval-2014
- SemEval-2015
- SemEval-2016



SemEval2016 task 의 목적은 소비자 리뷰들에서 토픽에 관한 특정 aspect에 대해 소비자들이 표현한 의견들을 밝혀내는 것이다.

특히, 데이터 셋으로부터 특정 주제에 대해 text review 가 주어졌을 때, 2016 의 목적은 다음과 같은 밑의 tasks들을 설명하는 것이다.



- Aspect category classification
  - 이 task 의 목적은 토픽과 aspect 쌍을 발견하는 것이며 의견이 텍스트 내에서 표현된다.
  - 토픽과 aspect는 이미 정의된 토픽 유형 set와 영역당 기준에서 선택해야 한다.
- Opinion target expression(OTE)
  - 각각의 entity-aspect 쌍에 대해서 리뷰된 entity를 참조하는 text input에서 사용된 언어적 표현을 추출하는 task 다. (리뷰된 entity가 반영된 text input?)
  - OTE는 시퀀스에서 하나의 시작 및 종료 오프셋으로 정의된다.
  - 만일 어떠한 entity도 명료하게 언급되지 않았다면, 그 값은 null 을 반환한다.
- Sentiment polarity classification
  - 각각의 식별된 토픽 그리고 aspect 쌍에 대해서 감성의 극단을 예측하는게 목적이다.
  - 감성의 극단의 값은 positive, negative, neutral, conflict 가 있다.
- Subtask 1 : Sentence Level
  - input은 보통 전체 텍스트 수준 텍스트에서 얻은 한 문장으로 구성됩니다.
- Subtask 2 : Text Level
  - input 은 몇몇의 aspects 들이 동시에 언급된 전체 리뷰가 사용된다. 
  - 똑같은 aspects에 대한 다른 의견들이 주어질 수 있다.



## ABSA without BERT

SemEval2016  에서 최고의 성능을 자랑했던 머신러닝 기술들은 서포트 벡터 머신이나 조건적인 랜덤 분류기들이다. 

비록 딥러닝 모델들이 감성 분석에서 좋은 성능을 보일지라도, 딥러닝을 사용한 기술들은 별로 사용되지 않았다.



svm 을 사용한 특징들은 보통 **GloVe를 통해서 추출된 문맥화된 단어 표현들** 또는 **데이터 셋으로부터 추출된 명사나 형용사**에 의해서 산출된 단어 리스트들이다.



## ABSA with BERT



지금까지는 absa 작업들 중 bert를 사용하지 않은 작업들을 살펴봤다.

이제 bert를 사용한 absa 작업을 살펴보도록 하자.



bert는 nlp 작업에서 많은 데이터들 덕에 좋은 성능을 보여주고 있다.

absa 작업을 위해서, 성능은 리뷰 텍스트에서 추가적인 학습을 통해 좋아지고 있다. (파인 튜닝을 이야기 하는 거 같다.)



absa 태스크를 해결하기 위해서, 이후 훈련 paper는 absa를 question answering problem 으로 만든다. 

리뷰들을 위한 기계 독해 이해 기술 "review reading comprehension" 과 함께



보조 문장을 구성하여, bert를 사용해 sentence-pair classification task로 absa를 해결하는 것은, 단일 문장 분류를 사용한 이전 최첨단 모델에 비해서 성능이 개선되는 것으로 나타났다.



보조 문장을 구성하여 BERT를 사용하여 문장 쌍 분류 작업으로 ABSA를 해결하는 것은 단일 문장 분류를 사용한 이전 최첨단 모델에 비해 결과를 개선하는 것으로 나타났다.



## Experiment







