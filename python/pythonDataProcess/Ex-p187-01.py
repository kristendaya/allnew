import pandas as pd

filename = 'data02.csv'
df = pd.read_csv(filename, header=None, index_col=0, names=['학년', '국어', '영어', '수학'])

df.index.name = '이름'
df.loc[['강호민'], ['영어']] = 40
df.loc[['박영희'], ['국어']] = 30

print(df)