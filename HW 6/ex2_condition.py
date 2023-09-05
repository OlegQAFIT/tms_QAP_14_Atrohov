#  2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым
import random

even = open('ex2_decision_even numbers.py', 'a')
odd = open('ex2_decision_odd numbers.py', 'a')

oll_nums = [random.randint(0, 350) for y in range(30)]
print(oll_nums)

with open('ex2_decision_even numbers.py', 'w') as file:
    file.write(str(oll_nums) + '\n')

with open('ex2_decision_odd numbers.py', 'w') as file:
    file.write(str(oll_nums) + '\n')

for i in oll_nums:
    if i % 2 == 0:
        even.write(str(i) + '\n')
    else:
        odd.write(str(i) + '\n')

even.close()
odd.close()
