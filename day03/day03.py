from itertools import product
from collections import defaultdict

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (dict)"""
        with open(filename) as f:
            data = {}
            for line in f:
                _id, values = line.split(' @ ')                  # '#123 @ 1,2: 2x3' --> ['#123', '1,2: 2x3']
                position, area = values.split(': ')              # '1,2: 2x3' --> ['1,2', '2x3']
                _id = int(_id[1:])                               # '#123' --> 123
                position = [int(p) for p in position.split(',')] # '1,2' --> [1, 2]
                area = [int(a) for a in area.split('x')]         # '2x3' --> [2, 3]
                data[_id] = (position, area)                     # {123: ([1, 2], [2, 3])}
        return data

    def solve_part1(self):
        """
        Returns result for part 1

        Each claim consists of:
        - The number of inches between the left edge of the fabric and 
        the left edge of the rectangle.
        - The number of inches between the top edge of the fabric and 
        the top edge of the rectangle.
        - The width of the rectangle in inches.
        - The height of the rectangle in inches.

        Returns the number of square inches which overlap.        
        """
        dct_coords = defaultdict(int)
        for _id, values in self.data.items():
            position, area = values
            X = range(position[0], position[0] + area[0])
            Y = range(position[1], position[1] + area[1])
            for coordinate in product(X, Y):
                dct_coords[coordinate] += 1

        counter = 0
        for count in dct_coords.values():
            if count > 1:
                counter += 1

        return counter

            



    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))