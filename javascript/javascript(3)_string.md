# 자바스크립트(3)-String



```javascript
var data = "It\s alright";
document.write(data + "<br/>");
document.write(data.length + "<br/>");
```



위의 data가 문자형이라고 할 수 있다. 문자형의 길이를 확인하는 함수는 `length()` 함수이다.



1)substring, sudstr, slice

```javascript
var str = "Apple, Banana, Kiwi";

document.write(str.slice(7,13) + "<br/>");
document.write(str.slice(-12,-6) + "<br/>");

document.write(str.substring(7,13) + "<br/>");
//substring 같은 경우에는 시작지점부터 찾는 길이를 설정
document.write(str.substr(7,6) + "<br/>");
document.write(str.substr(-12,6) + "<br/>");


```



`slice` 함수와 `substr` 함수 그리고 `substring` 함수는 동일한 역할을 하는 함수.

문자형의 특정 부분을 잘라올 수 있다.

단, slice와 substr 함수는 시작지점과 끝지점을 설정하여 뽑아오는 거라면,

substring 함수는 시작지점부터 잘라오고 싶은 개수를 지정하여 가져온다.



2)replace



```javascript
str = "Please visit Microsoft! and microsoft Microsoft";
document.write(str.replace("Microsoft","W3Schools") + "<br/>");
document.write(str.replace(/Microsoft/gi,"W3Schools")+"<br/>");
```



`replace` 함수를 이용하여 인덱스가 가장 앞에 있는 것부터 바꿀 단어를 바꾼다.



이때 `/Microsoft/gi` 의 의미가 중요하다. `g` 는 모든 문자열을 의미한다. 즉 우선순위에 의한 하나의 문자열만 바꾸는 것이 아니라 문자열안에 Microsoft라고 포함된 모든 것들을 replace한다. 또한 `i`는 대소문자 구분이 없음을 의미한다. Microsoft는 대문자로 구분되어 있지만 소문자 microsoft 또한 replace됨을 의미한다. 정리하면 대소문자 구분 없이 Microsoft에 포함되는 모든 문자열을 replace함을 의미.



3)toUpperCase() 와 toLowerCase()



```javascript
var text1 = "Hello !!"
document.write(text1.toUpperCase() + "<br/>");
document.write(text1.toLowerCase() + "<br/>");
```



text1 으로 되어있는 문자형을 대문자 소문자로 바꿀 수 있다.



4)concat()

```javascript
var text2 = "javascript";
document.write(text1.concat(text2) + "<br/>");
document.write(text1.concat(" ",text2) + "<br/>");
```



`concat` 함수는 문자형을 결합하는 함수이다. 1 + 1의 문자열을 합칠수도 있고 1 + 여러개의 문자열을 합칠수도 있다.



5) split()



```javascript
var txt = "a,b,c,d,e"
arr = txt.split(",")
document.write(typeof arr + " " + (arr instanceof Array) + "<br/>")

for (var index in arr)
    document.write(arr[index] + "<br/>");
```



`split` 을 하게 되면 배열로 반환하게 된다. `instanceof` 함수를 통해서 Array인지 파악 가능하다.



6)match, search



```javascript
var str3 = "The rain in SPAIN stays mainly in the plain";
var res = str3.match(/ain/g);

```



match는 일치하는 값들을 모두 반환. 없는 값이면 null 반환.



```javascript
res = str3.search("ain");
```



처음에 요소 문자열과 일치하는 인덱스를 반환한다.

일치하는 문자열이 없다면 -1을 리턴한다.





