# Selenium 크롤링(2)



자바스크립트 데이터 수집

coffeebean 홈페이지를 통한 실습



```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

from selenium import webdriver
import time
```



필요한 패키지와 모듈들을 모두 임포트 해준다.



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.coffeebeankorea.com/store/store.asp'
```



드라이브를 구현시켜준다.

단, 본래는 url 을 설정하고 바로 `driver.get(url)` 을 해서 웹페이지를 띄웠다면, 

이번에는 여러 번 띄울 예정이기 때문에 for 문 안에 `driver.get(url)` 을 넣어준다.



```python
result = []
```



크롤링한 결과들을 넣어줄 리스트를 만들어준다.



```python
for i in range(1, 5):
    driver.get(url)
    time.sleep(1) #웹 페이지 연결한 동안 1초 대기
    try:
        driver.execute_script('storePop2(%d)' % i)
        time.sleep(1)

        source = driver.page_source
        soupCB = BeautifulSoup(source,'lxml')

        #매점명
        store_name_h2 = soupCB.select_one('div.store_txt > h2').text
        
#         print(store_name_h2)

        #매점 주소
        store_info_add = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(3)>td')
        store_address = store_info_add.text
#         print(store_address)

        #매점 전화번호

        store_info_phone = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(4)>td')
        store_phone = store_info_phone.text
#         print(store_phone)
        
        #result에 매점정보 저장
        result.append([store_name_h2] + [store_address] + [store_phone])
    except:
        continue
        
    
```



먼저 최종적인 코딩이다.

하나하나 살펴보면,



```python
for i in range(1, 5):
    driver.get(url)
    time.sleep(1) #웹 페이지 연결한 동안 1초 대기
```



for문을 사용해서 몇 개의 매장 정보를 찾아볼지 range를 통해서 설정한다.

매장마다 새로운 창을 띄워야 하기 때문에 이 안에 driver.get 을 넣어준다.



```python
 try:
        driver.execute_script('storePop2(%d)' % i)
        time.sleep(1)

        source = driver.page_source
        soupCB = BeautifulSoup(source,'lxml')
```



홈페이지에 들어가서 <자세히보기> 를 눌러서 매장을 확인하면 팝업창이 뜬다.

이를 자바 스크립트로 구현해놨는데, 그 이름을 개발자 모드(f12) 로 살펴보면 `storePop2` 이다.

그리고 이러한 정보를 받아오는 selenium 함수는 `execute_script` 이다.

각 팝업마다 고유 번호를 가지고 있는데 각각을 for문의 i를 넣어줘서 창을 띄워준다.



그리고 selenium 에서는 page_source를 하면 페이지 정보가 저장이 된다.

(앞선 BeautifulSoup 에서는 request를 이용한다.)

저장된 자료형은 문자형인데 본래 `res.txt` 를 사용해서 매개변수 값으로 넣어줬는데, 이번에는 source 변수 그대로 넣어준다.

이렇게 되면 팝업창의 정보가 soupCB 에 담겨있게 된다.



또 개발자 모드로 HTML 을 확인해보면 DIV의 특정 클래스 안에 정보들이 담겨 있음을 확인할 수 있다.

이 경로를 잘 파악하여 다음과 같이 코드를 작성한다.



```python
        #매점명
        store_name_h2 = soupCB.select_one('div.store_txt > h2').text
        
#         print(store_name_h2)

        #매점 주소
        store_info_add = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(3)>td')
        store_address = store_info_add.text
#         print(store_address)

        #매점 전화번호

        store_info_phone = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(4)>td')
        store_phone = store_info_phone.text
```



매점명은 div 자식의 h2 에 적혀있기 때문에 위와 같이 BeautifulSoup 의 select 함수를 이용해서 정보를 변수에 담아준다.



매점 주소명은 div 밑의 table 태그에 담겨져 있다. 테이블의 tr 안의 td의 두 번째에 담겨있기 때문에 

`nth-of-type(<몇 번째>)` 로 특정 순서의 td를 꺼내서 변수에 담아준다.



전화번호도 위와 비슷하다.



이러한 것들이 각 매장정보마다 담겨야하기 때문에, for문을 사용한 것,

for문을 통해서 아래와 같이 result 에 담아준다.



```python
 #result에 매점정보 저장
            result.append([store_name_h2] + [store_address] + [store_phone])
```



그러면 x행 3열로 dataframe을 만들 수 있다.



*try ~ except를 하는 이유는, 홈페이지에 매장명이 담겨져 있지 않은 경우가 있어 에러가 발생하기 때문이다. 매장명이 없으면 그것을 스킵하고 다음으로 이어가게끔 except에 continue 를 넣어준다.



그러면 앞서 보여줬던 최종 코딩이 완성이 된다.

최종 완성된 코딩을 함수화 시킬 수 있다.



```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

from selenium import webdriver
import time


path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.coffeebeankorea.com/store/store.asp'
def coffeebean_store(result):
    for i in range(1, 6):
        driver.get(url)
        time.sleep(1) #웹 페이지 연결한 동안 1초 대기
        try:
            driver.execute_script('storePop2(%d)' % i)
            time.sleep(1)

            source = driver.page_source
            soupCB = BeautifulSoup(source,'lxml')

            #매점명
            store_name_h2 = soupCB.select_one('div.store_txt > h2').text

    #         print(store_name_h2)

            #매점 주소
            store_info_add = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(3)>td')
            store_address = store_info_add.text
    #         print(store_address)

            #매점 전화번호

            store_info_phone = soupCB.select_one('div.store_txt>table.store_table>tbody>tr:nth-of-type(4)>td')
            store_phone = store_info_phone.text
    #         print(store_phone)

            #result에 매점정보 저장
            result.append([store_name_h2] + [store_address] + [store_phone])
        except:
            continue

def main():
    result = []
    coffeebean_store(result)

    cb_tbl = pd.DataFrame(result, columns=['store','address','phone'])
    cb_tbl.to_csv('./data_crowling/CoffeeBean.csv', encoding='cp949', index = True )
    
if __name__ == '__main__':
    main()

    
```









