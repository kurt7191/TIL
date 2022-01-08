# 판다스 시작 2



### 기능바꾸기



```python
from functools import partial
data.head  =  partial(data.head, n=10)
data.head()
```



functools 패키지의 partial 를 통해서 기존 함수의 기능을 바꿀 수 있다.

본래 head() 의 n 디폴트 값은 5이다. 

partial을 통해서 n=10으로 바꾸면 head() 를 사용하면 10개가 나온다.



## **describe**



```python
data.describe()
```



범주 데이터가 아니라 구간 데이터에 한해서 통계적 정보를 줌

(평균, 표준편차, 사분위수, 개수)



```python
data.describe().T
data.describe(include=np.number).T
```



전치행렬로 바꾸면 좀 더 가시적이게 볼 수 있음.

include에 np.number로 하면 숫자형 모두 다 가져올 수 잇음



```python
data.describe(include=['float64','object']).T
data.describe(include=['object'])
```



include 매개변수를 이용해서 문자형으로 되어 있는 것도 집계를 낼 수 있다.

단, 숫자형이여야지 계산 가능한 통계적 수치는 `NaN`으로 채워진다.



include에 object 만 집어넣으면 object 형만 수치 계산이 되어서 나온다.﻿

숫자형이랑 같이 보고 싶으면 float64도 같이 넣어주어야 한다.



## **values 관련**



```python
data['day'].values.size
data['day'].value_counts()
```



칼럼 내에 데이터가 몇 개 들어있는지 `values.size` 로 확인 가능.

`value_counts()` , 각 레이블 별 데이터 개수를 셀 수 있음.



## **isin을 이용한 인덱싱**



```python
#같은 칼럼에 있는 것을 비교 할 때
b = data['day'].isin({'Sun','Sat'}
data[b]
```



칼럼이 같은 경우에만 사용할 수 있다.



## **where**



```python
a = np.array([1,2,3,4])

#인자는 조건, 조건에 맞는 INDEX 위치를 반환
np.where(a>3)

#참이 나오면 0을 리턴해주고, 거짓이면 100을 리턴해줘라

np.where(a>3,0,100)
```



where인자에 조건을 넣어주고 조건에 True인 위치를 반환해준다.

2번째 3번째 인자를 넣으면 True이면 2번째 인자값이 나오고, False이면 3번째 인자값이 나온다.

