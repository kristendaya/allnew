import numpy as np
import pandas as pd

from pandas import DataFrame, Series


mydata = [[60.00,np.nan,90.00],[np.nan, 80.00, 50.00],[40.00, 50.00, np.nan]]
myindex= ['강감찬','김유신','이순신']
mycolumn= ['국어','영어','수학']

myframe=DataFrame(data=mydata , index=myindex, columns=mycolumn)
print(myframe)
print('\nBefore')

# print(myframe.mean())
myframe.loc[myframe['국어'].isnull(), '국어']= myframe['국어'].mean()
myframe.loc[myframe['영어'].isnull(), '영어']= myframe['영어'].mean()
myframe.loc[myframe['수학'].isnull(), '수학']= myframe['수학'].mean()
print('\nAfter')
print(myframe)


