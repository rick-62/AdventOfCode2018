import numpy as np 
from itertools import product

class Puzzle:

    def __init__(self, i):
        self.input = int(i)

    def power(self, x, y):
        return (((x+10) * y + self.input) * (x+10) // 100) % 10 - 5

    def cell_array(self, X=300, Y=300):
        arr = np.zeros((X+1, Y+1), dtype=int)
        for x,y in product(range(1,X+1), range(1,Y+1)):
            arr[x,y] = self.power(x,y)
        return arr

    def solve(self, arr, s=3):
        X,Y = arr.shape
        S = {}
        for x,y in product(range(1,X-s+1), range(1,Y-s+1)):
            S[(x,y)] = arr[x:x+s, y:y+s].sum()
        return max(S.items(), key=lambda k: k[1])


    def solve_part1(self):
        """Returns result for part 1"""
        arr = self.cell_array()
        return self.solve(arr)[0]

    def solve_part2(self):
        """Returns result for part 2"""
        arr = self.cell_array()
        S = {}
        for s in range(3,20):
            c, m = self.solve(arr, s=s)
            S[(*c,s)] = m
        return max(S.keys(), key=lambda k: S[k])
        

if __name__ == "__main__":
    test = input("Test?(y/n): ")
    if test.upper() == "Y":
        puzzle = Puzzle(8)
        t0 = puzzle.input
        t1 = puzzle.cell_array()[3,5]
        t2 = puzzle.power(3,5)
        puzzle.input = 57
        t3 = puzzle.cell_array()[122,79]
        puzzle.input = 18
        t4 = puzzle.solve(puzzle.cell_array())[0]
        puzzle.input = 42
        t5 = puzzle.solve(puzzle.cell_array())[0]
        try:
            assert t0 == 8 , "{} != 8".format(t0)
            assert t2 == 4 , "{} != 4".format(t2)
            assert t1 == 4 , "{} != 4".format(t1)
            assert t3 == -5, "{} != -5".format(t3)
            assert t4 == (33,45), "{} != (33,45)".format(t4)
            assert t5 == (21,61), "{} != (21,61)".format(t4)
        except AssertionError as e:
            print("Fail: ", e)
        print("Testing was successful.")

    else:
        puzzle = Puzzle(input("Enter puzzle input: "))
        print("Part 1 = {}".format(puzzle.solve_part1()))
        print("Part 2 = {}".format(puzzle.solve_part2()))