import sys
sys.path.append("src")

import unittest

from src.sudoku import *

class TestSudoku(unittest.TestCase):
    def test_get_num(self):
        test = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"
        s = Sudoku(test)
        self.assertEqual(s.get_num(0,1), 5)
        
    def test_get_row(self):
        test = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"
        s = Sudoku(test)
        self.assertEqual(s.get_row(0), [0,5,0,7,0,3,0,6,0])
        
    def test_get_column(self):
        test = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"
        s = Sudoku(test)
        self.assertEqual(s.get_column(0), [0, 0, 0, 0, 0, 7, 9, 8, 0])
        
    def test_get_block(self):
        test = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"
        s = Sudoku(test)
        self.assertEqual(s.get_block(0,1), [7,0,3,
                                            0,0,0,
                                            8,1,6])
    def test_get_block2(self):
        test = "050703060007000800000816000000030000005000100730040086906000204840572093000409000"
        s = Sudoku(test)
        self.assertEqual(s.get_block(2,2), [2,0,4,
                                            0,9,3,
                                            0,0,0])

if __name__ == "__main__":
    unittest.main()