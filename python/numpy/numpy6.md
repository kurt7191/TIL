# 구조화된 배열



## **배열의 열의 이름과 데이터 타입 지정**

 

array는 기본적으로 homogeneous 다. 동종의 데이터 타입만을 저장한다.

그러나 서로 다른 유형의 데이터 타입으로 묶을 수 있는데 그때 사용법이 정해져 있다.



```python
import numpy as np
x = np.array([('Rex',9,81.0),('Fibo',10,27.0)],
             dtype=[('name','U10'),('age','i4'),('weight','f4')])
```



먼저, 타입이 다른 열들로 배열을 만들 때, 튜플을 사용하여 만든다.

dtype을 설정하지 않고 배열을 만들게 되면 인자에 str이 포함되어 있으면 모든 인자를 str로 받아주게 됨.

따라서 array를 만들 때, dtype에 튜플로 각 열의 이름과 데이터 타입을 지정해줘야 함



```python
print(type(x[0][0]))
print(type(x[0][1]))
print(type(x[0][2]))
```



타입을 각각 확인해보면 str, int, float으로 나타남.

dtype을 하지 않은 경우에는 모두 str 로 나타남.



```python
x['name']
x['age']
x['weight']
```



배열의 열 데이터 접근은 딕셔너리처럼 가능하다.

 

주목해야할 점은...

구조화된 배열에서 데이터 접근법은 다음과 같다.

 

배열에 대한 행에 대한 접근은 행의 번호를 붙여서 가능하다. x[0] 과 같이...

마찬가지로 배열에 대한 열의 접근도 가능하다. 열의 접근은 열의 이름을 사용하여 가능하다.

x['name']과 같이..



```python
x[0]
x[[0,1]] #Fancy Indexing
x[0:2] # slicing
x[[True,False]]
```



구조화된 배열에 대해서는 똑같이 indexing 기법들이 먹힘