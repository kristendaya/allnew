import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import os.path
#datatime 그냥써도 되는데 한번더 임포트 해주셨음

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

url = 'https://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'

today= (datetime.today()- timedelta(1)).strftime("%Y%m%d") #이전날짜 열두시
print(today)

params = '?serviceKey=' + get_secret("data_apiKey")
params += '&pageNo=1'
params += '&numOfRows=500'
params += '&apiType=JSON'
params += '&status_dt=' + str(today)

url += params
print(url) #제대로 가져왔는지 확인

response = requests.get(url)
print(response)
print('-' * 50)

contents = response.text
print(type(contents))
print(contents)
print('-'*50)

dict = json.loads(contents)
print(type(dict))
print(dict)
print('#'*50)

items = dict['items']
print(type(items))
print(items)
print('#'*50)

df = pd.DataFrame(items).rename(index={0:'result'}).T
print(type(df))
print(df)
print('-'* 50)
##items 로 바꾸는 이유는 키와 밸류값을 자유자재로 쓰기 위해서임.
##dictionary를 쓰면 key값 만 갖고오게 되잖아. 

data = df.loc[df['국적별'] == '말레이시아']
print(type(data))
print(data)
print('-' * 50)