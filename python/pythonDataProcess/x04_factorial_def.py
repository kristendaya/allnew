# def factorial(x):
#     if x == 0:
#         return 1
#     else :
#         return x * factorial(x-1)
#
# input = int(input("Input the number: "))
# print(f'{input} factorial = {factorial(input)}')

#### 파라미터는 내부적으로 전달, 내부적으로 self로 전달(?)
class Factorial:
    def __init__(self, x):
        self.x = x

    def factorial(self):
        if self.x == 0:
            return 1
        else:
            return self.x * Factorial(self.x - 1).factorial()


input_number = int(input("Input the number: "))
factorial = Factorial(input_number).factorial()
print(f"{input_number} factorial = {factorial}")

##선생님
class Factorial:
    def __init__(self, x):
        self.x = x

    def factorial(self):
        if self.x == 0 :
            return 1
        n=self.x
        self.x -=1
        return n * self.factorial()

input = int(input("input the number:"))
fact = Factorial(input)
print(f'{input} factorial = {fact.factorial()}')

class Factorial(object):
    def __init__(self, x):
        self.x = x
    def factorial(self):
        n=1
    for i in range(1, self.x+1):
        n = n*i

    return n

input = int(input("input the number:"))
fact = Factorial(input)
print(f'{input} factorial = {fact.factorial()}')