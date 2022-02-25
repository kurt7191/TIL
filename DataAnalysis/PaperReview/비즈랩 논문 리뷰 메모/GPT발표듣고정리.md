# GPT-1



GPT : 

- 언어 모델, 

- Generative Training(직접 레이블링을 할 필요가 없기 때문), 

- Pre - Traning(이전 단어들이 주어졌을 때 다음 단어가 무엇인지 맞히는 과정을 사전 훈련)

  ㄴ> 사전 훈련



GPT 는 BACKWARD 를 사용하지 않음.

<HR>



- GPT는 트랜스포머의 디코더를 사용하는 모델

- MASKED 멀티 헤드 어텐션만 사용한다.

- 사전학습을 언어 모델로 진행

- 추가적인 업무를 파인 튜닝을 통해서 진행



(Alammar 블로그)





# GPT - 2



파인 튜닝했을 때 다른 TASK 에 사용하기가 힘들다는 것.

GPT-1 의 파인 튜닝을 없앴음.



GPT2 는 파인 튜닝 없이 자연어 처리를 할 수 있다.???

<HR>



GPT2는 변수의 크기가 엄청 크다. 데이터 셋이 엄청 크다. 임베딩 차원도 모델이 커질수록 커진다.





MASK SELF ATTENTION  ->  FEED FORWARD NEURAL NETWORK -> 



구조는 같지만 학습된 가중치가 다르다.



GPT2 또한 토큰화 할 떄 바이트 페어 인코딩 방식 사용.



<HR>

데이터 사용.

제로샷 러닝이 뭐야??



<HR>

# GPT - 3





지금까지 GPT 문제점 파인 튜닝을 충분히 진행해야지 성능이 좋았다. 즉 사전 학습만으로 좋지 않았다.



한계 :

실제 사람의 작업 방식과 다르다.

허위 관계, 실제 사람은 많은 데이터 필요 X



해결하기 위한 방법으로 Meta-learning 제안



학습 과정에서 다양한 세트의 스킬과 패턴을 인지하는 능력을 개발하는 것.





in-context learning(오타 수정, 연산 등등) 을 모델을 학습하면서 한 번에 학습할 수 있다.





few shot

ont shot

zero shot

에 대해서 알아볼 것.



few show에서 예시가 추가될 때마다 파인 튜닝을 하지 않는다.



<hr>

GPT3 는 attention 을 모든 단어에 대해서 진행 x

 sparse attention 진행



<hr>

GPT3의 training -cost



<HR>

Validation 과 train data 셋에서 성능 차이를 보이고 있다.



<hr>

특정 task에서는 문장을 생성하는 건 힘들다.

뒤쪽의 문장을 앞으로 가져올 수 없기 때문에 문맥 파악을 잘 할 수 없다.

















