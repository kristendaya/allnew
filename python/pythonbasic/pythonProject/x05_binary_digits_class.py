# num = int(input("10진수입력:"))
#
# alist = []
# while num!=0:
#     alist.append(num % 2)
# num = num // 2
#
# alist.reverse()
#
# print(alist)


# def convert2binary(num)
#     temp= []
#
#     while True:
#         remain = num %2
#         num = num //2
#         temp.append(remain)
#
#         if num < 2 :
#             temp.append(num)
#             break
#
#             temp.reverse()
#             result = "".join(map(str, temp))
#             return result
#
#         num = 25
#         binary_num = convert2binary(num)
#         print(binary_num)

# class Binarydigits:
#     def __init__(self,x):
#         self.x = x // 2
#
#     def convertbinary(self):
#         if self.x ==

#
# class BinaryConverter:
#     def __init__(self, x):
#         self.x = x
#
#     def convertbinary(self):
#         temp = []
#
#         while True:
#             remain = self.x % 2
#             self.x = self.x // 2
#             temp.append(remain)
#
#             if self.x < 2:
#                 temp.append(self.x)
#                 break
#
#         temp.reverse()
#         result = "".join(map(str, temp))
#         return result
#
#     input_number = 25
#     binary_converter = BinaryConverter(input_number)
#     binary_x = binary_converter.convertbinary()
#     print(binary_x)
#
#
# import random
#
# class BinaryConverter:
#     def __init__(self, x):
#         self.x = x
#
#     def convertbinary(self):
#         temp = []
#
#         while True:
#             remain = self.x % 2
#             self.x = self.x // 2
#             temp.append(remain)
#
#             if self.x < 2:
#                 temp.append(self.x)
#                 break
#
#         temp.reverse()
#         binary = ''.join(str(i) for i in temp)
#         return binary
#
#     def random_decimal_to_binary(self):
#         decimal = random.randint(4, 16)
#         binary = self.convertbinary(decimal)
#         print(f"{decimal} in binary is {binary}")
#
# converter = BinaryConverter(0)
# converter.random_decimal_to_binary()

