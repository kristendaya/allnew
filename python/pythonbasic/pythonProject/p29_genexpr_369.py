# tsn = [str(i) if set(['3', '6', '9']).isdisjoint(set(list(str(i))))
#        else '👏'
#        for i in range(1, 101)]
#
# print(tsn)

##1부터 10 / 두자리수 /
for i in range(1, 101):
    if i < 10:
        if i in (3, 6, 9):
            print("짝")
        else:
            print(i)
    else:
        i = str(i)
        if i[0] in ['3', '6', '9'] and i[1] in ['3', '6', '9']:
            print("짝짝")
        elif i[0] in ['3', '6', '9'] or i[1] in ['3', '6', '9']:
            print("짝")
        else:
            print(i)


