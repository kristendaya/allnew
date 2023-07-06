from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # 도시와 기온 데이터
    cities = ['Tokyo', 'Seoul', 'New York']
    temperatures = {
        'Tokyo': [9.2, 9.7, 11.9, 16.2, 20.4, 23.9, 27.6, 29.2, 25.9, 20.8, 15.2, 11.2],
        'Seoul': [1.0, 2.6, 7.6, 13.7, 18.6, 22.5, 25.8, 27.6, 22.7, 16.4, 9.2, 3.8],
        'New York': [2.8, 3.6, 6.2, 12.2, 17.8, 23.3, 26.7, 25.8, 21.1, 14.5, 8.9, 4.0]
    }
    
    # 그래프 생성
    months = range(1, 13)
    plt.plot(months, temperatures['Tokyo'], label='Tokyo')
    plt.plot(months, temperatures['Seoul'], label='Seoul')
    plt.plot(months, temperatures['New York'], label='New York')
    plt.xlabel('Month')
    plt.ylabel('Temperature (°C)')
    plt.title('Yearly Temperature Comparison')
    plt.legend()

    # 그래프를 이미지로 저장
    graph_path = 'static/graph.png'
    plt.savefig(graph_path)
    plt.close()

    return render_template('index.html', cities=cities, graph_path=graph_path)

if __name__ == '__main__':
    app.run