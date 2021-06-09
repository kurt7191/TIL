# python matplotlib 시각화

> **plt.figure(figsize=())**
>
> **plt.axes()**
>
> **plt.plot()**
>
> **plt.title()**
>
> **plt.grid()**﻿
>
> **plt.xlabel()**
>
> **plt.ylabel()**
>
> **plt.xticks()**
>
> **plt.yticks()**
>
> **plt.xlim()**﻿



```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

```



matplotlib 패키지와 seaborn 패키지 중에 matplotlib을 살펴볼 예정



```python
plt.figure(figsize=(10,5))

```



그래프의 가로 세로 비율 설정



```python
plt.axes()
```



그래프를 보여줌



```python
plt.figure(figsize=(10,5),facecolor = 'red')
plt.axes()
```



만일 같은 axes()와 figure()이 같은 셀에 있다면 figure 설정대로 그대로 시각화 해줌

하지만, plt.axes() 같은 경우에는 figure를 설정하지 않아도 기본적으로 figure를 설정함. 따라서 단독으로 사용 가능하다.



```python
plt.figure(figsize=(10,5), facecolor = 'red')
plt.figure(figsize=(10,5), facecolor = 'green')
plt.axes([0,0,0.3,0.5]) #[left,bottom,width, length]
plt.axes([0,0.5,0.5,0.5])
plt.axes([0.5,0.5,0.5,0.5])
# plt.axes([0.3,0.3,0.5,0.5])

```



한 셀에 같이 작성하면 겹쳐서 시각화가 된다.

한 셀에 작성하면 겹쳐서 나온다는 점에 주목하자.



```python
plt.figure(figsize=(10,5))
plt.axes()
plt.plot([1,2,3,4])
plt.plot([3,4,5,6])
```



figsize = (10,5) 이기 때문에 더 큰 사이즈로 이미지가 그려진다.

그릐고 plot을 통해서 직선이 그어지고, 한 셀에 같이 있기 때문에 하나의 그래프 안에 동시에 그려진다.



![first](C:/study/workspace_python/first.png)





```python
plt.title('my first graph title')
plt.plot([1,2,3,4])
```



plt.title()을 통해서 그래프의 타이틀을 설정할 수 있다.



```python
plt.figure(figsize=(10,5))
plt.axes()
plt.plot([1,2,3,4])
plt.title('my first title')
```



지금까지 배운거 모두 합쳐서 작성하면 위와 같다.



```python
plt.title('나의 첫 한글 타이틀')
plt.plot([1,2,3,4])
```



title로 한글을 사용하면 한글이 깨진다.



**참조!**﻿

**한글화 깨질 때 사용법** 



```python
import matplotlib as mp

fm = mp.font_manager.FontManager()
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.title('나의 첫 한글 타이틀')
plt.plot([1,2,3,4])
```



mp를 이용해서 font_manager.FontManager() 객체를 생성한다.

그리고 reParams의 font.family를 원하는 글꼴로 설정한다.



```python
plt.rc('font', family = 'Malgun Gothic')
```



위의 코드처럼 다른 한글 설정 법도 존재한다.

둘 중에 되는 코드를 선택하면 됨







---



```python
plt.title('한글')
plt.grid()
```



plt.grid() 는 그래프 모양을 바둑 모양으로 바꿔준다.



![test2](C:/study/workspace_python/test2.png)





```python
plt.title('한글')
plt.grid()
plt.xlabel('x라벨')
plt.ylabel('y라벨')

```



x축과 y축의 이름을 정할 수 있는데 바로 plt.xlabel() 과 plt.ylabel() 이다.



```python
plt.xticks([1,2,3])

```



x축의 넓이를 xticks를 통해서 정할 수 있다.



```python
plt.yticks([2,3,4], labels=['가','나','다'])
```



ticks 같은 경우에는 넓이를 숫자로 넣어줘야하고 라벨을 labels 파라미터르 통해서 정해줘야 한다.



```python
#xlim은 x축에서 그래프를 보여줄 만큼 자른다.
plt.xlim(0.2,0.6)
```

![test3](C:/study/workspace_python/test3.png)

## **style**



```python
print(plt.style.available)
tips  = sns.load_dataset('tips')
tips.groupby('sex')['tip'].mean().plot.bar()
```



그룹바이를 sex 별로 하고 그룹바이 함수 mean과 함께 시각화한 작업





![test4](../../../../../../study/workspace_python/test4.png)



```python
plt.style.use('ggplot')
tips.groupby('sex')['tip'].mean().plot.bar()
```



클래식 버전으로 바꿀 수 있음.

plt.style.use() 함수를 사용하여 인자에 원하는 스타일을 집어 넣으면 그래프가 바뀌게 된다.



![test6](../../../../../../study/workspace_python/test6.png)





```python
plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)


```



plt.subplot() 은 화면을 나누어 한 화면에 시각화한 결과를 나타내는 함수이다.

위의 함수들은 2행 2열로 나누고 마지막 인자는 나눈 곳 중에 어디에 그래프를 넣을지 결정하는 인자이다.



![test8](../../../../../../study/workspace_python/test8.png)

plt.title() 를 subplot 바로 아래에 사용하여 그래프 이름을 적는다.



```python
plt.subplots(2,2)

```



plt.subplots 처럼 subplots를 사용하면 자동으로 2행 2열로 그래프를 만든다.



```python
fig, axes = plt.subplots(2,2)
axes[1,0].plot([1,2,3])
```



subplots 은 두 값을 return 언팩킹으로 두 값을 받는다.

1행 0열에 plot함수를 사용한다는 의미



axes를 통해서 몇행 몇열에 어떤 그래프를 그릴지 결정을 하고

fig는 그 값을 그래프로 화면에 보여준다.



```python
fig, (axes1,axes2) = plt.subplots(2,2)
axes1[0].plot([1,2,3])
axes2[1].plot([1,2,3])

```



axes1[0] 은 0행 0열을 의미하고

axes2[1] 은 1행 1열을 의미한다. 

언팩킹으로 받은 axes를 위의 코딩으로 plot그래프로 설정하고 fig를 띄우면 그래프가 나온다.



```python
fig, ax = plt.subplots(1,1)
ax.set_title('그래프')
plt.rcParams['font.family'] = 'Malgun Gothic'
```



ax에 dir을 해서 살펴보면 set_title이 보인다. 그래프의 타이틀을 정할 수 있다.



```python
fig, ax1 = plt.subplots(1,2)
p = tips.groupby('sex')['tips'].mean().plot
p.bar(ax = ax1[0])

fig
```



subplots 을 통해서 1행 2열의 그래프를 만들고

p데이터를 plot처리하여 더이터 처리 한 이후에

p.bar 매개변수 값에 ax1[0] 즉, 1행 1열에 bar그래프를 넣는다는 말임.



```python
fig, ax = plt.subplots(1,2)
a = pd.Series({'Male' : tips[tips['sex']=='Male']['tip'].mean()})
b = pd.Series({'Female' : tips[tips['sex']=='Female']['tip'].mean()})
a.plot(kind = 'bar', ax=ax[0])
b.plot(kind = 'bar', ax=ax[1])
plt.savefig('seriesMake')
```



성별 팁의 평균 값을 하나하나 뜯어서 각자 그래프를 만드려면 numpy에서 그래프를 그리지 못하기 때문에 series로 변환한 이후에 그래프를 그려야만 한다.

![seriesMake](../../../../../../study/workspace_python/seriesMake.png)