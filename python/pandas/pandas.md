# 판다스 시작



> 판다스 기본 기능들



```python
data = pd.read_csv('C:\study\workspace_python\pdsample/num.txt',header=None)
```



판다스 데이터 불러오기

header를 설정하지 않고 txt파일을 읽어오게 되면 txt 파일의 첫 번째 줄이 header가 되어서 나타남.

따라서 header 자동 설정을 풀어줘야 하는데, 파라미터 header의 매개변수에 None 인자를 넣으면 됨.



```python
#칼럼 열
print(data[0])
print(type(data[0]))

#행
print(data.iloc[0])
type(data.iloc[0])
```



열과 행 모두 Series를 반환한다.

이를 통해 데이터 프레임은 여러 Series의 묶음임을 알 수 있다.



```python
data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")

```



인터넷에 있는 데이터를 긁어올 때 `read_csv`로 긁어올 수 있다.



```python
data.info()
```



데이터 프레임에 대한 정보를 얻을 수 있다.

(데이터의 개수, 칼럼의 개수, 데이터 타입 정보, null 값의 개수 등을 알 수 있다.)



```python
data.head()
data.tail()
data.head(10)
data.tail(10)
```



데이터 앞의 5개 정보를 보려면 `head()` 사용

뒤 5개를 보려면 `tail()` 사용

head와 tail 안에 인자를 설정하면 보이는 데이터 개수를 설정할 수 있다.



```python
data.sample()
data.sample(10)
```



데이터를 랜덤으로 하여 보여주는 기능이 있다. `sample()` 도 마찬가지로 인자 값을 설정하면 랜덤으로 보이는 데이터의 개수를 설정할 수 있다.



```python
data.values #데이터만 가져온다.
data.index #인덱스를 가져온다.
data.columns #데이터의 컬럼들을 가져온다.
```



데이터 프레임의 value와 index 그리고 칼럼들을 확인할 수 있다.



## **본격 데이터 프레임 인덱싱**



> iloc, loc 별 index, slicing, comma, fancy



```python
data.iloc[3]
data.iloc[0:5] #Slicing
data.iloc[[0,3,5]] #Fancy
data.iloc[0,4] #comma
data.iloc[:,[0,3,5]] #Slicing & Fancy
```



comma를 사용하기 전에는 행만 가져옴.

comma를 사용하여 행과 열을 특정지어서 가져오기 가능 (이때 `:`  사용 가능)

*`iloc` 는 인덱스를 이용해서 데이터 값을 가져오는 것!



```python
data['tip'] #열 1개
data[['tip','day']] #열 여러 개는 안에 리스트로 받아서
```



열을 한 개 가져올 때는 이름만 적는다.

열을 여러 개 가져올 때는 리스트로 받는다.



```python
data['tip']
data[['tip']] #Fancy 가능
```



Fancy로 인덱싱을 할 시 칼럼을 하나만 집어 넣어도 데이터 프레임으로 리턴한다.



```python
data.loc[:,'tip']
```



특정 행과 특정 열을 가져올 때,

`loc` 는 열의 이름을 통해서 가져올 수 있게 해준다.



## **at**



```python
data.at[0,'tip'] # == data.loc[0,'tip']
```



하나의 값만 가져오는 게 가능하다.

slicing 사용이 불가능하다.



## **iat**



```python
data.iat[0,1]
```



인덱스로만 가져온다.

그러나 slicing 사용하지 못한다.



## **boolean indexing**



```python
data.tip>5
data['tip'] >= 5
```



True/False의 결과값을 가지는 Series를 가져온다.



```python
data[data['tip'] >= 5]
data[data.tip>5]
```



True/False를 가지고 있는 시리즈를 data에 넣으면 True인 값만 반환한다.

전체 데이터 프레임을 반환해줌



```python
data[data['tip']>5]['tip']
data[data['tip']>5].sex
```



어떤 조건하의 데이터 프레임 중에서 특정 열을 추출하고 싶을 때 위의 코드처럼 사용



```python
data[data['tip']>=5].loc[:,'tip':'size']
```



loc,iloc와 혼합해서 사용할 수 있음



```python
data[(data['day']=="Sun") | (data['day'] == "Sat")][['tip','day']]
a['day'].unique()
```



조건에 맞았늕 맞지 않았는지 unique로 확인하기



## **rename()**



```python
data.size
```



size 컬럼 데이터를 가져오고 싶었는데, python size 함수가 이미 존재한다.

size 함수는 요소의 개수를 세는 함수이므로 컬럼 데이터를 가져오는 게 아니라 요소의 개수를 가져온다.

따라서 이름을 바꿔줘야 한다.



```python
#mapper는 dic같은 것
data.rename(mapper={'size': 'size_'}, axis = 1, inplace = True)
#columns 매개변수도 같은 기능
data.rename(columns={'size': 'size_'}, axis = 1, inplace = True)
```



shift + tab을 누르면 매개변수에 mapper가 존재한다.

mapper는 dic 형식으로 사용한다. (columns도 똑같은 기능)

그 이외에 axis, inplace 매개변수 존재.



## **category**



```python
data['sex']= data['sex'].astype('category')
data.info()
```



category 데이터 타입으로 sex를 바꾸면, info를 통해서 확인하면 object 타입이었던 것이 category로 바뀌어 있는 것을 확인할 수 있다.



데이터 타입을 바꿀 때는 `astype()` 을 이용한다.

