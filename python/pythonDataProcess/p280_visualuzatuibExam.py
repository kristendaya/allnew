import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
from math import sqrt

font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font',family=font_name)
# plt.rcRarams['fontfamily']='malgun'

theaterfile = 'theater.csv'
colnames = ['id','theater','region','bindo']
dftheater = pd.read_csv(theaterfile, names= colnames, header=None)
dftheater = dftheater.rename(index=dftheater.id)
dftheater = dftheater.reindex(columns=['theater','region','bindo'])
dftheater.index.name ='id'

print('전체 조회')
print(dftheater)
print('-'*50)

print('극장별 상영 횟수 집계')
mygrouping = dftheater.groupby('theater')['bindo']
sumSeries = mygrouping.sum()
meanSeries = mygrouping.mean()
sizeSeries = mygrouping.size()

print('3개의 시리즈 이용 데이프레임 생성')
df = pd.concat([sumSeries, meanSeries, sizeSeries], axis =1)
df.columns = ['합계','평균','개수']
print(df)
print('-'*50)

df.plot(kind='barh', rot=0)
plt.title(str(len(df))+ '개 매장 집계데이터')
plt.show()
filename='visualizationExam_01.png'
plt.savefig(filename)
print(filename+'saved...')

print('집계 메소드를 사전에 담아 전달')
print('지역의 개수와 상영횟수의 총합')
mydict = {'bindo' : 'sum', 'region': 'size'}
result= dftheater.groupby('theater').agg(mydict)
print(result)

print('넘파이를 이용한 출력')
result=mygrouping.agg([np.count_nonzero, np.mean, np.std])
print(result)
print('-'*50)

def myroot(values):
    mysum = sum(values)
    return sqrt(mysum)
#이전함수를 호출하는 방법
def plus_add(values, somevalue):
    result = myroot(values)
    return result+ somevalue

#이미 작성된사용자 정의 함수와 그룹바이 함수를 적용하여 데이터를 만들어 보기. 빈도수에 루트를 씌운 값으룩하고이씅ㅁ. 2번째 예시에서는 매게변수 2개 .
mygrouping =dftheater.groupby('theater')['bindo']
print('groupby와 사용자 정의 함수 사용하기')
result= mygrouping.agg(myroot)
print(result)
print('-'*50)

print('grouby와 사용자 정의함수(매개변수 2개)사용')
result = mygrouping.agg(plus_add, somevalue =3)
print(result)
print('-'*50)

newDf = df.loc[:, ['평균','개수']]
newDf.plot(kind='bar', rot=0)
plt.title('3개의 극장의 평균과 상영관의 수')

filename= 'visualizationExam_02.png'
plt.savefig(filename)
print(filename + ' saved...')

labels = []
explode = (0, 0.03 ,0.06)

for key in sumSeries.index:
    mydata = key + '(' + str(sumSeries[key]) + ')'
    labels.append(mydata)

figl, axl = plt.subplot()
mytuple = tuple(labels)
axl.pie(sumSeries, explode=explode, labels=mytuple, autopct ='%1.1f',shadow=True, startangle=90 )

axl.axis('eqal')