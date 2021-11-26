# 데이터베이스구조와운용(12) - MySQL(1)





> 데이터 정의 (데이터 정의어 DDL)
>
> 데이터 조작 (데이터 조작어 DML)
>
> 데이터 제어 (데이터 저어어 DCL)
>
> 
>
> 오늘은 각각의 것들을 직접 실천해봄





### 테이블 생성



```mysql
CREATE TABLE 고객(
  고객아이디 VARCHAR(20) NOT NULL,
  고객이름 VARCHAR(10) NOT NULL,
  나이 INT,
  등급 VARCHAR(10) NOT NULL,
  직업 VARCHAR(20),
  적립급 INT DEFAULT 0,
  PRIMARY KEY(고객아이디));
  
 CREATE TABLE 제품(
   제품번호 CHAR(3) NOT NULL,
   제품명 VARCHAR(20),
   제고량 INT,
   단가 INT,
   제조업체 VARCHAR(20),
   PRIMARY KEY(제품번호),
   CHECK (재고량 >= 0 AND 재고량 <= 10000));
   
  CREATE TABLE 주문(
    주문번호 CHAR(3) NOT NULL,
    주문고객 VARCHAR(20),
    주문제품 CHAR(3),
    수량 INT,
    배송지 VARCHAR(30),
    주문일자 DATE,
    PRIMARY KEY(주문번호),
    FOREIGN KEY(주문고객) REFERENCES 고객(고객아이디),
    FOREIGN KEY(주문제품) REFERENCES 제품(제품번호));
    
    
    CREATE TABLE 배송업체(
      업체번호 CHAR(3) NOT NULL,
      업체명 VARCHAR(20),
      주소 VARCHAR(100),
      전화번호 VARCHAR(20),
      PRIMARY KEY(업체번호));

ALTER TABLE 고객 ADD 가입날짜 DATE;

ALTER TABLE 고객 DROP COLUMN 가입날짜;

ALTER TABLE 고객 ADD CONSTRAINT CHK_AGE CHECK(나이 >=20);

DROP TABLE 배송업체;

INSERT INTO 고객 VALUES ('apple', '정소화', 20, 'gold', '학생', 1000);
INSERT INTO 고객 VALUES ('banana', '김선우', 25, 'vip', '간호사', 2500);
INSERT INTO 고객 VALUES ('carrot', '고명석', 28, 'gold', '교사', 4500);
INSERT INTO 고객 VALUES ('orange', '김용욱', 22, 'silver', '학생', 0);
INSERT INTO 고객 VALUES ('melon', '성원용', 35, 'gold', '회사원', 5000);
INSERT INTO 고객 VALUES ('peach', '오형준', NULL, 'silver', '의사', 300);
INSERT INTO 고객 VALUES ('pear', '채광주', 31, 'silver', '회사원', 500);

INSERT INTO 제품 VALUES ('p01', '그냥만두', 5000, 4500, '대한식품');
INSERT INTO 제품 VALUES ('p02', '매운쫄면', 2500, 5500, '민국푸드');
INSERT INTO 제품 VALUES ('p03', '쿵떡파이', 3600, 2600, '한빛제과');
INSERT INTO 제품 VALUES ('p04', '맛난초콜릿', 1250, 2500, '한빛제과');
INSERT INTO 제품 VALUES ('p05', '얼큰라면', 2200, 1200, '대한식품');
INSERT INTO 제품 VALUES ('p06', '통통우동', 1000, 1550, '민국푸드');
INSERT INTO 제품 VALUES ('p07', '달콤비스킷', 1650, 1500, '한빛제과');


INSERT INTO 주문 VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '2019-01-01'); 
INSERT INTO 주문 VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '2019-01-10'); 
INSERT INTO 주문 VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '2019-01-11'); 
INSERT INTO 주문 VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '2019-02-01'); 
INSERT INTO 주문 VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '2019-02-20'); 
INSERT INTO 주문 VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '2019-03-20'); 
INSERT INTO 주문 VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '2019-03-15'); 
INSERT INTO 주문 VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '2019-04-10'); 
INSERT INTO 주문 VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '2019-04-11');
INSERT INTO 주문 VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '2019-05-22');



```



### 테이블 조회



```mysql
#고객 테이블에서 고객 아이디, 고객이름, 등급속성을 검색해보자

SELECT 고객아이디, 고객이름, 등급
FROM 고객;

SELECT * FROM 고객;

SELECT DISTINCT 제조업체
FROM 제품;

SELECT DISTINCT 제조업체 AS 현재공급업체
FROM 제품;

SELECT 제품명, 단가 AS 가격
FROM 제품;

```



### 연산



```mysql

SELECT 제품명, 단가 + 100 AS 조정단가
FROM 제품;
```



### 조건 조회



```mysql
SELECT 제품명, 단가
FROM 제품
WHERE 단가 > 2000;

#주문 테이블에서 2019년 3월 이후의 데이터만 검색

SELECT *
FROM 주문
WHERE 주문일자 > '2019-03-01';

#제품 테이블에서 한빛제과가 만든 제품명, 재고량을 검색

SELECT 제품명, 재고량
FROM 제품
WHERE 제조업체 ='한빛제과';

#주문테이블에서 APPLE 고객이 15이상 주문한 주문제품, 수량, 주문일자

SELECT 주문제품, 수량, 주문일자
FROM 주문
WHERE 주문고객 = 'apple' and 수량 >= 15;

#제품테이블에서 단가가 2500원 이상이면서
#3500원 이하인 제품의 제품명, 단가, 제조업체

SELECT 제품명, 단가, 제조업체
FROM 제품
WHERE 단가 >= 2500 AND 단가 <= 3500;

#고객 테이블에서 성이 김씨인 고객의
#고객이름, 나이, 적립급

SELECT 고객이름, 나이, 적립금
FROM 고객
WHERE 고객이름 LIKE '김%'; 

#고객 테이블에서 고객 아이디가 5자인 고객의 고객아이디
#고객이름, 등급

SELECT 고객아이디, 고객이름, 등급
FROM 고객
WHERE LENGTH(고객아이디) = 5;

SELECT 고객아이디, 고객이름, 등급, 적립금
FROM 고객
WHERE 고객아이디 LIKE '_____';

#NULL 이용
#고객테이블에서 나이가 아직 입력되지 않은 고객을 검색해보자

SELECT *
FROM 고객
WHERE 나이 IS NULL;

SELECT *
FROM 고객
WHERE 나이 IS NOT NULL;

#정렬검색
#ORDER BY

#고객테이블에서 나이를 기준으로 내림차순

SELECT *
FROM 고객
ORDER BY 나이 DESC;

#그 반대
SELECT *
FROM 고객
ORDER BY 나이;


#주문테이블에서

SELECT 주문제품, 수량, 주문일자
FROM 주문
WHERE 수량 >= 10
ORDER BY 주문제품;

#주문제품으로 ASC 하되, 똑같은 이름의 제품은 DESC로 
SELECT *
FROM 주문
WHERE 수량 >= 10
ORDER BY 주문제품 ASC, 수량 DESC;


SELECT AVG(단가)
FROM 제품;

#한빛제과에서 제조한 모든제품의
#재고량의 합계

SELECT SUM(재고량)
FROM 제품
WHERE 제조업체 = '한빛제과';

#고객 테이블의 몇명인지
#이럴 때는 NULL 값 때문에 * 를 사용한다.
SELECT COUNT(나이)
FROM 고객;

SELECT COUNT(*)
FROM 고객;

#제조업체는 겹치는 기업이 많음
#UNIQUE 제조업체만 검색
SELECT COUNT(DISTINCT(제조업체))
FROM 제품;

SELECT COUNT(제조업체)
FROM 제품;

```



### GROUP BY 검색, HAVING 검색



```mysql
#GROUP BY
#group by 조건은 HAVING 으로~
#주문테이블에서 주문제품별 수량의 합계 검색

SELECT 주문제품, SUM(수량) AS 총주문수량 
FROM 주문
GROUP BY 주문제품
ORDER BY 총주문수량 DESC;

#제품테이블에서 제조업체별로 제조한 제품의 개수와
#제품중 가장 비싼 단가를 검색

SELECT 제조업체, COUNT(*) AS 제조개수, MAX(단가) AS 최고가
FROM 제품
GROUP BY 제조업체;

#고객 테이블에서 적립금의 평균이 1000원 이상인
#등급에 대해 등급별 고객수와 적립금 평균 검색

SELECT 등급, COUNT(*) AS 고객수, AVG(적립금) AS 적립금평균
FROM 고객
GROUP BY 등급
HAVING AVG(적립금) >= 1000;


#주문테이블에서
#각 주문고객이 주문한 제품의 총주문수량을 주문제품별로 검색

SELECT 주문제품, 주문고객, SUM(수량) AS 총주문수량
FROM 주문
GROUP BY 주문고객, 주문제품;
```





발표나 이런게 다음주에 공지가 있을 예정



ERD 기반으로 일단 준비해놓기



매니저 관점에서 어떤 정보를  뽑고 싶은지, 가치있는 정보를 뽑아내고 있는지 질의문을 작성하기.

