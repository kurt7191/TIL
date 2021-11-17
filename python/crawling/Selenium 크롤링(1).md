# Selenium 크롤링



동적인 작업을 수행할 수 있는 크롤링



```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
```



필요한 패키지와 모듈들 설치



### Naver에서 id가 1개일때 

### 그리고 검색어 입력



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)
```



webdriver 크롬을 다운받았다면 해당 다운받은 경로로 webdriver.chrome 을 가동한다.



```python
url = 'https://www.naver.com'
driver.get(url)
```



driver에 `.get()` 함수를 쓰면 웹페이지를 가동시킬 수 있다.



```python
inputSearch = driver.find_element(By.ID, 'query')
```



html  요소를 id를 이용하여 찾는 법은 괄호에 `By.ID` 를 사용하는 것.

선택된 요소를 `inputSearch` 에 저장한다.



inputSearch 는 query 아이디를 가지고 있는 검색창이다.

검색창에 입력은 어떻게 할까?



```python
inputSearch.send_keys('겨울왕국')
```



`send_keys` 함수를 이용하여 검색어를 집어 넣는다.



```python
buttonSearch = driver.find_element(By.ID, 'search_btn')
buttonSearch.click()
```



id를 이용해서 버튼 창 요소를 선택하고 click() 함수를 이용하여 클릭하게 한다.



### Google 에서 class가 1개 일때

### 그리고 검색어입력



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'https://www.google.com/'
driver.get(url)
```



마찬가지로 드라이브를 구동시키고 웹페이지를 띄운다.



```python
btns = driver.find_element(By.CLASS_NAME, 'gLFyf')

# 검색어를 입력한다.
btns.send_keys('겨울왕국')

#btns.click() # click( )안됨
btns.submit()
```



id 선택과 비슷하게 By.<클래스명> 을 하여 선택한다.



### 네이버에서 많이 본 뉴스 목록 보기



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.naver.com'
driver.get(url)
```



드라이브 구동과 창 띄우는 것은 똑같다.



```python
news = driver.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2)')

news.click()
```



요소(태그) 를 선택할 때 , 해당 웹사이트에 들어가서 개발자 모드로 들어간 이후(f12),

원하는 태그를 선택하고 주소를 copy 한다.



이때, 두 가지 링크가 있는데 바로 css_selector 와 xpath 이다.

두 가지 모두 기능은 똑같다. 하지만 css_selector 같은 경우에는 숫자 수정을 할 때, 어려움을 겪는다. xpath 같은 경우가  숫자 수정에 능하다.



위의 코드에서 css_selector에 가져온 주소는 selector 주소이다.



```python
news_rank = '//*[@id="_rankingList0"]/li[1]/div/div/div/a[1]'

driver.find_elemet_by_xpath(news_rank).click()
time.sleep(3)
```



위의 링크가 xpath 링크라고 할 수 있다. 대괄호 안에 숫자가 있기 때문에 이 숫자로 선택을 구체적이게 할 수 있다.



위의 작업들은 css_selector 로 뉴스 a 링크를 불러오고 뉴스 페이지에서 뉴스랭크 버튼을 xpath 로 클릭한 것이다.



```python
news = driver.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2)')
news.click()

for n in range(1, 6):
    news_rank = '//*[@id="_rankingList0"]/li[%d]/div/div/div/a[1]' % n
    driver.find_element_by_xpath(news_rank).click()
    time.sleep(3)
```



xpath 를 조작해서 한 번에 여러 페이지를 둘러볼 수 있다.

이때 중요한 점이 time.sleep() 을 하지 않은 경우에는 페이지가 확확 넘어가기 때문에 몇 초 정도 뜸을 들일지 설정해야만 한다. 위의 코드는 3초를 뜸들였다.



### 네이버 로그인



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'http://www.naver.com'
driver.get(url)
```



역시나 똑같이 웹드라이브 크롬을 구동하고 웹페이지를 띄운다.

다음으로는 웹페이지의 로그인 창 요소를 선택하고 클릭 동적 처리를 해줘야만 한다.



```python
log = driver.find_element_by_xpath('//*[@id="account"]/a')
log.click()

```



xpath 링크를 이용해서 불러왔다.

click() 함수를 이용해서 요소를 클릭해준다.

로그인 버튼을 누르게 되면 아이디와 비밀번호를 입력하는 칸이 나타난다.



```python
inputid = driver.find_element_by_id('id')
inputpw = driver.find_element_by_id('pw')
time.sleep(3)

inputid.send_keys('####')
inputpw.send_keys('####')
```



먼저 아이디와 비밀번호 요소를 선택해야만 한다.

앞서 겨울왕국이라는 검색어를 집어 넣었듯이 아이디와 비밀번호에도 텍스트를 집어넣을 수 있다.

바로 `send_keys` 이다.



```python
login = driver.find_element_by_xpath('//*[@id="log.login"]')
login.click()
```



그리고 최종적으로 로그인을 할 수 있는 로그인 버튼을 xpath 를 가져와서 불러오고 클릭 동적처리를 한다. (네이버는 보완이 걸려 있어서 로그인을 실제로 하지는 못한다.)



### 교보문고 베스트 링크 가져와서 파일로 저장하기



```python
path = './lib/chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'http://www.kyobobook.co.kr'
driver.get(url)
```



역시나 똑같이 드라이버를 구동하고 웹페이지를 띄운다.



```python
bestBtn = driver.find_element_by_css_selector('#header > div.navigation_bar > ul.gnb_sub > li:nth-child(1) > a')
bestBtn.click()
```



selector 링크를 이용해서 베스트 페이지로 들어간다.



```python
source = driver.page_source
html_s =  BeautifulSoup(source, 'lxml')
```



`page_source` 를 이용해서 페이지 전체의 데이터를 불러올 수 있다.

이때 자료형은 문자형이기 때문에 `BeatifulSoup` 에 바로 넣을 수 있다.

(본래는 res = request.get(<url>) 을 통해서 얻은 url 페이지의 정보를 res.text를 해서 넣어줘야 했다.)



이 코드에서 중요한점은 셀레니움은 드라이버에서 page_source를 통해서 페이지 정보를 가져올 수 있다는 점. (request가 아니라)



```python
title_list = html_s.select('div.detail > div.title')
```



BeatifulSoup 은 태그를 선택할 때 find, find_all, select_one, select 가 있었다.

find => select_one 처럼 하나만 선택할 경우고

select, find_all 같은 경우에는 모두 선택할 때 사용된다.

위의 `div.detail` 는 `('div', {"class":"detail}) ` 처럼 특정 클래스 값을 가지고 있는 특정 태그를 선택할 때 사용하는 선택 기법이다.



여기다 `div.detail > div.title` 와 같은 부모 자식과 같은 선택기법을 선택하여 title을 선택했다.

왜냐하면 책의 목록들이 div 안에 title 클래스에 들어가 있기 때문이다.



title_list 는 몇 개의 정보를 가지고 있는데 index를 이용해서 text를 이용해야지만 책의 제목을 꺼낼 수 있다.

title_list 는 여러 정보를 가지고 있기 때문에 바로 text를 사용할 수 없다.



```python
with open(file_path, mode = 'w', encoding='utf-8') as f:
    for n in range(len(title_list)):
        line = re.sub('\n','', title_list[n].text)
        if line is not None:
            f.write(line)
            f.write('\r\n')
f.close()
print('크롤링 완료')
```





