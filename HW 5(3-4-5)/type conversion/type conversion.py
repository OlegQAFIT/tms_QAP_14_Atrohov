# Преобразование типов
# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]

def list(str1):
    """
    Converts str to list
    """
    return str1.split()

print(list("Robin Singh"))


def list_1(my_str):
    """
    Converts list to str
    """
    global str_to_array
    str_to_array = my_str.split()
    return str_to_array

print(list_1("I love arrays they are my favorite"))

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
def list_to_array():
    """
    Join str to list
    """
    my_array = ["Ivan", "Ivanov"]
    city = "Minsk"
    country = "Belarus"
    return f"Привет," + " " + ' '.join(my_array) + "!" + " " + "Добро пожаловать в " + city + " " + country

print(list_to_array())

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"
def list_to_str(*args):
    """
    Converts list to str
    """
    return ' '.join(args)

print(list_to_str("I love arrays they are my favorite"))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
def del_elem(**kwargs):
    """
    Remove elem from dict
    """
    kwargs.pop("f")
    return kwargs


print(del_elem(a=1, b=2, c=11, d=4, e=5, f=6, g=7, h=8, i=9, j=10))

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
def dicts():
    """
    Merge dicts
    """
    for key in set(list(a.keys()) + list(b.keys())):
        ab[key] = [a.get(key), b.get(key)]
    return ab

print(dicts())


