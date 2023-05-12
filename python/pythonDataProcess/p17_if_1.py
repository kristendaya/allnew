a = int(input("Input the Fisrt Number: "))
b = int(input("Input the Secound Number: "))

max_value = a if a > b else b
#true 면 [앞 구문이 적용된다 if 면~ )

print(f"Max is {max_value}")
# f fomating way like %. 변수의 자리를 잡아준다는게 = formating. 1. % 2. f 쓰는방법 3. .format()
