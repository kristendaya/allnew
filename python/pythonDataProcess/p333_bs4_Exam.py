import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame
import pandas as pd

url = "https://movie.daum.net/ranking/reservation"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs={'class':'thumb_cont'})

# print('-' * 40)
# print(infos)
# print('-' * 40)

no = 0
result = []
for info in infos:
    no += 1
    mytitle = info.find('a', attrs={'class':'link_txt'})
    title = mytitle.string

    mygrade = info.find('span', attrs={'class':'txt_grade'})
    grade = mygrade.string

    mynum = info.find('span', attrs={'class':'txt_num'})
    num = mynum.string

    myrelease = info.find('span', attrs={'class':'txt_info'})
    release = myrelease.span.string

    result.append((no, title, grade, num, release))
# print(result)

import matplotlib.pyplot as plt
from matplotlib import font_manager


print('-' * 40)

mycolumn = ['순위', '제목', '평점', '애매율', '개봉일']

myframe = DataFrame(result, columns=mycolumn)
newdf = myframe.set_index(keys=['순위'])
print(newdf)
print('-' * 40)

filename = 'daumMovie.csv'
myframe.to_csv(filename, encoding='utf-8', index=False)
print(filename, ' saved...', sep='')
print('finished')

filename = 'daumMovie.csv'

myframe = pd.read_csv(filename, index_col='제목', encoding='utf-8')
myframe.index.name = '제목'
myframe.columns.name = '시험 평점'

myframe.plot(kind='barh', rot=0, stacked=True, title='평점 및 예매율', legend=True)

filename = 'dataframeGraph02_04.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' Saved...')
print('-' * 100)
plt.show()

