import unittest  # PyUnit
from kmp import *

class KmpTestSuite(unittest.TestCase):

    def setUp(self):
        pass 

    def test_check_inbetween(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 5")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()