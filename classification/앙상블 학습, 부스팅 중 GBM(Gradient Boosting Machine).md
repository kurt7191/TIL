# 앙상블 학습, 부스팅 중 GBM(Gradient Boosting Machine)

> 부스팅 기법에 대해서 알아보자



### GBM의 개요 및 실습



  앙상블 기법에는 크게 보팅, 배깅, 부스팅이 있음을 살펴봤다. 앞서 보팅 기법과 배깅의 대표적 기법인 랜덤 포레스트를 살펴봤다. 따라서 이번에는 부스팅 기법을 살펴보려고 한다. 부스팅 알고리즘은 여러 개의 약한 학습기를 순차적으로 학습-예측하면서 잘못 예측한 데이터에 가중치를 부여하여 오류를 개선해 나가면서 학습하는 방식이다. 부스팅의 대표적인 구현은 크게 AdaBoost(Adaptive boosting) 와 그래디언트 부스트가 있다. 먼저 AdaBoost의 알고리즘 원리를 살펴보도록 하자.



![다운로드](앙상블 학습, 부스팅 중 GBM(Gradient Boosting Machine).assets/다운로드.png)



  첫 번째 step1을 살펴보면 첫 번째 약한 학습기가 분류 기준 1로 +와 -의 분류를 예측한 것을 볼 수 있다. 하지만 동그라미 쳐져 있는 +들을 살펴보면 정확하게 분류가 이루어지지 않았다는 것을 볼 수 있다. 따라서 step2에서 학습기가 잘못 예측된 데이터에 가중치를 부여하여 크기를 크게 만든다. step3에서는 이런 가중치들을 바탕으로 다음 약한 분류기가 분류 기준2로 분류를 예측한 것을 볼 수 있다. 이 때 - 3개가 잘못 분류된 것을 볼 수 있다. 앞선 단계에서 보여줬듯이 다음 약한 분류기들이 잘 학습하여 예측할 수 있도록 이 세 개에 가중치를 부여하여 크기를 크게한다. 따라서 세 번째 약한 분류기가 이러한 배경을 바탕으로 분류 기준 3으로 분류를 예측한다. 마지막으로 이 세 개의 분류 기준을 결합해보니, 정확하게 데이터가 분류된 모습을 확인할 수 있다.

 

 GBM(Gradient Boost Machine)도 에이다부스트와 유사하지만 가중치 업데이트 방식에 차이를 보인다. GBM은 가중치 업데이트를 경사 하강법(Gradient Descent)를 이용하여 진행한다. 경사 하강법은 실제값 y와 예측 함수 F(x) 사이의 오차가 최소화 되게끔 반복적으로 가중치 값을 업데이트하는 것을 말한다. 즉, 오차제곱합인 SSE가 최소화가 되게끔 지속적으로 가중치를 업데이트 하는 방식을 말한다.

 

(에이다부스트와 그래디언트부스트의 큰 차이점은 가중치 업데이트를 하는 방식에 있다. 그래디언트 부스트는 경사 하강법을 사용하며, 경사 하강법은 예측 함수(예측 값)와 실제 값의 오차가 최소화 되게끔 지속적으로 가중치를 업데이트 하는 방식을 말한다.)



```python
from sklearn.ensemble import GradientBoostingClassifier
import time
import warnings
warnings.filterwarnings('ignore')

gr = GradientBoostingClassifier(random_state=0)
gr.fit(x_train,y_train)
gr_pred = gr.predict(x_test)
accuracy = accuracy_score(y_test,gr_pred)

print(gb_accuracy)
```

