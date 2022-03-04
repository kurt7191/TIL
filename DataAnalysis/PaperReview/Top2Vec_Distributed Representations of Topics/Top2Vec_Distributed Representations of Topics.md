# Top2Vec_Distributed Representations of Topics



# ABSTRACT



토픽 모델링은 잠재된 의미 구조 (주제) 를 documents 들의 collection 으로부터 찾는다.

지금까지 보통 LSA 와 LDA 를 사용해서 토픽 모델링을 진행했다.

널리 사용되고 사랑받는 기법들이긴 하지만 몇 가지 문제점들을 안고있다.

이 용법들은 최적의 성능을 내기 위해서 lemmatization, stop-word list, stemming 등등의 전처리를 진행한다.

또한 BOW(bag of words) 방식의 단어 representation 을 사용하기 때문에 표현이 단어의 순서나 의미를 제대로 담고있지 못하다.

그래서 단어나 문서의 Distributed representation 들이 단어나 문장의 의미를 남아낼 수 있기 때문에 인기 있었던 것이다.

논문의 연구원들은 공동 docs들과 단어 의미 임베딩을 이용해서 "토픽 벡터" 를 찾는 **top2vec** 을 제안한다.

top2vec은 사전 전처리 작업 즉, stemming, lemmatization, stop-word 등등을 할 필요가 없으며 자동으로 토픽들으 개수를 찾는다.

top2vec을 통해 도출된 토픽 벡터들은 의미론적 유사성을 나타내는 문서 및 단어 벡터와 함께 결합되어 있다.

논문 연구원들은 top2vec이 확률 기반의 토픽 모델들보다 더 유익하고(정보를 제공하고) 너 대표성이 있다고 주장한다.



## Introduction



대량의 text 들을 요약하고 조직하고 찾는건 nlp 에서 흔한 task 이다.

토픽 모델링은 규모가 큰 데이터 셋에서 사람에 의해서 읽혀질 수 없고 정렬되어질 수 없을 때 사용되는 모델 기법이다.



문서라고 불리는 많은 text들의 구성으로 이루어진 corpus 가 주어지면,(즉 corpus 가 주어지면)

토픽 모델은 문서 안에 있는 잠재된 의미론적 구조 또는 토픽을 찾는다.

그러면 토픽 모델링은 큰 규모의 docs의 높은 수준의 요약을 할 수 있다.

(관심있는 문서를 검색하고 비슷한 docs들끼리 그룹화한다.)



##### what is topic

토픽(topic) 이 무엇인지에 대한 이야기는 계속해서 진행 중이다. (분절된 가치들 science, politics 등등)

하지만 우리가 다루는 토픽은 위의 것들이 아니다. 왜냐하면 이러한 type 혹은 정의의 토픽들은 sub-topic들로 분화될 수 있기 때문이다.

추가적으로 "politics" 와 같은 토픽들은 다른 토픽들 예컨데 "health" 와 같은 토픽과 겹친다. 왜냐하면 그들은 공통된 sub-topic들을 공유하기 때문이다.

(politics 와 health 는 sub topic 으로 "health care" 를 공유한다.)



이러한 것들 중에 아무거나.. 중에서, 그들(토픽)의 combination 이나 variations 들은 weighted 된 단어들의 독특한 set으로 묘사될 수 있다.

논문은 토픽을 토픽에 대해서 표현하기 위해 사용된 weighted 된 단어들의 무한히 많은 조합들로 연속적이라고 가정한다.

ex) weighted word1 + weighted word2 + weighted word3 + weighted word4 + ... weighted word5 ...weighted word..i



또한 이것 뿐만 아니라 논문은 document 가 그 자체의 topic 을 가지고 있다고 가정한다.



> ##### 가정
>
> 1. 토픽은 weighted word 들의 연속체이다.
> 2. 어떤 document 는 그 자 체의 토픽을 가지고 있다.



따라서 논문에서 말하는 토픽을 찾는다고 함은, 문서의 정보를  가장 잘 나타내는 단어들의 weighted sets을 찾는 것이다.



그후 논문 Introduction 에서는 관련된 작업들과 토픽의 분산 표현에 대해서 소개한다.

그리고 section 2에서는 top2vec 모델에 대해서 살펴보고 section3 에서는 토픽 정보 이득을 설명하고 논문의 실험을 요약한다. 그리고 section4에서 결론을 내린다.



##### Traditional Topic Modeling Methods



-LDA 와 PLSA

토픽 모델링과 관련된 작업인 전통적인 토픽 모델링들에 대해서 살펴보자.

전통적으로 corpus 에 대한 토픽 모델링은 LDA를 통해 이루어져왔다.

이 모델은 생성적인 확률 모델(generative probability model) 로 각각의 documents 들을 topic 들의 혼합으로 보며, 각각의 topic 들은 word들의 분포로 본다.

LDA 는 확률적인 잠재적 의미 분석인 PLSA 를 일반화한다, document-topic(특정 document d의 topic 분포) 과 topic-word(특정 토픽 k의 word 분포) 분포에 Dirichlet 분포를 추가해서 잠재적 의미 분석인 PLSA 를 일반화한다.



-LDA, PLSA 약점

LDA와 PLSA 는 연속된 토픽 공간을 t topics 들로 이산화하고 model documents 들을 t topics들의 혼합으로 본다.

##### 이 모델들은 토픽들의 숫자 t가 알려져있다고 가정한다. (LDA 를 만들 때 임의의 토픽의 숫자를 사용자가 직접 정해준다.)

토픽을 이산화 하는 것은 documents 와 words들의 관계를 모델링 하기 위해서 필수적이다.

이게 이 모델(LDA) 의 가장 큰 약점이다.

주제의 수 t 또는 그것을 추정하는 방법은 거의 알려지지 않았다. 특히 크고 친숙하지 않은 데이터셋에서는 더욱 그렇다.



-stop words 제거 (전처리 작업)

위와 같은 방법으로 만들어진 토픽들은 단어 확률 분포이다.

토픽에서 가장 높은 확률을 가지고 있는 단어들은 "the", "and" 와 같은 것들이다. (다른 언어도 마찬가지)

이런 common-word 들은 stop-words 라고 불린다.

Stop-words 들은 토픽을 해석가능하게끔 하기 위해서 제거 되기도 한다. 그리고 유익한 토픽 단어들을 추출한다.

stop word를 찾아서 제거하는 일은 언어와 corpus 특이적이기 때문에 하찮은 일이 아니라 중요한 일이다.

(강아지에 관한 글이 있을 때, 강아지가 나온 빈도수가 많을 것이기 때문에 이를 stop-word로 간주하고 제거할 것이다. 왜냐하면 정보가 많이 담겨있다고 생각하지 않기 때문이다.)





LDA 와 LSA 는 입력값으로 bow 방식으로 표현된 단어 표현을 사용한다.

bow 방식의 표현은 단어의 의미를 무시한다.



> Canada - Canadian
>
> big - large



Canada 와 Canadian 은 의미상으로 유사함에도 불구하고 완전 다른 단어로 표현된다. (bow의 비슷함이 없다.)

Stemming과 lemmatizaion 전처리가 이런 문제를 해결하기 위해서 사용되는데, big 이나 large 같이 둘은 의미상으로 유사함에도 불구하고 stem단어를 공유하지 않았기 때문에 그 둘의 유사함을 인지하지 못한다.



확률적인 생산 모델(LDA, PLSA) 의 목적은 본래의 문서 단어 분포를 최소한의 오류로 재현 할 수 있는 토픽을 찾는 것이다. (특정 토픽의 단어 분포를 이용해서 doc의 n번째 단어를 생성한다. 이때 토픽도 문서 내의 토픽 분포에 의해서 결정된다.)

하지만, 모든 택스트들의 큰 부분은 주제적으로 고려될 수 없을, 정보 가치가 없는 단어들을 포함한다. 문서 내 단어들을 정보가 있는지 없는지 구분해야 하는데, LSA, LDA 와 같은 모델들은 이런 구분을 할 수 없다. 왜냐하면 그들의 목적은 단순하게 문서의 단어 분포를 재현하는데 맞춰져 있기 때문이다.

따라서 토픽 내에서 높은 확률분포를 가지고 있는 단어들은 부득이하게 사용자가 직관적으로 주제 단어라고 생각하는 것과 일치할 수 없다.



##### Distributed Representation of Words and Documents



- word 와 documents 에 대한 vector representation.

- 분포 가설 (distributed hyphothesis) 비슷한 context 에서는 비슷한 의미 단어들이 사용된다.
- word2vec (전통적인 방법들과 비교해서 언어적인 업무들에서 최첨단의 방법)
- PMI(point wise mutual information) 방식을 이용한 GLOVE 방식 등.
- Document 에 대한 vector 를 얻기.



##### Distributed Representation of Topics



Semantic space(의미 공간) 에서의 distance 는 **의미론적 연관성** 을 표현한다.

단어의 의미론적 임베딩을 위한 많은 시도들이 있었고, word2vec이 그 중에 하나다.

doc2vec 모델은 같은 공간에서 함께 임베딩된 word와 document vector 들을 배울 수 있다.



함께 임베드된 document와 word vector들은 학습될 수 있다 word vector 의미론적으로  가까운 document vector처럼.

doc2vec 에서 공동으로 포함된 doc과 word 벡터는 doc 벡터가 의미론적으로 유사한 word 벡터와 가깝도록 생성된다.

이 속성을 통해서 word 벡터를 통해서 유사한 문서를 query 할 수 있게 된다. (doc 벡터가 유사한 word 벡터와 가깝게 학습이 되기 때문에.)

그리고 어떤 단어가 문서와 가장 유사한지 그리고 가장 대표적인지 파악할 수 있다.

##### 그래서 doc 벡터와 가장 유사한 word 벡터는 doc 토픽을 가장 대표할 가능성이 높다.



이렇게 document 와 word를 함께 임베딩하는 건 의미론적(semantic) 임베딩과 같다.

왜냐하면 임베딩된 공간의 거리는 document와 words 간의 의미론적 유사도를 측정하기 때문이다. 이를 쉽게 말하면 doc과 word를 동시 임베딩하게 되면 임베딩된 각각의 벡터간의 차이는 의미론적 유사도를 의미한다.



전통적인 BOW 기반의 topic modeling 과는 다르게, 의미론적(semantic) 임베딩은 word와 documents 같은 의미론적 유사도를 측정하는데 의미가 있다. (그 doc과 많이 유사한 단어는 토픽으로 간주될 수 있는건가?)

논문(연구원들)은 의미론적 공간은 그 스스로 연속적인 토픽 표현이라고 주장한다.

space에서의 점들은 토픽을 의미하고, 이 각각의 토픽 point 들은  각각 그것들의 가장 가까운 단어들에 의해서 요약된 토픽들이다. (nearest words)

(space 의 점들 주변은 그 점과 유사한 단어들의 분포되어 있는건가?)

##### doc의 밀집된 지역은 유사한 토픽들을 가진 많은 문서들로 여겨진다. => 이게 뭔말이지



연구원들은 이 가정을 document vectors 들의 밀집된 지역으로부터 계산된 분산 토픽 벡터인 top2vec을 주장하기 위해서 사용한다.

top2vec에서 발견되는 밀집된 지역의 숫자는 눈에 띄는 주제의 숫자로 가정된다.

(keyword = dense area,  dense area의 개수가 토픽의 숫자.. 기존의 LDA 처럼 하이퍼파라미터가 아니라 모델이 토픽의 개수를 정해준다.)



자. 이제 dense로부터 주제 벡터가 도출이 되는데, doc의 밀집 지역의 중심이 주제 벡터로 계산된다. 

dense area는 매우 유서한 문서들의 영역이다. 

또 dense area 의 중심 혹은 토픽 벡터는 그 dense area 를 가장 대표하는 평균 document 로 여겨질 수 있다.

(Leverage = 활용하다, 자주나오네)

각 토픽의 가장 대표적인 word를 찾기 위해서 의미론적 임베딩을 활용(leverage, 단어 복습^^)한다. by 토픽 벡터와 가장 가까운 word 벡터들을 찾음으로써 



top2vec 모델은 임베드된 토픽, doc, word 벡터들을 만든다. 그리고 그것들간의 거리는 의미론적 유사성을 나타낸다.

그 전의 LDA, pLSA와 다르게 토픽을 찾는데 있어서, top2vec 은 전처리 작업들(lemmatization, stop-words, stemming) 이 필요하지 않다. (다른 모델에 비한 이점)



이 토픽 벡터는 유사한 doc을 찾을 때 사용될 수 있으며 word는 유사한 토픽을 찾는데 사용될 수 있다.

word2vec 과 같이 설명되어지는 벡터의 똑같은 선형(나는 shape을 설명하고 싶은거라 생각했다.) 은 단어들, 문서들 그리고 토픽 벡터들 사이에서 사용될 수 있다.



토픽 벡터들은  각각의 **문서 벡터의 최근접 토픽 벡터** 를 기반으로 **토픽 사이즈** 들이 계산되어지는걸 허용한다.

또한 주제 벡터에서 주제 감소를 수행하여 유사한 토픽들을 계층적으로 그룹화하고 발견된 토픽들의 개수를 줄인다.



top2vec 모델들과 확률적인 생산 모델의 가장 큰 차이점은 각 모델이 주제를 어떻게 모델링 하는지이다.

LDA와 plsa는 최소한의 오류로 본래의 doc word 분포를 재현하는데 사용되는 단어의 분포로 토픽을 모델링한다.

이는 종종 토픽 안에서 높은 확률을 가지고 있는 주제에 적합하지 않은 단어들을 취한다.

왜냐하면 그들은 모든 text들의 큰 비중으로 이루어져 있기 때문이다.

대조적으로 의미론적 임베딩 top2vec의 토픽 벡터는 문서들 사이에서 공유되어지는 눈에띄는 토픽을 표현한다.

**토픽 벡터** 와 가장 가까운 주변 단어들은 토픽을 묘사하고 그 단어들은 가장 문서를 잘 나타낸다.

이는 동시 doc, word 학습 task 때문이다. 이것은 어떤 word가 doc을 가장 잘 나타내는지 예측하기 위한 공동 문서와 단어 포함 학습 작업 때문이다. 따라서 **토픽 벡터** 가 가장 유익한 단어에 가장 가깝다.



## Model Description



























 























































