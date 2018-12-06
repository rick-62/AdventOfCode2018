from itertools import product, chain
from collections import Counter

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.limit = 32 if test else 10000
        self.data = self.load_into_memory(filename)

        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = [(int(x), int(y)) for x,y in 
                    (line.split(', ') for line in f.readlines())]
        return data

    def distance(self, c1, c2):
        """Manhatten distance between 2 coordinates"""
        return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

    def closest(self, g):
        """
        Given grid coordinate (g) cycle through input coordinates (data),
        calculate the input coordinate with the minimum distance to g.
        In some cases 2+ coordinates share the same distance.
        Returns list of coordinates at a minimum distance to g.
        """
        s = {}
        for c in self.data:
            s[c] = self.distance(c, g)
        m = min(s.values())
        return [c for c in s.keys() if s[c] == m]

    def total(self, g):
        """
        Given grid coordinate (g) cycle through input coordinates (data),
        calculates the distance to each input coordinate, and
        returns sum of distances.
        """
        s = []
        for c in self.data:
            s.append(self.distance(c, g))
        return sum(s)


    def remove(self, C, xs, ys):
        """
        For each grid coordinate in dict C, if
        coordinate is on edge of coordinate boundary,
        marks the associated input coordinate for removal.
        Returns list of coordinates to exclude.
        """
        mx = [min(xs), max(xs)]
        my = [min(ys), max(ys)]
        removal = []
        for x,y in C.keys():
            if x in mx or y in my:
                removal.append(C[(x,y)][0])
        return removal
    
    def solve_part1(self):
        """
        Returns result for part 1:
        Calculates boundary based on input coordinates (data), then 
        cycles through each coordinate to establish which input coordinates
        are closest. 
        The coordinates on the boundary and those with a shared distance
        are removed. 
        The remaining coordinates are counted and the most common is returned.
        """
        xs = [x for x,y in self.data]
        ys = [y for x,y in self.data]

        X = range(min(xs), max(xs) + 1)
        Y = range(min(ys), max(ys) + 1)

        C = {}
        for g in product(X, Y):
            C[g] = self.closest(g)

        removal = self.remove(C, xs, ys)
        count = Counter([c[0] for c in C.values() 
                         if len(c) == 1 and c[0] not in removal])
        return count.most_common(1)[0]


    def solve_part2(self):
        """
        Returns result for part 2:
        Calculates boundary based on input coordinates (data), then 
        cycles through each coordinate and totals up to the distances to
        each input coordinate. 
        Totals below the limit (10,000) are counted and this count is 
        returned as the answer.
        """
        xs = [x for x,y in self.data]
        ys = [y for x,y in self.data]

        X = range(min(xs), max(xs) + 1)
        Y = range(min(ys), max(ys) + 1)

        C = {}
        count = 0
        for g in product(X, Y):
            if self.total(g) < self.limit:
                count += 1
        return count


if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))