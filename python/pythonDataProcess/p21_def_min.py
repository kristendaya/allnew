
def min(a,b):
    if a > b:
        return b
    else:
        return a

a=input("input first number: ")
b=input("input Second number:")

print("{} vs {} : Min number ={}".format(a,b, min(a,b)))