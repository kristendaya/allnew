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

@app.get('/graph_data_by_date')
async def getDatebytime(start, end):
    myframe = mycol.find({},{"_id":0})
    # frame = list(myframe)
    df = pd.DataFrame(myframe)
    df = df.set_index("국적별")
    # df.drop(["_id"] , axis = 1, inplace = True)
    # print(df.index)
    df = df.loc[:, start : end]
    df = df.reset_index()
    # return df
    js = df.to_dict(orient="records")
    # return js
    ##얘를 보내는구나

# df = getDatebytime("2017년06월" , "2017년09월")
# print(df.head())
# js = df.to_dict(orient="records")
# print(js[:5])
# return {"filename": filename, "data": js}
# def create_bar_plot(df):
    labels = df['국적별']
    data = df.loc[:, df.columns != '국적별']
    filename = "graph1_data_by_date"
    fig, ax = plt.subplots(figsize=(10,8))
    ax.barh(labels, data.sum(axis=1), color='dodgerblue')
    
    ax.set_xlabel('방문자수')
    ax.set_ylabel('국적별')
    ax.tick_params(axis= "y", labelsize=5)
    

    start_month = df.columns[1]
    end_month = df.columns[-1]
    title = f'{start}부터 {end}까지 입국자수의 합'    
    ax.set_title(title)
    plt.savefig(filename, dpi=800, bbox_inches= None)
    plt.xticks(rotation=40, ha='right')
    # plt.yticks(fontsize=10)  # y축 라벨의 글자 크기 조절

    plt.show()
    return {"filename": filename, "data": js}

# start_month = "2017년06월"
# end_month = "2017년09월"
# df = getDatebytime(start_month, end_month)

# 그래프 생성
# create_bar_plot(df)

# ###################### 날짜/국가##########################
# @app.get('/graph_date_and_country')
# async def get_data_for_country(country, start, end):
#     myframe = mycol.find({},{"_id":0})
#     df = pd.DataFrame(myframe)
#     df = df.set_index("국적별")
#     df = df.loc[:, start : end]
#     df = df.reset_index()
#     # js = df.to_dict(orient="records")
#     labels = df['국적별']
#     # data = df.loc[:, df.columns != '국적별']
#     filename = "graph2_data_by_date"

# # def create_bar_plot_for_country(df):
#     labels = df.columns[1:]
#     data = df.iloc[0, 1:]
#     filename = "graph2_date_and_country"

#     fig, ax = plt.subplots(figsize=(10, 5))
#     width = 0.8
#     ax.bar(labels, data, color='dodgerblue', width=width)

#     ax.set_ylabel('방문자 수')
#     ax.set_xlabel('날짜')

#     country = df.iloc[0, 0]
#     title = f'{country}의 월별 방문자 수'
#     ax.set_title(title)

#     plt.xticks(rotation=45, ha='right')
#     plt.savefig(filename,dpi=800, bbox_inches= None)

# # 데이터 가져오기
# start_month = "2017년06월"
# end_month = "2017년09월"
# country = "일  본"
# df = get_data_for_country(country, start_month, end_month)

# # 그래프 생성
# create_bar_plot_for_country(df)

#################국가별#################
@app.get('/graph_by_country')
def get_all_dates_data(country):
    myframe = mycol.find({}, {"_id": 0})
    df = pd.DataFrame(myframe)
    df = df.set_index("국적별")
    df = df.reset_index()
    
# def create_bar_plot_for_country_all_dates(df):
    labels = df.columns[1:-1]
    data = df.iloc[0, 1:-1]
    filename= 'graph3_country'
    fig, ax = plt.subplots(figsize=(10, 5))
    width = 0.8
    ax.bar(labels, data, color='dodgerblue', width=width)

    ax.set_ylabel('방문자 수')
    ax.set_xlabel('날짜')
    ax.tick_params(axis= "x", labelsize=5)

    country = df.iloc[0, 0]
    title = f'{country}의 전체 기간 동안 월별 방문자 수'
    ax.set_title(title)
    
    plt.xticks(rotation=45, ha='right')
    plt.savefig(filename,dpi=800,bbox_inches="tight")
    plt.show()

# def get_data_for_country_all_dates(country):
    df = get_all_dates_data()
    country_data = df[df['국적별'] == country]
    return {"filename": filename}


# 데이터 가져오기
# country = "일  본"
# df = get_data_for_country_all_dates(country)

# 그래프 생성
# create_bar_plot_for_country_all_dates(df)

