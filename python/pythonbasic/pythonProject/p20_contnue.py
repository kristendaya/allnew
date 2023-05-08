sum = 0
for i in range(10):
    if i % 2 == 0 :
        continue
    sum +=i
    print(f'sum +={i}')
print()
print(f"sum = {sum}")

#지역변수 = 자동변수 . 이거를 쓰는 이유는 예를들어 for문을 돌고 삭제가 됨. 그러면 print 불가 . for문이 끝나고 나서 사용을 할수없다 /
#그래서 미리 선언읋 하는것.


