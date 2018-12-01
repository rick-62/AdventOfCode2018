import itertools

class Puzzle:

    def __init__(self):
        self.mem_blocks = self.load_into_memory("input.txt")
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            mem_blocks = [int(m) for m in f.readlines()]
        return mem_blocks

    def solve_part1(self, input_freq=0):
        """Returns resulting frequency for part 1"""
        freq = input_freq
        for change in self.mem_blocks:
            freq += change
        return freq

    def solve_part2(self, input_freq=0):
        """Returns repeated frequency for part 2"""
        freq = input_freq
        freq_list = set()
        for change in itertools.cycle(self.mem_blocks):
            freq += change
            if freq in freq_list:
                return freq
            freq_list.add(freq)
        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))