#  2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым

import random

numbers = [random.randint(0, 350) for y in range(30)]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

with open("ex2_decision_even numbers.py", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

with open("ex2_decision_odd numbers.py", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")
