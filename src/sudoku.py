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
        pass
    
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