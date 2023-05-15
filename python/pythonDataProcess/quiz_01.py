import pandas as pd
from pandas import DataFrame as dp
import numpy as np
from bs4 import BeautifulSoup

html = open("ex5-10.html", "r", encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")

result = []
tbody = soup.find("tbody")
tds = tbody.findAll('td')
for data in tds:
    result.append(data.text)
print(result)
print('-' * 50)

mydata = np.array(result)
reshapedata = mydata.reshape(4, 3)
print(reshapedata)
print('-' * 50)

myframe = pd.DataFrame(reshapedata, columns=['이름', '국어', '영어'])
print(myframe)
print('-' * 50)

df = myframe
newdf = df.set_index(keys=['이름'])
print(newdf)
print('#' * 50)

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'malgun gothic'
newdf = newdf.astype(float)


newdf.index.name = '이름'
newdf.columns.name = '시험 과목'

newdf.plot(kind='line', rot=0, title = '영어국어점수', legend=True)
filename ='dataframeGraph_quiz01.png'
plt.savefig(filename, dpi = 400, bbox_inches='tight')
print(filename + '...saved')
plt.show()