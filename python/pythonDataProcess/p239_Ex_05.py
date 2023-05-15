import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family']= "Malgun Gothic"
filename= 'ex802.csv'

myframe =pd.read_csv(filename,index_col='type',encoding='utf-8')
myframe.plot(kind='line',rot=0,title="지역별 차종교통량", legend=True)

filename= 'p249_seriesGrapgh02.pngg'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+ 'saved...')
plt.show()