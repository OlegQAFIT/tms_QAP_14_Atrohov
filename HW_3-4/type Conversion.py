# Преобразование типов
# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_1 = "Robin Singh"
str_2 = "I love arrays they are my favorite"

print(str_2.split())
print(str_1.split())

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
lst = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"

print("", "Привет", " ".join(lst), "!", "Добро пожаловать в", city, country)

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
my_lst = ["I", "love", "arrays", "they", "are", "my", "favorite"]

print(" ".join(my_lst))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
lst_4 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
lst_4.insert(2, 11)
del lst_4[6]

print(lst_4)

# 5.
# Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
for key in set(list(a.keys()) + list(b.keys())):
    ab[key] = [a.get(key), b.get(key)]
print(ab)

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
my_lst_1 = [1, 5, 2, 9, 2, 9, 1]

for u in my_lst_1:
    if my_lst_1.count(u) < 2:
        print(u)
