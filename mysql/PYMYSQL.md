# 파이썬 MYSQL 연동





```python
!pip install pymysql
```



우린 pymysql을 사용하여 파이썬과 mysql을 연동 할것임.



```python
import pymysql
conn = pymysql.connect(host='localhost',port=3306, user='root', password = 'a1234', db='classicmodels')
cur = conn.cursor()
cur
```



mysql ip 주소를 설정해야 한다. 기본적으로 로컬로 mysql이용 중이기 때문에

기본 로컬 ip인 127.0.0.1로 설정한다. 간편하게 `localhost` 로 ip를 지정할 수 있다.

또한 서버에는 많은 문들이 존재한다. 문은 port라고 부르며 보통 mysql 은 3306을 열어둔다.

아이디와 비번도 적어주고 연결을 끝낸다.



##### PYMYSQL 에서 SELECT



```python
cur = conn.cursor()
sql = 'SELECT * FROM customers'
cur.execute(sql)

result = cur.fetchone()
print(result)
```



conn은 현재 데이터베이스를 불러온 것이다.

cur = conn.cursor() 객체를 생성한다.

cur을 통해서 execute 함수를 사용하여 쿼리문을 실행한다.



받아온 자료들을 cur.fetchone을 통해서 하나씩 나타낼 수 있다.



```python
result = cur.fetchall()
for i in result:
    print(i[0],i[1])
    
conn.close() #db접속 종료
```



fetchall로 하면 모든 데이터를 다 불러올 수 있음 tuple형태로 존재한다.

반복문을 통해서 모두 꺼낼 수 있다.

중요한 것은 데이터베이스와의 연결을 업무가 끝나면 끊어줘야 한다.



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='classicmodels')
cur = conn.cursor()
num = 119
sql = 'SELECT * FROM customers WHERE customerNumber = %s'
cur.execute(sql,(num))
```



pymysql은 쿼리문을 실행할때 마다 연결을 다시 해줘야 한다.



그리고 위의 num값을 집어넣을 때  list , tuple이면 위의 코드처럼 실행한다.

=> %s로 넣어야하며, execute 괄호 안에 튜플 형태로 value를 집어넣어야 한다.



```python
result = cur.fetchone()
print(result[0],result[1])
```



fetchall로 가져오지 않은 이유는 where 절 밑의 칼럼이 프라이머리 키이기 때문이다.

프라이머리 키는 중복된 값을 허용하지 않기 때문에 `fetchone()`이 맞다.

만일 프라이머리 키가 아니라면 `fetchall()` 을 사용해도 무방하다.



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='classicmodels')
cur = conn.cursor()

search = 'A'
sql = 'SELECT * FROM customers  WHERE customerName LIKE BINARY "%%%s%%"' % search
cur.execute(sql)

result = cur.fetchall()
print(sql)
for i in result:
    print(i)
    

```



와일드카드를 이용한 조건문 활용시 sql문을 작성할 때 주의해야만 한다. 퍼센트지 `%`를 두 번 사용해줘야 사용 가능하다. 또한 `''`, `""` 를 적어주야 시행이 된다.



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='classicmodels')
cur = conn.cursor()

search = 'A'
sql = 'SELECT * FROM customers  WHERE customerName LIKE BINARY %s'
cur.execute(sql,"%%%s%%" % search)

result = cur.fetchall()
print(sql)
for i in result:
    print(i)
    

```



위와 동일하지만 sql 작성문을 execute에 집어넣느냐 sql변수에 집어넣느냐의 차이를 가진다.



##### pymysql 에서 update



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()
id = int(input())
name = input()
sql = 'UPDATE person SET name = %s WHERE ID = %s'
# sql = "UPDATE person SET age = 15 WHERE id = %s, name = %s"
cur.execute(sql,(name,id))
print(sql)
conn.commit()
conn.close()

```



`input()` 을 이용하여 수정할 데이터를 입력 받아 수정 수행.

PYMYSQL 을 통해서 UPDATE 쿼리를 실행하기.



입력받은 id와 name의 age를 15 로 바꾸는 코드

이때 중요한게 commit을 사용해줘야 한다.

만일 commit을 하지 않는다면 db의 실제 데이터는 바뀌지 않는다.



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()
id = int(input())
name = input()
data = {"id":id,"name":name}
sql = 'UPDATE person SET name = %(name)s WHERE ID = %(id)s'
cur.execute(sql,data)
print(sql)
conn.commit()
conn.close()

```



sql문을 dic으로 넣는 코드

튜블로 넣을 경우에는 execute에 순서에 맞지 않게 넣어도 상관이 없다.

즉, dic으로 execute를 조절할 경우에는 순서에 상관없이 조작이 된다.



##### PYMYSQL 에서 INSERT



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()

data = (40,'이기상',21)
sql = 'INSERT INTO person(id,name,age) VALUES (%s,%s,%s)'
cur.execute(sql,data)
conn.commit()
conn.close()

```



inser 또한 원리는 다른 dml 명령어와 비슷하다.



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()

data = [(70,'오우야',21),(60,'그린',25)]
sql = 'INSERT INTO person(id,name,age) VALUES (%s,%s,%s)'
cur.executemany(sql,data)
conn.commit()
conn.close()

```



앞선 insert는 `execute()`를 사용하여 데이터 하나를 집어넣은 것이고

`executemany()`  는 여러 개의 데이터를 집어 넣는 경우임



```python
conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()

data = [{"id":88,"name":"강아지","age":32},{"id":90,"name":"고양이","age":17}]
sql = 'INSERT INTO person(id,name,age) VALUES (%(id)s,%(name)s,%(age)s)'
cur.executemany(sql,data)
print(sql)
conn.commit()
conn.close()

```



dic을 이용하여 inser하는 방법, 위의 명령어들과 원리는 같다.



```python
id = int(input())

conn = pymysql.connect(host='localhost', port = 3306, user = 'root', password = 'a1234',
                      db='shop')

cur = conn.cursor()

data = (id)
sql = 'DELETE FROM person WHERE id = %s'
cnt = cur.execute(sql, data)
print(sql)
print("delete : %s" %(cnt))
conn.commit()
conn.close()

```



변수로 execute를 받으면 수행한 갯수를 반환한다.



### 날짜 데이터 받기



```mysql
SELECT now(), curdate(), current_date, current_date();
SELECT curdate(), curdate() + 0 , curdate() + 1;
```



맨 먼저 sql의 날짜 문법부터 살펴보자

sql은 날짜와 관련된 함수를 제공한다.

맨 첫줄은 하이폰 `-` 이 포함된 상태로 날짜 값들이 출력

두 번째 줄은 `-` 이 생략된 상태로 출력



```mysql
#날자 사이의 일수 알기
SELECT datediff(curdate(), '2021-06-02');
```



오늘 날짜와 설정한 날짜 사이의 차이를 뽑아온다.



```mysql
#월만 뽑아오기
SELECT month(curdate());
SELECT day(curdate());
SELECT weekday(curdate());
SELECT dayofweek(curdate()); #일요일 : 1, 월요일 : 2
SELECT week(curdate()) #일년을 기준으로 해서 현재 몇 번째 주인지 알려줌
```



특정한 날짜도 뽑아올 수 있다.

`weekday()` 는 요일을 뽑아오는데 월요일을 0으로 리턴하고 화요일을 1로 리턴하는 순서를 가진다.

`dayofweek()`  또한 요일을 뽑아오는데 대신에 일요일을 1로 기준잡고 날짜릊ㄹ 뽑아온다.

`week()` 는 일년을 기준으로 현재가 몇 번째 주인지 알아봐준다.



