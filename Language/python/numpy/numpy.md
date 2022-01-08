# 넘파이 시작하기

> 넘파이의 기초부터 시작해보자.



### numpy 값 만들기



```python
import numpy as np

a = np.array([1,2,3,4])
```



- numpy에서 1차원 배열은 벡터라고 부른다.

  

```python
b = np.array([[1,2],[3,4]])
```



- 2차원 배열은 행렬이라고 부른다.

  

```python
type(a)
type(b)
print(dir(a))
print(dir(b))
```



- 1차원 배열이든 2차원 배열이든 type과 dir은 동일하다. 

  

```python
c = np.array([[[1,2],[3,4],[5,6]]])
type(c)
print(dir(c))
```



- 3차원 배열도 type과 dir은 동일하다 3차원 이상의 배열부터는 텐서(tensor) 라고 부른다.



```python
a = np.array([1,'2','3'])
b = np.array(['a',1,True])
```



배열(벡터) 의 요소에 문자 데이터가 하나라도 있다면 요소의 데이터 타입은 문자형으로 바뀜

논리값고 숫자값이 문자형이 같이 공존해도 문자형으로 변환

즉, heterogeneous 가 아니라 homogeneous



- 넘파이는 homogeneous, 문자형이 최고 우선순위
- 넘파이는 본래 계산이 목적, 문자나 논리형을 지원을 하긴 하지만 일반적으로 숫자를 입력



### numpy 함수들



##### 1)np.zeros()



```python
a = np.zeros((4,3))
b = np.zeros(5)
```



zeros의 인자에 tuple (4,3)을 집어 넣게 되면 4행 3열의 행렬을 만들게 된다.

zeros의 인자에 int형으로 하나 넣게 되면 1차원 벡터가 만들어진다.

또한 zeros의 가장 큰 특징은 numpy 요소들이 모두 0이라는 점이다.

그리고 데이터 타입은 float형이기 때문에 요소가 0으로 출력이 되는 게 아니라 0. 으로 출력이 된다.



##### 2)np.eye()



np.eye는 단위 행렬을 만들 때 사용된다.



```python
a = np.eye(10)
b = np.eye(4,2)
```



eye의 인자는 shape가 아님 (shape인지 아닌지 판단하는 게 중요 shift + tab을 눌러서 확인)

eye의 인자로 int 하나를 집어넣게 되면(n) n x n 배열을 생성하게 된다.

eye의 인자에 int 두 개를 집어넣게 되면 n x m 의 배열을 생성하게 된다.

(위의 예시로는 4행 2열의 배열 생성이 됨)



```python
c = np.eye(5,6, k=1)
```



eye는 zeros와 달리 1의 값이 배열에 추가되는데, 1이 추가되는 시작 위치를 k 매개변수 값을 조정하면서 조절할 수 있다. 만일 k값을 설정하지 않으면 0열부터 1이 채워지게 된다. k=2가 되면 3번째 열부터 1이 채워지게 된다. 위의 예시는 첫 번째 열부터 1이 채워지는 경우다.



##### 3)np.identity()



```python
a = np.identity(3)
```



eye()와 동일한 결과를 내지만 다른 점은 identity는 n * n의 행렬(단위행렬)만을 만들 수 있다.

두 개의 int를 집어 넣게 되면 TypeError가 존재한다.



##### 4)np.full()

full은 다른 함수와 다르게 배열의 요소에 어떤 값이 들어갈지 정할 수 있다.



```python
a = np.full((3,2),1)
```



full의 인자는 shape이다. shape은 보통 tuple로 행과 열의 개수를 지정하라는 말과 같다.

그리고 fill_value 매개변수에 값을 필수적으로 할당해야만 한다. 이 매개변수는 배열 요소에 어떤 값을 집어넣을지 결정하는 값이다.

결과 값으로 3행 2열의 1의 값들이 도출된다.



```python
b = np.full(5,10)
```



shape는 기본 tuple을 집어넣는다. 하지만 단일한 int도 넣을 수 있다.

5를 단일한 int로 두고 fill_value를 10으로 설정한 경우는 위처럼 적는다. 이때 단일한 int는 열의 개수를 의미한다.

따라서 1행 5열의 배열이 만들어지며 그 요소값들은 10을 의미한다.



```python
a = np.full((1,5),[5,10,11,12,13])
#두 번째 인자 값에 array_like가 들어갈 수 있음
```



fill value 매개변수에 단일한 int를 집어 넣어서 배열의 요소를 결정할 수 있지만

array_like를 집어 넣어서 그 값을 결정할 수 있다. 대신 열의 개수에 맞게 작성해야만 한다.

위의 예시는 shape 매개변수란에 tuple을 통해서 열과 행을 결정하였다.

array_like도 이에 맞게 5열의 리스트를 넣어서 값을 넣었다.

만일 shape의 튜플에 행값을 2로 집어 넣으면, fill_value가 한 번 복사되어서 2행에 추가된다.

**shape의 행열을 array_like와 맞아야한다.*



##### 5)np.empty() **중요



```python
a = np.empty(3)
```



empty의 인자도 shape이다. shape에는 단일한 int를 집어넣을 수도 있고 tuple을 집어넣을수도 있다.

단일한 int를 집어 넣게 되면 1행 3열의 난수 배열이 생성된다.



```python
np.zeros((4,5))
np.empty((4,5))
np.zeros(1,5)
np.empty(5)
```



중요한 점은 empty는 zeros와 연관되어 있다.

(모든 0과 1의 배열을 생성하는 함수와 관련있다. 모든 0과 1의 배열을 생성하는 함수와 아래와 같은 관계를 가진다.)

(zeros, eye, identity 등등)

 

!만일 zeros를 이용해서 4행 5열의 배열을 먼저 만들었다면, empty를 통해서 4행 5열의 배열을 만들면 난수가 생성되는 게 아니라 0이 생성된다. 즉, zeros를 먼저 만들었다면 empty는 그 값을 그대로 가져오게 된다.

 

!또한 empty가 단일한 int를 넣어서 1행 n열의 난수를 만들 수 있는데, 만일 zeros의 tuple 행과 열의 곱이 empty의 1행 n열의 곱과 같다면 난수를 생성하지 않고 0을 요소로 가져온다.(zeros를 그대로 가져온다)

 

즉 zeros의 shape을 (1,5) 로 집어 넣었다면 empty(5)는 1행 5열의 0을 요소로 하는 배열을 가져온다.



##### 6)np.ones()



```python
np.ones(3)
np.ones((3,4))
np.ones([3,4]) #another sequence
```



ones()도 역시 shape을 인자로 받는다. 하지만 이때 shape 는 int와 sequence이다. sequence는 tuple도 포함하지만 list도 포함한다. (일반적으로는 tuple을 사용한다)

 

ones는 요소를 전부 1로 채운다 (zeros와 비슷하다고 생각하면 됨)

 

!또한 np.ones는 np.empty와 연관되어 있다. (zeros와 같음.) 이때는 요소가 모두 1로 채워짐



##### 7) _like

empty_like

_like는 기존의 배열의 구조를 참조하여 새로운 배열을 반환한다.

따라서 기존의 배열과 구조를 맞춰서 배열을 생성해야 하는 경우 유용하게 쓰인다.



```python
a = np.array([[1,2,3],[4,5,6]])
a_like = np.empty_like(a)
```



a의 shape는 2행 3열이다. 따라서 a_like도 2행 3열의 배열을 만들게 된다.

이때 메모리 할당 때문에 empty 난수를 생성할 수도 있고 a의 배열 요소 그대로 가져오는 경우도 있다.



ones_like



```python
b = np.ones_like(a)
```



a shape로 1을 채움



zeros_like



```python
c = np.zeros_like(a)
```



a shape을 0을 채움



##### 8)linspace()



```python
np.linspace(0,99)
len(np.linspace(0,99)) #100개 생성, 간격 1
```



start와 end 매개변수를 설정하면 일정한 간격으로 배열을 생성



```python
np.linspace(1,100,3)
np.linspace(1,100,3, endpoint = False)
```



1 ~ 100까지의 숫자 중 3개를 선택하여 배열을 만들라는 의미. (3간격이 아니라 개수를 조정)

이때 마지막 숫자는 그대로 반환되는데 endpoint를 통해서 반환할지 안할지 조정가능하다.