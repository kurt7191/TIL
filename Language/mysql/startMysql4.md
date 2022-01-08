# MYSQL 시작하기 4



### 오름차순 내림차순 정렬



```mysql
SELECT buyprice
FROM  products
ORDER BY buyprice ASC;

SELECT buyprice
FROM  products
ORDER BY buyprice DESC;

```



```mysql
SELECT buyprice,
ROW_NUMBER() OVER(ORDER BY buyprice) ROWNUMBER,
RANK() OVER(ORDER BY buyprice) RNK,
DENSE_RANK() OVER(ORDER BY buyprice) DENSERANK
FROM products
```



ROW_NUMBER 중복되어도 순위를 매김

DENSE_RANK 와 RANK 는 중복되면 같은 순위를 매김

단, DENSE_RANK는 중복된 순위 다음의 순위를 그대로 이어가는 반면에

RANK는 한 단계 뛰어서 매긴다.



### SUBQUERY



