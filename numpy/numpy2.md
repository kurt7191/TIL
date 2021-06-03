# 넘파이 시작하기 2

> 넘파이 관련 이론 2



### 넘파이 copy 생성



### 1)파이썬 copy



파이썬은 기본적으로 Shallow Copy이다. Shallow Copy란 카피된 것과 원본이 메모리 주소를 공유하고 있는 copy를 의미한다.



```python
x = [1,2,3]
y = x.copy()
print(x)
print(y)
print(x  == y)
print(x is y)
x[0] = 7
print(x)
print(y)
```



데이터가 1차일때는 copy를 하여도 주소를 공유하지 않는다. 따라서 값을 바꾸어도 x, y의 데이터 값은 다르다.



```python
x = [[1,2,3]]
y = x.copy()
print(x)
print(y)
print(x == y)
print(x is y)
print(x[0] is y[0])
x[0][0] = 7
print(x)
print(y)
```



하지만 데이터가 2차일 경우에는 2차 데이터의 값을 변경한다면 메모리 주소를 공유한다. 따라서 값을 변경하면 x,y의 두 값이 변경이 된다.



```python
x = [1,2,3]
y = x[:]
print(x)
print(y)
print(x == y)
print(x is y)
x[0] = 7
print(x)
print(y)
```



인덱싱을 통해서 복사를 한 것도 마찬가지다. 1차 데이터의 경우에는 메모리 주소를 공유하지 않는다.



```python
x = [[1,2,3]]
y = x[:]
print(x)
print(y)
print(x==y)
print(x is y)
print(x[0] is y[0])
x[0][0] = 7
print(x)
print(y)
```



역시나 2차 데이터일 경우에는 인덱싱으로 복사를 하면 메모리 주소를 공유하여 값이 같이 바뀐다.



```python
#deepcopy

import copy
c = copy.deepcopy(a)
c
```



이러한 주소 공유 카피를 Shallow Copy라고 하는데 Shallow Copy와 반대되는 것은 DeepCopy이다.

딥카피를 하면 메모리 주소를 공유하지 않는다. 대신에 IMPORT를 해주어야만 한다.

 

이처럼 파이썬은 기본적으로 Shallow Copy에 속한다.



##### 2)넘파이 copy



넘파이는 파이썬과 다르게 Shallow Copy가 아니라 Deep Copy이다. 



```python
a = np.array([1,2,3])
b = a.copy()
a is b
a[0] = 7
print(a)
print(b)
```



데이터가 파이썬 기본 자료구조인 리스트가 아니라 넘파이로 배열을 만들게 되면 이 배열에 대한 copy를 `copy()` 함수를 사용해도 메모리 주소는 공유되지 않는다. 따라서 deep copy이다.



```python
a = np.array([[1,2,3]])
b = a.copy()
a is b
a[0] is b[0]
b[0][0] = 7
print(a)
print(b)
```



2차 넘파이 배열 또한 마찬가지로 카피를 해도 주소를 공유하지 않는 deep copy이다.



### 넘파이 타입변환, AS

=> array, asarray, asfarray



```python
list1 = [1,2,3]
test_array = np.array(list1)
test2_array = np.asarray(list1)
test3_array = np.asfarray(list1)
```



넘파이를 이용해서 리스트를 넘파이 배열로 바꿀 수 있다. 이때 그대로 `array`함수를 이용해서 바꾸는 방법이 있고 `asarray`를 사용하여 넘파이 배열로 바꿀 수 있다.

이때 바뀐 배열 요소의 자료형은 `int` 이다. (본래 리스트 데이터 요소의 자료형을 그대로 가져옴)

 

다른 방식으로 asf를 사용하게 되면 요소들이 `float` 으로 바뀌게 된다.



```python
list1 = [1.,2.,3.]
test_array = np.asarray(a)
type(test_array[0])
```



만일 리스트 데이터 요소들이 float이면 as를 사용해서 변환하면 본래 데이터 타입인 float을 반환한다.

 

`asarray` -> 본래 리스트 데이터 요소 자료타입 그대로 가져옴

`asf` -> 요소를 float으로 변경해서 가져옴



### 넘파이 값 가져오기

**=> 인덱싱**

##### 1)콤파 (comma) 이용

파이썬은 `,` 를 이용해서 가져올 수 없다.

```python
a = [[1,2,3],
	[1,2,3]]
a[0]
a[slice(0,1)] 
```



slice함수를 이용해야지만 콤마로 가져올 수 있다.

slice(0,1) 은 0행에서부터 1행 미만을 가져온다. 결국 0행을 가져온다.



```python
b = [[1,2,3],
	[1,2,3]]
b[0,0]
```



넘파이는` ,` 를 이용해서 몇행 몇열로 값을 인덱싱하고 가져올 수 있다.

 

***,를 사용하면 넘파이array\***

***,를 사용못하면 list\***



##### **2)boolean 이용**

파이썬은 불린을 이용해서 값을 불러올 수 없음(list에다가)

그러나 넘파이 array는 boolean을 이용하여 값을 불러올 수 있다.



```python
a = np.arange(101)
a[a<50]
```



50이하의 값들만 들어오게 됨. 모든 원소에 불린을 계산하여 논리값을 반환한다.

결국 `[]` 안에 논리값을 넣어주면 각원소에 그 논리값과 맞는 값을 반환한다. (elemetwise)

 

애초에 논리값을 배열로 정해줘서 다른 배열의 인덱스에 사용할 수 있다.



```python
test_array[np.array([[True, True, True, False]])]

```



개수만 맞는다면 논리값에 맞게 0번째 1번째 값을 반환한다.



```python
c =  np.array(['데이터','사이언스','공부중'])
print(c[c == '데이터'])
```



string 타입도 가능하다. 그러나 string을 array에 사용할 이유가 없다.



##### 3)세미콜론, 콤마



```python
b = np.arange(100).reshape(20,5)
b[:]
b[0:3]
b[0:3,0:3]
```



`b[0:3]` => 0행 1행 2행 불러오기

`b[0:3,0:3]` => -0행 1행 2행 데이터 중에 0 ~2열 데이터들



```python
b[[3,6,9],[3,6,9]]

```



연속된 행과 열의 데이터가 아니라 단절된 행과 열의 데이터를 추출하기 위해서는 fancy indexing이 필요하다.

3행 6행 9행 데이터 중에서 3열 6열 9열의 데이터를 가져온다. 

 

*단, fancy indexing은 `:` 을 사용할 수 없다.*

*단, 행과 열의 개수가 맞아야 한다.*



```python
b[:,[3,6,9]]
b[[3,6,9],:]
```



특정 행과 특정 열을 가지고 오고 싶을 때. (모든 행, 특정 열, 모든 열, 특정 행)