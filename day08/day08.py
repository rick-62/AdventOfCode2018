from collections import deque

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        self.part1_sum = 0
        
    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            data = deque(int(n) for n in f.read().split())
        return data

    def create_nodes(self, d):
        """
        Creates tree of node objects, recusively assigning children and 
        adding metadata.
        Returns Parent Node of tree, which contains all child nodes.
        """
        n = Node()
        c = d.popleft()
        m = d.popleft()
        for _ in range(c):
            n.children = self.create_nodes(d)
        for _ in range(m):
            n.metadata = d.popleft()
        self.part1_sum += sum(n.metadata)
        return n

    def solve_part1(self):
        """Returns result for part 1"""
        self.create_nodes(self.data.copy())
        return self.part1_sum

    def solve_part2(self):
        """Returns result for part 2"""
        parent = self.create_nodes(self.data.copy())
        return parent.value

class Node:

    def __init__(self):
        self._children = []
        self._metadata = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, child):
        self._children.append(child)

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        self._metadata.append(metadata)

    @property
    def value(self):
        if len(self._children) == 0:
            return sum(self._metadata)
        else:
            return sum(self._children[i-1].value 
                       for i in self._metadata 
                       if i <= len(self._children))
    

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))