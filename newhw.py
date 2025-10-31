# 1. Найти минимальное число в списке (можно создать любой список чисел)
a=[-1,0,1,2,3]
# print(min(a))
min_num=a[0]
for num in a:
    if num<min_num:
        min_num=num
print('Минимальное число:', min_num)


# 2. Посчитать количество цифр в строке (например в такой "Сегодня 05.09.2025")
# - в питоне есть метод для проверки на число isdigit() он тебе поможет)

# Кол-во символов в целом
# a= 'Сегодня 05.09.2025'
# print(len(str(a)))

a= 'Сегодня 05.09.2025'
count = 0  # счетчик цифр

for char in a:
    if char.isdigit():
        count += 1
print(count)
# a= '05092025'
# if not a.isdigit():
#     print(len(str(a)))
# else:
#     print('только числа')

# 3. У тебя есть строка с паролем " Py1234 "
# Убери лишние пробелы.
# Если длина пароля меньше 8 символов — выведи "Пароль слишком короткий".
# Если пароль содержит хотя бы одну цифру — выведи "Пароль содержит цифры".
# Сделай пароль полностью заглавными буквами и выведи результат.

a=" Py1234 "
# убираем пробелы методом замены
# print(a.replace(" ",""))
# убираем пробелы методом strip()
print(a.strip())
# выведи "Пароль слишком короткий"
a=" Py123435 "
if len(a.strip()) < 8:
    print('Пароль слишком короткий')
else:
    print('Пароль больше 8 символов')
# выведи "Пароль содержит цифры"
a=" Py1234 "
for char in a:
    if char.isdigit():
        print('Пароль содержит цифры')
        break
# Сделай пароль полностью заглавными буквами
a=" Py1234 "
print(a.upper())

# 4. Есть строка "20250908"
# Используя срезы, извлеки день, месяц и год.
# Если день < 10 — добавь ведущий ноль.
# Выведи дату в формате "DD.MM.YYYY".

a="20250908"
# # извлеки день, месяц и год
print(a[6:],a[4:-2],a[:4])
# добавь ведущий ноль
a="20250908"
if int(a[6:])<10:
    print(f"{a[6:]:02}")
else:
    print('день>10')
# Выведи дату в формате "DD.MM.YYYY"
# from datetime import datetime
# a="20250908"
# b=datetime.strptime(a, "%Y%m%d")  # два аргумента: строка и формат
# print(b.strftime("%d.%m.%Y"))
a = "20250908"

year = a[0:4]   # первые 4 символа — это год
month = a[4:6]  # следующие 2 — месяц
day = a[6:8]    # последние 2 — день

print(f"{day}.{month}.{year}")

# Вычислить факториал числа
import math
a = "2"
result = math.factorial(int(a))
print(result)

# Подсчитать, сколько раз встречается каждое слово в списке, и сохранить их в переменную.
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# from collections import Counter
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# print(Counter(words))

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for word in words:
    if word in counts:          # если слово уже встречалось — увеличиваем счётчик
        counts[word] += 1
    else:                       # если встречается впервые — создаём запись
        counts[word] = 1
print(counts)