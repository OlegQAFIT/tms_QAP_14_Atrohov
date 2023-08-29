# Условия
# 1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.
def number(num):
    """
    checks whether the number is positive or negative.
    If it is positive, it adds 1, and if it is negative, it does nothing.
    As a result, we derive the number
    """
    if num > 0:
        num += 1
    return num


print(number(10))


# 2. Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.
def positive(our_list):
    """
    There are numbers in the list and you only need to find the sum
    """
    ctr = 0
    for i in our_list:
        if i > 0:
            ctr += 1
    return ctr


print(positive([5, 13, -14]))


# 3. Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).
def our_year(year):
    """
    check if year is leap year or not
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year = 365
    else:
        year = 366
    return year


print(our_year(1992))


# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор- ник» и т. д.).
def day(day_number):
    """
    from the entered number we derive the day of the week
    """
    days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    if 1 <= day_number <= 7:
        return days[day_number - 1]
    else:
        return "Не тот день"


day_number = int(input("Введите число от 1 до 7: "))
day_name = day(day_number)
print(f"День: {day_name}")


# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер едини- цы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах
def convert(unit_number, mass):
    """
    calculate body weight in kilograms
    """
    conversions = [1, 0.000001, 0.001, 1000, 100]

    if 1 <= unit_number <= 5:
        return mass * conversions[unit_number - 1]
    else:
        return "Error"


unit_number = int(input("Введите массу (1-5): "))
mass = float(input("Введите массу тела: "))
result = convert(unit_number, mass)
if isinstance(result, str):
    print(result)
else:
    print(f"Масса тела в килограммах: {result} кг")
