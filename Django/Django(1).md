# Django(1) MVC 원리 살펴보기





MVC 원리대로 진행



**MODEL (models.py) , Controller (Views.py),  View(templates)** 



<hr>



따로 환경 생성

프로젝트 파일 생성

앱 생성 후 프로젝트 setting에 앱 목록 추가

프로젝트 파일 urlspattern 수정 -> app urls.py 로 보내기

앱 폴더에 urls.py 생성

그곳에 urlpatterns 입력 -> 보여줄 뷰로 가야하기 때문에 view.index로 보냄

함수 생성하고 매개변수로 request 받기

서버 실행하기



(manage.py 로 app도 생성하고 서버도 실행하기)



# Application 구성하기



프로젝트는 여러 개의 app으로 구성이 된다. 프로젝트마다 app 개수나 구성은 다르다.

프로젝트를 만들면 그 안에 manage.py 파일이 있는데 이 파일을 이용해서 앱을 만든다.

(경로는 manage.py 가 있는 곳)



```python
python manage.py startapp my_to_do_app
```



manage.py 를 이용해서 app을 만든 걸 확인할 수 있다.



```django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_to_do_app'
]
```



app을 하나 생성했으면 project 폴더에서 setting 을 만져줘야 한다. 

setting 파일에 들어가면 `INSTALLED_APPS` 에 새로 추가한 APP명을 추가해야 한다.

따라서 my_to_do_app 을 추가했다.



# URL 설정하기



프로젝트를 실행했다면 URL 을 연결, 서버를 연결해야 한다.

서버를 연결하는 것  또한 manage.py를 이용해서 가능하다.



```django
python manage.py runserver
```



runserver 를 켰다면 url 주소를 입력해야 한다.



```django
urlpatterns = [
    path('admin/', admin.site.urls), #사용자가 admin에 접근했을 때 콤마 오른쪽으로 접근
    path('',include('my_to_do_app.urls')),
]

```



저urlpatterns를 만져줘야 하는데, path함수의 매개변수의 의미를 살펴보면,

admin에 접속하게 되면 콤마 뒤의 변수로 이동함을 의미한다.

우리는 admin 자리에 url 주소를 입력할건데 

우리는 보통 local 로 작업을 하기 때문에 `''` 로 실행한다.

이때 url에 접속하면 어디로 이동할지 콤마 뒤의 변수를 설정해야만 하는데, 

앞서 만든 app의 urls.로 이동하게 설정한다



```django
from django.urls import path, include
```



include를 임포트 해주고 `include('my_to_do_app.urls') ` 로 설정을 해준다.

위처럼 코딩을 하면 우리가 설정한 local url 에 접속하면 my_to_do_app 에 접속해서 urls로 이동한다.



```django
from django.urls import path
from. import views

urlpatterns=[
    path('',views.index)
]
```



하지만 my_to_do_app 에 들어가면 urls.py 가 없기 때문에 직접 파일을 만들어준다.

그리고 코드를 직접 적어준다.

my_to_do_app 에서 view로 화면을 보낼거기 때문에 view를 임포트 해준다.

urlpatterns가 필요하기 때문에 path 또한 임포트 해준다.

urlpatterns도 url에 들어가게 되면 view로 보내주고 싶기 때문에 `views.index` 로 적는다.



```django
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'my_to_do_app/index.html') ##html 을 view에서 보여줄때 사용하는 함수 render
    #request는 user나 session 정보를 담고 있으며, view로 화면을 보여줄 때 정보가 동시에 이동된다.

# Create your views here.

```



따라서 view를 최종적으로 설정해준다.

우리가 앞서 보낸 값들을 request로 받는다.

request는 user에 대한 정보나 session 에 대한 정보가 담겨져 있다.

HttpResponse는 view에 보여질 것들을 만드는 것을 의미한다.

하지만 webpage는 글씨만 적히는 게 아니라, 다양한 html 태그들이 들어간다.



따라서 html 템플렛을 다운받아서 app에 넣으려고 한다.



!!이때 필수적으로 html 파일의 경로를 설정해야할 게 있다.

장고는 templates 폴더에서 app의 이름과 같은 폴더에 들어가 html 파일을 읽는다.

따라서 template폴더를 만들고 그 폴더 안에 app 이름과 같은 폴더를 만든다.

그리고 html 파일을 업로드한다.

그리고 return 값을 파일명은 `index.html` 

` return render(request, 'my_to_do_app/index.html')` 작성한다.

















