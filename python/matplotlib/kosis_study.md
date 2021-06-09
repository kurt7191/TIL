# 통계적 신생아수 시각화



## **통계청 신생아수 데이터 matplotlib 시각화**





기술통계 시각화 작업을 해봄.

*=> 기본적인 전처리와 Seaborn의 다양한 그래프를 사용해봤다.*



```python
df['variable'].str.split('.', expand = True) #의 return 은 DataFrame임.

df['variable'].str.split('.', expand = True)[index] #는 return 이 Series임.
```



전처리 중에 `df['variable'].str.split('.', expand = True)`  를 사용하여 전처리 하는 쉬운 방법 알아냄

(이 함수는 split을 모든 행에 적용시켜준다.)



```python
for i in df['variable']:
    df['연도'] = i.split('.')[0]
    df['월'] = i.split('.')[1]
    df['성별'] = i.split('.')[2]
```



사실 나는 이렇게 하려고 했는데, 문젠 성별 정보를 안가지고 있는 variable 데이터 같은 경우에 out of index 오류가 뜸. 그래서 try except 같은 걸로 if에 continue 걸어서 무슨 방법이 있겠거니 해볼라다 저런 방법이 있다는 걸 알고 그냥 앞으로 저거 쓰기로함.. 간단한 길이 있었음...

 

 **Seaborn 다양한 시각화 해봄**

 

1)lineplot



```python
plt.figure(figsize=(10,5))
sns.lineplot(data = <블라블라>, x = '연도', y = '출생아수')

sns.lineplot(data = <블라블라>, x = '연도', y = '출생아수', ci = None)

sns.lineplot(data = <블라블라>, x = '연도', y = '출생아수', ci = None, hue = '월')
```



lineplot이 있는데 평균적인 선 하나랑 평균이 아닌 분포를 나타내는 굵은 선이 있음

ci 를 None으로 하면 평균적인 선만 나오고 생략하면 분포선도 같이 나옴



2)boxplot



```python
plt.figure(figsize=(15,4))

sns.boxplot(data = <블라블라>, x = '연도', y = '출생아수')

sns.boxplot(data = <블라블라>, x = '연도', y = '출생아수', hue = '월')
```



이건 뭐 많이 사용했던 boxplot 시각화고.

(범주 데이터에 주로 많이 사용한듯)

 

3)pointplot



```python
plt.figure(figsize=(15,4))

sns.pointplot(data = <블라블라>, x = '연도', y = '출생아수')

sns.pointplot(data = <블라블라>, x = '연도', y = '출생아수', hue = '시군구별')

plt.legend(loc = 'center right', bbox_to_anchor=(1.17,0.5), ncol=1)
```



이것도 두 범주 데이터를 비교할 때 사용하는 범주 데이터 그래프 같음. 교차분류그래프의 선 version ? 느낌

 

legend 위치를 설정해주는거 몰랐음 loc로 위치 조절가능,

bbox_to_anchor의 인자는 다음과 같음 => (x,y,width,height)

x,y 인자는 생략해도 가능한듯?

 