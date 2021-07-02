# 공공 데이터 포털API 활용

> 기상청_관광코스별 관광지 상세 날씨 조회서비스 데이터 활용



공공데이터의 api 를 이용하기 위해서는 url 과 key가 필요하다.



미리보기 안에 들어가면 주소가 보일텐데 그 주소를 이용해서 url 과 key 를 작성한다.



```python
#미리보기 url 과 key가 필요

url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnWthrIdx'
key = 'hTEB1sAjGztkULg3VIm8OcBn2W7q5TM7c8owlS0SdpbphQTKifBdVAcmqTgv8Miol%2B2FkUDNriXGyNYfCnD4Jg%3D%3D'


url += '?serviceKey=' + key
url += '&pageNo=1&numOfRows=10&dataType=XML&CURRENT_DATE=2019122010&HOUR=24&COURSE_ID=1'
    
    
response = requests.get(url)
```





주소란을 보면 url 뒤에 `?serviceKey` 라고 보이는 게 있다.

이 부분 뒤는 키 값이 들어가 있다.

또한 페이지에 대한 정보, xml 같은 정보들이 더 붙어져 있는데 위와 같이 url 하나에 합쳐준다.



```python
url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getTourStnVilageFcst'
#encoding -> decoding   (디코딩이 utf-8로 바꿔준거)
#key = 'B4QVX9oRn6HfmIKPAZyWMkU2EIAIzUbTEcQBY2awLLopq4s8oBjKIhAG8GdkYaLUbTk0H6vrlnHkoM6IAPn5aQ%3D%3D'
#key = requests.utils.unquote(key, encoding='utf-8')

#request의 파라미터 값을 넣어주려면 key 값을 디코딩 값을 집어넣어야한다.

key = 'B4QVX9oRn6HfmIKPAZyWMkU2EIAIzUbTEcQBY2awLLopq4s8oBjKIhAG8GdkYaLUbTk0H6vrlnHkoM6IAPn5aQ=='


#링크의 ? 이후를 딕셔너리로 만들어주는 과정을 가진다. (매개변수로 넣기 위해)

queryParams ={'serviceKey':  key,
               'pageNo' :1,
               'numOfRows' : 10,
               'dataType': 'XML',
               'CURRENT_DATE' : 2019122010,
               'HOUR': 24,
               'COURSE_ID' :1}

    
response = requests.get(url, params=queryParams)  
print(response.status_code)
print(response.text)

```



key 값은 디코딩과 인코딩 값이 있다.

만일 인코딩을 했을시 한글이 깨질 수 있다.



앞서서 페이지의 정보를 읽어올 때 `request` 함수를 사용했는데,

request 함수는 매개변수가 하나 더 존재한다.

이 param에 key 정보와 페이지 정보를 딕셔너리 형태로 담아서 request에서 한번에 처리하는 방법ㅇ이 있다.

즉, url 을 `serviceKey` 앞까지만 설정하고 매개변수로 key 정보와 그 이외의 정보를 넣어준다.

이 경우는 디코딩 방법이라고 할 수 있다.



response는 정보를 잘 받아왔을 것이다.



```python
#ensure_ascii =False : 파일이 저장될때 한글이 유니코드 형태로 저장되지 않는다.

if response.status_code == 200:
    xd = xmltodict.parse(response.text) #xml 형식 데이터를 dict형식으로 바꾸겠다.
    xdj = json.dumps(xd,ensure_ascii=False) #dict 을 json 형태로 바꾸기
    xdjd = json.loads(xdj) #json 형식의 데이터를 dict 형식으로 변환
    
    
    
```



만일 정보를 잘 받아왔을 경우에는 200 이 뜰 것이고 아니면 400대 오류가 뜰 것이다.

따라서 잘 받아왔을 경우 페이지 정보를 dict -> json -> dict 으로 변환하여 가져온다.



xml 을 딕셔너리로 딕셔너리를 제이손으로 제이손을 다시 딕셔너리로 바꾼 경우다.





```python
#item 접근
w_data = xdjd['response']['body']['items']['item']
```



특정 태그에 접근하는 방법.



```python

#필요한 item 출력
for i in range(len(w_data)):
    print('관광지명 : ' + w_data[i]['spotAreaNamea'])
    print('시간 : ' + w_data[i]['tm'])
    print('기온 : ' + w_data[i]['th3'])
    print('강수확률 : ' + w_data[i]['pop'])
    print('기상상태 : ' + w_data[i]['sky'])
    print('-----------------------------------------')
    
    
totalCount = xdjd['response']['body']['totalCount']
print('totalCount : ', totalCount)
```



w_data에는 특정 데이터가 담겨 있는데 for 문을 통해서 모든 정보를 꺼내준다.

dict 형태로 되어 있기 때문에 i번째의 key이름을 적어줘서 콘솔창에 띄운다.



