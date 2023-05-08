from random import *
users = range(1,21) # 1부터 20까지 숫자 생성
print(type(users))
users = list(users)
print(users)
shuffle(users)
print(users)


winners = sample(users, 4)

print("--당첨자 발표 -- ")
print("치킨 당첨자 :{0}".format())
print("커피 당첨자 :{0}".format())