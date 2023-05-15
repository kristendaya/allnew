import pandas as pd

afile = 'android.csv'
bfile = 'iphone.csv'

atable = pd.read_csv(afile, encoding='utf-8')
btable = pd.read_csv(bfile, encoding='utf-8')

print(atable)
print('-' * 40)

print(btable)
print('-' * 40)

atable['phone'] = '안드로이드'
btable['phone'] = '아이폰'

mylist = []
mylist.append(atable)
mylist.append(btable)
print(mylist)

result = pd.concat(objs=mylist, axis=0, ignore_index=True)
#axis=1 로하면 새로운 데이터프레임을 만든다. 원래는 objs=[atable,btable]

filename = 'result.csv'

result.to_csv(filename, encoding='utf-8')
print(filename + '저장완료')

print(result)
