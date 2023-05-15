tuple01 = (10, 20, 30)
tuple01 = tuple01 + (40, )
##튜플 원래 못바뀌는건데, 이거는 가능함. 값 고대로에 붙이는거.
print('print Tuple :', tuple01 )

tuple02 = 10, 20, 30, 40
##이렇게 해도 tuple이 됨.

mylist= [10,20,30,40]
tuple03 = tuple(mylist)

if tuple02 == tuple03:
    print("Component equal")
else:
    print("Component not equal")

tuple04 = (10, 20, 30)
tuple05 = (40, 50, 60)
tuple06 = tuple04 + tuple05
print(tuple06)

tuple07 = tuple04 * 3
print(tuple07)

#수학기능(값은 바뀌지 않지만 이렇게 쓸수있다.
a, b = (11, 22)
a, b = b, a

print('a=', a, 'b=', b)

tuple08 = (11,22,33,44,55,66)
print(tuple08[1:3])
print(tuple08[3:])

# tuple08[0] = 100 => 이런게 안된다구 xxxx


