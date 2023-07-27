# Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
#  return a + b
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> 55
# add_two_symbols('a', 'b') -> 'ab’
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#  return a + b + с
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001


def typed(type_):
    def decorator(func):
        def wrapper(*args):
            converted_args = []
            for arg in args:
                try:
                    converted_arg = type_(arg)
                except ValueError:
                    converted_arg = arg
                converted_args.append(converted_arg)

            return func(*converted_args)

        return wrapper

    return decorator

@typed(type_=str)
def add_two_symbols(a, b):
    return a + b

@typed(type_=int)
def add_three_symbols(a, b, c):
    return a + b + c



print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))