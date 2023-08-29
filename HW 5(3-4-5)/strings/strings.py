# Строки:
# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.


def str(my_str):
    """
    extracting characters from a string
    """
    return f"{my_str[0]}\n{my_str[-1]}\n{my_str[2]}\n{my_str[-3]}\n{(len(my_str))}"


print(str("I try hard to learn everything."))


# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку

def str(our):
    """
    output slices
    """
    mid = int(len(our) / 2)
    return our[0:7:1], our[mid - 2:mid + 2], our[2:14:3], our[::-1]


print(str("My_name_is_Oleg"))


# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.

def my_name(str_2):
    """
    Replaces second 'name' in string to user's name
    """
    user_name = "Oleg"

    return f"{str_2[:11]}{user_name}{str_2[16:]}"


print(my_name("my name is name"))


# 4. Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”


def string(str):
    """
    Prints where the letter w is located,
    counts the number of letters l
    Checks if a string starts with the substring: "Hello"
    """
    return str.find('w'), str('l'), str[0:4].istitle(), \
        str.islower()


print(string("Hello world!"))
