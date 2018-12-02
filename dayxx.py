
class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = [int(m) for m in f.readlines()]
        return data

    def solve_part1(self):
        """Returns result for part 1"""
        pass

    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))