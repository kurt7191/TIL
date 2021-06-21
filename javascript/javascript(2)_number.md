## 자바스크립트(2) - Number



```javascript
var data = 100;
var str = data.toString();
```



숫자형 자료형을 문자형 자료형으로 바꾸는 방법 중 하나는 `toString()` 을 사용하는 것. 



```javascript
var obj = new Number(100);

document.write(data + ',' + str + ',' + obj + "<br/>");
document.write(typeof data + ',' + typeof str + ',' + typeof obj + "<br/>");
```



obj 객체까지 만들고 반환값을 확인하면 100, 100, 100 으로 보인다.

화면상으로는 똑같이 보이기 때문에 자료형을 확인하려면 `typeof`를 확인해야만 한다.

확인하면 data는 `number` str은 `String` obj 는 `object` 로 보인다.

  

```javascript
var res = data / "korea";
var res2 = data / "10";
```



숫자와 String은 당연히 연산이 안된다. 이걸 설명하고 있네...



```javascript
var k = 200;
document.write(typeof k.toString() + "<br/>");
document.write(typeof (200).toString() + "<br/>");
document.write(typeof (true).toString()+"<br/>");
```



k는 본래 숫자형이다. `toString` 함수를 이용하여 `String` 형으로 바꿀 수 있다. 

변수를 통해서 문자형으로 바꿀 수 있는 게 아니라 괄호를 사용해서도 할 수 있다.

`boolean` 형도 문자형으로 바꿀 수 있다.



# Global 객체에서 제공하는 number 타입 변환 메소드





- Number()
- parseInt()
- parseFloat()



1)Number()

```javascript
var data = true;
document.write(Number(data) + " " + typeof Number(data) + "<br/>");
var data = false;
document.write(Number(data) + " " + typeof Number(data) + "<br/>");
```



데이터의 자료형이 `boolean` 형이라면 `Number(<데이터>)` 를 사용하면 True이면 1을 false이면 0을 반환한다.

  

2)parseInt, parseFloat

```javascript
data = true;
document.write(typeof parseInt(data) + "<br/>")
document.write(typeof parseFloat(data) + "<br/>")
```



`parseInt`  나 `parseFloat`  같은 경우에는 `boolean` 에 대해서 숫자로 변환하지 못한다.



```javascript
data = "10"
document.write(typeof parseInt(data) + "<br/>")
```



하지만 문자형 같은 경우에는 `parseInt` 나 `parseFloat` 을 이용해서 변환가능하다.



# Globa eval() 메소드



숫자형으로 이루어지지 않은 연산을 숫자형 연산을 가능하게 해주는 함수는 바로 `eval()` 함수이다.



```javascript
var data = eval("3+2");
data = eval("3" + "2");
data = eval("3");
data = eval("3") + eval("2");
```



위의 코드처럼 모두 연산 가능하다.



```java
var arr =  '[1,2,3,4,5]';
data = eval(arr)
    document.write(typeof data +" " + data+" " +
                  (data instanceof Array) + <br/>);
```



eval함수를 통해서 문자형으로 이루어져 있는 배열을 진짜 `Array` 바꿀 수 있다.



```javascript
var obj = '{one:"java",two:"jsp"}';
data = eval("(" + obj + ")");

```



딕셔너리 형태의 문자형을 eval을 통해서 딕셔너리로 바꿀 수 있다. 

!단, eval 요소에 양쪽으로 `(` 와 `)` 를 넣어줘야 한다.

 