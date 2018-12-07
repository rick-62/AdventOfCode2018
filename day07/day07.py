import re
from collections import defaultdict

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        r = re.compile(r'Step\s([A-Z]).+step\s([A-Z])')
        with open(filename) as f:
            data = (re.findall(r, line)[0] for line in f.readlines())
        return data

    def build_order(self, nodes, stack=set(), output=''):
        for s, n in nodes.items():
            if s not in output and n.parents.issubset(output):
                stack.add(s)
        try:
            output += min(stack)
            stack.remove(min(stack))
        except ValueError:
            return output

        return self.build_order(nodes, stack, output)

    def solve_part1(self):
        """Returns result for part 1"""
        nodes = defaultdict(Node)
        for p,c in self.data:
            nodes[c].add_parent(p)
            nodes[p].add_child(c)
               
        return self.build_order(nodes)
        

    def solve_part2(self):
        """Returns result for part 2"""
        pass


class Node:

    def __init__(self):
        self._children = set()
        self._parents = set()

    def add_child(self, child):
        self._children.add(child)

    def add_parent(self, parent):
        self._parents.add(parent)

    def remove_parent(self, parent):
        self._parents.remove(parent)

    @property
    def children(self):
        return self._children

    @property
    def parents(self):
        return self._parents

        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))