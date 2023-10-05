import random

#3
def generate_and_process_numbers(file_path):
    nums_flt = [random.uniform(5, 50) for i in range(5)]
    print(nums_flt)

    with open(file_path, 'w') as file:
        file.write(str(nums_flt) + '\n')

        nums_flt_1 = list(map(float, nums_flt))
        for i in range(len(nums_flt_1)):
            nums_flt_1[i] = nums_flt_1[i] ** 2
        print(nums_flt_1)
        file.write(str(nums_flt_1) + '\n')

#4
def create_and_write_files():
    nums_5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nums_6 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    with open('ex_4_first.bin', 'wb') as file_1:
        b_1 = bytearray(random.sample(nums_5, len(nums_5)))
        file_1.write(b_1)

    with open('ex_4_second.bin', 'wb') as file_2:
        b_2 = bytearray(random.sample(nums_6, len(nums_6)))
        file_2.write(b_2)


def change_file_content():
    with open('ex_4_first.bin', 'rb') as file_1:
        dat_1 = bytearray(file_1.read())

    with open('ex_4_second.bin', 'rb') as file_2:
        dat_2 = bytearray(file_2.read())

    with open('ex_4_first.bin', 'wb') as file_1:
        file_1.write(dat_2)

    with open('ex_4_second.bin', 'wb') as file_2:
        file_2.write(dat_1)
