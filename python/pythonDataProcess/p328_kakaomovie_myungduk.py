#1. thumb_cont 검색 해본다. 몇개인지 확인하고. 이런패턴이구나라는걸 확인
#첫번재 thumb이 클래스시작


import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

url = "https://movie.daum.net/ranking/reservation"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

infos = soup.findAll('div', attrs={'class':'thumb_cont'})

# print('-' * 40)
# print(infos)
# print('-' * 40)

no = 0          ##순위를 돌거니까~
result = []
df = pd.DataFrame()
# print(df)
for info in infos:
    no += 1
    mytitle = info.find('a', attrs={'class':'link_txt'})
    title = mytitle.string
    # print(title)

    a = info.find('span', attrs={'class':'txt_grade'})
    grade = a.string
    # print(grade)

    b = info.find('span', attrs={'class': 'txt_num'})
    num = b.string
    # print(num)

    c = info.find('span', attrs={'class': 'txt_info'})
    d = c.find('span', attrs={'class': 'txt_num'})
    info = d.string
    # print(info)

    result.append([no, title, grade, num, info])
    df = pd.concat([df, pd.DataFrame(result)], axis= 0)
    result = []  #중복값이 안들어갑니다.

df.columns = ['순위', '제목', '평점', '예매율', '개봉일']
df.set_index("순위", inplace=True)
print(df)
print(df.info())
#
# print(result)


import matplotlib.pyplot as plt

# plt.rcParams['font.family'] = 'AppleGothic'
#
# filename = 'daummovie.csv'
#
# myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
# myframe.index.name = '이름'
# myframe.columns.name = '시험 과목'
#
# myframe.plot(kind='bar', rot=0, stacked=True, title='학생별 누적 시험 점수', legend=True)
#
# filename = 'dataframeGraph02_04.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename + ' Saved...')
# print('-' * 100)
# plt.show()

# plt.rc('font', family='malgun gothic')
#
# ratings = df[['평점']]
# book_rates = df[['예매율']]
#
# ratings['평점'] = ratings['평점'].astype(float)
# book_rates['예매율'] = book_rates['예매율'].str.replace('%', '').astype(float)
# fig, ax = plt.subplots(figsize=(10, 8))
#
# ax.barh(ratings.index, ratings['평점'], label='평점')
# ax.barh(book_rates.index + 0.4, book_rates['예매율'], label='예매율')
#
#
# ax.set_xlabel('점수/예매율')
# ax.set_ylabel('영화 제목')
# ax.set_title('영화 순위')
# ax.legend()
# plt.show()
# filename = 'moviegraph33.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename + 'Saved...')
# plt.show()




# import matplotlib.pyplot as plt
#
# plt.rc('font', family='malgun gothic')
#
# ratings = df['평점']
# book_rates = df['예매율']
#
# ratings['평점'] = ratings['평점'].astype(float)
# book_rates['예매율'] = book_rates['예매율'].str.replace('%', '').astype(float)
#
#
# ratings[['', '예매율']].plot(kind='barh', rot=0, title='영화 순위', legend=True)
# print(ratings)
# print('-' * 40)
#
# filename = 'a.png'
# plt.savefig(filename, dpi=400, bbox_inches='tight')
# print(filename + 'Saved...')
# plt.show()




# y = range(len(df))
# w = 0.4  # 막대의 너비
# plt.barh(y, ratings, height=w, label='평점')
# plt.barh(y, book_rates, height=w, label='예매율')
#
# # 그래프에 제목, 레이블, 범례 등을 추가합니다.
# plt.title('영화 순위별 평점과 예매율')
# plt.yticks(y, df['제목'])
# plt.xlabel('평점/예매율')
# plt.legend()

# # 그래프를 출력합니다.
# plt.show()


