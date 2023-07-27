#  1.Написать обычную функцию для факториала, генератор и
#    рекурсию. Сравнить их время работы

import time
from timeit import timeit


# Функция
def fact(f):
    factorial = 1
    for i in range(2, f + 1):
        factorial *= i
    return factorial


print(fact(5))

j = (f"Среднее время вычисления функции: "
     f"{round(timeit('fact(5)', number=10, globals=globals()) / 10, 7)} с.")


# Рекурсия
def factr(r):
    if r == 0:
        return 1
    return factr(r - 1) * r


print(factr(5))

m = (f"Среднее время вычисления рекурсии: "
     f"{round(timeit('factr(5)', number=10, globals=globals()) / 10, 7)} с.")


# генератор
def fact_generator(g):
    result = 1
    for i in range(1, g + 1):
        result *= i
        yield result


generator_obj = fact_generator(5)

result_list = list(generator_obj)
print(result_list[-1])

l = (f"Среднее время вычисления функции: "
     f"{round(timeit('fact(5)', number=10, globals=globals()) / 10, 7)} с.")

print(j)
print(m)
print(l)

import time

# Нашел два варианта расчитывания времени,точно не могу определиться какой более верный

number = 10

# Обычная функция для факториала
start_time = time.time()
result_normal = fact(number)
end_time = time.time()
time_normal = end_time - start_time

# Рекурсивная функция для факториала
start_time = time.time()
result_recursive = factr(number)
end_time = time.time()
time_recursive = end_time - start_time

# Генератор для факториала
start_time = time.time()
result_generator = list(fact_generator(number))
end_time = time.time()
time_generator = end_time - start_time

# Вывод результатов
print(f"Обычная функция: Факториал {number} = {result_normal}, Время выполнения: {time_normal} сек.")
print(f"Рекурсивная функция: Факториал {number} = {result_recursive}, Время выполнения: {time_recursive} сек.")
print(f"Генератор: Факториал {number} = {result_generator[-1]}, Время выполнения: {time_generator} сек.")
