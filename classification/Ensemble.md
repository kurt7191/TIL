# 앙상블 학습 개요

> - 앙상블 학습 개요
> - 보팅 유형
> - 위스콘신 유방암 데이터를 통한 앙상블 기법



### 앙상블 학습 개요



 앙상블 학습(Ensemble Learning) 을 통한 분류는 여러 개의 분류기(Classifier)를 생성하고 그 예측을 결합함으로써 보다 정확한 최종 예측을 도출하는 기법을 말한다. 앙상블 알고리즘의 대표는 크게 랜덤 포레스트와 그래디언트 부스팅이라고 할 수 있다. 하지만 요즘 부스팅 기법이 많이 애용이 되면서 XGboost와 LightGBM 기법이 발명이 되었다.

 

 

 앙상블 학습의 유형은 전통적으로 크게 보팅(Voting), 배깅(Bagging), 부스팅(Boosting)의 세 가지로 나눌 수 있다. 먼저 보팅은 서로 다른 알고리즘을 결합한 앙상블 유형이라고 할 수 있으며 배깅은 서로 같은 알고리즘으로 결합한 앙상블 유형이라고 할 수 있다. 이 때 보팅과 배깅의 더 큰 차이점은 배깅은 원본 데이터를 부트스트래핑(Bootstrapping) 하여 데이터 샘플링 한 것을 각각 분류기를 통해서 결과값을 반환하는 것이고, 보팅같은 경우에는 원본 데이터를 그대로 사용하면서 서로 다른 알고리즘으로 결과 값을 반환하는 것이다.

 부스팅은 여러 개의 분류기가 순차적으로 학습을 수행하되 앞에서 학습한 분류기가 예측이 틀린 데이터에 대해서는 올바르게 예측할 수 있도록 다음 분류기에 가중치를 부여하면서 학습과 예측을 진행한다. 이처럼 계속해서 분류기에게 가중치를 부스팅하면서 학습이 진해오디기 때문에 부스팅이라고 불린다.



### **보팅 유형 (하드 보팅, 소프트 보팅)**



 보팅 방법에는 두 가지가 존재한다. 바로 하드 보팅(Hard Voting)과 소프트 보팅(Soft Voting)이다. 하드 보팅은 각각의 알고리즘 혹은 분류기에서 예측한 결과값에서 다수결로 결정된 값을 최종 결정값으로 정하는 방식이다. 즉, 분류기들끼리의 다수결 원칙에 따른 결과값을 의미한다. 소프트 보팅은 각각의 분류기에서 각각의 레이블 값에 대한 확률이 있을텐데 모든 분류기들의 각각의 레이블 값에 대한 확률을 더한 이후에 평균값을 내고 가장 높은 평균을 기록하는 레이블을 최종 결정값으로 선정하는 방식을 말한다. 주로 소프트 보팅이 많이 사용되어진다.



## **위스콘신 유방암 데이터를 통한 앙상블 기법 유형 중 보팅 기법 살펴보기**



```python
import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```



먼저 사이킷런의 다양한 모듈을 불러오도록 하자.



```python
cancer = load_breast_cancer()
data_df = pd.DataFrame(cancer.data,columns=cancer.feature_names)
data_df.info()
```



 데이터를 불러오니 `target`, `data`, `feature_names`로 정리가 되어 있었다. 먼저 cancer를 데이터 분석하기 쉽게 데이터 프레임으로 변환하도록 하자. 판다스 dataframe 함수안에 cancer의 data부분을 데이터로 넣고 칼럼명을 `feature_names`를 통해서 삽입하도록 하자. 그리고 데이터의 정보를 확인해서 잘 나오고 있는지 확인해보자.

```python
Logistic = LogisticRegression()
Knn = KNeighborsClassifier(n_neighbors=8)
```



 보팅의 다양한 알고리즘을 선정하는데, 이번에는 로지스틱 회귀분석과 knn알고리즘을 사용하여 보팅을 해보려고 한다. 위에서 말한 것과 같이 보팅은 단일한 알고리즘이 아니라 다양한 알고리즘을 이용한다.

```python
vot = VotingClassifier(estimators=[('LR',Logistic),('KNN',Knn)], voting='soft')
x_train,x_test,y_train,y_test = train_test_split(cancer.data,cancer.target,test_size = 0.2, random_state = 10)
```



 앙상블 보팅 객체를 VotingClassifier을 통해서 만들고 그 안에 logistic회귀모형과 knn모형을 집어 넣는다. 그리고 하드 보팅 방식과 소프티 보팅 방식 중에 이번에는 소프티 보팅 방식을 사용해 보려고 한다. (voting = soft)



```python
vot.fit(x_train,y_train)

pred = vot.predict(x_test)

accuracy = accuracy_score(y_test,pred)
```



 보팅 모델을 학습시키고 결과를 확인한 후에 모델을 정확도를 기준으로 평가를 해보니 93퍼센트의 정확도를 보인다. 그렇다면 보팅에 사용되었던 두 개의 알고리즘은 각각 몇 퍼센트의 정확도를 보이고 있을까?



```python
x = [Logistic,Knn]

for i in x:
    i.fit(x_train,y_train)
    pred = i.predict(x_test)
    accuracy = accuracy_score(y_test,pred)
    print('{}의 정확도 : {}'.format(i,accuracy))
```



  각각 92%의 정확도를 보이고 있다. 즉 앙상블 기법(보팅, 배깅, 부스팅) 중 하나인 보팅 방식에서 소프트 보팅 방식을 사용한 결과 단일한 알고리즘을 사용했을 경우보다 정확도가 더 높게 나왔다. 앙상블 기법이 무조건 더 모델 성능이 좋게 나오는 것은 아니라는 점을 주의하자.