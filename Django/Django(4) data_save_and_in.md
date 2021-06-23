# Django(4) 데이터 저장과 불러오기



클라이언트로부터 데이터를 받아서 데이터 베이스에 저장하는 과정을 거쳐보자



먼저 메모를 입력받았을 때 뜨는 창이 다르려면 어떻게 해야할까?



```django
rlpatterns = [
    path('admin/', admin.site.urls), #사용자가 admin에 접근했을 때 콤마 오른쪽으로 접근
    path('',include('my_to_do_app.urls')),
    
]
```



본래 myproject 의 본진의 urls를 살펴보면 로컬링크를 받았을 때 가야될 app 링크를 보여준다. 이 화면은 첫 번째 화면으로서 고정이라고 보면 된다. 



따라서 우리가 수정해야할 urls 는 app의 urls이다.



```django
urlpatterns=[
    path('',views.index, name='index'),
    path('createToDo/',views.createToDo, name='createTodo')
]
```



```django
                <form action="./createToDo/" method="POST">{% csrf_token %}
                    <div class="input-group">
                        <input id="todoContent" name="todoContent" type="text" class="form-control" placeholder="메모할 내용을 적어주세요">
                        <span class="input-group-btn">
                            <button class="btn btn-default" type="submit">메모하기!</button>
                        </span>
                    </div>
                </form>
```



클라이언트 input을 확인하기 위해서 mvc의 view 담당인 templates을 확인

클라이언트에서 input한 값이 어디로 가는지 form의 action 을 통해서 확인 가능하다.



form 의 action 을 확인하니 `./createToDO/` 로 되어있다. 

따라서 EVENT  `./createToDO/` 가 발생했을시 어떻게 처리할지 app의 urlpatterns를 위의 코드로 수정한다.



controller 역할인 view로 가서 함수를 처리하니 새로운 함수인 createToDo를 실행한다.



```djan
def createToDo(request):
    return HttpResponse('create ToDo!!')
```



request를 view의 createToDo 가 받을시 HttpResponse를 통해서 나타날 화면을 "create ToDo" 글씨가 적히는 것으로 했다. 이를 통해서 데이터 흐름이 잘 되고 있음을 알 수 있다.



하지만 우리의 목표는 데이터 베이스에 데이터를 저장하고 다시 화면에 데이터를 송출하는 일이다.



```django
from .models import *
```



따라서 view.py 에 앞서 생성한 models를 임포트해준다.

(models 에서는 class로 모델을 정의내렸다. 즉, 테이블을 정의내렸다.)



먼저 사용자가 input에 넣었던 value를 찾아야한다. 

앞서 form 코드를 살펴보면 method가 post임을 알 수 있다.

클라이언트 요청인 request에는 다양한 정보가 담겨져 있는데 이 중에서 특정 input을 꺼내오기 위해선 특정 input의 이름을 이용하여 다음과 같은 코드를 작성한다.



```django
def createToDo(request):
    #return HttpResponse('create ToDo!!')
    user_input_str = request.POST['todoContent']
```



request에서 todoContent 이름을 가지고 있는 정보를 가져온다.

이를 이용하여 데이터 베이스에 저장해야한다.

이때 우리가 만들었던 데이터 베이스 클래스를 참고하자.



```django
class Todo(models.Model):
    content = models.CharField(max_length = 255)
    
```



models.py에서 만든 클래스이다

데이터 테이블은 클래스를 통해서 정의가 가능하다.

클래스의 이름이 테이블의 이름이며

밑의 요소 이름이 칼럼명이다.



따라서 이 클래스를 이용해서 데이터를 저장 가능하다.



```django
def createToDo(request):
    #return HttpResponse('create ToDo!!')
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    return HttpResponse('create Todo=' + user_input_str)
```



앞서 request.POST로 받아온 정보를 데이터 테이블 클래스 변수로 집어넣는다.

그러면 테이블을 정의내린대로 데이터가 저장이된다.

중요한점은 `new_todo.save()` 를 해줘야 한다는 점이다.

이를 다시 화면에 보여주려면 `return HttpResponse('create Todo=' + user_input_str)` 를 하면 된다.



이를 통해서 데이터 베이스에 저장한 정보를 보여줄 수 있음을 알 수 있다.



하지만 우리의 목표는 데이터 베이스에 저장된 데이터를 다시 화면에 띄우는 것이다.

이때 사용하는 return 함수가 HtttpResponseRedirect 이다.



```django
urlpatterns=[
    path('',views.index, name='index'),
    path('createToDo/',views.createToDo, name='createTodo')
]
```



url을 쉽게 매핑하기 위해서 name을 지정해준다.



```django
from django.urls import reverse
```



reverse 함수를 이용하기 위해서는 위와 같은 import 가 필요하다.



그리고 저장한 이후에 다시 메인 페이지로 넘어오기 위해서는 앞서 name = 'index'로 저장했기 때문에 다음과 같이 작성한다.



```django
def createToDo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()
    # return HttpResponse('create Todo=' + user_input_str)
    return HttpResponseRedirect(reverse('index'))
```



사용자가 메모를 하고 입력을 누르면 화면상에 바뀐건 없지만 실제로 내부에서는



사용자 -> 데이터 베이스 -> 다시 화면 



으로 돌아간 것이다.



따라서 화면에 그 정보를 보여주고 싶다면 mvc 중에 view 부분을 수정해야 한다. 즉, templates의 index를 수정해야한다. 그리고 index 함수도 수정해야 한다.



먼저 index 함수에서 데이터 베이스에 있는 데이터들을 모두 불러와서 어떤 변수에 저장해야 한다. 따라서 다음과 같이 수정해야한다.



```django
def index(request):
    todos = Todo.objects.all()
    content = {'todos' : todos}
    return render(request, 'my_to_do_app/index.html',content) 
```



return 할 때도 데이터 베이스 불러온 객체를 리턴 해줘야한다.



```django
 <div class="toDoDiv">
                <ul class="list-group">
                    {% for todo in todos %}
                    <form action="" method="GET">
                        <div class="input-group" name='todo1'>
                            <li class="list-group-item">{{todo.content }}</li>
                            <input type="hidden" id="todoNum" name="todoNum" value="{{todo.id}}"></input>
                            <span class="input-group-addon">
                                <button type="submit" class="custom-btn btn btn-danger">완료</button>
                            </span>
                        </div>
                    </form>
                    {% endfor %}
                </ul>
            </div>
        </div>
```



`{% 내용 %}`  을 이용해서 django 에서 파이썬 함수를 사용할 수 있다.

return 으로 불러온 데이터 베이스의 정보를 for문으로 모두 꺼낸다.

todo 안의 칼럼명을 적어주면 그 데이터가 나온다 => `todo.<칼럼명>` 

그리고 value에는 자동으로 생성되었던 데이터의 id를 적어준다. => `todo.<데이터id>` 



그러면 사용자가 입력했던 데이터를 데이터 베이스에 저장하고 다시 메인 화면으로 넘어와서

데이터 베이스의 정보를 화면에 띄우게 된다.



```django
def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
```



또한 입력받은 데이터를 지울 수도 있다.

controller에 함수를 설정했다면 mvc의 view부분과 연동해야 한다.

urls를 하나 더 생성해주고 mvc의 view부분을 설정해준다.



```django
 <form action="./doneTodo/" method="GET">
                        <div class="input-group" name='todo1'>
                            .
                            .
                            .
```



action 부분을 입력해주고



```django
    path('doneTodo/',views.deleteTodo, name = 'doneTodo')
```



path를 새로 입력해준다.

그리고 제일 위의 코드처럼 deleteTodo 함수를 입력해준다.







