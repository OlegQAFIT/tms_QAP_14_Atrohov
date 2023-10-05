import unittest
import os
import random
from ex_3_Real_numbers_float import process_and_write_numbers

class Test_1(unittest.TestCase):

    def setUp(self):
        with open('ex_3_Real_numbers_float.py', 'w') as file:
            file.write('')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            process_and_write_numbers([1, 2, 'invalid'])
    def test_process_and_write_numbers(self):
        nums_flt = [random.uniform(5, 50) for i in range(5)]
        process_and_write_numbers(nums_flt)

        with open('ex_3_Real_numbers_float.py', 'r') as file:
            result = list(map(float, file.readlines()))

        expected = [x ** 2 for x in nums_flt]
        self.assertEqual(result, expected)
    def tearDown(self):
        if os.path.exists('ex_3_Real_numbers_float.py'):
            os.remove('ex_3_Real_numbers_float.py')

    def test_small_input(self):
        with self.assertRaises(ValueError):
            process_and_write_numbers([1])
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            process_and_write_numbers([])



