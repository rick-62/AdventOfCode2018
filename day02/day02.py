from collections import Counter
from itertools import combinations

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = f.readlines()
        return data

    def solve_part1(self):
        """
        Returns result for part 1:
        Counts the number that have an ID containing 
        exactly two of any letter and then separately 
        counting those with exactly three of any letter. 
        Two counts muliplied together to get a 
        rudimentary checksum
        """
        cnt = Counter()
        for row in self.data:
            letter_counts = set(Counter(row).values())  # abbcd --> (1,2)
            cnt += Counter(letter_counts)
        return cnt[2] * cnt[3]

    def solve_part2(self):
        """
        Returns result for part 2:
        Identifies the two boxes which have IDs 
        which differ by exactly one character 
        at the same position in both strings
        and returns the common letters between the two IDs.
        """
        length = len(self.data[0])  # length of each id is the same
        for id1, id2 in combinations(self.data, 2):
            common_letters = [a for a, b in zip(id1, id2) if a == b]
            if len(common_letters) == (length - 1):
                return ''.join(common_letters)
        

if __name__ == "__main__":
    puzzle = Puzzle(test=False)
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))