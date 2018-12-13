import numpy as np
from io import StringIO
import time
import os

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.arr = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            lst = [list(l.strip('\n')) for l in f.readlines()]
            arr = np.array(lst)
        return arr

    def printer(self, arr, pause=1):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in arr:
            print(''.join(row))
        time.sleep(pause)

    def solve_part1(self):
        """Returns result for part 1"""
        for _ in range(4):
            self.printer(self.arr)



    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle(test=True)
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))