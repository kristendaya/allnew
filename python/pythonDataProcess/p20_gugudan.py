while True:
    n = input("input number(q: quit):")
    if ('q' == n):
        break;
    elif i < 2 or i > 9:
     print('{input number range 2~9!!}')

    else:
        for i in range(1, 10):
            print(f'{n} * {i}  ={n * i}')
        break