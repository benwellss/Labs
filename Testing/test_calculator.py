import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(1000, 2000), 3000)

    def test_subtraction(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 2), 3)
        self.assertEqual(calc.subtract(-5, -2), -3)
        self.assertEqual(calc.subtract(100, 50), 50)

    @unittest.skip("skipping...")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "skipping also")
    def test_skip_if(self):
        pass


if __name__ == '__main__':
    unittest.main()
