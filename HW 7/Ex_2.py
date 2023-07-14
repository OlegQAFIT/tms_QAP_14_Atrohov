# 2 Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

class MyError(Exception):
    def __init__(self):
        pass


sentence = " thequick brown fox jumps over the lazy dog"
lst_sentence = sentence.split()

for element in lst_sentence:
    try:
        if element == ("the") or "the" in element:
            raise MyError()
        print(len(element))
    except MyError:
        print('Содержит запрещенное значение - "The"')
