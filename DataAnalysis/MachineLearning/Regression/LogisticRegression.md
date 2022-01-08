# 로지스틱 회귀



> 로지스틱 회귀
>
> 

## **로지스틱 회귀**

 

 로지스틱 회귀는 선형 회귀 방식을 분류에 적용한 알고리즘이다. 로지스틱 회귀 역시 선형 회귀 방법이다. 선형 회귀인지 아닌지는 변수의 degree에 따르는 것이 아니라 변수의 계수에 따라 나뉜다. 로지스틱 회귀의 가장 큰 특징은 학습을 통해서 최적의 선형 회귀선을 찾는 것이 아니라 시그모이드(Sigmoid) 함수 최적선을 찾는 것이다.

 

 많은 자연 현상에서 특정 변수의 확률 값은 선형이 아니라 시그모이드 함수와 같은 S자 커브 형태를 가진다. S자 커브 형태의 시그모이드 함수의 가장 큰 특징은 X가 아무리 +,- 쪽으로 나아가도 0이나 1에 수렴한다는 것이다.



```python
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


cancer =  load_breast_cancer()
scaler = StandardScaler()
data_scaled = scaler.fit_transform(cancer.data)

x_train, x_test, y_train, y_test = train_test_split(data_scaled, cancer.target, test_size = 0.3, random_state = 1)
```



  StandardScaler로 위스콘신 유방암 관련 데이터를 표준 정규화 시키고 그것을 train test split으로 분할 후 학습시킨 로지스틱 회귀 모형 코딩이다.



```python
from sklearn.metrics import accuracy_score, roc_auc_score

logistic = LogisticRegression()
logistic.fit(x_train, y_train)
pred = logistic.predict(x_test)
pred_proba = logistic.predict_proba(x_test)
accuracy = accuracy_score(y_test, pred)
roc_auc_score = roc_auc_score(y_test, pred)

print('accuracy : {:.3f}'.format(accuracy))
print('roc_auc_score : {:.3f}'.format(roc_auc_score))
```



이러한 모델의 정확도와 auc score을 구할 수 있다. 



```python
from sklearn.model_selection import GridSearchCV

params = { 'penalty' : ['l2','l1'],
         'C':[0.01, 0.1, 1, 1, 5, 10]}

grid = GridSearchCV(logistic, param_grid = params, scoring = 'accuracy', cv=3)
# grid.fit(data_scaled, cancer.target)
grid.fit(data_scaled, cancer.target)
print('최적 하이퍼 파라미터 : {}, 최적 평균 정확도 : {:.3f}'.format(grid.best_params_, grid.best_score_))
```



 로지스틱 회귀 분석의 하이퍼 파라미터 값은 penalty 와 C이다 penalty란 L2규제인지 L1규제인지 정하는 것을 말한다. 말인 그리고 C는 튜닝 하이퍼파라미터 값인 alpha 값의 역을 말한다. 따라서 C값이 작을수록 alpha값이 커지는 것을 의미하기 때문에 규제가 강해지는 것을 의미한다. GridSearchCV의 하이퍼 파라미터 값은 model, param_grid, scoring 인데, param_grid에서 시험해볼 하이퍼 파라미터 값들을 집어 넣는다. 그리고 평가 기준을 정확도로 판단한다. 따라서 어떤 하이퍼 파라미터 값을 정할 때 최적의 모델 성능을 가질 수 있는지 알아낸다.