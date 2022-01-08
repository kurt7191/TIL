# 자바 스크립트(1) - object



```javascript
var data = 10;
var obj = new Number(data); 
```



자바스크립트는 객체를 생성할 수 있는데 그 형식은 위의 코드와 같이 new와 함께 사용한다.



```javascript
document.write(typeof data + "<br/>");
document.write(typeof obj + "<br/>");

```



typeof를 통해서 데이터의 자료형을 확인할 수 있다. data 같은 경우에는 10으로 설정했기 때문에 number를 반환한다.. 하지만 Number 클래스를 이용해서 10을 넣었을경우 typeof는 object를 반환한다.



```javascript
document.write((obj.toString() instanceof String)+"<br/>")
```



객체를 toString으로 했을 시 String 형이 됐는지 `instanceof` 를 통해서 확인해보면 False를 반환함을 확인할 수 있다.



```javascript
var str1 = new String(data);
var str2 = new String(obj);
```



숫자형 객체를 만들 때는 `new Number()` 를 사용했지만, 문자형 객체를 만들 때는 `new String()` 로 만들 수 있다.



```javascript
document.write(typeof str1 + "<br/>");
document.write(typeof str2 + "<br/>");

```



문자형 객체를 만든 `str1` 과 `str2` 의 자료형을 확인해보면 위의Number 객체와 같이 `object` 를 반환한다.



```javascript
document.write((str1 instanceof String) + "<br/>") 
document.write((str2 instanceof String) + "<br/>") 
```



문자형 객체 같은 경에는 본래 `String` 을 가지고 있으므로 True를 반환한다.



```javascript
data = 10
var obj = new Number(data);
var str1 = new String(data);

document.write(typeof obj) // object
document.write(typeof obj.toString()) // object
document.write(obj instanceof String) // False

document.wrtie(typeof str1) //object
document.write(str1 instanceof String) //True


```



정리하자면 위의 코드와 같이 숫자형 객체와 문자형 객체를 만들 수 있다.

또한 자료형을 확인하면 object로 나오며, 문자형 객체인지 숫자형 객체인지에 따라서 instanceof의 자료형이 String인지 Number인지 확인할 수 있다.





```javascript
document.write(typeof data + "<br/>");
document.write(typeof obj + "<br/>");

```