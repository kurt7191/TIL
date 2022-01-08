# 정규 표현식 2

```python
r = re.compile('&#(0[0-7]+|[0-9]+|x[0-9a-fA-F]);')
data = """&#06;
&#09;
&#xa;"""
m = r.findall(data)
print(m)
```



괄호를 사용하면 여러 개의 조건을 넣을 수 있다.



```python
r = re.compile('''
&#              # START OF A NUMBER ENTITY REFERENCE
(
0[0-7]+         # OCTAL FORM
|[0-9]+         # DECIMAL FORM
|x[0-9a-fA-F]   # HEXADECIMAL FORM
)
;               # Trailing semicolon
''', re.X) #re.VERBOSE

data = """&#06;
&#09;
&#xa;"""
m = r.findall(data)
print(m)
```



# 백슬래시 사용

```python
r = re.compile('\section')
m = r.match(' ection')
print(m)
```



\s 가 공백을 의미하기 때문에 이렇게 해야지 match 가 된다.



```python
r = re.compile('\\\\section')
m = r.match('\\section')
print(m)
```



`\` 를 문자 그대로 가져오기 위해서 본래 \ 를 두번 넣으면 된다. 

하지만 compile 에서는 `\\` 에다가 `\\` 를 추가해줘야 한다.

결국 compile 에서 `\` 를 표현하기 위해서는 `\\\\` 로 사용해야한다.



```python
r = re.compile(r'\\section')
m = r.match(r'\section') #raw string(일반문자열)
print(m)
```



r을 적어주면 문자 그대로를 의미한다.

compile에서는 똑같이 백슬래시 그대로를 보여주기 위해서 `\\` 로 사용한다.

하지만 match 함수를 사용할 때는 한 번만 사용해주면 된다.



# 문자열 소모가 없는 메타 문자



1)

`|` => or

```python
r = re.compile('Crow|Servo')
m = r.match('CrowHello')
print(m)
```



2)

`^` => 문자열의 맨 처음과 일치함을 의미



```python
r = re.compile('^Life')
m = r.match('Life is too short')
print(m)
```



3)

`$` => 앞의 문자가 마지막에 와야함을 의미



```python
r = re.compile('short$')
m = r.match('short')
print(m)
```



하지만 match 랑 같이 쓰면 앞의 문자가 제일 앞에도 와야 하고 제일 마지막에도 와야한다.

따라서 short 밖에 맞는 게 없음



```python
r = re.compile('short$')
m = r.search('Life is too short')
print(m)
```



따라서 Search 로 바꾸어 사용해야만 한다.



4)

`\A` => 



```python
r = re.compile('\Apython', re.M)
data="""python one
life is too short
python two
you need python
python three"""
m = r.findall(data)
print(m)
```



re.M 을 사용해도 전체 문자열 중에 가장 먼저인 단어만 파악한다.

^ 와는 차이를 보인은게, ^ 는 re.M 을 하게 되면 문장별(라인별)로 가장 먼저 온 단어를 비교한다.

^ 와 \A 와의 차이점을 기억해야 한다.



5)

`\Z` 는 Z앞에 단어가 마지막 단어로 들어가야지 매치가 된다.



```python
r = re.compile('python\Z', re.M)
data="""python one
life is too short
python two
you need python
python python"""
m = r.findall(data)
print(m)
```



6)

`\b` => 단어 구분자(word boundary) 이다. 보통 단어는 whitespace에 의해 구분이 된다.

\b => 공백을 가지고 구분자를 사용할 때 사용된다.



```python
r = re.compile('\\bclass\\b')
# r = re.compile('class')
m = r.search('no class at all')
print(m)
```



```python
# r = re.compile('\bclass\b')
r = re.compile(r' class ')
m = r.search('no class at all')
print(m)
```



공백이 들어가면 row `r` 로 사용하면 된다.



7)

`\B` => WHITESPACE 가 아니라 문자, 단어



```python
r = re.compile('\Bclass\B')
m = r.findall('the declassified algorithm')
print(m)
```



whitespace를 인식 하지 않겠다는 의미며, 글자로 양쪽으로 채워져 있는 것을 찾는다는 것을 의미한다.



# 그룹핑



그룹핑은 문자열이 계속해서 반복되는지 조사하는 정규식



`()` 를사용, 그룹을 만들어주는 메타문자임.



group(0) => 매치된 전체 문자열

group(1) => 첫 번째 그룹에 해당하는 문자열

group(2) => 두 번째 그룹에 해당하는 문자열

group(n) => n 번째 그룹에 해당하는 문자열



| group(0) | 매치된 전체 문자열             |
| -------- | ------------------------------ |
| group(1) | 첫 번째 그룹에 해당하는 문자열 |
| group(2) | 두 번째 그룹에 해당하는 문자열 |
| group(n) | n 번째 그룹에 해당하는 문자열  |
|          |                                |
|          |                                |



```python
r = re.compile('(ABC)+')
m = r.findall('ABCABCABC OK!')
print(m)
```



그룹핑을 findall 로 하면 한번만 리턴된다.



```python
r = re.compile('(ABC)+')
m = r.search('ABCABCABC OK!')
print(m)
```



search 는 세 개 다 가져옴.



```python
r = re.compile(r'\w+\s+\d+-\d+-\d+')
m = r.search('park 010-1234-5678')
print(m)
```



문자열 그대로를 이렇게 표현할 수 있다.

`\s+` 에서 `+` 를 사용했는데, 공백이 하나라 +를 굳이 넣어도 되지 않지만 혹시 몰라서 넣은 것.



```python
r = re.compile(r'\w+\s+(\d+[-]?)+')
m = r.search('park 010-1234-5678')
print(m)
```



`\w+\s+(\d+[-]?)+'` 에서 \d 를 통해서 숫자를 나타내고 \d+ 는 숫자 여러 개를 나타냄.

거기다 -에 ? 를 넣어서 0개거나 1개를 의미하게 하고. 이러한 조합을 그룹핑해서 ()+ 를 붙여 여러 개가 나올 수 있게 했다.



```python
r = re.compile(r'(\w+)\s+((\d+)-\d+-\d+)') #왼쪽-> 오른쪽, 바깥에서 안쪽으로
m = r.search('park 010-1234-5678')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

```



해석을 왼쪽에서 오른쪽으로, 바깥에서 왼쪽으로 하게 된다.



위는 왼쪽에서 오른쪽으로 먼저 하기 때문에

park , 그리고 010-1234-5678 이 group(1) 과 group(2) 에 해당하여 도출된다.

그리고 group(3) 을 통해서 괄호 안에 있는 010이 읽힌다 (바깥부터 앞서 읽었기 때문)



정규식에서 괄호가 있을 때 읽는 순서는 수학과 다르다.

*왼쪽에서 오른쪽, 바깥에서 왼쪽 순으로 해석해야 한다!* 



```python
r = re.compile(r'(\b\w+)\s+(\b\w+)')
# r = re.compile(r'(\b\w+)\s+\1')
m = r.search('Paris in the the the spring')
print(m)
```



위는 괄호가 두 개를 사용했다. 따라서 group(1), group(2) 가 사용이 된 것.



하지만



```python
# r = re.compile(r'(\b\w+)\s+(\b\w+)')
r = re.compile(r'(\b\w+)\s+\1')
m = r.search('Paris in the the the spring')
print(m)
```



이렇게 사용하게 된다면 그룹핑 1번을 반복한다는 의미다. \1에서 숫자는 그룹핑 번호를 적어준 것.

이때 이에 해당하는 것은 반복되는 문자열일 수 밖에 없으니 'the the' 가 도출된다.



즉, 재참조를 한다면 똑같은 문자가 나와야만 한다.



# 전방탐색



```python
# ':' 앞에 있는 문자열만 가져오기
r = re.compile('.+:')
m = r.search('http://google.com')
print(m)
```



`:` 을 기준으로 문자열을 가져오는 법



```python
r = re.compile('.+')
m = r.search('http://google.com')
print(m)
```



모든 문자열을 다 가져오게 됨.



```python
r = re.compile('.+(?=:)')
m = r.search('http://google.com')
print(m)
```



`?=`  는 긍정형 전방탐색 이용해서 http 만 가져온다.
이때 `:` 을 검색을 하지만 검색 결과로 : 을 제거한다.



```python
r = re.compile('.+(?!:)')
m = r.search('http://google.com')
print(m)
```



부정형 전방탐색.

`?!` 는 부정을 의미. 따라서  `.+` 대로 검색을 하게 된다.

?! : 에서 : 가 정규식과 매치가 되면 안됨을 의미하며

조건이 통과되어도 문자열이 소멸되지 않는다.(즉 찾는 대상의 문자열에서 없어지지 않는다.)



```python
#bar 이거나 cf 만 가져오고 싶을 때
r = re.compile('.*[.](bar|cf)$')
file = ['foo.bar', 'autoexec.bat', 'sendmail.cf']

for i in file:
    m = r.search(i)
    if m:
        print(m)

```



[.] => .를 문자하나가 아니라 있는 그대로의 문자로 본것.

위의 식은 긍정형 전방이 아니라 그냥 찾은 거다. (이거 때문에 헷갈리지 말자)

`?=` 과 `?!` 를 이용해서 가져오고 싶은 것만 가져올 수 있다.



```python
#bat 이거나 exe 가 아닐 때
r = re.compile('.*[.](?!bat|exe).+$')
file = ['foo.bar', 'autoexec.bat', 'sendmail.cf']

for i in file:
    m = r.search(i)
    if m:
        print(m)

```



부정형 전방탐색을 할 때는 `.+` 를 이용해서 모든 걸 다 가져오고 그 중에서 (?!bat|exe) 를 제외시킨다.

만일 `.+(?=:)` 이 있다면, `:` 되어있는 것을 먼저 검색하고 결과를 `:` 를 제외하고 반환한다.

즉, 긍정형은 검색어를 포함해서 검색후에 검색어를 제외하고 반환한다면,

부정형 전방탐색은 일단 모두 찾은 이후에 `?!<단어>` 를 제외하고 반환한다.

(따라서 모두 찾는 `.+` 와 같은 문자가 필요하다.)

 



# Greedy vs Non-Greedy



```python
# * 메타문자는 매우 탐욕스러워서 매치할 수 있는 최대한의 문자열을 가져온다.
# * 가 문자열을 모두 소모시킨다고 부른다.
r = re.compile('<.*>')
m = r.match('<html><head><title>Title</title>')
print(m.group())
len(m.group())
```



`r = re.compile('<.*>')` 을 사용하게 되면 data의 모든 문자열을 전부 불러오게 된다.

왜냐하면 `<html><head><title>Title</title>`  에서 `*` 가 탐욕스럽기 때문에 ,

`html><head><title>Title</title` 를 전부 문자로 여기기 때문이다.

이를 모두 소모시킨다고 부른다. 이를 greedy 하다고 부른다.(탐욕스럽다)

모두 소모시키지 않으면서 탐욕스럽지 않으려면 non-greedy 를 사용한다.



```python
#non-greedy 문자 ?은 *?,+?,??,{m,n}? 과 같이 사용한다.
#가능한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.

r = re.compile('<.*?>')
m = r.match('<html><head><title>Title</title>')
print(m.group())
len(m.group())
```



?를 사용하면 하나만 가져오게 된다.



