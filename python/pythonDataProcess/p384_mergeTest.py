import pandas as pd

mystorefile = 'store.csv'
mystore=pd.read_csv(mystorefile, encoding='utf-8', index_col=0, header=0)
print('\매장테이블')
print('mystore')

districtfile = 'districtmini.csv'
district =pd.read_csv(districtfile, encoding='utf-8', index_col=0, header=0)
print('\n행정구역 테이블')
print('mystore')

result = pd.merge(mystore,district, on=['sido','gungu'], how= 'outer', suffixes=['','_'],indicator=True)
###빈공간에 붙는다. outer는 합집합 inner 교집합, merge 어디에 존재하는지 보여주는거! 칼럼을 하나 더 만들어서 보여주는거 .

print('\nMerge Result')
print(result)

m_result=result.query('_merge == "left_only"')
print('\n좌측에만 있는 행')
print(m_result)

gungufile= open('gungufile.txt', encoding='utf-8')
gungu_list = gungufile.readlines()

gungu_dict={}
for onegu in gungu_list:
    mydata=onegu.replace('\n','').split(':')
    gungu_dict[mydata[0]]= mydata[1]
print('\n군구사전내용')
#그냥 만들기만한거임
print(gungu_dict)

#바꾸는작업
mystore.gungu= mystore.gungu.apply(lambda data : gungu_dict.get(data,data))
#data= '진해시' 였는데 apply는 하나하나 적용시켜줌. get 키값이 있으면 밸류를 갖고오고 아니면 data값을 그대로 넣는다.

print('\n수정된 가게 정보 츨력')
print(mystore)
