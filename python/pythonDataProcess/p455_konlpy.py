from konlpy.tag import Komoran

sentence = '코로나 바이러스 태블릿 PC, 설진욱, 가나다라'
print('#before user dic')
komo = Komoran()
print(komo.pos(sentence))
print('-'*20)

komo = Komoran(userdic='user_dic.txt')
print('# after user dic')
print(komo.pos(sentence))
print('-'*20)

print('#komo.nouns')
result = komo.nouns(sentence)
print(result)
print('#'*20)

print('# komo.morphs')
presult = komo.morphs(sentence)
print(result)