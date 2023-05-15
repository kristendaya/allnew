from pandas import Series, DataFrame
import numpy as np

myindex = ['윤봉길', '김유신', '신사임당']
mylist = [30, 40, 50]

myseries = Series(data=mylist, index=myindex)
print('\n시리즈 출력결과')
print(myseries)

myindex = ['윤봉길', '김유신', '이순신']
mycolumns = ['용산구', '마포구', '서대문구']
mylist = list(3 * onedata for onedata in range(1, 10))

myframe = DataFrame(np.reshape(np.array(mylist), (3, 3)), index=myindex, columns=mycolumns)
print(myframe)

print('\nDataFrame + Series')
result = myframe.add(myseries, axis=0)
print(result)

myindex2 = ['윤봉길', '김유신', '이완용']
mycolumns2 = ['용산구', '마포구', '은평구']
mylist2 = list(5 * onedata for onedata in range(1, 10))