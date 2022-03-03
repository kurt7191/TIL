# 데이터베이스구조와운용(13) - MYSQL(2)



```mysql
CREATE TABLE 고객(  
        고객아이디 varchar(20) NOT NULL,  
        고객이름 varchar(10) CHARACTER SET utf8,  
        나이 integer,  
        등급 varchar(10) not null,  
        직업 varchar(20),  
        적립금 int default 0,  
        primary key(고객아이디));

CREATE TABLE 제품(  
제품번호 char(3) NOT NULL,  
제품명 varchar(20) CHARACTER SET utf8,  
재고량 integer,  
단가 integer,  
제조업체 varchar(20),  
primary key(제품번호),  
check(재고량 >=0 AND 재고량 <=10000));

CREATE TABLE 주문(  
주문번호 char(3) NOT NULL,  
주문고객 varchar(20),  
주문제품 char(3),  
수량 integer,  
배송지 varchar(30) CHARACTER SET utf8,  
주문일자 DATE,  
primary key(주문번호),  
FOREIGN KEY(주문고객) REFERENCES 고객(고객아이디),  
FOREIGN KEY(주문제품) REFERENCES 제품(제품번호)  
);

CREATE TABLE 배송업체(  
업체번호 char(3) NOT NULL,  
업체명 varchar(20) CHARACTER SET utf8,  
주소 varchar(100),  
전화번호 varchar(20),  
primary key(업체번호)  
);

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

INSERT INTO 주문 VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '01/JAN/2019'); 
INSERT INTO 주문 VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '10/JAN/2019'); 
INSERT INTO 주문 VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '11/JAN/2019'); 
INSERT INTO 주문 VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '01/FEB/2019'); 
INSERT INTO 주문 VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '20/FEB/2019'); 
INSERT INTO 주문 VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '02/MAR/2019'); 
INSERT INTO 주문 VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '15/MAR/2019'); 
INSERT INTO 주문 VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '10/APR/2019'); 
INSERT INTO 주문 VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '11/APR/2019');
INSERT INTO 주문 VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '22/MAY/2019');
```



<HR>

```mysql
SELECT 제품.제품명
FROM 제품, 주문
WHERE 주문.주문고객 = "banana" AND 제품.제품번호 = 주문.주문제품;


--CARROR 고객이 주문한 제품들의 평균 단가

SELECT 주문.주문고객, AVG(제품.단가) AS 평균단가
FROM 주문, 제품
WHERE 주문.주문고객 = "carrot" AND 주문.주문제품 = 제품.제품번호;

--나이가 30세 이상인 고객이 주문한 제품의 주문제품과 주문일자를 검색


SELECT 주문.주문제품, 주문.주문일자
FROM 고객 e, 주문 o
WHERE e.나이 >= 30 AND o.주문고객 = e.고객아이디;


--고명석이라는 고객이 주문한 제품의 제품명을 검색

SELECT 제품.제품명
FROM 주문, 고객, 제품
WHERE 고객.고객이름 = '고명석'
AND 고객.고객아이디 = 주문.주문고객 AND 제품.제품번호 = 주문.주문제품;




```





```python
--매운쫄면을 제조해는 제조업체의 제품들의 평균단가


SELECT 제조업체, AVG(단가) AS 평균단가
FROM 제품
WHERE 제품명 = (
  SELECT 제품명
  FROM 제품
  WHERE 제품명 = "매운쫄면");
  
  
--banana 고객이 주문한 제품의 제품명과 제조업체를 검색

SELECT 제품명, 제조업체
FROM 제품
WHERE 제품번호 IN (select 주문제품 from 주문 where 주문고객 = 'banana');

--한빛제과에서 제조한 모든 제품의 단가보다 비싼 제품의  제품명과 단가와 제조업체를 검색하라

SELECT 제품명, 단가, 제조업체
FROM 제품
WHERE 단가 > ALL (select 단가 from 제품 where 제조업체 = '한빛제과');

--2015년 3월 15일에 제품을 주문한 고객의 이름을 검색

SELECT 고객이름
FROM 고객
WHERE exists (
  select * 
  from 주문
  where 주문일자 = '2019-05-15'
  and
  주문.주문고객 = 고객.고객아이디);
  
SELECT 고객이름
FROM 고객
WHERE not exists (
  select * 
  from 주문
  where 주문일자 = '2019-05-15'
  and
  주문.주문고객 = 고객.고객아이디);
```



```PY
--제품번호가 p03인 제품의 제품명을 통큰파이로 수정

UPDATE 제품
SET 제품명 = '통큰파이'
WHERE 제품번호 = 'P03';

--제품테이블에 있는 모든 제품의 단가를 15%인상해보자

UPDATE 제품
SET 단가 = 단가 * 1.15
WHERE 제조업체 = '한빛제과';

--2019년 5월 15일에 주문한 모든 주문내역을 삭제해보자

DELETE
FROM 주문
WHERE 주문일자 = '2019-05-15';

```

