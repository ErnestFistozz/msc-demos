import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(2.0,Calculator.divide(4,2))
        
    # raises ZeroDivisionError exception
    def test_divide_raises_exception(self):
        self.assertRaises(ZeroDivisionError, Calculator.divide, 5, 0)

    def test_subtract(self):
        self.assertEqual(4, Calculator.subtract(3,7))

if __name__ == '__main__':
    unittest.main()