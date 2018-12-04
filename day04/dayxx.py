import re
import datetime as dt
from collections import OrderedDict


class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory"""
        data = {}
        recomp = re.compile(r'\[(.+)\]|Guard #([0-9]+)|(wakes)|(asleep)')
        with open(filename) as f:
            for line in f:
                record = re.findall(recomp, line)
                timestamp = dt.datetime.strptime(record[0][0], '%Y-%m-%d %H:%M')
                event = ''.join(record[1])
                data[timestamp] = event
        return OrderedDict(sorted(data.items()))

    def solve_part1(self):
        """
        Returns result for part 1:
        Finds the guard that has the most minutes asleep and
        identifies the minute they are asleep the most.
        Returns the ID of the guard * minute most asleep.
        """
        # {guard_ID: {5: 1, 6: 2, 7:2, 8: 2, 9: 3, 10: 3, ... 58: 1}}
        # sum values to get minutes for each guard
        # get most common minute for worst guard
        pass

    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.data)
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))