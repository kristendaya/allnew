import requests
import json
import pandas as pd 
import os.path
from pymongo import mongo_client
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, './secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read()) 


app = FastAPI()
url="http://192.168.1.10:5000/countries"



res=requests.get(url)
print(res.text)
print(type(res.text))
print('-' * 50)

dict = json.loads(res.text)
print(type(dict))
print(dict)
print('-' * 50)
##리스트가됨 
#파싱은 구문분석해서 알맞는 형태로 바꿔서 주는것.
#리스트객체이면서 딕셔너리로 쓸수있는 데이터가 된거임.이전까지는 그냥 문자열에 불과.

df = pd.DataFrame(dict)
# print(df.values)
print(df.head())
print(df.columns)
# print(df.T)

# data = df.
# data = df.loc[df['아시아주']]
# data = df[['countries']]
# print(type(data))
print(data)
# print('-' * 50)


# 사용자로부터 검색할 국적과 선택할 열 인덱스(숫자)를 입력받습니다.
country = input("검색할 국적을 입력하세요: ")
column_index = int(input("선택할 열 인덱스를 입력하세요: "))

# '국적별' 열을 기준으로 입력한 국적을 검색하고, 선택한 열 인덱스로 데이터를 가져옵니다.
data = df.loc[df['국적별'] == country, df.columns[column_index]]

print(data)

Data= df.set_index(keys="국적별").T
print(Data)
Data= Data.reset_index()
print(Data.to_dict)


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("Ubuntu_Hostname")



client = mongo_client.MongoClient(HOSTNAME)
print('Connected to Mongodb....')

mydb = client['test']
mycol = mydb['traveler']

mycol.delete_many({})
mycol.insert_many(dict)

# print(mycol.find()) #이건 오브젝트 그 자체
print(list(mycol.find()))


