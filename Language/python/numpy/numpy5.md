# 차원확대, 차원교환



## **np.expand_dims(a, axis = ?)**



```python
np.expand_dims(a,axis = 0) #차원 확대
```



`axis = 0` 이기 때문에 딥스를 확대하는 것. 2차원에서 3차원으로 확장이 된다.

`a[newaxis,:,:]`  와 동일한 결과를 얻는다.

인자를 적을 때 `axis = 0`  처럼 키를 이용해서 적어도 되지만 키를 생략하고 숫자만 적어도 된다.



```python
np.expand_dims(a,1)
```



`axis = 1` 로 확대를 한 것이기 때문에 `a[:,newaxis,:]`  와 동일하다.

행을 기준으로 차원을 확장한 것.

(행이 본래 일차원이였는데, 각 행은 1차원에서 2차원으로 확장이 됨)



```python
np.expand_dims(a,2)
```



`axis = 2`와 동일, 따라서 `a[:,:,newaxis]`  와 동일

열별로 하나씩 가져와서 하나의 뎁스를 차지한다.



## **array 한줄로 펴기**

 

**flatten**



```python
a = np.arange(12).reshape(3,4)
a
b = a.flatten()
```



3행 4열로 되어있던 행렬을 한 줄로 펼 수 있음



## **차원교환**

 

np.swapaxes(a,axis1,axis2)



```python
#a의 0번 차원과 1번 차원을 서로 바꾸는 것
b = np.swapaxes(a,0,1)
b = np.swapaxes(a,1,0)
```



axis1, axis2 매개변수에 1과 0을 집어넣어주면 행과 열을 transpose 해준다.

만일 a가 2행 1열이면 swapaxes를 하면 1행 2열로 바뀜