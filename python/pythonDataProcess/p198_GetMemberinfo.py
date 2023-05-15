import pandas as pd

filename = 'memberInfo.csv'
df = pd.read_csv(filename)
print(df)

newdf01 = df.set_index(keys=['id'])
print(newdf01)

newsdf02 = df.set_index(keys=['id'], drop=False)
print(newsdf02)

df02 = pd.read_csv(filename, index_col='id')
print(df02)