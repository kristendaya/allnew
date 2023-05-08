while True:
    i = input("Input the number (q : Quit) : ")

    if i == 'q':
        break
    else:
        #그냥 정수로 지정할게~ 캐스팅!
        if int(i) >0:
            print("This is positive")
        elif int (i) == 0:
            print("This is zero")
        else:
            print("this is negative")



