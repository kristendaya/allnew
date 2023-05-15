import pandas as pd
import matplotlib as plt

plt.rc('font',family='malgun gothic')
filename = "tips.csv"

myframe=pd.read_csv(filename,encoding='utf-8')
print('head() 메소드 결과')
print(myframe.head())
print('-' * 40)

print('info() 메소드 결과')
print(myframe.info())
print('-' * 40)

mycolors = ['r', 'g', 'b']
labels = ['두산', 'LG', '키움']
print(labels)

