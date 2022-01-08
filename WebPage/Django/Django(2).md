# Django(2) Model, 데이터 베이스 연동



app의 models.py에서 데이터를 정의내릴 수 있다.

이때 클래스를 사용하여 데이터 테이블을 만든다.



```django
from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length = 255)
    
```



하나의 모델은 하나의 클래스로 표현 (하나의 테이블을 하나의 클래스로 표현)

장고는 테이블을 model로 표현, model을 정의내릴 때는 class로 정의.

즉, 데이터 테이블(model)을 class로 표현



따라서 Todo라는 클래스 이름이 모델의 이름과 마찬가지이다.

그리고 클래스 내부에 데이터의 이름과 형태를 정할 수 있다.

데이터의 이름은 content 이고 형태는 charField 255이다.



model 명 : Todo

데이터명 : content

데이터형태 : CharField, 255



```python
python manage.py makemigrations
```



app에서 models에서 모델명과 데이터명 그리고 데이터 타입을 결정지었다면, 

즉 테이블을 결정지었다면 이를 바탕으로 데이터 베이스에도 데이터를 생성해야만 한다.

우리가 작성한 models를 초안으로 하기 위해서 위와 같이 작성한다.

그러면 app폴더에 migrations 폴더 하단에 initial.py가 생성된다. 즉, 초안이 생성된다.



```python
python manage.py migrate
```



위의 코드를 작성하면 실제 데이터 베이스가 완성이 된다.



```python
python manage.py dbshell
```



데이터베이스가 완성이 되었는지 안되었는지 확인하기 위해서 위와같은 코드를 작성한다.

만일 sqlite 로 마지막 줄에 되어 있다면 데이터 테이블이 완성이 된것이다.

(mysql 이 아니라 sqlite를 기본으로 사용함)



그리고 `.tables` 를 입력하면 존재하는 테이블들을 내놓는다.

이때 우리가 만든 테이블은 `<app이름>`  + `_`  + `<함수이름>`  으로 나타난다.



```python
pragma table_info(my_to_do_app_todo);
```



테이블이 무엇이 있는지 확인했으면 테이블에 대한 정보를 구체적으로 얻고 싶을 수 있다.

위의 코드를 작성하여 테이블의 구조를 살펴볼 수 있다.



**순서|이름|형태|not null 여부|pk 여부** 

1|content|varchar(255)|1|0



위와같은 형태로 정보가 나타난다.

null 부분을 살펴보면 값이 1이면 null 허용이 안되고 0이면 허용을 의미한다.

primary key 도 마찬가지이다. 1이면 해당 값이 pk라는 것. 0이면 아니라는 것이다.



