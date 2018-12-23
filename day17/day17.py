import re
import numpy as np
import time


class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        self.arr = None
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = f.readlines()
        return data

    def extract_coords(self):
        d = self.data
        py = re.compile(r'y=(\d+)..(\d+)?')
        px = re.compile(r'x=(\d+)..(\d+)?')
        X,Y = [],[]
        for line in d:
            Y.append([int(r) for r in re.findall(py, line)[0] if r != ''])
            X.append([int(r) for r in re.findall(px, line)[0] if r != ''])
        print(list(zip(Y,X)))
        return X,Y

    def create_arr(self, X, Y):
        i_max = max([max(y) for y in Y])
        j_max = max([max(x) for x in X])
        self.j_min = min([min(x) for x in X])

        self.arr = np.full((i_max+1, j_max+2), ['.'], dtype=str)
        self.arr[:, :self.j_min-1] = '@'
        self.arr[(0, 500)] = '+'

        for i,j in zip(Y,X):
            if len(i) == 2:
                self.arr[i[0]:i[1]+1, j[0]] = '#'
            elif len(j) == 2:
                self.arr[i[0], j[0]:j[1]+1] = '#'
    

    def printer(self, arr=False, t=0.5):

        if not arr:
            arr = self.arr

        for row in arr[:,self.j_min-1:]:
            print(''.join(row))

        time.sleep(t)


    def solve_part1(self):
        """Returns result for part 1"""
        X,Y = self.extract_coords()
        self.create_arr(X,Y)
        self.printer()


    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle(test=True)
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))