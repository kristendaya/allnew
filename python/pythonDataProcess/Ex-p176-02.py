import numpy as np
from pandas import Series, DataFrame

myindex = ['강감찬', '이순신', '김유신', '광해군','연산군','을지문덕']
mylist = [50, 60,40, 80, 70, 20]
myseries = Series(data=mylist, index= myindex)
print(myseries)

print('n\n1번쨰 항목을 100으로 변경')
myseries[1]=100

print('\n2번째부터 4번째까지 999로 변경')
myseries[2:5] = 999

print('\n강감찬과 을지문덕을 30으로 변경')
myseries[['강감찬','을지문덕']] = 30

print('\n시리즈 내용 확인')
print(myseries)