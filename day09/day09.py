from collections import deque, defaultdict
from itertools import cycle

class Puzzle:

    def __init__(self, test=False):
        self.players = 9 if test else 459
        self.marbles = 25 if test else 72103

    def solve_part1(self):
        """Returns result for part 1"""
        d = deque([0])
        scores = defaultdict(int)
        players = cycle(range(self.players))
        for m in range(1,self.marbles+1):
            p = next(players)
            if m % 23 == 0:
                d.rotate(7)
                scores[p] += d.pop() + m
                d.rotate(-1)
            else:
                d.rotate(-1)
                d.append(m)
        return max(scores.values())

    def solve_part2(self):
        """Returns result for part 2"""
        self.marbles *= 100
        return self.solve_part1()
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))