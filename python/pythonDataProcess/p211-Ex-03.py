import numpy as np
import pandas as pd
from pandas import Series

filename = '과일매출현황.csv'

print('\n# 누락된 데이터가 있는 샘플 DataFrame')
myframe=pd.read_csv(filename, index_col='과일명')
print(myframe)

print('\n#누락데이터 채워넣기')
mydict = {'구입액': 50,'수입량':20}
myframe.fillna(mydict, inplace= True)
print(myframe)
print('-' * 40)

print('\n#구입액과 수입량의 각 소계')
print(myframe.sum(axis =0))

print('-' * 40)

print(myframe.sum(axis =1))
print('-' * 40)

print(myframe.mean(axis =0))
print('-' * 40)

print(myframe.mean(axis =1))
