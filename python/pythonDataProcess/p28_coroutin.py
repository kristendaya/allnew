def handler():
    print("initialize Handler")
    while True:
        # v1, v2 = (yield )
        # print(f"{v1} + {v2} = {v1+v2}")
        #
        value = (yield )
        print("%s + %s = %d" % (value[0], value[1], value[0]+value[1]))

listener = handler()
listener.__next__()
#yield를 찾을때까지 도는애.
listener.send([4,5])
listener.send("message")

#값을 주면 대답해주라.


