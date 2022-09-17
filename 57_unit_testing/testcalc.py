# testcalc.py

import sys

from calc import Calculator



import unittest

NUMBER_1 = 3.0
NUMBER_2 = 2.0
FAILURE = 'incorrect value'


class CalculatorTestSuite(unittest.TestCase):


    def setUp(self):
        self.calc = Calculator()

    # --------------------------- Tests start

    def test_last_answer_init(self):
        value = self.calc.last_answer
        self.assertEqual(value, 0, FAILURE)

    def test_add(self):
        value = self.calc.add(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract(self):
        value = self.calc.subtract(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_subtract_negative(self):
        value = self.calc.subtract(NUMBER_2, NUMBER_1)
        self.assertEqual(value, -1, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_multiply(self):
        value = self.calc.multiply(NUMBER_2, NUMBER_1)
        self.assertEqual(value, 6, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide(self):
        value = self.calc.divide(NUMBER_1, NUMBER_2)
        self.assertEqual(value, 1.5, FAILURE)
        self.assertEqual(value, self.calc.last_answer, FAILURE)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, NUMBER_1, 0)

    # --------------------------- Tests end

    def tearDown(self):
        pass


if __name__ == '__main__':


    unittest.main()
