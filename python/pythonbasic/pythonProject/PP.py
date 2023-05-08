# 배추가격 = 1000
# i = 0
#
# while i < 5:
#     배추가격 = 배추가격 * 1.1
#     i +=1
# print(배추가격)

# import random
#
# lotto = []
#
# while len(lotto)< 6:
#     num = random.randint(1,45)
#     if num not in lotto:
#         lotto.append(num)
#
# print(lotto)

# apart =[[101,102], [201,202], [301,303], [401,404]]
#
# for 층 in apart :
#     for 세대 in 층:
#         print(세대,end=" ")
#     print(" ")

# for i in range(5):
#     for j in range(5):
#         print("*", end= '')
#     print("")

# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print("")

# for i in range(5):
#     #공백을 위한 루프
#     for j in range(5-1-i):
#         print("", end= '')
#         #별을 위한 루프
#     for j in range(i+1):
#         #즐바꿈
#         print("*", end='')
#
#     print("")
#
# for i in range(5):
#     for j in range(5-1-i):
#         print("",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print("") #다음줄로 줄바꿈

# for i in range(5):
#    for j in range(5-1-i):
#         print("", end='')
#     for j in range(i+1):
#         print("*", end='')
#     print("")


# def average(num1, num2):
#     val = (num1 + num2)/2
#     print(val)
# ##그니까 여기까지가 정의인거야. print하는거까지가
# average(10,20)


def mymax(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

def mymin(num1, num2):
    if num1 < num2:
        print(num1)
    else:
        print(num2)

mymax(5,3)
mymin(6,7)
