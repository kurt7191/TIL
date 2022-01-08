# 넘파이 배열 나누고 합치기



## **array 쪼개기**



```python
a = np.arange(24)
a
```



1차원 배열 생성



```python
a = np.split(a,2)
```



default는 axis = 0임

나누면 행으로 2개로 나뉘어지게 됨



## **array 합치기**

**hstack, vstack**

**
**

쪼갰으면 합쳐보자



```python
a =  np.arange(24)
x,y,z = np.split(a,3)
```



split으러 3개로 일단 나눈다. 행기준



```python
np.hstack((x,y))
```



수평으로 쭉 이어 붙여진다



1,2,3,4,5,6,7,8,8,~~ 결과는 1차원 배열이다



```python
np.vstack((x,y))
```



수직으로 이어붙여준다. 따라서 데이터는 2차원 배열이된다.



## **stack**

axis = 0부터 합쳐진다.



```python
a = np.arange(16).reshape(4,4)
a
```



배열 생성



```python
np.split(a,2) #axis = 0으로 고정 되어있음
x,y = np.split(a,2,axis=1)
```



행기준 2 개로 나눠도 보고 열기준으로도 나눠도 봄



열 기준으로 나눈걸 변수에 넣기



```python
np.stack((x,y)).shape #axis = 0
```



stack으로 합쳐지면 차원으로 합쳐준다.

axis = 0이 default이다.



```python
np.stack((x,y), axis = 1)
```



axis = 1은 여기서는 행을 의미 따라서 행을 기준으로 합쳐줌



```python
np.stack((x,y),axis = 2)
```



axis = 2는 열을 기준으로 합침





정리하면 배열을 나누는 함수는 np.split(a,2) 이다.

axis를 0, 1로 하는지에 따라서 행과 열로 나눌지 결정한다.



배열을 합치는 함수는 stack, hstack, vstack 세 개가 있음

stack은 3차원으로 합칠수 있고, 행과 열로도 합칠 수 있음



```python
np.stack((x,))
```



stack이 차원을 높여준다는 것을 활용하여 3차원으로 만들 때 위의 코드처럼 칠 수 있다.

(default 가 axis = 0 이기 때문에)



## **concatenate**



배열을 합치는 다른 함수



```python
np.concatenate((x,y)) #행으로 합치기
```



기본 axis = 0으로 행으로 되어 있음

따라서 행으로 붙이게 됨



```python
np.concatenate((x,y),axis=1)
```



열을 기준으로 붙임



## **차원 확장**﻿ 

**
**

**reshape, stack, newaxis**



```python
a = np.arange(12).reshape(3,4)
```



reshape로 차원 확장 가능



```python
np.stack((a,))
```



stack이 차원을 확장하는 특징이 있기 때문에 이 방법으로 차원 확장



```python
a[np.newaxis]
a[np.newaxis].shape
```



a가 본래 (3,4) 인데 newaxis로 인해서 차원이 늘어나서 (1,3,4) 가 된다.



```python
a[np.newaxis,:,:]
```



이 코드랑 의미가 같다.



```python
a[:,np.newaxis,:]
```



행을 기준으로 차원을 늘리기



```python
a[:,:,np.newaxis]
```



열을 기준으로 차원을 늘리기