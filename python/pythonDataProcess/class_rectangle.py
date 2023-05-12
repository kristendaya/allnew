class Rectangle(object):
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def printCount(cls):
        print(cls.count)

    def isSquare(wid,hei ):
         return(wid == hei)


    def calcArea(self):
        return self.width * self.height



    def calcArea(self, width, height):
        return self.width * self.height


#함수는 호출될때 해석을 한다. 그러면 rec 을 안에서 이미 정의가 될거다. 됐다는전제로 본다. __init__을 생성자로 봄. rec을 자기자신을 부르는걸 징그러워서 cls.count로 부른다.
