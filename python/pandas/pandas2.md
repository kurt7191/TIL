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

