import pandas as pd

peri = 'pelicana.csv'
chega = 'cheogajip.csv'

atable = pd.read_csv(peri, encoding='utf-8')
btable = pd.read_csv(chega, encoding='utf-8')

print(atable)
print('-' * 40)

print(btable)
print('-' * 40)

atable['name of chi'] = '페리카나'
btable['name of chi'] = '처가집'

mylist = []
mylist.append(atable)
mylist.append(btable)
print(mylist)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
#axis=1 로하면 새로운 데이터프레임을 만든다. 원래는 objs=[atable,btable]

filename = 'chickenlist.csv'

result.to_csv(filename, encoding='utf-8')
print(filename + '저장완료')

print(result)