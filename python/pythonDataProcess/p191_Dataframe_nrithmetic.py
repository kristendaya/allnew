import numpy as np
from pandas import Series, DataFrame

myindex = ['강호민', '유재준', '신동진']
mylist = [30,40,50]

myseries = Series(data=mylist, index= myindex)
print('\nSeries print')
print('myseries')

myindex= ['강호민', '유재준', '이수진']
mycoulums = ['서울', '부산', '경주']
mylist = list(10 * onedata for onedata in range(1,10))

myframe = DataFrame(np.reshape(np.array(mylist), (3,3)), index= myindex, columns = mycoulums)

print('\nDataFrame print')
print(myframe)

print('\nDataFrame + Series')
result = myframe.add(myseries, axis = 0)
print(result)

myindex2 = ['강호문', '유재준', '김병준']
mycoulums2 = ['서울', '부산', '대구']
mylist2 = list(5* onedata for onedata in range(1,10))

myframe2 =  DataFrame(np.reshape(np.array(mylist2), (3,3)), index= myindex2, columns= mycoulums2)
print('\nDataFrame print')
print(myframe2)

print('\nDataFrame + Dataframe')
result = myframe.add(myframe2, fill_value=0)
print(result)

