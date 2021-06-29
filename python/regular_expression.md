# 파이썬 정규표현식



```python
import re
```



정규표현식을 위해서 re를 임포트



```python
r = re.comile('a.c')
r.search('abc')
```



match가 됨



정규 표현식과 관련된 함수 4가지가 있음



- match() : 문자열 처음부터 정규식과 매치되는지 조사  
- search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사  
- findall() : 정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴.  
- finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴  



# 1)Search



Search 는 문자열 전체를 검색하여 찾는 문자와 match 되는 게 있는지 살펴본다.



### 정규 표현식 문자



정규표현식에 사용되는 문자들이 있다.

1) `.` 

`.` 은 문자 한 개를 나타낸다.



2) `?` 

?앞의 문자가  존재할 수도 있고 존재하지 않을 수도 있는 경우

=> ? 앞의 문자가 0개이거나 1개

? : {0,1} 의미한다.



```python
r = re.compile('ab?c')
m = r.search('abbc')
m = r.search('abc')

```



'ab?c' 에서 ? 앞의 문자 b가 존재할수도 있고 존재하지 않은 경우만 True로 매치를 반환한다.

첫 번째 m은 b가 두 개이기 때문에 None

두 번째는 1개이기 때문에 match를 반환한다.



```python
m = r.search('abc korea abc')
print(m)
```



처음으로 일치하는 것만 match 객체로 가져온다.



```python
m = r.search('korea abc')
print(m)
```



일치하는 게 뒤에 있기 때문에 뒤에만 가져온다.



```python
m = r.search('ac')
print(m)
```



'ab?c' 에서 ? 는 앞의 문자가 없어도 가져오기 때문에 이 또한 match를 가져오게 된다.



```python
m = r.search('koreaac')
print(m)
```



뒤에 `ab?c` 를 만족하는 부분이 있기 때문에 match 객체를 반환한다.

 

3)`*` 

`*` 앞의 문자가 0개 이상인 것.



```python
r = re.compile('a.*c')
m = r.search('axxxxc')
print(m)
```



4) `+`

`+` 앞의 문자가 최소 1개 이상은 와야한다.

```python
r = re.compile('ab+c')
```



5) `^`

`^` 뒤의 문자는 시작되는 문자를 지정



```python
r = re.compile('^a')
```



a로 무조건 시작해야만 한다.



6)숫자



```python
r = re.compile('ab{2}c')
m = r.search('ac')
```



b가 안왔기 때문에 none



```python
m = r.search('abbc')
print(m)
```



매치된다.



```python
m = r.search('abbec')
print(m)
```



compile가 달리 다른 문자가 들어갔기 때문에 none 반환



```python
r = re.compile('ab{2,4}c')
m = r.search('ac')
print(m)
```



{} 괄호 안에 숫자 두 개를 콤마를 이용해서 적어주면 몇 이상 몇 이하로 된다.

따라서 b를 2개 이상 4개 이하 적어줄 수 있다.

5개부터는 none.



```python
r = re.compile('a{2,}bc')
m = r.search('abc')
print(m)
```



위의 코드처럼 치면 2개 이상이라는 의미.

위의 코드대로면 none을 가져옴.

즉, 2개 이상만 되면 상관 없는 것.



```python
m = r.search('akaabc')
print(m)
```



k를 새롭게 추가해도 뒤에 일치하는 문자열이 있기 때문에 그대로 불러온다.



```python
r = re.compile('ab{,3}c')
m = r.search('ac')
```



3 이하도 위와 같이 표현 가능.

위의 식은 이상 없이 match 객체 반환.

왜냐하면 3 이하이기 때문에 0개도 되기 때문.



6) [ <문자열> ]



대괄호 안에 있는 문자열과 일치하면 match 객체 반환



```python
r = re.compile('[abc]')
m = r.search('zza')
print(m)
```



```python
m = r.match('kbaaca')
print(m)

```



매치는 처음부터 일치해야하기 때문에 일치 x



```python
m = r.findall('kbaaca')
print(m)
```



문자 전체에서 일치하는 문자를 리스트로 해서 반환.



```python
m = r.finditer('kbcca')
for i in m:
    print(i)
```



일치하는 문자를 반복가능한 객체로 반환



```python
r = re.compile('[a-z]')
m = r.search('bac')
print(m)
```



[a-z] 로 하게 되면 a부터 z에 포함이 되면 true로 보고 반환한다.



```python
r = re.compile('[a-z]+')
m = r.findall('life is too short')
print(m)
```



[] 와  + 를 결합하면 [] 안에 있는 문자가 1개 이상인 경우를 이야기 하기 때문에

" " 가 들어가기 전으로 리스트로 모든 일치하는 문자열을 가져온다.



```python
r = re.compile('[a-z]+')
m = r.findall('li2fe is %too short3')
print(m)
```



문자열이 일치하는 것만 가져오기 때문에 2와 % 3 을 기준으로 끊어서 가져온다.



```python
r = re.compile('[^abc]')
m = r.search('kabc')
print(m)
```



^ 는 처음 시작하는 단어를 설정해준다.

하지만 [] 와 함께 사용하면 <문자>^ 를 제외한 것만 True로 match 로 반환한다.

따라서 위의 kabc 는 match 반환된다.



만일 abc 였다면  반환하지 않는다.



# match



match는 처음부터 일치하는 것만 가져온다.



```python
m = r.match('ackorea')
print(m)
m = r.match('koreaac')
print(m)
```



처음 m은 가져오지만

두 번째 m은 못가져온다.

왜냐하면 match는 처음부터 일치하는 것만 match 객체를 반환하기 때문.



# findall



```python
m = r.findall('ackoreaac')
print(m)
```



findall은 일치하는 모든 문자를 찾아서 리스트로 반환한다.

앞서 search() 함수와 match() 함수가 match 객체를 반환한 것에 비해 리스트로 반환한다.



search 도 모든 문자 전체를 검색하는 것은 마찬가지지만, 

반환은 처음 일치하는 것만 반환한다.

하지만 findall은 일치하는 모든 것을 반환한다.



# finditer



```python
m = r.finditer('ackoreaac')
print(m)
for i in m:
    print(i.group(),i.start(),i.end(),i.span())
```



정규식과 일치하는 모든 문자열을 반복가능한 객체로 리턴해준다.

따라서 for문을 사용해서 꺼낼 수있다.

이때 객체는 match 객체로 group, start, end, span 함수를 사용할 수 있다.



# 정규 표현식 모델 함수



1)split()



```python
m = re.split('\n', text)
print(m)
```



기준 문자열로 전체문자열을 나눔 => 리스트로 반환



```python
m = re.split('\+', text)
print(m)
```



`+` 를 문자열 그대로 사용하려면 `\` 를 사용해준다.



```python
r = re.compile('[0123456789]+')
m = r.findall(text)
print(m)

r = re.compile('[0-9]+')
m = r.findall(text)
print(m)

r = re.compile('\d+')
m  = r.findall(text)
print(m)
```



0~9 까지의 숫자가 한 개 이상 포함한 것만 가져올 때 사용한다.

이때 `[a-z]` 로 사용했던 것처럼 숫자도 `[0-9]` 로 사용할 수 있다.

또한 `\d` 를 사용하여도 똑같은 결과를 가져온다 .



```python
r = re.compile('\D+')
m = r.findall(text)
print(m)
```



`\D` 는 숫자가 아닌 것만 찾아서 반환한다.



2)sub()



```python
r = re.compile('blue')
m = r.sub('color', 'blue socks and red shoes')
print(m)
```



blue와 일치하는 것을 찾고  지정한 문자로 바꿔준다.

위의 코드는 blue 를 color로 바꾼 것.



```python
r = re.compile('blue|red|green')
m = r.sub('color', 'blue socks and red shoes')
print(m)
```



여러 개를 동시에 바꾸는 것도 가능

or 를 의미하는 `|` 를 사용하여 위의 코드처럼 치면 blue red green 에 해당하는 문자는 color로 바뀜



```python
r = re.compile('[^a-zA-Z]')
m = r.sub('', text)
print(m)
```



자연어 처리에서는 위와 같이 특수문자에 대해서 제거할 수 있다.



```pytho
m = re.sub('[^a-zA-Z]','',text)
```



정규 표현식을 `compile()` 을 이용해서 찾을 수 있지만

위의 코드처럼 바로 함수 매개변수 안에 넣어서 사용할 수 있다.



3)subn()



```python
r = re.compile('blue|red|green')
m = r.subn('color', 'blue socks and red shoes')
print(m)
```



`sub()` 함수와 비슷하지만 return 값이 튜플이다.

또한 튜플 안에 바뀐 개수도 나타난다.



# 정규 표현식  텍스트 전처리



```python
r = re.compile('[ \t\n]')
m = r.split(text)
print(m)
```



위는 공백, tab, 줄 나눔을 의미하는 코드



```python
r = re.compile('[\t\n]')
m = r.split(text)
print(m)
```



위는 공백이 없다. 따라서

tab, 줄 나눔을 의미



```python
m = re.split('\s+', text)
print(m)
```



공백을 기준으로 나눌 때 위처럼 `\s+` 를 사용한다.

`+` 를 쓰는 이유는 하나 이상도 하나로 치기 위해서.



```python
r = re.compile('[0-9]+')
m = r.findall(text)
print(m)
```



숫자만 꺼내올 때 위의 코드로 사용



```python
r = re.compile('\d+')
m = r.findall(text)
print(m)
```



숫자만 꺼내올 때 위의 코드처럼 사용 가능.



```python
r = re.compile('[A-Z]{4}')
m = r.findall(text)
print(m)
```



대문자가 4개로 된 것만 추출



```python
m = re.findall('[A-Z]{4}', text)
print(m)
```



이렇게 바로 compile 없이 사용할 수 있다.



```python
r = re.compile('[A-Z][a-z]+')
m = r.findall(text)
print(m)
```



대문자와 소문자가 섞인 여러 개의 문자를 추출



# 컴파일 옵션 - 정규식을 컴파일할 때 사용하는 옵션



정규식을 컴파일할 때 사용하는 옵션을 컴파일 옵션이라고 부름


```python
r = re.compile('a.b')
m = r.match('a\nb')
print(m)
```



컴파일 문자에 `.` 은 어떠한 문자를 의미하느느데, 줄바꿈인 `\n` 은 적용이 안됨



```python
r = re.compile('a.b', re.S)
m = r.match('a\nb')
print(m)
```



줄바꿈도 적용을 하고 싶을 때는 `re.S` 를 사용하면 된다.




```python
r = re.compile('a.b', re.DOTALL)
m = r.match('a\nb')
print(m)
print(m.group(),m.start(),m.end(), m.span())
```



`re.S` 를 `re.DOTALL` 로 바꿔서 사용해도 똑같은 결과를 얻을 수 있다.



```python
r = re.compile('[a-zA-Z]')
m = r.match('Life is too short')
print(m)
```


대소문자 구분 없이 가져올 때 위와 같이 사용한다. 



```python
r = re.compile('[a-z]', re.I)
m = r.match('Life is too short')
print(m)
```



`re.I` 를 사용하게 되면 `[a-zA-Z]` 를 사용하지 않아도 대소문자 둘 다 적용이 된다.



```python
r= re.compile('^python\s\w+')
data="""python one
life is too short
python two
you need python
python three"""

m = r.findall(data)
```



\w => [a-z] 와 똑같은 의미.

위는 `^` 이기 때문에 처음 시작 단어가 컴파일과 일치하는지 확인한다.



```python
r= re.compile('^python\s\w+', re.M)
data="""python one
life is too short
python two
you need python
python three"""

m = r.findall(data)
print(m)
```



`re.M` 을 사용하면 모든 문자열에서 컴파일 식과 일치하는 것을 찾게 된다.

