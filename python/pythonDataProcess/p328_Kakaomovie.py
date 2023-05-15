import os.path
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pandas import DataFrame

myparser = 'html.parser'
myurl = 'https://movie.daum.net/ranking/reservation'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)
infos = soup.findAll('div',attrs={'class': 'thumb_cont'})
print('-'*40)
print(infos)
print('-'*40)


no=0
result= []
for info in infos:
    no +=1
    mytitle = info.find('a', attrs={'class' : 'link_txt'})
    title = mytitle.string
    print(title)

#평점
no=0
result= []
for info in infos:
    no +=1
    mygrade = info.find('span', attrs={'class' : 'txt_grade'})
    grade = mygrade.string
    print(grade)

#예매율 -> 둘다 txt_num임. 그래서 어떻게 구분함?
no=0
result= []
for info in infos:
    no +=1
    mydate = info.find('span', attrs={'class' : 'txt_num'})
    date = mydate.string
    print(date)
#
no=0
result= []
for info in infos:
    no +=1
    mydate = info.find('span', attrs={'class' : 'txt_num'})
    date = mydate.string
    print(date)

