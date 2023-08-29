# Цикл while
# 1. Дано число N. Найти произведение всех чисел от 0 до N.
def composition(y):
    """
    product of all numbers
    """
    lst_1 = 1
    s = 0
    while s < y:
        lst_1 *= s
        s += 1
    return lst_1


print(composition(20))

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
def num(sum_number=0, count=0):
    """
    Sum and number of digits
    """
    number_1 = int(input("Введите число: "))
    the_last = number_1 % 10
    while number_1 != 0:
        last_digit = number_1 % 10
        sum_number += last_digit
        count += 1
        number_1 = number_1 // 10
    return f"Сумма цифр: {sum_number}\nКоличество цифр: {count}"


print(num())
