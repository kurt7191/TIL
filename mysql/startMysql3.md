# MYSQL JOIN



### LEFT JOIN, INNER JOIN 비교



```mysql
SELECT * FROM orders;
SELECT * FROM customers;
SELECT * FROM orders LEFT JOIN customers
ON orders.customerNumber = customers.customerNumber;

```



LEFT JOIN  코드를 기준을 왼쪽에 있는 테이블에 오른쪽 테이블(CUSTOMERS 테이블)을 JOIN 하는 것.

이때 공유하는 게 같은 칼럼만 JOIN 한다. 

`ON` 뒤에 같이 공유하고 있는 칼럼을 적어주면 된다.



즉 LEFT 쪽에 있는 테이블에 있는 건 모두 가져온다. 그리고 추가로 오른쪽에 있는 데이터의 정보를 가져오는데, 다 가져오는 게 아니라 특정 컬럼을 선정하고 그 칼럼과 공통된 데이터를 가지고 있는 행들만 오른쪽 테이블에서 가져온다.



```mysql
SELECT o.orderNumber,o.customerNumber ,c.customerNumber
FROM orders o INNER JOIN customers c
ON o.customerNumber = c.customerNumber;
```



LEFT 는 왼쪽 테이블과 오른쪽 테이블 정보 중에서 LEFT를 다 가져왔다.

하지만 INNER는 왼쪽이든 오른쪽이든 특정 칼럼이 동일하게 데이터를 공유하고 있는 행들만 쿼리로 불러온다.





