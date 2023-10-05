import unittest
import os
from Initial_conditions_with_HW_6 import create_and_write_file, change_content


class Test_2(unittest.TestCase):

    def setUp(self):
        with open('ex_4_first.bin', 'wb') as file_1, open('ex_4_second.bin', 'wb') as file_2:
            file_1.writelines(b'')
            file_2.writelines(b'')

    def tearDown(self):
        if os.path.exists('ex_4_first.bin'):
            os.remove('ex_4_first.bin')
        if os.path.exists('ex_4_second.bin'):
            os.remove('ex_4_second.bin')

    def test_create_and_write_file(self):
        create_and_write_file()
        self.assertTrue(os.path.exists('ex_4_first.bin'))
        self.assertTrue(os.path.exists('ex_4_second.bin'))

    def test_change_content(self):
        create_and_write_file()
        change_content()

        with open('ex_4_first.bin', 'rb') as file_1, open('ex_4_second.bin', 'rb') as file_2:
            content_1 = file_1.read()
            content_2 = file_2.read()

        self.assertEqual(content_1, b'')
        self.assertEqual(content_2, b'')
