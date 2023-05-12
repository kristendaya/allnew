from class_animal import *

dog= Dog('doggy')
print(dog.name)
dog.move()
dog.speak()

duck = Duck('donald')
print(duck.name)
duck.move()
duck.speak()

zoo = [Dog('marry'), Duck('dduck')]

for z in zoo:
    print(z.name)
    z.speak()

    #move라는 글자가 뜨게한다 speak은 다름. 상속을 해서 animal 속성만 정의하면 move method는 프린트. main / speak은 pass. 독 이라는 상속을 만다ㅡㄹ어.
    #기본 클래스가 있을거고 상속 받은 클래스가 2개 있을거고
