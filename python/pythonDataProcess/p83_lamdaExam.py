def nolamda(x,y):
    return 3 * x + 2 * y

x, y = 3, 5

result = nolamda(x,y)
print('일반 함수 방식: %d' % (result))

yeslamda = lambda x,y : 3 * y + 2 * y
result = yeslamda(x,y)
print("람다방식: %d" % (result))

result = yeslamda(5,7)
print("람다방식2 : %d" % (result))

##이름을 부르기 애매한 함수를 람다. 익명함수. 특별한 기능을 하기는 하지만, 아주 단순한 기능을 인풋하면 해주는 함수.