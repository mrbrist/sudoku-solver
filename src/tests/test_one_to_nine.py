import sys
sys.path.append("src")

import unittest

from src.one_to_nine import *

class TestOneToNine(unittest.TestCase):
    def test_one_to_nine(self):
        test = [1,2,3,4,5,6,7,8,9]
        self.assertTrue(one_to_nine(test))
    def test_one_to_nine2(self):
        test = [6,7,8,9,1,2,3,4,5]
        self.assertTrue(one_to_nine(test))

if __name__ == "__main__":
    unittest.main()