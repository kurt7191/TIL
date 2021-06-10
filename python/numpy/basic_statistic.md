# 파이썬과 넘파이로 기초통계

> 파이썬으로 본 통계와 넘파이로 본 통계





### 파이썬 함수로 기초통계



##### 총합계 구하기



```python
height = [175,165,180,160]
weight = [75,70,95,72]
```



임의의 키와 몸무게 데이터를 생성하자.



```python
h_sum = sum(height)
w_sum = sum(weight)
```



파이썬 내장 함수인 `sum` 함수를 통해서 총합을 구할 수 있다.



##### 평균 구하기



```python
h_mean = sum(height)  / len(height)
w_mean = sum(weight)  / len(weight)
```



리스트 객체의 길이를 잴 수 있는 `len` 함수를 통해서 평균을 구할 수 있다.



##### 편차 구하기



편차 => Data - Mean(average) 이다.



```python
h_data = [i - h_mean for i in height]
w_data = [i - w_mean for i in weight]

sum(h_data)
sum(w_data)
```

##### 

반복문 comprehension 사용

데이터와 평균의 차이를 리스트로 다 받는다.



##### 분산 구하기



```python
h_data2 = [i**2 for i in h_data]
h_var = sum(h_data2) / len(height)
w_data2 = [i**2 for i in w_data]
w_var = sum(w_data2) / len(weight)
```



반복문 comprehension 사용

리스트로 받은 편차 값들을 제곱하여 모두 더해주고 개수로 나눈다.



##### 표준편차 구하기



```python
import math
h_std = math.sqrt(h_var)
w_std = math.sqrt(w_var)
```



math 패키지를 임포트



##### 공분산 구하기



```python
hw_deviation = [i * j for i,j in zip(h_deviation,w_deviation)]
hw_cov = sum(hw_deviation) / len(height)
```



##### 상관관계 구하기



```python
a = h_std * w_std
hw_cov / a
```



### numpy 함수로 기초통계



##### 총합



```python
height = np.array([175,165,180,160])
weight = np.array([75,70,95,72])
```



임의의 데이터 생성



```python
h_sum = np.sum(height)
w_sum = np.sum(weight)
```



##### 평균



```python
h_mean = np.mean(height)
w_mean = np.mean(weight)
```



##### 편차



```python
h_deviation = height - h_mean
w_deviation = weight = w_mean
```



##### 분산



```python
h_var = np.var(height)
w_var = np.var(weight)
```



##### 표준편차



```python
h_std = np.std(height)
w_std = np.std(weight)
```



##### 공분산



```python
hw_cov1 = np.cov(height, weight, ddof=0)
hw_cov = hw_cov1[0,1]
```



ddof는 분산을 만들 때도 사용하는데 불편분산을 계산할지 or 표본분산을 계산할지 결정하는 매개변수다. 

ddof = 0, 표본분산을 의미



np.cov 함수는 공분산 값을 리턴하는 게 아니라 공분산행렬을 반환한다.

1행 1열은 height 자기 자신의 공분산 즉, height 의 분산값을

2행 2열은 weight 자기 자신의 공분산 즉, weight의 분산값을 반환한다.

따라서 1행 2열 그리고 2행 1열만 두 변수의 공분산을 반환한다.



##### 상관계수



```python
hw_coef = np.corrcoef(height, weight)
hw_coef[0,1]
```



np.corrcoef 함수 역시 행렬을 반환한다. (2행 2열)

1행 1열과 2행 2열은 height와 weight  변수들의 스스로의 상관계수를 나타낸다.

1행 2열과 2행 1열만이 두 변수의 상관계수를 반환한다.



