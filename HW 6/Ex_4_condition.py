# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа
import os
import pickle

import q as q


fl_1 = open('Ex_4_First.bin', 'wb')
fl_2 = open('Ex_4_Second.bin', 'wb')
fl_3 = open('draft.bin', 'wb')

nums_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_6 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

b_1 = bytearray(nums_5)
b_2 = bytearray(nums_6)

fl_1.write(b_1)
fl_2.write(b_2)

fl_1.close()
fl_2.close()
fl_3.close()

fl_1 = open('Ex_4_First.bin', 'rb')
dat_1 = fl_1.read()
print(dat_1)
fl_1.close()

fl_3 = open('draft.bin', 'wb')
fl_3.write(dat_1)
fl_3.close()

fl_2 = open('Ex_4_Second.bin', 'rb')
dat_2 = fl_2.read()
print(dat_2)
fl_2.close()

fl_1 = open('Ex_4_First.bin', 'wb')
fl_1.write(dat_2)
fl_1.close()

fl_2 = open('Ex_4_Second.bin', 'wb')
fl_2.write(dat_1)
fl_2.close()



# s = pickle.dump(b_1, fl_1)
# q = pickle.dump(b_2, fl_2)









