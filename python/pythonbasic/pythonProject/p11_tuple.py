#!/usr/bin/env python

person = ("Kim",24,"male")
print(person)

a = ()
print(a)

b=(person)
print(b)

name, age, gender = person
print("name:" , name )
print("age:" , age)
print("gender:", gender)

n = 1
numbers = [1,2]
print(type(person))
print(type(n))
print(type(person))

print(person[0])
print(person[-1])
#왜 -1 ? 도넛형태를 가지고있다

fruits = ('apple', ('banana', 'cherry'), ('strawberry', 'watermelon'))
print(fruits)
print(fruits[0])
print(fruits[1][0])
print(fruits[2][1])
