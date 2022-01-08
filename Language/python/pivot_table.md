# 파이썬 피봇 테이블 만들기



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mp

#한글 폰트 삽입

fm = mp.font_manager.FontManager()

plt.rcParams['font.family'] = 'Malgun Gothic'
```



패키지들 다 불러오고, 한글 폰트 삽입



```python
#데이터 프레임 생성 시리즈 붙여서 가능
kmovies = pd.DataFrame({'MovieID':['1193','1194','1195'],
                        'Title':['디바','무림의 고수','정직한 후보'],
                        'Genres':['드라마','액션','코미디']})
kusers= pd.DataFrame({'UserID':[1,2,3,4,5],
                      'Gender':['F','M','M','F','M'],
                      'Age':[13,56,25,33,43]})

kratings= pd.DataFrame({'UserID':[1,1,1,2,2,2,3,3,3,4,4,4],
                        'MovieID':['1193','1194','1195','1193','1194','1195','1193','1194','1195','1193','1194','1195'],
                        'Rating':[2,5,None,3,1,5,None,2,5,5,None,3]})

```



영화와 이용자 그리고 영화평점에 관련된 데이터 프레임들을 생성.

지금까지 데이터 프레임을 만들어왔던 방식과 다르게 시리즈로 넣는 형태.



```python
kdata = kratings.merge(kusers).merge(kmovies)
```



데이터 프레임끼리 합치는 방법!

merge를 통해서 똑같은 열을 가지고 있는 데이터 프레임끼리 합친다.

merge() 함수 사용!



```python
krecom_data = kdata[['UserID','MovieID','Rating']].copy()


```



```python
krecom_pivot = krecom_data.pivot(index='UserID', columns='MovieID',
                                values='Rating')
```



피봇테이블을 만들기 위해서 원하는 행과 열을 지정하고 값들도 지정한다.

우리가 원하는 것은 사용자별 영화별 평점이기 때문에 index = '사용자', columns = '영화', values = '평점' 을 설정한다.



```python
krecom_pivot.fillna(0, inplace = True)
```



피봇 테이블의 NA 값을 fillna를 통해서 채울 수 있다. 하지만 이 방식 이외의 다른 방식이 있다.



```python
#aggfunc 기능 사용하여 요약 기능 전달 가능(기본은 평균)
#fill_value => na값 대체 가능

krecom_pivot_table = krecom_data.pivot_table(index='UserID', columns='MovieID',
                                values='Rating',aggfunc = 'min',
                                            fill_value = 0)
```



aggfunc 함수를 min을 사용해서 value를 요약할수도 있고 max, mean으로도 요약할 수 있다.



```python
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                          "bar", "bar", "bar", "bar"],
                    "B": ["one", "one", "one", "two", "two",
                          "one", "one", "two", "two"],
                    "C": ["small", "large", "large", "small",
                          "small", "large", "small", "small",
                          "large"],
                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
```



새로운 피보 테이블을 위한 데이터 프레임 생성



```python
table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                       aggfunc={'D': np.mean,'E': np.mean})
```



value값만 지정하고 column 값을 따로 지정하지 않아도 자동으로 value 열들이 컬럼이 된다.



요약 정보를 dic형태로 aggfunc 인자로 집어 넣는다.

이때  mean 을 넘파이 사용



```python
table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                       aggfunc={'D': np.mean,
                                'E': [min,max,np.mean]})


table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                       aggfunc={'D': np.mean,
                                'E': [np.min,np.max,np.mean]})
```



aggfunc 인자에 각각의 칼럼에 쓰일 요약정보를 지정할 때 넘파이를 쓰든 파이썬 내장함수를 쓰든 같다.



```pythin
#최솟값 최댓값이 있는 index 값을 가져옴

print(np.argmin(a))
print(np.argmax(a))
```



aggfunc에 집계함수들  중에서 후에 머신러닝에 많이 사용되는 함수

최댓값과 최솟값이 있는 인덱스를 반환한다.

