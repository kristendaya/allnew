from pandas import Series

mylist = [10,40,30,20]
myseries = Series(data=mylist, index=['김유신','이순신','강감찬','광해군'])

print('\nData Type')
print(type(myseries))

myseries.index.name = '점수'
print('\nindex name of series')
print(myseries.index.name)

print('\nname of index')
print(myseries.values)

print('\nvalue of series')
print(myseries)

print('\nprint information of series')
print(myseries)

print('\nrepeat print')
for idx in myseries.index:
    print('Index:'+ idx + ',Value:' + str(myseries[idx]))