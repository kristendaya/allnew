from flask import Flask, render_template

app = Flask(__name__)

# 정적 파일 디렉토리 설정
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
