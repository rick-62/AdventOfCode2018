
class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = f.read().strip('\n')
        return data

    
    def destroy_opposite_polarity(self, polymer):
        """
        Recursive function, to repeatedly remove units which
        are adjacent, and of opposing Capitilisation e.g. "a" and "A".
        Returns length of remaining units.
        """
        polymer_length = len(polymer)
        new_polymer = []

        i = 0
        while i < (polymer_length - 1):
            if abs(polymer[i] - polymer[i + 1]) == 32:  # difference in ascii codes between lower and upper cases
                i += 2
            else:
                new_polymer.append(polymer[i])
                i += 1
        new_polymer.append(polymer[-1])
            

        if len(new_polymer) == polymer_length:
            return polymer_length
        else:
            return self.destroy_opposite_polarity(new_polymer)

            


    def solve_part1(self):
        """
        Returns result for part 1:
        Converts polymer string into ascii code, then
        calls a function/method to remove unwanted units.
        Returns length of returned list of units.
        """
        polymer = bytes(self.data, 'ascii')
        return self.destroy_opposite_polarity(polymer)
        
        
    def solve_part2(self):
        """
        Returns result for part 2:
        Converts polymer string into ascii code, then 
        removes each unit type from the polymer and
        calls a function/method to remove unwanted units.
        Returns minimum polymer length.
        """
        polymer = bytes(self.data, 'ascii')
        sizes = []
        for utypes in zip(range(65, 90), range(97, 122)):
            test_polymer = [b for b in polymer if b not in utypes]
            polymer_length = self.destroy_opposite_polarity(test_polymer)
            sizes.append(polymer_length)
        return min(sizes)


if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))