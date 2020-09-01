import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(calc.sub(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calc.mul(10, 5), 50)

    def test_divide(self):
        self.assertEqual(calc.div(10, 5), 2)

        with self.assertRaises(ValueError):
            calc.div(10, 0)


if __name__ == '__main__':
    unittest.main()