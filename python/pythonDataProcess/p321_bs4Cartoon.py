from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = 'http://comic.naver.com/webtoon/weekday'

#이페이지에 request해서 데이터를 가져온 후 변수에 저장한다.

response = urlopen(myurl)

print(type(response))

soup = BeautifulSoup(response, 'html.parser')

title =soup.find("title")