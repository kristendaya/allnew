import pandas as pd

filename = 'seoul.csv'

#데이터프레임 =df

df = pd.read_csv(filename)
print(df)

result=df.loc[(df['시군구'] == ' 서울특별시 강남구 신사동')]
print(result)


result= df.loc[(df['시군구'] == '서울특별시 강남구 신사동') & (df['단지명'] == '상지')]

newdf= df.set_index(keys=['도로명'])
print(newdf)

#[[]] 인덱스가 레이블일때는 괄호 [[]]를 쓴다(?)
result= newdf.loc[['동일로']]
print(result)
##리스트를 뽑고 카운트를 해라.
# count=newdf.loc[['동일로']].count()
# count = result.count()
count=len(newdf.loc['동일로'])
count = result.size
print(result)
print(count)