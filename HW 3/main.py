# Задание 1.2 Определить переменные всех типов и выведете их на экран
from statistics import mean

import oleg as oleg

# Nubbers(числа)
a = 5
b = 6.3

print(a + b)

# Strings (строки)
name_1 = "Oleg"
name_2 = "Oleg1 "

print(name_1 == name_2)

# Lists (списки)
lt_1 = [1, 2, 3]
lt_2 = [1, 2, 3, 4, 5]

print(lt_1 + lt_2)

# Dictionaries (словари)
a = dict.fromkeys(['oleg', 'Harry'], "Supper")
d = {"oleg": 1, "Harry": 2}
print(a)
print(d)

# Tuples (кортежи)
(a, b, c) = ("good", "morning", "everybody")

print(a)
print(b)
print(c)
print(a, b, c)

# Boolean (логический тип данных)
my_name = "Oleg"
sister_name = ""

print(bool(my_name))
print(bool(sister_name))

print(bool(my_name) == bool(sister_name))

# Задание 1.3 Найти значение выражений
x1 = (17 / (2 * 3)) + 2

x2 = 2 + ((17 / 2) * 3)

x3 = (19 % 4) + (15 / (2 * 3))

x4 = (15 + 6) - (10 * 4)

x5 = (17 / 2) % (2 * (3 ** 3))

print(x1)
print(x2)
print(x3)
print(x4)
print(x5)

# Задание 1.4 Создать три переменные, содержащие возраст трех
#       ближайших соседей, найти сумму и вывести ее на экран.
#       Создать еще одну переменную равную среднему арифметическому возрасту, и вывести это значение на экран.

age_olia = 38
age_kirill = 25
age_dima = 33
summ_age = (age_dima + age_kirill + age_olia)
average_age = (age_dima, age_kirill, age_olia)

print(summ_age)
print(mean(average_age))
# Or
average_value = summ_age / len(average_age)
print(average_value)

# 1.Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99

print(int(a), int(b))

# 2.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
adress = "'www.my_site.com#about'"

print(adress.replace("#", "/"))

# 3.Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
a = "ing"
b = "stroka"

print(b + a)

# 4.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"


name = "Ivanou Ivan"
words = name.split()  # Разбить строку на список слов
reordered_name = " ".join(words[::-1])  # Поменяйте порядок слов и соедините их пробелом
print(reordered_name)

# 5.Напишите программу которая удаляет пробел в начале, в конце строки
my_list1 = ' New York City is a metropolis that has long been a center of culture '

print(my_list1.strip())

# 6.Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1а": 20, "1б": 18, "2а": 22, "2б": 25, "3а": 20, "3б": 24, "4а": 15, "4б": 25, "5а": 25, "5б": 24,
          "6а": 10, "6б": 12, "7а": 19, "7б": 21, "8а": 22, "8б": 29, "9а": 21, "9б": 24, "10а": 18, "10б": 17,
          "11а": 28, "11б": 23}

print(school)

# 7.Создайте список и извлеките из него списка второй элемент.
my_list = "New York City is a metropolis that has long been a center of culture"

print(my_list[4:8])

# 8.Вывести входит ли строка1 в строку2 (пример: employ и employment )
usa_city = "New York City is a metropolis that has long been a center of culture, commerce, and innovation. Located in the northeastern United States, it is the largest city in the country and home to more than 8 million people."
str = "oleg"

print(usa_city.find(str))

# 9.Вывести нужные символы
#       x = "My name is Agent Smith"
#       print(x[?]) #y
#       print(x[?:?:?]) #nesgt
x = "My name is Agent Smith"

print(x[1])
print(x[3:18:3])

# * Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
#       Напишите программу, которая будет выводить уникальное число
#       PS: создать ПР, использовать git (через терминал), если кто-то уже работал с функциями использовать их при написании дз
