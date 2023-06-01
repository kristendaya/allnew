import requests
import json
import os.path
import pydantic
from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import pandas as pd
import io
import base64
from typing import List
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family'] = 'AppleGothic'

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

# to connect mongodb
# client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
# print('Connected to Mongodb....')
HOSTNAME = get_secret("Ubuntu_Hostname")
client = mongo_client.MongoClient(HOSTNAME)
mydb = client['project']
mycol = mydb['importdb']

def getDatebytime(start, end):
    myframe = mycol.find({},{"_id":0})
    # frame = list(myframe)
    df = pd.DataFrame(myframe)
    df = df.set_index("국적별")
    # df.drop(["_id"] , axis = 1, inplace = True)
    # print(df.index)
    df = df.loc[:, start : end]
    df = df.reset_index()
    return df

df = getDatebytime("2017년06월" , "2017년09월")
print(df.head())

js = df.to_dict(orient="records")
print(js[:5])


def create_bar_plot(df):
    labels = df['국적별']
    data = df.loc[:, df.columns != '국적별']
    filename = "xxxxtourist3"
    fig, ax = plt.subplots(figsize=(10,8))
    ax.barh(labels, data.sum(axis=1), color='dodgerblue')
    
    ax.set_xlabel('방문자수')
    ax.set_ylabel('국적별')
    ax.tick_params(axis= "y", labelsize=5)
    

    start_month = df.columns[1]
    end_month = df.columns[-1]
    title = f'{start_month}부터 {end_month}까지 입국자수의 합'    
    ax.set_title(title)
    plt.savefig(filename, dpi=800, bbox_inches= None)
    plt.xticks(rotation=40, ha='right')
    # plt.yticks(fontsize=10)  # y축 라벨의 글자 크기 조절

    # plt.show()

# start_month = "2017년06월"
# end_month = "2017년09월"
# df = getDatebytime(start_month, end_month)

# 그래프 생성
# create_bar_plot(df)


# # to insert data to mongodb 
# @app.get('/get_data')
# async def get_data():
#     response = requests.get(URL)
#     contents = response.text
#     dict = json.loads(contents)
#     # response = requests.get(URL)
#     # data = response.json()
#     # mycol.insert_many(data)
#     mycol.insert_many(dict)
#     return dict

    #  mycol.delete_many({})




#http://localhost:8000/get_data_by_date?year=2023&month=3
# 날짜별 데이터 조회 및 그래프 생성

@app.get("/get_data_by_date")
# start_year = int(input("startyear"))
# start_month = int(input("startmonths"))
# end_year=int(input("endyear"))

async def get_data_by_date(start_year: int, start_month: int, end_year: int, end_month: int):
    if not (1 <= start_month <= 12) or not (1 <= end_month <= 12):
        return {"message": "Invalid month value. Month should be between 1 and 12."}

    query = {}

    if start_year == end_year:
        # 시작 연도와 종료 연도가 동일한 경우 / d= deci
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
    filename='graph2.png'

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
    result_dict = {"countries": countries, "values": values}
    return result_dict


    #****d = deci *****

#     plt.bar(months, values)
#     plt.xlabel("Month")
#     plt.ylabel("Total Visitors")
#     plt.title("Total Visitors by Month")
#     plt.xticks(rotation=90)

#     plt.savefig(filename, dpi=400, bbox_inches='tight' )

#     return {filename}

#     # image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

#     # return {"graph_image": image_base64, "data": json.loads(df.to_json(orient="records", default_handler=str))}


# # GET /get_most_10countries?start_year=2018&start_month=10&end_year=2018&end_month=12
# @app.get("/get_most_10countries")
# async def get_most_10countries(start_year: int, start_month: int, end_year: int, end_month: int) 
# #confirm month
#     if not (1 <= start_month <= 12) or not (1 <= end_month <= 12):
#         return {"message": "Invalid month value. Month should be between 1 and 12."}

#     query = {}

#     if start_year == end_year:
#         # 시작 연도와 종료 연도가 동일한 경우
#         months = [f"{start_year}년{month:02d}월" for month in range(start_month, end_month + 1)]
#         query["$and"] = [{month: {"$exists": True}} for month in months]
#     else:
#         # 시작 연도와 종료 연도가 다른 경우
#         start_months = [f"{start_year}년{month:02d}월" for month in range(start_month, 13)]
#         end_months = [f"{end_year}년{month:02d}월" for month in range(1, end_month + 1)]
#         query["$or"] = [{month: {"$exists": True}} for month in start_months + end_months]

#     projection = {"_id": 0}  # 필요한 경우 필드 제한
#     result = mycol.find(query, projection)
#     data = list(result)

#     if len(data) == 0:
#         return {"message": "No data found for the given date range."}

#     # 데이터를 데이터프레임으로 변환하여 처리
#     df = pd.DataFrame(data)
#     df = df.applymap(str)  # numpy int64 타입을 문자열로 변환

#     # 월별로 가장 많이 방문한 국가 10개를 구함
#     countries = df["국적별"].tolist()
#     months = [f"{year}년{month:02d}월" for year in range(start_year, end_year + 1) for month in range(1, 13)]
#     counts = Counter([country for month in months for country in df[month].tolist()])
#     most_common_countries = [country for country, count in counts.most_common(10)]

#     return most_common_countries


# @app.get("/get_most_10countries")
# def get_most_10countries():
#     pipeline = [
#         {"$match": {"국적별": {"$exists": True}}},
#         {"$group": {"_id": "$국적별", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 10}
#     ]

#     result = mycol.aggregate(pipeline)
#     data = list(result)

#     if len(data) == 0:
#         return {"message": "No data found."}

#     countries = [item["_id"] for item in data]
#     counts = [item["count"] for item in data]

#     return {"countries": countries, "counts": counts}


@app.get('/dropdata')
def dropdata():
    mycol.drop()
    return {"Data has been dropped"}

