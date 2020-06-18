# chapter02_webdriver.py
#   : selenium의 web driver 사용 방법(chrome driver)

from selenium import webdriver

# instagram 페이지에서 원하는 해시태그로 selenium 접속(+chrome driver)
driver=webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')
# 상대주소 : 내 현재 위치에서 다른 파일을 찾아가는 경로(반)절대주소:가장 상위 폴더에서부터 시작하는 경로)
# 코드 작성 시 절대주소를 사용하면 개발한 컴퓨터에서만 적용된다

# URL 주소에 한글이 있는 경우 유니코드로 변환된다(한글은 깨지는 경우 존재)
url='https://www.instagram.com/explore/tags/catstagram/'
driver.get(url)

# driver.close() : 실행 후 브라우저 종료