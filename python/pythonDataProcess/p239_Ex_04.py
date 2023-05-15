from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family']= "Malgun Gothic"

mylist = [30, 20, 40, 60, 50]
myindex = ['이상화','한용운','노천명','윤동주','이육사']

print(myindex)
print(mylist)
print('-' * 50)

myseries = Series(data =mylist, index= myindex)
myylim=[0, myseries.max() + 10]
myseries.plot(title= "금월실적", kind= 'line', ylim = myylim, grid = False, rot =10, use_index =True)
##rot 눈금
filename= 'p249_seriesGrapgh02.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+ 'saved...')
plt.show()