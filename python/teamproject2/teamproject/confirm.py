import requests
import json
import os.path
import pydantic
from fastapi import FastAPI, File, UploadFile
from pymongo import mongo_client
from bson.objectid import ObjectId
import pandas as pd
import io
import base64
from typing import List
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine, text
from PIL import Image
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

plt.rcParams['font.family'] = 'AppleGothic'

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

os.makedirs("./images", exist_ok=True)
app.mount("/images", StaticFiles(directory="./images"), name='images')

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


HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}'

engine = create_engine(DB_URL, pool_recycle=500)


def InsertImageDB(filename):
    os.chdir('./images')
## jpg dpi 100x100, png dpi 72x72
    with open(filename, "rb") as image_file:
        binary_image = image_file.read()
        binary_image = base64.b64encode(binary_image)
        binary_image = binary_image.decode('UTF-8')
        img_df = pd.DataFrame({'filename':filename,'image_data':[binary_image]})
        img_df.to_sql('images', con=engine, if_exists='append', index=False)
    os.chdir('../')
    return f'Image file : {filename} Inserted~!!'

def SelectImageDB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from images"))
        resultDict = []
        for row in result:
            resultDict.append({"id" : row.id, "filename":row.filename})
        print(resultDict)
    return resultDict


@app.get('/dropdata')
def dropdata():
    mycol.drop()
    return {"Data has been dropped"}

# to insert data to mongodb 
@app.get('/insert_data')
async def insert_data():
    response = requests.get(URL)
    contents = response.text
    dict = json.loads(contents)
    # response = requests.get(URL)
    # data = response.json()
    # mycol.insert_many(data)
    mycol.insert_many(dict)
    mycol.find_one({})
    return {"ok": True}


def getDatebytime(start, end):
    myframe = mycol.find({},{"_id":0})
    df = pd.DataFrame(myframe)
    df = df.set_index("국적별")
    df = df.loc[:, start : end]
    df = df.reset_index()    
    return df

@app.get('/getdata')
async def getdata(start, end):
    df = getDatebytime(start,end)
    js = df.to_dict(orient="records")
    return js





@app.get('/graph_data_by_date')
async def graph_data_by_date(start:str,end:str):
    # print(start,end)
    df = getDatebytime(start, end)
    print(df)
    labels = df['국적별']
    data = df.loc[:, df.columns != '국적별']
    filename = "graph1_data_by_date.png"

    fig, ax = plt.subplots(figsize=(10,8))
    ax.barh(labels, data.sum(axis=1), color='dodgerblue')
    
    ax.set_xlabel('방문자수')
    ax.set_ylabel('국적별')
    ax.tick_params(axis= "y", labelsize=5)
    

    start = df.columns[1]
    end = df.columns[-1]
    title = f'{start}부터 {end}까지 입국자수의 합'    
    ax.set_title(title)
    plt.savefig(f"./node/public/{filename}", dpi=200, bbox_inches= None)
    plt.xticks(rotation=40, ha='right')
    # plt.yticks(fontsize=10)  # y축 라벨의 글자 크기 조절
    pic= InsertImageDB(filename)

    return {"filename": filename}

#################국가별#################

def get_data_by_nationality(nationality: str):
    myframe = mycol.find({"국적별": nationality}, {"_id": 0})
    df2 = pd.DataFrame(myframe)
    return df2

#http://192.168.1.10:3000/get_gra_by_nationality?nationality=%EB%A7%90%EB%A0%88%EC%9D%B4%EC%8B%9C%EC%95%84
@app.get('/get_gra_by_nationality')
def create_nationality_graph(nationality: str):
    df = get_data_by_nationality(nationality)
    df = df.set_index("국적별")
    df = df.drop("계", axis=1)  # "계" 열 제거
    labels = df.columns[:]
    data = df.iloc[0, :]

    filename = "nationalitygraph.png"

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.bar(labels, data, color='dodgerblue')

    ax.set_xlabel('기간')
    ax.set_xticklabels(labels, rotation=40, ha='right')
    ax.set_title(f'{nationality} 입국자수')
    ax.tick_params(axis= "x", labelsize=5)    

    plt.savefig(f"./node/public/{filename}", dpi=200, bbox_inches='tight')
    plt.show()
    return {"filename": filename}
    


# 빼고싶은 국가목록! 이거를 IS IN 해서 쓰자~ 
exclude_list = ["전 체", "아시아주", "미 주", "구 주", "기 타", "교포", "아프리가주", "기타","아시아주 기타"]
def get_top(df):
    sorted_df = df.sort_values(ascending=False)
    top_countries = sorted_df.head(20)
    return top_countries

def filter_countries(df, exclude_list):
    #     return df[~df['국적별'].isin(exclude_list)] ~:not을 의미함(반전)
    return df[df['국적별'].apply(lambda x: x not in exclude_list)]

@app.get('/get_top')
async def get_top_countries(start: str, end: str):
    df = getDatebytime(start, end)
    filtered_df = filter_countries(df, exclude_list)
    total_visitors = filtered_df.set_index("국적별").sum(axis=1)
    top = get_top(total_visitors)
    
    filename = "most_countries.png"

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(top.index, top.values, color='dodgerblue')

    ax.set_xlabel('방문자수')
    ax.set_ylabel('국적별')
    ax.set_title(f'Top 10 Countries ({start} - {end})')
    ax.tick_params(axis="y", labelsize=8)

    plt.savefig(f"./node/public/{filename}", dpi=200, bbox_inches='tight')
    plt.close(fig)

    # return {"filename": filename}

    return {
        'date_range': f"{start} - {end}",
        "filename": filename,
        # 'visitors_data': filtered_df.to_dict(orient='records'),
        'top_countries': top.to_dict()
    }

    


    