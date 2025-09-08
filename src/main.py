from sudoku import *

test =   "050703060007000800000816000000030000005000100730040086906000204840572093000409000"

s = Sudoku(test)

print("Unsolved Sudoku:")
s.display()
print("Solving using backtrack...")
s.solve_backtrack(True)
print("Solved!")
s.display()
print(f"Solved?: {s.is_solved()}")