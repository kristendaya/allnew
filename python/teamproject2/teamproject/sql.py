import pandas as pd 
from sqlalchemy import create_engine, text
from PIL import Image
import base64
from io import BytesIO
from typing import List
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os.path
import json

app = FastAPI()

os.makedirs("./images", exist_ok=True)
app.mount("/images", StaticFiles(directory="./images"), name='images')

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

# “/”로 접근할 때 보여줄 HTML 코드 (가장 기본적으로 보여지는 부분)
@app.get("/")
async def main():
    content = """
        <head>
        <script>
            function getImagesList() {
                const xhr = new XMLHttpRequest();
                const method = "GET";
                const url = "/selectImages";
                xhr.open(method, url);
                xhr.setRequestHeader("content-type", "application/json");
                xhr.send();

                xhr.onload = () => {
                    if (xhr.status === 200) {
                        const res = JSON.parse(xhr.response);
                        console.log(res);
                        const element1 = document.getElementById("ss1");
                        element1.innerHTML = JSON.stringify(res);
                        const element2 = document.getElementById("ss2");
                        element2.innerHTML = "";
                        var imgList = document.getElementById('imgSelect');
                        imgList.innerHTML = "";
                        for (var i = 0; i < res.length; i++) {
                            val = res[i]['filename']
                            console.log(val)
                            var option = document.createElement('option')
                            option.innerHTML = val;
                            imgList.append(option)
                        }
                    } else {
                        console.log("HTTP error", xhr.status, xhr.statusText);
                    }
                };
            }

            function showImage() {
                const inputVal = document.getElementById("imgSelect").value;
                const element = document.getElementById("ss2");
                if (inputVal == "") 
                    var tag = '<h4>Select Image DB 버튼을 누르세요.</h4>';
                else
                    var tag = '<img src="/images/' + inputVal +  '">';
                element.innerHTML = tag;
            }
        </script>
        </head>
        <body>
        <h3>Image File Upload to MySQL DB</h3>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        <hr />
        <input type="button" value="Select Image DB" onclick="getImagesList()">
        <div id="section1" style="margin-top: 20px;">
         <span id="ss1"></span>
        </div>
        <hr />
        <select id="imgSelect" style="width=100px">
        <input type="button" value="Show Image" onclick="showImage()">
        <div id="section2" style="margin-top: 20px;">
         <span id="ss2"></span>
        </div>
        </form>
        </body>
    """
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3000)

@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    UPLOAD_DIRECTORY = "./images"
    for file in files:
        contents = await file.read()
        with open(os.path.join(UPLOAD_DIRECTORY, file.filename), "wb") as fp:
            fp.write(contents)

    filename = [file.filename for file in files]
    print({"filename": filename})  

    result = InsertImageDB(filename[0])
    return result
  
@app.get('/selectImages')
async def selectImages():
    result = SelectImageDB()
    return result

    