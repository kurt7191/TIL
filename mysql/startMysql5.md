# 데이터 추가,업데이터



```mysql

INSERT INTO dept(num,dname,dloc)
VALUES(10,'sales','seoul');

```



칼럼명을 다 적던가.



```mysql
INSERT INTO dept
VALUES(20,'human','inchon');
```



모든 칼럼을 추가하면 칼럼명을 안적어도 된다.



```mysql
INSERT INTO dept
VALUES(30,NULL,NULL);
```



NULL 값을 넣을 수 있다.



```mysql
UPDATE dept
SET dname = 'management', dloc  = 'gangneung'
WHERE num = 30;
```



where 로 업데이트할 행을 지정해야한다.

(num primary key로 지정하라고 함)



```mysql
DELETE FROM dept
WHERE num=40;
```



num=40인 행 모두 삭제



