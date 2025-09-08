from one_to_nine import *

class Sudoku():
    def __init__(self, data):
        self.arr = [[],[],[],
                    [],[],[],
                    [],[],[]]
        
        split = [data[i:i+9] for i in range(0, len(data), 9)]
        
        for i in range(len(split)):
            split2 = [int(ch) for ch in split[i]]
            self.arr[i].extend(split2)
        
    def get_num(self, x, y):
        return self.arr[x][y]
    
    def get_row(self, x):
        # Get a row from the puzzle
        return self.arr[x]
    
    def get_column(self, y):
        # Get a column from the puzzle
        res = []
        for i in self.arr:
            res.append(i[y])
        return res
    
    def get_block(self, x, y):
        # Get a block from the puzzle
        res = []
        for i in range(x*3,x*3+3):
            for j in range(y*3,y*3+3):
                res.append(self.arr[i][j])
                
        return res
    
    def is_solved(self):      
        for i in range(0,9):
            if not one_to_nine(self.get_row(i)):
                return False
            if not one_to_nine(self.get_column(i)):
                return False
            
        blocks = [(0,0),(0,1),(0,2),
                  (1,0),(1,1),(1,2),
                  (2,0),(2,1),(2,2)]
        
        for i in blocks:
            if not one_to_nine(self.get_block(i[0],i[1])):
                return False
        
        return True
    
    def display(self):
        for i, row in enumerate(self.arr):
            if i % 3 == 0 and i != 0:
                print("-" * 22)

            row_str = ""
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += " |"
                cell = str(val) if val != 0 else "."
                row_str += " " + cell
            print(row_str)