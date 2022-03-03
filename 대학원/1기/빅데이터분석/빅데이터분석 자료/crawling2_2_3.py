from selenium import webdriver
from bs4 import BeautifulSoup
import time
 
url = 'https://news.naver.com/main/read.nhn?m_view=1&\includeAllCount=true&mode=LSD&mid=shm&sid1=100&oid=422&aid=0000430957'

 
#웹 드라이버
driver = webdriver.Chrome(executable_path=r'D:/kjw/lecture/bda_21_2_대학원공통과목/week12/chromedriver_win32/chromedriver.exe')
driver.get(url)
 
#기사제목 추출
article_head = driver.find_elements_by_css_selector('div.article_info > h3 > a')
print("기사 제목 : " + article_head[0].text)


article_head1 = driver.find_elements_by_xpath('/html/body/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/h3/a')
print("기사 제목 : " + article_head1[0].text)

article_head1 = driver.find_elements_by_xpath('//h3[@id="articleTitle"]/a')
print("기사 제목 : " + article_head1[0].text)
 
#기사시간 추출
article_time = driver.find_elements_by_css_selector('div.sponsor > span.t11')
print("기사 등록 시간 : " + article_time[0].text)

article_time1 = driver.find_elements_by_xpath('/html/body/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/div/span')
print("기사 등록 시간 : " + article_time1[0].text)

article_time1 = driver.find_elements_by_xpath('//div[@id="main_content"]/div[1]/div[2]/div/span')
print("기사 등록 시간 : " + article_time1[0].text)

#더보기 계속 클릭하기
while True:
    try:
        btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        btn_more.click()
        # time.sleep(1)
    except:
        break
 

html = driver.page_source
dom = BeautifulSoup(html, "lxml")

# 댓글이 들어있는 페이지 전체 크롤링
comments_raw = dom.find_all("span", {"class" : "u_cbox_contents"})


# 댓글의 text 추출
comments = [comment.text for comment in comments_raw]

comments[:3]
