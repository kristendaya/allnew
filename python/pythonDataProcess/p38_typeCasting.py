str1 = '100'
str2 = '200'
str3 = '12.345'

int1 = int(str1)
int2 = int(str2)
float1 = float(str3)

print(int1 == str1)
print(type(int1))
print(type(int2))
print(type(float1))

sum = int1 + int2
#산술연살자
print('result1:',sum)

float2 = float1 + 35.2
print('result2 ', float2)