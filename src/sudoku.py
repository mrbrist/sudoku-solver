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
    
    def get_full_arr(self):
        return self.arr
    
    def display(self):
        for i, row in enumerate(self.arr):
            # Add horizontal separator every 3 rows (except top)
            if i % 3 == 0 and i != 0:
                print("-" * 22)

            row_str = ""
            for j, val in enumerate(row):
                # Add vertical separator every 3 columns (except leftmost)
                if j % 3 == 0 and j != 0:
                    row_str += " |"
                # Print value or dot for empty (0)
                cell = str(val) if val != 0 else "."
                row_str += " " + cell
            print(row_str)