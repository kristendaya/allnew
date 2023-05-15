import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')

text = myfile.read()

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-' * 40)

bindo = wordcloud.words_
print(type(bindo))
print('-' * 40)

sortedData = sorted(bindo.items(), key=lambda x : x[1], reverse=True)
print(sortedData)
print('#' * 40)

chartData = sortedData[0:10]
print(chartData)
print('-' * 40)

xtick = []
chart = []
for item in chartData:
    xtick.append(item[0])
    chart.append(item[1])

mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#fff0f0', '#ccffbb', '#05ccff', '#11ccff']
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 Top10')
filename = 'wordCloudEx01_01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')

plt.figure(figsize=(20, 20))
plt.imshow(wordcloud)
plt.axis('off')

filename = 'wordCloudEx01_02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + ' file saved...')
plt.show()