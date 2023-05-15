import numpy as np
from pandas import DataFrame

mydata = [[10.0, np.nan, 20.0 ],\
          [20.0, 30.0,40.0], \
            [np.nan, np.nan, np.nan],\
            [40.0,50.0,30.0]]
myindex = ['이순신','김유신','윤봉길','계백']
mycolumn = ['국어','영어','수학']
myframe = DataFrame(data=mydata,\
        index = myindex, columns=mycolumn)
print('\n# 성적데이터프레임 출력')
print(myframe)

print('\n# 집계함수는 기본적으로 NaN은 제외하고 연산')
print('\n# sum(), axis = 0, 열방향')
print(myframe.sum(axis=0))

print('\n# sum(), axis = 1,행방향')
print(myframe.sum(axis=1))

print('\n# mean(), axis =1, skipna=False')
print(myframe.mean(axis=1, skipna = False))
print('-' *40)

print('\n# mean(), axis = 1, skipna=False')
print(myframe.mean(axis=1, skipna = False))
print('-' *40)

print('\n# idxmax(), 최대값을 가진 색인 출력')
print(myframe.idxmax())
print(myframe)

print('\n# 원본 데이터프레임 출력')
print(myframe)

print('\n# 누적합 메소드, axis=0 출력')
print(myframe.cumsum(axis=0))

print('\n# 누적합 메소드, axis=1 출력')
print(myframe.cumsum(axis=1))

print('\n# 최대요소 메소드, axis=1 출력')
print(myframe.cumsum(axis=1))

print('\n# 최소요소 메소드, axis=1 출력')
print(myframe.cummin(axis=1))

print('\n#평균')
print(np.floor(myframe.mean()))
#1.국어에서is null 인애를 찾는다. 얘를 최소 10점은 맞을수있게
myframe.loc[myframe['국어'].isnull(), '국어' ] = np.min(myframe['국어']) -5
myframe.loc[myframe['영어'].isnull(), '영어' ] = np.min(myframe['영어']) -5
myframe.loc[myframe['수학'].isnull(), '수학' ] = np.min(myframe['수학']) -5

#누적합이라는거는 전체행을다 해버리는건데, 특정한 필드값으로 특정할필드를채울수없음.
print(myframe)

print(np.round(myframe.describe()))