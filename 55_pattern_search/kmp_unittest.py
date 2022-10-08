import sys
import unittest
from kmp import *

'''
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
'''

class kmptestsuite(unittest.TestCase):

    def setUp(self):
        pass 

    def test_check_inbetween(self):
        s = "ABCDPQRABDC"
        p = "PQR"
        expected_result = 5 # scalar value
        obtained_result = KMPSearch(p, s) # List
        self.assertEqual(expected_result, obtained_result[0], 'Test failed')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()