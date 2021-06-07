# 넘파이 행렬 배치와 연산

> 행렬을 배치 해보고 행렬 끼리의 연산을 해보자



### range, reshape



```python
np.arange(10)
```

1부터 9까지의 1차원 array를 만든다.



```python
np.arange(10).reshape(2,5)
```



10에 맞춰서 2행 5열로 배열을 만든다.



행렬의 shape을 reshape을 조정할 수 있다.



```python
a = np.arange(24).reshape(2,3,4)
```



깊이를 깊게 하여 만들 수 있다.



```python
a.reshape(2,3,-1)
```





### 행렬곱 연산



##### 파이썬을 @을 이용한 연산



```python
a = np.array([[0,1,2],[3,4,5]])
b = np.array([[6,7,8],[9,10,11]])
```



a와 b의 shape을 보면 2 * 3이기 때문에 연산곱의 조건을 만족시키지 못함



따라서 b를 전치시켜서 행렬곱을 수행할 것임



```python
b.T
a @ b.T
```



hape이 3행2열이 되면서 a의 2행 3열의 shape과 행렬곱으르 할 수 있는 조건이 됨



파이썬 내장 함수인 @을 사용해서 행렬의 곱을 할 수 있음



`@` 은 matrix든 ndarray들 상관없이 사용 가능



##### 넘파이 DOT 사용한 행렬 곱



```python
np.dot(a,b.T)
```



dot은 matrix든 ndarray든 행렬곱을 가능하게 해준다.

넘파이에서 제공한다.



```python
a.dot(b)
```



dot은 method 형식으로도 제공한다.



### numpy broadcasting



```python
a + np.array([3,4])
```



a가 2행 3열이고 뒤에 array가 1행 2열이기 때문에 broadcasting이 되지 않음



행의 개수가 같거나 열의 개수가 같아야지 broadcasting 가능



```python
a + np.array([3,4,5])
```



### axis



```python
a = np.arange(12).reshape(3,4)
np.sum(a)
```



행렬 내의 숫자들의 총 합을 구한다.



```python
np.sum(a,axis=0)
```



axis = 0은 행을 기준으로 합함을 의미함. 이때 주의해야함, 행을 기준으로 한다는 것은 행렬을 수직으로 더함을 의미

(axis = 0은 행을 의미, axis = 1 은 열을 의미)



```python
a = np.arange(24).reshape(2,3,4)
a.sum(axis = 0)
```



공간 기준으로 다 더해버림.

즉 1차원 2차원으로 다 더함



```python
a = np.range(24).reshape(3,2,4)
a.sum(axis = 0)
```



3개의 깊이로 확장해도 똑같음



```python
a.sum(axis=1)
```



각 깊이마다 행 기준으로 값을 모두 더함

따라서 3차원 2행 4열일 경우에는 3행 4열의 모습이 됨



```python
a.sum(axis=2)
```



### ufunc

ufunc은 universal function의 줄임말이다. 
universal은 모든 사람을 위한, 범용성이라는 뜻을 가지고 있다



```python
np.add(np.array([1,2,3]),np.array([4,5,6])) #array 처리
np.add([1,2,3],[4,5,6]) #리스트 처리
np.add(3,4) #스칼라 처리

```



add가 ufunc이기 때문에 array, list, 스칼라를 처리 가능하다.



### resize



바로 값이 바뀌어 버려서 reshape를 사용하지 resize는 잘 사용하지 않는다.



```python
a = np.range(24)
a.resize(2,3,1)
a
```



resize는 변수로 새로 받지 않아도 함수를 통해서 바로 형태가 바뀜



또한 원소의 개수가 달라도 변형이 됨



reshape는 변수로 받아야지 새롭게 바뀌게 되고 원소의 개수가 맞아야 바뀐다.



```python
a = np.arange(24)
a.resize(2,3,8)
a
```



본래의 원소 개수보다 더 크게 행렬을 변형시키면 초과된 공간은 모두 0으로 채운다.