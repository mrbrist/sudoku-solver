import cmd
from sudoku import *

class CLI(cmd.Cmd):
    prompt = '>>> '
    intro = 'Welcome to SudokuSolver. Type "help" for available commands.'
    
    def do_solve(self, sudoku):
        """Solves a sudoku in a oneline format"""
        s = Sudoku(sudoku)
        print("Solving...")
        s.solve_backtrack(False)
        print(f"Solved?: {s.is_solved()}")
        s.display()
    
    def do_visual(self, sudoku):
        """Solves a sudoku in a oneline format with visual"""
        s = Sudoku(sudoku)
        print("Solving...")
        s.solve_backtrack(True)
        print(f"Solved?: {s.is_solved()}")
        s.display()
        
    def do_display(self, sudoku):
        """Displays a sudoku puzzle in a useful way"""
        s = Sudoku(sudoku)
        s.display()
        
    def do_generate(self, sudoku):
        """Generates a new sudoku puzzle in a one line format"""
        pass
    
    def do_difficulty(self, sudoku):
        """Estimates the difficulty of a sudoku puzzle"""
        pass

    def do_exit(self, line):
        """Exit the CLI."""
        return True