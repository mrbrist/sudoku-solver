import cmd
from sudoku import *
from bcolors import *
import random

class CLI(cmd.Cmd):
    prompt = '>>> '
    intro = 'Welcome to SudokuSolver. Type "help" for available commands.'
    
    def do_solve(self, sudoku):
        """Solves a sudoku in a oneline format"""
        s = Sudoku(sudoku)
        print("Solving...")
        s.solve_backtrack(False)
        
        print(f"Solved?: {bcolors.OKGREEN}{s.is_solved()}{bcolors.ENDC}")
        print(f"Steps: {bcolors.OKBLUE}{s.get_steps()}{bcolors.ENDC}")
        s.display()        
        
    def do_bulksolve(self, path):
        """Solves all sudokus in a text file seperated by new line"""
        f = open(path)
        split = f.read().split("\n")
        for i in range(len(split)):
            s = Sudoku(split[i])
            s.solve_backtrack(False)
            print(f"Solved #{i+1} in {bcolors.OKBLUE}{s.get_steps()}{bcolors.ENDC} steps")
    
    def do_visual(self, sudoku):
        """Solves a sudoku in a oneline format with visual"""
        s = Sudoku(sudoku)
        s.solve_backtrack(True, 0.01)
        print(f"Solved?: {bcolors.OKGREEN}{s.is_solved()}{bcolors.ENDC}")
        s.display()
        
    def do_display(self, sudoku):
        """Displays a sudoku puzzle in a useful way"""
        s = Sudoku(sudoku)
        s.display()
        
    def do_generate(self, pre_solved):
        """Generates a new sudoku puzzle in a one line format"""
        s = Sudoku("000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        s.generate(int(pre_solved) if pre_solved else random.randrange(6,30))
        s.display()
        print(f"One line format: {bcolors.OKCYAN}{s.get_one_line()}{bcolors.ENDC}")
        print(f"Estimated difficulty is: {s.estimate_difficulty()}")
    
    def do_difficulty(self, sudoku):
        """Estimates the difficulty of a sudoku puzzle"""
        print("Estimating...")
        s = Sudoku(sudoku)
        print(f"Estimated difficulty is: {s.estimate_difficulty()}")

    def do_exit(self, line):
        """Exit the CLI."""
        return True