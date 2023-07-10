# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными
# числами

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = []


def create_generator():
    for i in numbers:
        if i > 0:
            yield i
        else:
            i = + 1


positive_numbers = create_generator()
for i in positive_numbers:
    print(i)
