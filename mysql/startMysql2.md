# MYSQL 시작하기2



### MYSQL 명령어

SELECT !! 살펴보기



**0)USE `<데이터베이스명>` **



작업할 DataBase 선택

명령어로 database 선택시 해당 데이터 베이스를 더블 클릭하거나 위의 명령문을 사용하면 된다.



**1)SELECT `<칼럼명>` FROM `<table명>` **



특정 table의 특정 colum 데이터를 가져오기 위해 select를 사용한다.

만일 여러 개의 칼럼을 가져오고 싶다면 `<칼럼명>` 과 `,` 를 같이 사용한다.

칼럼명 입력란에 *를 사용하게 되면 모든 칼럼을 가져온다.



만일 FROM절을 생략하게 되면 내부에서 `FROM dual` 을 자동으로 생성하여 실행.

반드시 SELECT 절에는 FROM 이 있어야 하지만 MYSQL 내에서 연산을 하려고 할 때 가상의 테이블 `dual` 을 붙여서 연산이 가능하게끔 컴퓨터가 처리하는 것.



SELECT에 **조건** 을 붙이고 싶을 때는 `WHERE` 사용

SELECT에 **그룹**을 짓고 싶을 때는 `GROUP BY` 사용

SELECT에 **그룹조건** 을 짓고 싶을 때는 `HAVING` 을 사용

SELECT에 **정렬순서**를 정하고 싶을 때는 `ORDER BY` 을 사용



***입력순서*** 

WHERE -> GROUP BY -> HAVING -> ORDER BY

***해석순서***

FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY



**2)SELECT 응용**



```mysql
SELECT distinct city FROM customers;
```



distinct 를 이용하면 python 의 unique 같은 기능을 사용 가능



```mysql
SELECT count(customerNumber) FROM customers;
```



칼럼의 데이터 숫자를 알기 위해서 count(<칼럼명>) 사용 가능.



```mysql
SELECT count(customerNumber), count(city) FROM customers;
```



count를 사용해서 두 칼럼을 동시에 비교 가능하다.



```mysql
SELECT amount, amount*2 FROM payments;
SELECT amount, amount*2 AS bonus FROM payments;
```



출력되는 테이블의 칼럼명을 변경할 때  AS를 사용한다.

즉, 별칭을 이용할 때는 AS를 사용한다는 것.



**3)SELECT 조건절 WHERE** 



```mysql
SELECT * FROM orderdetails
WHERE priceeach > 30;
```



priceeach 칼럼의 값이 30 초과인 데이터만 쿼리로 가져오라는 명령어



```mysql
SELECT * FROM orderdetails
WHERE priceeach >= 30 AND priceeach <=50; 

##다른 방식

SELECT * FROM orderdetails
WHERE priceeach BETWEEN 30 AND 50;
```



`<and>` ,` <or>`  연산자를 사용해서 조건을 만들기도 가능.

위의 코드는 `<and>` 를 이용한 where절 조작. 

또한 BETWEEN A AND B를 사용. => A이상 B이하 의미



```mysql
SELECT customerNumber
FROM customers
WHERE country = 'USA' OR country = 'Canada';

SELECT customerNumber
FROM customers
WHERE country in ('USA', 'Canada');

SELECT customerNumber
FROM customers
WHERE not(country = 'USA' OR country = 'Canada');

SELECT customerNumber, country
FROM customers
WHERE country Not in ('USA', 'Canada');
```



위의 코드는 `<or>` 을 이용한 where절 조작

 or과 in 을 이용해서 where 절을 조작할 수 있다.

앞에 not을 붙이면 포함하지 않는 것을 의미.



```mysql
SELECT employeeNumber, firstName, reportsTO
FROM employees
WHERE reportsTO IS Null;

SELECT employeeNumber, firstName, reportsTO
FROM employees
WHERE reportsTO IS NOT Null;
```



NULL 값을 가지고 있는 데이터를 추출하기 위해서 `IS NULL ` 을 사용해야 한다.

(*주의 = NULL 사용 못함)

NULL 이 아닌 데이터만 가지고 오고 싶으면 `IS NOT NULL` 



```mysql
SELECT addressLine1
FROM customers
WHERE addressLine1 LIKE '%ST%';

SELECT addressLine1
FROM customers
WHERE addressLine1 LIKE '%ST';

SELECT addressLine1
FROM customers
WHERE addressLine1 LIKE 'ST%';
```



와일드카드를 이용해서 특정 문자를 포함하는 데이터만 추출할 수 있다.

이때는 WHERE절에 LIKE가 사용이 된다.

`%<내용>%` 은 <내용> 을 가지고 있는 데이터를 추출하는 것

`%<내용>` 은 <내용> 으로 끝나는 데이터를 추출하는 것

`<내용>% ` 은 <내용> 으로 시작하는 데이터를 추출하는 것.



```mysql
SELECT addressLine1
FROM customers
WHERE addressLine1 LIKE '_T%';
```



와일드카드에서 `_` 은 글자 하나를 의미한다 (엑셀로 치면 ?).

따라서 위의 코드는 맨 첫 글자가 아무거나 와도 좋지만 두 번째에 `T` 가 와야됨을 이야기 한다.



```mysql
SELECT addressLine1
FROM customers
WHERE addressLine1 LIKE BINARY '%st%';
```



대소문자를 구분하여 와일드카드를 사용하기 위해서는 `BINARY` 를 사용해야 한다.



```mysql
SELECT count(customerNumber), city
FROM customers
GROUP BY city;
```



그룹별로 구분하여 어떤 통계적 수치를 구하고 싶을 때, `GROUP BY`  를 사용한다.

즉, 집계함수와 GROUP BY 는 같이 사용된다. 

예를 들어서 집계함수는 `count`, `mean` 등등이 있다.

위의 코드는 CITY 별로 몇 개의 데이터를 가지고 있는지 구하는 코드이다.



```mysql
SELECT sum(CASE WHEN city = 'Nantes' THEN 1 ELSE 0 END)   cnt
FROM customers;

SELECT sum(CASE WHEN city = 'Nantes' THEN 1 
WHEN city = 'Las Vegas' THEN 2
WHEN city = 'Stavern' THEN 3 ELSE 0 END)   cnt
FROM customers;

```



`CASE WHEN`  은 파이썬의 `IF`문이라고 생각하면 된다.

CASE WHEN `<조건>  ` THEN `<참값>` ELSE `<거짓값>  `  을 기본으로 한다.

그리고 다중 IF문을 위의 코드처럼 할 수 있다.



```mysql
SELECT count(employeeNumber),count(reportsTO), count(*)
FROM employees; 
```



`count()` 함수의 인자에 칼럼을 넣게 되면 NULL 값을 뺀 후의 갯수를 반환한다.

하지만 `count(*)` 를 하게 되면 null 값을 포함하고 갯수를 센다.





