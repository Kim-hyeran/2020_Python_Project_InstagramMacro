# chapter03_selenium_crawl.py
#   : selenium을 이용해서 페이지를 크롤링하는 방법

from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')

url='https://www.instagram.com/explore/tags/catstagram/'
driver.get(url) # 웹 드라이버로 URL 페이지 접속
time.sleep(5) # 5초 기다린 후 소스코드 출력
# time.sleep() 사용 이유
#   : 웹 드라이버에서 페이지가 완전히 로딩되기 전에 page_source를 가져오기 때문에 미완성된 코드를 수집하는 데 한계가 있음
#     그래서 5초 간의 시간을 주고 페이지가 전부 로딩되면 그 때 소스코드를 가져오도록 함

page_code=driver.page_source # 해당 URL의 전체 소스코드 가져오기(beautifulsoup의 resp와 같음)
print(page_code)