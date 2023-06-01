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
import matplotlib.pyplot as plt

plt.rcParams['font.family']= 'malgun gothic'

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
async def get_data():
    response = requests.get(URL)
    contents = response.text
    dict = json.loads(contents)
    # response = requests.get(URL)
    # data = response.json()
    # mycol.insert_many(data)
    mycol.insert_many(dict)
    return dict


#http://localhost:8000/get_data_by_date?start_year=2017&start_month=1&end_year=2017&end_month=3

@app.get('/get_data_by_date')
async def get_data_by_date(start_year: int, start_month: int, end_year: int, end_month: int):
    if not (1 <= start_month <= 12) or not (1 <= end_month <= 12):
        return {"message": "Invalid month value. Month should be between 1 and 12."}

    start_date = f"{start_year}년{start_month:02d}월"
    end_date = f"{end_year}년{end_month:02d}월"

    query = {"$and": [{"계": {"$exists": True}}]}
    projection = {"_id": 0, "국적별": 1}

    for year in range(start_year, end_year + 1):
        if year == start_year:
            start_month_range = range(start_month, 13)
        elif year == end_year:
            start_month_range = range(1, end_month + 1)
        else:
            start_month_range = range(1, 13)

        for month in start_month_range:
            date = f"{year}년{month:02d}월"
            projection[date] = 1         

    projection["국적별"] = 1  # 국적별 필드를 projection에 추가

    result = mycol.find(query, projection)
    data = list(result)
    filename="tourgraph"

    if len(data) == 0:
        return {"message": "No data found for the given date range."}

    filtered_data = []
    for item in data:
        filtered_item = {key: value for key, value in item.items() if key in projection and start_date <= key <= end_date}
        filtered_data.append(filtered_item)

    return filtered_data

@app.get('/generate_graph')
async def generate_graph(start_year: int, start_month: int, end_year: int, end_month: int):
    if not (1 <= start_month <= 12) or not (1 <= end_month <= 12):
        return {"message": "Invalid month value. Month should be between 1 and 12."}

    start_date = f"{start_year}년{start_month:02d}월"
    end_date = f"{end_year}년{end_month:02d}월"

    query = {"$and": [{"계": {"$exists": True}}]}
    projection = {"_id": 0, "국적별": 1}

    for year in range(start_year, end_year + 1):
        if year == start_year:
            start_month_range = range(start_month, 13)
        elif year == end_year:
            start_month_range = range(1, end_month + 1)
        else:
            start_month_range = range(1, 13)

        for month in start_month_range:
            date = f"{year}년{month:02d}월"
            projection[date] = 1

    projection["국적별"] = 1  # 국적별 필드를 projection에 추가

    result = mycol.find(query, projection)
    data = list(result)
    filename='xxxxxgraph2.png'

    if len(data) == 0:
        return {"message": "No data found for the given date range."}



    # filtered_data = []
    # for item in data:
        
    #     filtered_item = {key: value for key, value in item.items() if key in projection and start_date <= key <= end_date}
    #     filtered_data.append(filtered_item)

    # if len(filtered_data) == 0:
    #     return {"message": "No data found with '국적별' key for the given date range."}

    # # 그래프 생성
    # plt.figure(figsize=(10, 6))
    # x_values = list(projection.keys())[1:]  # 월별 날짜

    # for item in filtered_data:
    #     y_values = list(item.values())[1:]  # 월별 데이터 값
    #     plt.plot(x_values, y_values, label=item["국적별"])

    # # 그래프 설정 및 국적명 표기
    # plt.title("월별 데이터 추이")
    # plt.xlabel("날짜")
    # plt.ylabel("데이터 값")
    # plt.legend()
    # plt.xticks(rotation=45)

    # for item in filtered_data:
    #     y_values = list(item.values())[1:]  # 월별 데이터 값
    #     for j, y_value in enumerate(y_values):
    #         plt.text(j, y_value, item["국적별"], ha='center', va='bottom')

 
    # plt.savefig(filename, dpi=400, bbox_inches='tight' )

    # return {'filename'}
    
       