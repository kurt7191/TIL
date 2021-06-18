# HTML 나름 정리



### 요소 위치

어떤 위치를 기준으로 하는지가 가장 중요한 관건이다.



##### STATIC



STATIC은 전혀 정해져 설정이 되어있지 않은 초기 위치를 의미한다.

따라서 따로 정해둘 필요가 없다.



##### RELATIVE



STATIC위치를 기준으로 사용자가 TOP, BOTTOM, LEFT, RIGHT를 정할 수 있다.



##### ABSOLUTE



부모에 RELATIVE, ABSOLUTE, FIXED가 없다면 가장 위인 BODY로 가서 BODY를 기준으로 위치를 조정함. 만일 부모에 적혀 있다면 부모를 기준으로 위치를 조정함.



<hr>

### 

### 요소 수평 정렬



부모 요소에 overflow : hidden; 적용 !



자식은 float으로 right할지 left할지 설정!



<hr>

### 레이아웃 중앙 정렬



중앙정렬할 요소에 margin :0 auto;



<hr>

### 가시 속성



display : none => 속성을 보이지 않게.

display : block => div속성을 가지게

display : inline => span 속성을 가지게

display : inline-block => div + span 속성을 가지게



<hr>

### 요소:nth-of-type()



요소의 자손들 중에 몇 번째 요소를 선택



이 이외의 구조 선택법



요소:first-child{

}

요소:last-child(){

}

요소:nth-child(n){

} => n번째 요소 선택









