# Turtle Game

> 거북이 게임을 만들어 보자
>
> 거북이 게임에 쓰이는 명령어들



```python
import turtle as t
import random

t.speed(0)
t.shape('turtle')

t.forward(30)

print(t.pos()) #현재 위치 알려주기

```



`shape()` 은 움직이는 이미지의 모습.

`speed()` 는 거북이가 움직이는 속도.

`forward()` 함수는 거북이가 나아가는 distance.

`pos()` 는 현재 이미지의 위치.



```python
import turtle as t
import random

t.speed(0)
t.shape('turtle')

t.forward(30)
t.right(45)
t.forward(30)


print(t.pos()) #현재 위치 알려주기

```



방금과 달리 `right()` 이 추가됨.  오른쪽으로 몇도 각을 돌지 결정.

`pos()` 위치가 달라졌을 것임.



```python
import turtle as t
import random

t.speed(0)
t.shape('turtle')

t.goto(-30,30) #x는 -30 y는 +30으로 이동

```



이미지의 x축의 위치와 y축의 위치를 지정해주는 `goto()` 함수.



```python
import turtle as t
import random

t.speed(0)
t.shape('turtle')

t.setx(-60)

```



`setx()` 는 x축만 이동.



```python
import turtle as t
import random

t.speed(0)
t.shape('turtle')

t.goto(-100, -43)

print(t.distance(0,0))

```



`t.distance()` () 안의 좌표와 현재 이미지 거리상 간격을 리턴함. 



```python
t.setheading(0)
```



거북이가 바라보는 방향.

0도면 오른쪽 90도면 수직 위 180도면 왼쪽.



```python
t.goto(-40,-87)
print(t.towards(0,0))
```



-40, -87도로 거북이가 이동하면 (0,0)을 가기 위해서 몇 도를 꺾어야 되는지 리턴.

만일 고양이가 쥐를 쫒아가는 게임을 만들면 고양이가 쥐를 향한 각도를 알려줌.



```python
import turtle as t
import random


def OnUp():
    t.sety(t.ycor() + 10)


t.speed(1)
t.shape('turtle')
t.onkeypress(OnUp,"Up")
t.listen()

```



`onkeypress()`  어떤 키를 누르면 어떤 함수가 작용되게 할지 정하는 함수.

`t.ycor()`  은 현재 이미지의 y좌표

`t.sety()`  는 `t.setx()`  와 마찬가지로 x좌표 y좌표 설정하는 것.

`t.listen()`  이 거묵이 이미지를 받아주는 함수, 쓰지 않으면 거북이가 움직이지 않음.



*위 코드는 윗화살표 누르면 거북이가 위로 이동하는 모습을 보일 것임*



`home()` 거북이의 위치와 방향을 처음 상태로 되돌림.

`ontimer(함수, 시간)` -> 지정한 시간이 지난 뒤 지정한 함수를 실행.

`onscreenclick(함수)` -> 마우스 이벤트, 마우스 버튼을 눌렀을 때 지정한 함수를 실행.

