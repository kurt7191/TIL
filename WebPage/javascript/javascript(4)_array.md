

#  자바스크립트(4) - Arraay





```javascript
var cars = [ "Saab", "Volvo", "BMW" ];

for ( var index in cars)
			document.write(cars[index] + "<br/>");
		document.write("<hr/>");

document.write(typeof cars + " " + (cars instanceof Array));
document.write("<hr/>");
```



어느 프로그래밍 언어처럼 배열 가능.

타입을 확인하면 object 반환하면서 Array 를 True 반환한다.



```javascript
var cars2 = new Array("Saab", "Volvo", "BMW");
		for ( var index in cars2)
			document.write(cars[index] + "<br/>");
		document.write("<hr/>");
```



다른 언어들처럼 배열을 만들수도 있지만 다른 방식으로도 배열을 만들 수 있다.

`new Array()` 처럼 객체를 만드는 것처럼 배열을 생성가능하다.



```javascript
var person2 = [];
document.write(person2.length + "<br/>"); //0
person2[0] = "java";
person2[3] = "script";
document.write(person2.length + "<br/>");//4
```



빈 배열 칸을 만들고 배열안에 요소를 집어 넣을 때, 설정한 인덱스에만 값이 들어가고 그 이외에는 값이 들어가지 않는다.





