class Calculate(object):
    #제일먼저 이닛을 정의.
    def __init__(self,first,second):
        self.first = first
        #2.초기화를해준다
        self.second = second
    def add(self):
        result= self.first + self.second
        return 'add result = %d' % result

    def sub(self):
        result = self.first - self.second
        return 'sub result = %d' % result

    def mul(self):
        result = self.first * self.second
        return 'mul result = %d' % result

    def div(self):
        if self.second == 0 :
            self.second = 5
        result = self.first / self.second
        return 'add result = %f' % result

calc = Calculate(14,0)

print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())