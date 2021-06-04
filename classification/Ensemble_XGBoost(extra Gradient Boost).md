# 앙상블 학습, 부스팅  중 XGBoost(extra Gradient Boost)

> 1. XGBoost 개요
>
> 2. 사이킷런 래퍼 XGBoost 하이퍼 파라미터



### XGBoost 개요



 xgboost는 트리 기반의 앙상블 학습에서 가장 각광받고 있는 알고리즘 중 하나이다. GBM 대비 빠른 수행 시간을 보이고 있으며 그에 뒤지지 않는 뛰어난 예측 성능을 가지고 있다. xgboost의 핵심 라이브러리는 C/C++ 로 작성돼 있다. XGBoost 개발팀은 파이썬에서도 연동이 되게끔 파이썬 패키지를 제공하고 있다. 파이썬 패키지 안에는 xgboost 전용의 파이썬 패키지와 싸이킷런과 호환되는 래퍼용 xgboost가 존재한다.(파이썬 패키지 내에 1. xgboost 전용, 2. 사이킷런과 호환되는 패키지) 여기서 다룰 것은 사이킷런과 호환되는 xgboost를 살펴보려고 한다.

 

 사이킷런과 호환되는 xgboost같은 경우, 사이킷런에서 모델링 할 때 사용되는 함수들을 그대로 사용할 수 있게 해준다. 예를 들어서 모델을 학습시킬 때 사용하는 fit() 함수나 predict() 함수를 그대로 사용할 수 있다. 



### 사이킷런 래퍼 XGBoost 하이퍼 파라미터



\1. n_estimators

 

분류기의 개수

 

\2. max_depth

 

트리 깊이 조정을 통한 과적합 조정

 

3.learning_rate

 

 

 xgboost에서 유용하게 쓰이는 점은 학습을 도중에 중단할 수 있다는 점이다. 예를 들어서 학습용 데이터가 200개 있다고 가정해보자. 이 데이터를 통해서 모델이 학습을 하고 있는데 50번째 학습에서 0.52 성능을 구축했다고 해보자. 학습은 200개까지 해야하지만, 150번째까지 학습을 하여 나타난 결과가 0.52와 다를바 없다면 학습을 도중 중지한다. 따라서 모델링을 하는데 소요되는 시간을 줄이게 된다.

 

 조기 중단 코딩은 `fit()`  함수와 함께 사용이 된다.

 

\1. early_stopping_rounds

 

몇 개 이상 변화가 없으면 조기 중단을 할지 결정

 

\2. eval_metric

 

평가 방법

 

logloss, auc 등등

 

\3. eval_set

 

학습을 하면서 모델 성능을 확인해야 하는데, 그떄 활용될 테스트 데이터 지정

 

 

아래의 코딩은 위스콘신 유방암 데이터를 이용하여 xgboost를 연습한 것



```python
import xgboost
from xgboost import XGBClassifier

xgb_wrapper = XGBClassifier(n_estimators = 400, max_depth = 3, learning_rate = 0.1)
xgb_wrapper.fit(x_train, y_train)
xgb_predict = xgb_wrapper.predict(x_test)
xgb_predict_proba = xgb_wrapper.predict_proba(x_test)[:,1]
```



밑은 조기 중단을 사용한 xgboost 사례



```python
from xgboost import XGBClassifier

xgb_wrapper  =XGBClassifier(n_estimators = 1000, learning_rate = 0.1, max_depth = 3)
evals = [(x_test, y_test)]
xgb_wrapper.fit(x_train, y_train, early_stopping_rounds = 100, eval_metric = "logloss", eval_set = evals, verbose=True)
xgb_pred = xgb_wrapper.predict(x_test)
xgb_proba = xgb_wrapper.predict_proba(x_test)[:,1]
```

