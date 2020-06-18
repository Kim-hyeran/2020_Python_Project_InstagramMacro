import requests

#함수 생성(분업화 목적)
def crawl(url):
    resp=requests.get(url)
    print(resp, url)
    return resp.content