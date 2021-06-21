# 자바스크립트 응용



```javascript
window.onload = function(){
    var list_zone = document.getElementById("inner_list");

	var ul_li = list_zone.children;
          for (var i = 0; i<ul_li.length;i++){
               ul_li[i].children[0].onclick=function(){
               var ph = document.getElementById('photo').children[0];
                        ph.src = this.href;

                        //<a>태그를 클릭했을 때 링크가 되지 않도록 한다. 
                        return false;
                    }
                }
```



```javascript
<h1>동해안 갤러리</h1>
		<p id="photo">
			<img src="images/pic_1.jpg" width="320" alt="" />
		</p>
```



```javascript
<ul id="inner_list">
				<li><a href="images/pic_1.jpg"> <img
						src="images/pic_t1.jpg" alt="사진1" /></a></li>
				<li><a href="images/pic_2.jpg"> <img
						src="images/pic_t2.jpg" alt="사진2" /></a></li>
				<li><a href="images/pic_3.jpg"> <img
						src="images/pic_t3.jpg" alt="사진3" /></a></li>
				<li><a href="images/pic_4.jpg"> <img
						src="images/pic_t4.jpg" alt="사진4" /></a></li>
				<li><a href="images/pic_5.jpg"> <img
						src="images/pic_t5.jpg" alt="사진5" /></a></li>
				<li><a href="images/pic_6.jpg"> <img
						src="images/pic_t6.jpg" alt="사진6" /></a></li>
				<li><a href="images/pic_7.jpg"> <img
						src="images/pic_t7.jpg" alt="사진7" /></a></li>
				<li><a href="images/pic_8.jpg"> <img
						src="images/pic_t8.jpg" alt="사진8" /></a></li>
			</ul>
```



list에 접근 (getElementById를 통해서).

children을 통해서 자손 노드들에 접근. 이때 모든 노드들을 가지고 오는 게 아니라 요소 노드에 접근. 그때, 맨 첫번째 요소인 <a>를 선택하고 싶기 때문에 list_zone.children[0] 을 선택.

list_zone.children[0] 을 클릭했을 때 photo의 자손인 img의 src를 조작한다.

ph 변수에 document.getElementById('photo') .children[0] 을 담고.

ph.src 로 ph의 src에 접근 후에 `this.href` 를 넣어준다. 이때 `this`는 현재 이벤트를 의미한다.



마지막으로 return false 하는 이유는 링크를 타고 새로운 페이지로 가는 것을 막기 위해서이다.



```javascript
var m_num = 0 ;
                var b_btn = document.getElementById('next_btn');
                b_btn.onclick = function(){
                    
                    if(m_num >= ul_li.length - 3)
                        return false;

                    m_num++;
                    list_zone.style.marginLeft = marginLeft = -100 * m_num + 'px';

                    return false; //링크차단
                }
            }
```



페이지를 누를때마다 사진이 넘어가는 것을 구현하기 위한 스크립트

역시 버튼을 document.getElementById를 통해서 접근한다.

페이지를 넘길때마다 m_num이 증가하게 되고 만일 5번 넘기는 게 끝나게 되면 더이상 넘어가지 못하게 return false를 해주고



marginLeft 값에 음수를 줘서 페이지가 넘어가게 만든다.





