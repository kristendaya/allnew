i = input("input first number : ")
j = input("Input second number: ")

a = lambda a, i , j : i+j
print('{} + {} = {} '.format(i,j,a(int(i),int(j))))

