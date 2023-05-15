import numpy as np
from pandas import Series, DataFrame

sdata = {
          '국어' : [40, 60, 50,50,30],
          '영어' : [55,65,75,85,60],
          '수학' : [30,40,50,60,70]
     }

myindex = ['강감찬', '이순신', '김유신', '김구', '안중근']
myframe = DataFrame(sdata, index=myindex)
print(myframe)

print('\n# 짝수 행만 읽어보세요')
result = myframe.iloc[0::2]
print(result)

print('\n#  이순신 행만 읽어보세요')
result = myframe.loc['이순신']
print(result)

print('\n# 이순신 행만 읽어보세요')
result = myframe.loc[['강감찬'],['영어']]
print(result)

print('\n#  안중근과/ 강감찬의 국어/수학점수를 읽어보세요~ ')
result = myframe.loc[['안중근', '강감찬'],['국어','수학']]
print(result)

print('\n#  이순신과 강감찬의 영어 점수를 80점으로 변경하세요')
myframe.loc[['이순신','강감찬'],['영어']] =80

print('\n# 이순신부터 김구까지 수학 점수를 100으로 변경하세요')
myframe.loc['이순신':'김구' ,['수학']]=100
print(myframe)