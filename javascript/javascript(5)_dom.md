# 자바스크립트 (5) - dom 객체 사용



```javascript
<p>content1</p>
<p>content2</p>
<p>content3</p>
<p>content4</p>
<script>
var pNode = document.getElementsByTagName('p');
console.log(pNode);
console.log(pNode.length);
console.log(pNode + "")
</script>

```





```javascript
<script>
        function process(){
            var fname = document.frm.fname;
            alert(fname.value);
            return false;
        }
</script>

<form name="frm">
        <label for="fname">이름</label>
        <input type="text" name="fname" id="fname" value="이름..." />
        <input type="text" name="fpass" placeholder="비밀번호를 입력하세요"/>
        <button onclick="return process()" > click</button>
```



함수를 이용해서 태그의 요소에 접근할 수 있다.



```javascript
function process(){
            var fname = document.frm.fname;
            alert(fname.value);
            alert(fname.defaultValue);
            return false;
        }

<form name="frm">
        <label for="fname">이름</label>
        <input type="text" name="fname" id="fname" value="이름..." />
        <input type="text" name="fpass" placeholder="비밀번호를 입력하세요"/>
        <button onclick="return process()" > click</button>
```



이 코드에서 fname 의 value에 접근할 수 있다.

`fname.value` 

이때 defaultvalue 값이 존재하는데, defaultvalue값은 기존에 태그에 설정해놨던 속성인 `value` 의 값에 의해서 결정된다.



이때 주목해야할 점은 태그의 이벤트 속성이다.

이벤트 속성을 태그 안에 설정하는 것은 일반적이지 않다.



```javascript
        window.onload=function(){
            var btn = document.frm.btn;
            btn.onclick = function(){
                alert('submit');
            }

        }
```



따라서 <script> 안에 함수를 적어 이벤트를 담당해야 한다.

window.onload 는 현재 페이지가 메모리 로딩이 될 때를 의미한다. 메모리 로딩이 되면 밑의 함수를 실행해라는 의미가 담겨져 있다.



btn.`<이벤트>` 를 적어서 이벤트를 시행할 수 있다.



### 부모노드 접근



```javascript
    <script>
        window.onload=function(){
            var p2 = document.getElementById('p2');
            p2.parentNode.style.color='blue';
            
        }

    </script>


```



```javascript
    <div id="wrap">
		<p id="p1">content1</p><p id="p2">content2</p><p id="p3">content3</p>
	</div>
```



p2.parentNode는 p2의 부모를 의미한다.  따라서 p2의 부모인 wrap이 모두 파란색으로 바귄다.



```javascript
p2.previousSibling.style.fontSize = '20px';
p2.nextSibling.style.border = '1px solid black';
```



스크립트 안에 previousSibling 적어주면 p2를 기준으로 이전에 있는 요소에 함수를 적용해준다.

또한 p2를 기준으로 다음 요소에 접근하려면 nextSibling 적어주면 된다.



### 자식노드 접근



```javascript
window.onload=function(){
            var wrap = document.getElementById('wrap');
            var divChildNode = wrap.childNodes;
            console.log(divChildNode.length);
            console.log(divChildNode); //텍스트 노드도 포함해서 가져옴

            var divChildren = wrap.children;
            console.log(divChildren.length);
            console.log(divChildren);

            var aNode = document.getElementsByTagName('span')[0]; //0번째 요소를 가져옴
            console.log(aNode);
            aNode.style.backgroundColor = 'red';



        } //엘리먼트 노드들만 가져옴
```



```javascript
<div id="wrap">
		<p>content</p>
		<a href="">세미나 장소</a>
		<span><a href="">정보</a></span>
</div>
```



wrap 기준으로 정할 때 getElemetById를 통해서 가져온다.

wrap변수에 그 정보를 담아둔 이후에 wrap.childNodes 를 통해서 자식노드들을 모두 가져온다.

이때 주목할점은 childNode는 모든 노드들을 가져온다는 것.

엘리먼트 노드와 텍스트 노드를 속성 노드 전부 가져온다.

따라서 위의 body에서 가져오는 것들은

text,  p, text, a, text, span, text 이다.



```javascript
var divChildren = wrap.children;
console.log(divChildren.length);
console.log(divChildren);
```



이 부분은 자식노드의 모든 부분들을 가져오지 않고 엘리먼트노드들만 가져오게끔 하는 코드이다. `children` 함수가 이를 가능하게 해준다. 그렇다면 return 값은 `p` `a` `span` 이  된다.

(노드들은 엘리먼트, 요소, 텍스트)



```javascript
 var aNode = document.getElementsByTagName('span')[0]; //0번째 요소를 가져옴
            console.log(aNode);
            aNode.style.backgroundColor = 'red';
```



자식의 특정한 노드에 접근하기 위해서는 구체적인 코드가 필요.

만일 span 태그의 노드에 접근하려면 위의 코드처럼 작성한다.span 안에 여러가지 태그들이 있다면 `[]` 안에 인덱스를 집어넣어서 끄집어낼 수 있다. 위의 body에서는 하나의 태그뿐이기 때문에 0을 집어넣어서 빼낸다.

빼낸 이후에 style.backgroundColor = 'red' 로 하여 red 색깔을 집어넣는다.







