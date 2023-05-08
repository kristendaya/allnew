import calc_class

a= int(input('input first number:  '))
b= int(input('input second number: '))

my = calc_class.Calc(a,b)

print(f'{a}+{b} = {my.add()}')
print(f'{a}-{b}) = {my.sub()}')