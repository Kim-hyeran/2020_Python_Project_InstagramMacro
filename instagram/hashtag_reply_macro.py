# hashtag_reply_macro.py
#   : 해시태그 피드에 좋아요와 댓글을 반복적으로 다는 매크로 프로그램

from selenium import webdriver
import time, random
from bs4 import BeautifulSoup

# 1. Chrome Driver Setup
path='..'
driver=webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

# 2. Instagram Login
url='https://www.instagram.com/accounts/login/'
driver.get(url)
time.sleep(3)

# what is xpath?
# : W3C의 표준으로 확장 생성언어 문서의 구조를 통해 경로 위에 지정한 구문을 사용하여 항목을 배치하고 처리하는 방버을 기술한 언어
                                # 로그인 아이디 입력 칸으로 향하는 경로(div[1]의 경우 같은 레벨의 div 중 선택 : 0이 아닌 1부터 시작)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys('') #아이디 입력
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys('') #비밀번호 입력
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click() #로그인 버튼 클릭

# 3. Hashtag Searching
time.sleep(2)
hash_url='https://www.instagram.com/explore/tags/catstagram/'
driver.get(hash_url)

# 4. Board List Input&Output
def parse(page_code):
    soup=BeautifulSoup(page_code, 'html.parser')
    feed_list=soup.findAll('div', {'class', 'v1Nh3'}) # class값은 수시로 변경됨(실행할 때 확인)

    links=[]
    for one in feed_list:
        insta_link='https://www.instagram.com/'
        link_addr=one.find('a')['href']
        print(insta_link+link_addr)
        links.append(insta_link+link_addr)
    return links

time.sleep(4)
page_code=driver.page_source
links=parse(page_code)
print('Feed Count :', len(links))

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        driver.get(url)

        rnd_sec=random.randint(5, 15)
        time.sleep(rnd_sec)
        messege='♥♥♥'

        # 좋아요
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()

        #댓글
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(messege)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/button').click()

    except Exception as e:
        print(e)