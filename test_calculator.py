import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 4), 3)
        self.assertEqual(self.calc.add(3, 5), 8)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-1, 5), -6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(7, 3), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 3), 2)
        self.assertEqual(self.calc.modulo(10, 4), 2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()