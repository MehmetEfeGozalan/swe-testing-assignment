import unittest
from calc import compute

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(compute(5, '+', 3), 8)

    def test_sub(self):
        self.assertEqual(compute(10, '-', 4), 6)

    def test_divwithminus(self):
        self.assertEqual(compute(8, '/', -2), -4)

    def test_mulwithminus(self):
        self.assertEqual(compute(10, '*', -3), -30)

    def test_mulwithfraction(self):
        self.assertEqual(compute(10, '*', 0.5), 5.0)

    def test_mul(self):
        self.assertEqual(compute(6, '*', 7), 42)

    def test_div(self):
        self.assertEqual(compute(8, '/', 2), 4)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            compute(8, '/', 0)

if __name__ == '__main__':
    unittest.main()
