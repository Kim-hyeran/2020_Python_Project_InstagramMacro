# Python Project : Instagram Macro:camera:
Python 기반의 Selenium(feat. Chrome Driver)을 사용하여 인스타그램에 로그인하고, 원하는 해시태그로 피드를 검색한 후 피드별로 좋아요 클릭과 댓글 작성을 반복적으로 수행하는 매크로 프로그램

## :heavy_check_mark:Developer Environment
  - Language : [Python 3.7:crocodile:](https://www.python.org/)
  - IDE Tool : [Pycharm:computer:](https://www.jetbrains.com/ko-kr/pycharm/)
  - Package Manager : [Anaconda:snake:](https://www.anaconda.com/)
  - Using Package : [requests, selenium, beautifulsoup4, time, random](https://www.anaconda.com/library)
  - Using Web Driver : [Chrome Web Driver](https://chromedriver.chromium.org/downloads)
    > Use the same version as the Chrome Browser version you use

### Instagram Macro
#### Chrome Driver Setup(Selenium)
  - [Chrome Web Driver](https://chromedriver.chromium.org/downloads) 설치
  - Pycharm에 Web Driver 저장
  - 이용 경로를 불러와 driver에 담기
  
#### Instagram Login
  - 인스타그램 로그인 페이지 주소 가져오기
  - driver에 URL 주소 설정
  - 페이지 소스코드를 담아둔 driver에서 ID와 비밀번호 입력 칸 경로 찾기
  - ID와 비밀번호를 입력하고 로그인 버튼을 클릭하는 코드 작성
  
#### Hashtag Searching
  - 원하는 Hashtag Feed 페이지 주소를 저장
  - driver에 URL 주소 설정

#### Board List Input&Output(BeautifulSoup)
  - Feed의 각 게시물의 개별 주소만 수집

#### Like and Reply
  - for 반복문을 사용해 Feed 한 페이지의 게시물에 작업을 반복하도록 코드 작성
  - 무작위의 대기 시간 소요 후 작업을 수행하도록 설정
  - 댓글로 입력할 메시지 작성
  - 좋아요 버튼을 클릭하는 코드 작성
  - 댓글 입력 칸 클릭, 메시지 입력, 댓글 게시 버튼을 클릭하는 각각의 코드 작성
