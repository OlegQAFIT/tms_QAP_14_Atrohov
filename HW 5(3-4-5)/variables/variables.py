# Работа с переменными:
# 1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = "No"


# 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза,
# результат свяжите с переменной big_int.
def change_1():
    """
    Increase int up to 3.5 times
    """
    global new_int
    new_int = var_int * 3.5
    return new_int

# 3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# результат свяжите с той же переменной.
def change_2():
    """
     Decrease float val to 1 digit
    """
    global new_float
    new_float -= 1
    return new_float

# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных
# выражений не привязывайте ни к каким переменным.
def change_3():
    """
    Div values
    """
    a = var_int / var_float
    b = new_int / var_float
    return f"{a}\n{b}"

# 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# нового значения используйте операции конкатенации (+) и повторения строки (*).
def change_4():
    """
    Change strings
    """
    global var_str
    var_str = (var_str * 2) + ("Yes" * 3)
    return var_str


#6 Выведите значения всех переменных.

print(change_1())
print(change_2())
print(change_3())
print(change_4())