import pandas as pd
from pandas import DataFrame

data1 = {'name':["김유신", "김유신", "이순신","박영효","이순신","이순신","김유신"],  'korean': [60,50,40,80,30,55,45]}
data2 = {'name': ["이순신","김유신","신사임당"],'english':[60,55,80]}

df1 =DataFrame(data1)

df2= DataFrame(data2)

print('\n# Dataframe출력 01')
print(df1)

print('\n# Dataframe출력 02')
print(df2)

print('\n# 데이터합치기')
result = pd.merge(df1,df2, on=['name'])
print(result)

print('\n# 데이터합치기')
result = pd.merge(df1,df2, how='outer')
print(result)