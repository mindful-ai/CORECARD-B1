def sumx(arg):
    total = 0
    for val in arg:
        total += val
    return total

#################################
import unittest

'''
class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
'''


'''
class TestSum2(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
'''

from fractions import Fraction

class TestSum(unittest.TestCase):


    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sumx(data)
        self.assertEqual(result, 6, 'Test failed')

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sumx(data)
        self.assertEqual(result, Fraction(9, 10))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sumx(data)

if __name__ == '__main__':
    unittest.main()
