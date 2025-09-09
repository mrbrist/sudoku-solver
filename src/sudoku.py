from one_to_nine import *
from bcolors import *
import time
import random

MAX_STEPS = 1000000
class Sudoku():
    def __init__(self, data):
        self.data = data
        self.arr = [[],[],[],
                    [],[],[],
                    [],[],[]]
        self.steps = 0
        self.solve_aborted = False
        
        split = [data[i:i+9] for i in range(0, len(data), 9)]
        
        for i in range(len(split)):
            split2 = [int(ch) for ch in split[i]]
            self.arr[i].extend(split2)
            
    def __eq__(self, value):
        if self.arr == value.arr:
            return True
        return False
    
    def get_steps(self):
        return self.steps
    
    def get_one_line(self):
        res = ""
        
        for i in self.arr:
            for j in i:
                res += str(j)
        
        return res
            
    def get_num(self, x, y):
        return self.arr[x][y]
    
    def set_num(self, pos, num):
        x,y = pos
        self.arr[x][y] = num
    
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
                cell = f"{bcolors.OKCYAN}{str(val)}{bcolors.ENDC}" if val != 0 else "."
                row_str += " " + cell
            print(row_str)
            
    def find_next_empty(self):
        for i in range(9):
            for j in range(9):
                if self.arr[i][j] == 0:
                    return (i,j)
        return None
    
    def is_valid_position(self, pos, num):
        x, y = pos
        if num in self.get_row(x):
            return False
        if num in self.get_column(y):
            return False
        if num in self.get_block(x//3,y//3):
            return False
        
        return True
    
    def solve_backtrack(self, visual, delay=0.5, steps=0):
        if self.get_steps() >= MAX_STEPS:
            self.abort_solve()
            self.solve_aborted = True
            return True
        
        next_pos = self.find_next_empty()
    
        if not next_pos:
            return True
        
        for i in range(1, 10):
            if self.is_valid_position(next_pos, i):
                self.set_num(next_pos, i)
                
                if self.solve_backtrack(visual, delay, steps):
                    return True
                
                # Backtrack
                self.set_num(next_pos, 0)
                
        if visual:
            print("\033[H\033[J", end="")
            self.display()
            print("Solving...")
            print(f"Steps: {bcolors.OKBLUE}{self.get_steps()+1}{bcolors.ENDC}")
            time.sleep(delay)
            
        self.steps+=1
        return False
    
    def abort_solve(self):
        if not self.solve_aborted:
            print(f"{bcolors.FAIL}SOLVE ABORTED: Could not solve within {MAX_STEPS:,} steps{bcolors.ENDC}")
            return
        return
    
    def generate(self, pre_solved):
        print(f"Generating sudoku with {pre_solved} pre-solved numbers")
        while pre_solved != 0:
            x, y = random.randrange(0,9), random.randrange(0,9)
            num = random.randrange(1,10)
            if self.is_valid_position((x,y), num) and self.arr[x][y] == 0:
                self.arr[x][y] = num
                pre_solved-=1
                
    def get_givens(self):
        givens = 0
        for i in self.arr:
            for j in i:
                if j != 0:
                    givens += 1
        
        return givens
                
    def estimate_difficulty(self):
        givens = self.get_givens()
        self.solve_backtrack(False)
        steps = self.get_steps()
        score = (81 - givens) + steps // 50
        
        if score < 100:
            return f"{bcolors.OKGREEN}Easy{bcolors.ENDC}"
        elif score < 250:
            return f"{bcolors.OKCYAN}Medium{bcolors.ENDC}"
        elif score < 500:
            return f"{bcolors.WARNING}Hard{bcolors.ENDC}"
        else:
            return f"{bcolors.FAIL}Evil{bcolors.ENDC}"
        
    def show_all_valid_pos_for_number(self, num):
        num = int(num)
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i][j] == 0:
                    pos = i, j
                    if self.is_valid_position(pos, num):
                        self.arr[i][j] = "#"
                        
        for i, row in enumerate(self.arr):
            if i % 3 == 0 and i != 0:
                print("-" * 22)

            row_str = ""
            for j, val in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str += " |"
                cell = f"{bcolors.OKCYAN}{str(val)}{bcolors.ENDC}" if val != 0 and val != "#" else f"{bcolors.FAIL}{num}{bcolors.ENDC}" if val == "#" else "."
                row_str += " " + cell
            print(row_str)