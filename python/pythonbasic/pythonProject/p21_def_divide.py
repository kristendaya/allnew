def divide(a,b):
    return (a/b, a%b)

a = input("input first number:")
b = input("input second number: ")

print(f"input number {a}/ {b}")
q,r = divide(int(a), int(b))
print("Quotient: ",int(q))
print("Reminder:",r)

