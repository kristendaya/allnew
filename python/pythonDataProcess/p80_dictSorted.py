wordInfo = {'세탁기': 50, '선풍기': 30, '청소기': 40, '냉장고': 60 }

myxticks = sorted(wordInfo, key =wordInfo.get, reverse =True)
print(myxticks)

#값이 가장 큰애 순으로 정렬

revers_key= sorted(wordInfo.keys(), reverse= True)
print(revers_key)

#역순정렬.

chartdata = sorted(wordInfo.values(), reverse= True )
print(chartdata)