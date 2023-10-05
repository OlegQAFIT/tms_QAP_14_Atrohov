#  3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

import random

nums_flt = [random.uniform(5, 50) for i in range(5)]
print(nums_flt)
# Специально вывожу, чтобы продемонстрировать какие значения выводит

f_1 = open('ex_3_Real numbers_float.py')

with open('ex_3_Real numbers_float.py', 'w') as file:
    file.write(str(nums_flt) + '\n')

    nums_flt_1 = list(map(float, nums_flt))
    for i in range(len(nums_flt_1)):
        nums_flt_1[i] = nums_flt_1[i] ** 2
    print(nums_flt_1)  # Специально вывожу, чтобы продемонстрировать какие значения выводятся первые и вторые
    file.write(str(nums_flt_1) + '\n')

f_1.close()
