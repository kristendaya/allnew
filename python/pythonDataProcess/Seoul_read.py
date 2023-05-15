import pandas as pd

result=[]
myencoding = 'utf-8'
    sublist =[]
    sublist.append(name)
    sublist.append(age)
    result.append(sublist)

myframe = pd.DataFrame(result, columns = myColumns)

filename = 'csv_02_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode= 'w',index=False )