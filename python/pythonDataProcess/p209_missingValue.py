import numpy as np
import pandas as pd

from pandas import DataFrame, Series

print('\n# 시리즈의 누락된 데이터 처리하기')
print('# 원본시리즈')
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)

print('\n# isnull()함수: NaN이면 True')
print(myseries.isnull())

print('\n# notnull()함수: NaN이 아니면 True')
print(myseries.notnull())
print("-" * 40)

print('\n# notnull() 이용하여 참인 항목만 출력')
print(myseries[myseries.notnull()])

print('\n# dropna() 이용 누락 데이터 처리')
print(myseries.dropna())


filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col='이름', encoding='utf-8')
print(myframe)

print('\n# dropna() 이용 누락 데이터 처리')
cleaned = myframe.dropna(axis=0, how='all')
print(cleaned)

print('\n# how ="all"이용 누락 데이터처리')
cleaned = myframe.dropna(axis=0,how='any')
print(cleaned)

print('\n# [영어] 칼럼에 NaN 제거')
print(myframe.dropna(subset =["영어"]))

print('\n# 칼럼기준 how ="all"이용 누락 데이터처리')
cleaned = myframe.dropna(axis=1,how='all') ##인덱스만 담으라고...
print(cleaned)

print('\n# 칼럼기준 how ="all"이용 누락 데이터처리')
cleaned = myframe.dropna(axis=1,how='any')
print(cleaned)

print(myframe)
myframe.loc[['강감찬','홍길동'],['국어']] = np.nan
print('##After')
print(myframe)

print(myframe.dropna(axis=1, how="all"))

print('##thresh option') ##w조회되는 옵션이다. not null 이 아닌애를 찾는다.
print(myframe.dropna(axis=1, thresh=2)) #Nan이 아닌 갯수를 센다.

print('#######')
print(myframe.dropna(axis=1, how="any"))

print(myframe)