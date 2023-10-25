import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(2.0,Calculator.divide(4,2))

    def test_subtract(self):
        self.assertEqual(4, Calculator.subtract(3,7))
        
if __name__ == '__main__':
    unittest.main()