import random

class BinaryConverter:
    def __init__(self, x):
        self.x = x

    def convertbinary(self):
        temp = []
        while True:
            remain = self.x % 2
            self.x = self.x // 2
            temp.append(remain)

            if self.x < 2:
                temp.append(self.x)
                break
        temp.reverse()
        ## temp 라는 리스트한테 reverse 해!! 초창기만들어진 함수들은 원본을 변경함.
        return temp
        # 원본이 뭉게지지만 하나의 공간을 같이쓰니까 공간효율성이 좋음
        #코드테스트 
        #공간 복잡도를 reversed를 쓰먼 안됨.
    ## list는 return이 안됨.
        # return 0  ## reversed를 쓰면 공간을 만들어줌.
        #클라우드리 소스를 쓰니까 작게 최적화를 ....

x=random.randint(4,16)
n=BinaryConverter(x)
print(f'{x}={n.convertbinary()}')