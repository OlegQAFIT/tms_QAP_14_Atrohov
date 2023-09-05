# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
import os

import pickle


nums_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_6 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def add_content():
    b_1 = bytearray(nums_5)
    b_2 = bytearray(nums_6)

    with open('ex_4_first.bin', '+b') as file_1:
        file_1.write(b_1)
        dat_1 = file_1.read()
    with open('ex_4_second.bin', '+b') as file_2:
        file_2.write(b_2)
        dat_2 = file_2.read()
    add_content()


def change_content():
    global dat_2
    global dat_1
    with open('ex_4_sirst.bin', 'wb') as f_1:
        f_1.write(dat_2)
    with open('ex_4_second.bin', 'wb') as f_2:
        f_2.write(dat_1)

    change_content()












