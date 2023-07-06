# Логические операции:
# 1. Присвойте двум переменным любые числовые значения.
age_1 = 63
age_2 = 99
# 2. Составьте четыре сложных логических выражения с помощью оператора and, два из
# которых должны давать истину, а два других - ложь.
print(age_1 != 5 and age_2 < 100)
print(age_1 == 63 and age_2 <= 99.1)
print(age_1 <= 2458 and age_2 != 99)
print(age_1 != 63 and age_2 > 99.1)

# 3. Аналогично выполните п. 2, но уже используя оператор or.
print(age_1 != 5 or age_2 != 100)
print(age_1 == 63 or age_2 <= 99.1)
print(age_1 >= 2458 or age_2 == 99.1)
print(age_1 != 63 or age_2 > 99.1)

# 4. Попробуйте использовать в сложных логических выражениях работу с переменными
# строкового типа.
my_mame_surname = "Oleg Atrokhau"
sister_surname_name = "Atrokhava Tatiana"

print(my_mame_surname.startswith("Atrokhau") or sister_surname_name.endswith("Tatiana"))
print(sister_surname_name.endswith("Tatiana"))
print(len(sister_surname_name) < len(my_mame_surname))
