# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
import os

import pickle


nums_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_6 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def add_content():
    b_1 = bytearray(nums_5)
    b_2 = bytearray(nums_6)

    with open('Ex_4_First.bin', '+b') as file_1:
        file_1.write(b_1)
        dat_1 = file_1.read()
    with open('Ex_4_Second.bin', '+b') as file_2:
        file_2.write(b_2)
        dat_2 = file_2.read()
    add_content()


def change_content():
    global dat_2
    global dat_1
    with open('Ex_4_First.bin', 'wb') as f_1:
        f_1.write(date_2)
    with open('Ex_4_Second.bin', 'wb') as f_2:
        f_2.write(date_1)

    change_content()












