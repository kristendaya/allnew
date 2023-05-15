
import numpy as np
from pandas import DataFrame
myindex = ['이순신','김유신','강감찬','광해군','연산군']
mycolumns = ['서울','부산','광주','목포','경주']
mylist = list(10 * onedata for onedata in range(1,26))
print(mylist)

myframe= DataFrame(np.reshape(mylist,(5,5)),
                   index= myindex, columns=mycolumns)
print(myframe)

print('\n1 row data read of series')
result = myframe.iloc[1]
print(type(result))
print(result)

print('\nmulti row data read of series')
result = myframe.iloc[[1,3]]
print(type(result))
print(result)

print('\neven rowd data read of seires')
result = myframe.iloc[0::2]
print(type(result))
print(result)

print('\nodd row data read of series')
result = myframe.iloc[1::2]
print(type(result))
print(result)

print('\n김유신 included row data read of Dataframe')
result = myframe.loc[['김유신']]
print(type(result))
print(result)

print('\n이순신,강감찬 included row data read of Dataframe')
result = myframe.loc[['이순신','강감찬']]
print(type(result))
print(result)

print(myframe.index)
print('-'*50)

print('\n이순신, 광주 실적 included row data read of Dataframe')
result = myframe.loc[['이순신'], ['광주']]
print(type(result))
print(result)

print('\n연산군, 강감찬 / 광주, 목포 실적 included row data read of Dataframe')
result = myframe.loc[['연산군','강감찬'],['광주','목포']]
print(type(result))
print(result)

print('\n김유신~ 광해군 / 서울, 목포 실적 included row data read of Dataframe')
result = myframe.loc['김유신':'광해군','부산']
print(type(result))
print(result)

print('\nBoolean Data process')
result = myframe.loc[[False, True, True,False,True]]
print(result)

print('\n부산 실적 <= 100')
result = myframe.loc[myframe['부산']<= 100]
print(result)

cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140

print(type(cond1))
print('-' * 40)

df = DataFrame([cond1,cond2])
print(df)
print('-'* 40)

print(df.all())
print('-'*40)

print(df.any())
print('-'*40)

result = myframe.loc[df.all()]
print(result)

result = myframe.loc[df.any()]
print(result)

print('\nlambda function')
result = myframe.loc[lambda df : df['광주'] >= 130]
print(result)
print('\ndata set')

print('\ndata set 30 => 이순신,강감찬 부산 실적')
myframe.loc[['이순신','강감찬'],['부산']] =30
print(myframe)

print('\ndata set 80  => 김유신~ 광해군 경주 실적')
myframe.loc['김유신':'광해군',['경주']] =80
print(myframe)

print('\ndata set 50  => 연산군 모든 실적')
myframe.loc[['연산군'],:] =50
print(myframe)

print('\ndata set 60  => 모든 사람의 실적')
myframe.loc[:,['광주']] = 60
print(myframe)

print('\ndata set 0 : 경주실적 <= 60인 사람의 경주, 광주실적')
myframe.loc[myframe['경주'] <= 60, ['경주','광주']] = 0
print(myframe)
