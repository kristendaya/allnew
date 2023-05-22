import requests
import pandas as pd
import os.path
import timedelta
from fastapi import FastAPI
import pymongo

df = pd.read_csv('data.csv')

def MongoInsert()
    pass

app = FastAPI()

@app.get('/mongoinsert')
def mongoinsert()
    result = MongoInsert(getAPI())
    return result

