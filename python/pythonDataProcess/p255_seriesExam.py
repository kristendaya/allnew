from pandas import Series
import matplotlib.pyplot as plt

plt.rc('font', family='malgun Gothic')

myindex = ['강감찬', '홍길동', '이순신', '최영']
member = Series(data=[20, 60, 80, 40], index=myindex)
print(member)
print('-' * 50)

print('# values 속성을 이용 요소들의 값 확인')
print(member.values)
print('-' * 50)

print('# index 속성을 이용 색인 객체를 확인')
print(member.index)
print('-' * 50)

member.plot(kind='bar', rot=40, ylim=[0, member.max() + 20], use_index=True, grid=False, table=False, color=['r', 'g', 'b', 'y'])
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.title('학생별 시험 점수')

ratio = 100 * member / member.sum()
print(ratio)
print('-' * 50)

for idx in range(member.size):
    value = str(member[idx]) + '건'
    # 그래프 위에 "건수"표시
    ratioval = '%.1f%%' % (ratio[idx])
    # 그래프 중간에 비율 표시
    plt.text(x=idx, y=member[idx] + 1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=member[idx] + 2, s=ratioval, horizontalalignment='center')
#평균값을 수평선으로 그리기
meanval = member.mean()
print(meanval)
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
plt.text(x=0 + 1, y=meanval, s=average, horizontalalignment='center')

filename = 'graph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + 'Saved...')
plt.show()