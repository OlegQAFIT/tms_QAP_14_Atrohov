import unittest


def func(a_1, b_2):
    nat = 0
    for i in range(a_1, b_2 + 1):
        nat += i

    return nat


class TestFunc(unittest.TestCase):
    def test_1(self):
        self.assertEqual(func(1, 3), 6)

    def test_2(self):
        self.assertEqual(func(0, "?"), "Error")

    def test_3(self):
        self.assertEqual(func(-3, 8), 30)


if __name__ == '__main__':
    unittest.main()
