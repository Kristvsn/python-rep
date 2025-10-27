# # a='Hello world'
# # print(a)
# #
# # name= input('Имя?')
# # last_name=input('Фамилия?')
# # print(name,last_name)
# # print(type(name),type(last_name))
# #
# # print(f'Ваше имя {name} {last_name} {a}')
#
# # a=7
# # if a%2==0:
# #     print(f'Число {a} четное')
# # else:
# #     print(f'Число {a} нечетное')
#
# a=int(input ('Введите число'))
# if a%2==0:
#     print(f'Число {a} четное')
# else:
#     print(f'Число {a} нечетное')

# a=9           ----ВАРИАНТЫ ДЕЛЕНИЯ
# print(a/2)
# print(a//2)
# print(a%2)

# a=172438798989889890908908
# count=0
# print(len(str(a)))
# for number in str(a):
#     count+=1
#     print(count)
# print(count)

# a=172438798989889890908908 ---ВМЕСТО len (если нельзя преобразовать в строку)
# count=0
# while a!=0:
#     a=a//10
#     count+=1
# print(count)

# b='name' - только со строкой
# print(len(b))

import random
secret=random.randint(1,10)
while True:
    a=int(input("Enter a number: "))
    if a==secret:
        print("Correct")
        break
    elif a<secret:
        print("Число должно быть больше")
    elif a>secret:
        print("Число должно быть меньше")

