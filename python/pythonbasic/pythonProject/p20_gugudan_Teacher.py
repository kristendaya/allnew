while True:
    n=input("input number(q: quit): ")

    if(n=='q'):
        print("Exit")
        break

    n = int(n)

        if(n<2 or n > 9):
            print("input number range 2~9!")
            continue;
        else:
            for c in range(1,10)
