def factorial(n) :
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

n = input("input number : ")
print("{} factorial is {}".format(n, factorial(int(n))))

