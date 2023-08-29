# Цикл for
# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.


def number(a, b, c=0):
    """
    Calculate the sum of whole numbers
    """
    for num in range(a, b + 1):
        c = c + num
    return c


print(number(15, 30))


# 2. Найти сумму всех натуральных чисел в от A до B
def nat_num(digit_1, digit_2):
    """
    sum of natural digits
    """
    for nat_int_1 in (digit_1, digit_2):
        if nat_int_1 % nat_int_1 == 0 and nat_int_1 % 1 == 0:
            nat_int_1 += nat_int_1
    return nat_int_1


print(nat_num(5, 40))


# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
def count(*args):
    """
    Count of negative digits in list
    """

    positive_int = 1
    negative_int = 0
    negative_summ = 0
    for i in args:
        if i >= 0:
            positive_int = positive_int * i
        elif i < 0:
            negative_int += 1
            negative_summ += i
    return f"Произведение положительных  {positive_int}\nКоличество отрицательных " \
           f" {negative_int}\nСумма отрицательных {negative_summ}"


print(count(-5, 25, 1, 10, -10, -7, 10, 10, -3, -10))


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
def swimmer():
    """
    The best result of swimmers
    """
    swimmers = {"Бекиш Александр": 21.07, "Будник Алексей": 20.34, "Гребень Анастасия": 22.12, "Давидович Татьяна": 30,
                "Дешук Дмитрий": 24.01, "Казак Анна": 28.17}
    return min(swimmers, key=swimmers.get)


print(swimmer())


# 5. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу, которая будет выводить
# уникальное число
def lst_1(*args):
    """
    Unique digit
    """
    return [i for i in args if args.count(i) < 2]


print(lst_1(1, 5, 2, 9, 2, 9, 1))
