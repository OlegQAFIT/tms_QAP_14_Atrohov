# Цикл while
# 1. Дано число N. Найти произведение всех чисел от 0 до N.
n = 5
z = 0
composition = 0
while z < n:
    composition = composition + z
    z += 1
print(composition)

# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
s_1 = 10
s_2 = 2
year = 0
while s_1 > s_2 * 0.1:
    year += 1
    s_1 *= 2
    s_2 *= 3
print("Площадь цветов первого сорта: ", s_1)
print("Площадь цветов второго сорта: ", s_2)
if 4 >= year % 10 <= 4 and year % 10 != 0:
    print(year)
elif 4 < year <= 20:
    print(year)

# 3. Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.
num = int(input("Введите целое число: "))
number_sum = 0
count = 0
remainder = num % 10
while num != 0:
    remainder = num % 10
    number_sum += remainder
    count += 1
    num = num // 10
