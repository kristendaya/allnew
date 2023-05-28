from fastapi import FastAPI
from pydantic import BaseModel
import data

app = FastAPI()

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/get_data')
async def get_data():
    return data.get_data()