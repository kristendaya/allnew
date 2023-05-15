dictionary = {'김유신': 50, '윤봉길': 40, '김구': 60}
print('dictionary list : ', dictionary)

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key in dictionary.keys():
    print('{}의 나이는 {}입니다.'.format(key, dictionary[key]))

for key,value in dictionary.items():
    print('{}의 나이는 {}입니다.'.format(key,value))

##특정한 key가 존재하는지 찾고싶음.
findKey = '유관순'

if findKey in dictionary:
    print(findKey + '(은)는 존재합니다')
else:
    print(findKey + '(은)는 존재하지 않습니다')

result = dictionary.pop('김구')
print('after pop dictionary :', dictionary)
print('pop value:', result)

# dictionary list :  {'김유신': 50, '윤봉길': 40, '김구': 60}
# 김유신
# 윤봉길
# 김구
# 50
# 40
# 60
# 김유신의 나이는 50입니다.
# 윤봉길의 나이는 40입니다.
# 김구의 나이는 60입니다.
# 김유신의 나이는 50입니다.
# 윤봉길의 나이는 40입니다.
# 김구의 나이는 60입니다.
# 유관순(은)는 존재하지 않습니다
# after pop dictionary : {'김유신': 50, '윤봉길': 40}
# pop value: 60

dictionary.clear()
print('dictionary list:', dictionary)

#모든것을 지워버림.
