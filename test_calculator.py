import unittest

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        del self.calculator

    def test_soma(self):
        result = self.calculator.my_sum(1,2)
        expected = 3
        self.assertTrue(result==expected)
