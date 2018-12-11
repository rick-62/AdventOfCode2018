import re
import matplotlib.pyplot as plt
from itertools import combinations
from scipy import optimize

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
    
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        ptn = re.compile(r'-?\d+')
        with open(filename) as f:
            data = {i:[int(d) for d in re.findall(ptn, l)] 
                    for i,l in enumerate(f.readlines())}
            return data
            

    def equation(self, x1, y1, i, j, t):
        x2 = x1 + t * i
        y2 = y1 + t * j
        return (x2, y2)

    def manhatten(self, x1, y1, x2, y2):
        return abs(x2-x1) + abs(y2-y1)
        
    def distance(self, C):
        total = 0
        for c1,c2 in combinations(C, 2):
            total += self.manhatten(*c1, *c2)
        return total

    def adjacent(self, C):
        count = 0
        for x,y in C:
            if (x+1,y) in C or \
               (x-1,y) in C or \
               (x,y+1) in C or \
               (x,y-1) in C or \
               (x+1,y+1) in C or \
               (x+1,y-1) in C or \
               (x-1,y+1) in C or \
               (x-1,y-1) in C:
                count += 1
        return len(C) - count

    def solve(self, t):
        return set(self.equation(v[0], v[1], v[2], v[3], t) 
                   for k,v in self.data.items())

    def fun1(self, t):
        return self.distance(self.solve(t))

    def fun2(self, t):
        return self.adjacent(self.solve(t))


    def solve_part1(self):
        """Returns result for part 1"""
        t = int(optimize.minimize_scalar(self.fun1)['x'])

        mn = {}
        for t in range(t-5, t+5):
            mn[t] = self.fun2(t)
        t = min(mn.keys(), key=lambda x: mn[x])

        C = self.solve(t)
        plt.scatter(*zip(*C), s=100)
        plt.gca().invert_yaxis()
        plt.show()

        return t


    # def solve_part2(self):
    #     """Returns result for part 2"""
    #     pass
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 2 = {}".format(puzzle.solve_part1()))
    # print("Part 2 = {}".format(puzzle.solve_part2()))