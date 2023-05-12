
import random

def convertbinary(x):
    temp = []
    while True:
        remain = x % 2
        x = x // 2
        temp.append(remain)

        if x < 2:
            temp.append(x)
            break
    temp.reverse()
    return temp

x = random.randint(4, 16)
binary_x = convertbinary(x)

print(f'{x} = {binary_x}')
