# Словари:
# 1. Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
# 2б, 6а, 7в и т.д.).
school = {'1a': 28, "1б": 13, "2а": 15, "2в": 40, "3а": 21, "3б": 26, "4а": 35, "4б": 21, "5а": 10,
          "5б": 40, "6а": 323, "6б": 28, "7а": 29, "7б": 19, "8а": 26, "8б": 31, "9а": 24, "9б": 21,
          "10а": 25, "10б": 210}
# 2. Узнайте сколько человек в каком-нибудь классе.
print(school["6а"])

# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
school["6а"] = 1000
school["1б"] = 25
school["8а"] = 49

# ◦ в школе появилось два новых класса;
school["6в"] = 63
school["9в"] = 10
school["11а"] = 63

# ◦ в школе расформировали один из классов.
school.pop("10а")

# 4. Выведите содержимое словаря на экран.
print(school)