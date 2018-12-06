from itertools import product, chain
from collections import Counter

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = [(int(x), int(y)) for x,y in 
                    (line.split(', ') for line in f.readlines())]
        return data

    def distance(self, c1, c2):
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

    def closest(self, g):
        s = {}
        for c in self.data:
            s[c] = self.distance(c, g)
        m = min(s.values())
        return [c for c in s.keys() if s[c] == m]

    def remove(self, C, xs, ys):
        mx = [min(xs), max(xs)]
        my = [min(ys), max(ys)]
        removal = []
        for x,y in C.keys():
            if x in mx or y in my:
                removal.append(C[(x,y)][0])
        return removal
    
    def solve_part1(self):
        """Returns result for part 1"""
        xs = [x for x,y in self.data]
        ys = [y for x,y in self.data]

        X = range(min(xs), max(xs) + 1)
        Y = range(min(ys), max(ys) + 1)

        C = {}
        for g in product(X, Y):
            C[g] = self.closest(g)

        removal = self.remove(C, xs, ys)
        count = Counter([c[0] for c in C.values() if len(c) == 1 and c[0] not in removal])
        return count.most_common(1)[0]


    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))