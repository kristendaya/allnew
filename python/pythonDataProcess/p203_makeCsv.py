import random
import pandas as pd

result = []
mycoulmns = ('번호','이동','나이')
myencoding = 'utf-8'

for idx in range(1,3):
    sublist = []
    sublist.append(100 * idx)
    sublist.append('김철수' + str(idx))
    sublist.append((random.randint(1,10)))
    result.append(sublist)

myframe = pd.DataFrame(result, columns=mycoulmns)

filename = 'csv_01_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode= 'w', index= True)

filename = 'csv_01_02.csv'
myframe.to_csv(filename, encoding=myencoding, mode= 'w', index= False)

filename = 'csv_01_03.csv'
myframe.to_csv(filename, encoding=myencoding, mode= 'w', index= False, header=False)

filename = 'csv_01_04.csv'
myframe.to_csv(filename, encoding=myencoding, mode= 'w', index= False, sep="%")

print(filename+'파일저장완료')