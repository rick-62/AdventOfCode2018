from string import ascii_lowercase

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = f.read().strip('\n')
        return data

    
    def reduce_polymer(self, polymer):
        """
        Remove units which are adjacent, and 
        of opposing Capitilisation e.g. "a" and "A".
        Returns remaining units.
        """
        new_polymer = ['']
        for unit in polymer:
            prev = new_polymer[-1]
            if unit != prev and unit.lower() == prev.lower():
                new_polymer.pop()
            else:
                new_polymer.append(unit)
        return new_polymer[1:]


    def solve_part1(self):
        """
        Returns result for part 1:
        Returns length of returned list of units.
        """
        return len(self.reduce_polymer(self.data))
        
        
    def solve_part2(self):
        """
        Returns result for part 2:
        Removes unwanted units after each unit type is removed, in turn.
        Returns minimum polymer length.
        """
        sizes = []
        polymer = self.reduce_polymer(self.data)  # speed up
        for l in ascii_lowercase:
            test_polymer = [u for u in polymer if u.lower() != l]
            length = len(self.reduce_polymer(test_polymer))
            sizes.append(length)
        return min(sizes)


if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))