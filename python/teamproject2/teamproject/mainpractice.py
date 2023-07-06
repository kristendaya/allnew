import requests
import json
import os.path
import pydantic
from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from typing import List
from collections import Counter


pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, './../secret.json')

app = FastAPI()
URL = "http://192.168.1.10:5000/months"

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")
# to connect mongodb
# client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
# print('Connected to Mongodb....')
HOSTNAME = get_secret("Ubuntu_Hostname")
client = mongo_client.MongoClient(HOSTNAME)
print('Connected to Mongodb....')


mydb = client['project']
mycol = mydb['importdb']

# to insert data to mongodb 
@app.get('/get_data')
def get_data():
    response = requests.get(URL)
    contents = response.text
    dict = json.loads(contents)
    # response = requests.get(URL)
    # data = response.json()
    # mycol.insert_many(data)
    mycol.insert_many(dict)
    return dict
 
    #  mycol.delete_many({})

#http://localhost:8000/get_data_by_date?year=2023&month=3
# 날짜별 데이터 조회 및 그래프 생성

@app.get("/get_data_by_date")
# start_year = int(input("startyear"))
# start_month = int(input("startmonths"))
# end_year=int(input("endyear"))

def get_data_by_date(start_year: int, start_month: int, end_year: int, end_month: int):
    # 유효성 검사: 입력된 월 값이 1에서 12 사이인지 확인
    if not (1 <= start_month <= 12) or not (1 <= end_month <= 12):
        return {"message": "Invalid month value. Month should be between 1 and 12."}

    query = {}

    if start_year == end_year:
        # 시작 연도와 종료 연도가 동일한 경우
        months = [f"{start_year}년{month:02d}월" for month in range(start_month, end_month + 1)]
        query["$and"] = [{month: {"$exists": True}} for month in months]
    else:
        # 시작 연도와 종료 연도가 다른 경우
        start_months = [f"{start_year}년{month:02d}월" for month in range(start_month, 13)]
        end_months = [f"{end_year}년{month:02d}월" for month in range(1, end_month + 1)]
        query["$or"] = [{month: {"$exists": True}} for month in start_months + end_months]
        
#### query["$or"]를 사용하여 MongoDB에서 여러 개의 조건을 OR 연산으로 검색
    projection = {"_id": 0}  # 필요한 경우 필드 제한 
    # projection means selecting only the necessary data rather than selecting whole of the data of a document. 
    result = mycol.find(query, projection)
    data = list(result)

    if len(data) == 0:
        return {"message": "No data found for the given date range."}

    # 데이터를 데이터프레임으로 변환하여 반환
    df = pd.DataFrame(data)
    df = df.applymap(str)  # numpy int64 타입을 문자열로 변환

    # 그래프 생성
    countries = df["국적별"].tolist()
    months = [f"{year}년{month:02d}월" for year in range(start_year, end_year + 1) for month in range(1, 13)]
    values = [sum(df[month].astype(int)) for month in months]
    #to confirm the result
    # result_dict = {"countries": countries, "values": values}
    # return result_dict
    #****d = deci *****

    plt.bar(months, values)
    plt.xlabel("Month")
    plt.ylabel("Total Visitors")
    plt.title("Total Visitors by Month")
    plt.xticks(rotation=90)

    # 그래프를 이미지로 변환
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    # 이미지를 base64로 인코딩하여 반환
    encoded_image = base64.b64encode(buffer.read()).decode("utf-8")

    return {"image": encoded_image}

    # plt.close()  # 그래프를 닫음

    return {"image_data": image_data}