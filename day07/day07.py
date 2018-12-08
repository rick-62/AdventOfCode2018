import re
from collections import defaultdict
from itertools import count
from string import ascii_uppercase

class Puzzle:

    def __init__(self, test=False):
        if test:
            filename = "test.txt" 
            self.base_time = 0 
            self.workers = 2
        else:
            filename = "input.txt"
            self.base_time = 60 
            self.workers = 5
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory"""
        r = re.compile(r'Step\s([A-Z]).+step\s([A-Z])')
        with open(filename) as f:
            data = [re.findall(r, line)[0] for line in f.readlines()]
        return data

    def prepare_nodes(self):
        """Assigns each step a node and adds parent/child nodes"""
        nodes = defaultdict(Node)
        for p,c in self.data:
            nodes[c].add_parent(p)
            nodes[p].add_child(c)
        return nodes

    def build_order(self, nodes, stack=set(), output=''):
        """
        Recursive function to check for all available steps
        i.e. parent steps have been completed, adds them to
        the output in ascending order, and then repeats until
        all steps completed.
        Returns output as a string.
        """
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
        nodes = self.prepare_nodes()
        return self.build_order(nodes)

    def next_jobs(self, nodes, complete, allocated, stack=[]):
        """
        Check for all available jobs i.e. parent jobs have been completed, 
        adds them to the stack in ascending order, and removes
        already allocated jobs.
        Returns stack as a list.
        """
        for s, n in nodes.items():
            if s not in complete and n.parents.issubset(complete):
                stack.append(s)
        stack.sort()
        return [j for j in stack if j not in allocated]

    def solve_part2(self):
        """Returns result for part 2"""
        nodes = self.prepare_nodes()
        steps = len(self.solve_part1())
        workers = set(Worker() for _ in range(self.workers))
        complete = []
        allocated = []
        for second in count():
            complete += [l for l in [w.check_completed() for w in workers] if l]
            for j in self.next_jobs(nodes, complete, allocated):
                for w in workers:
                    if w.is_free:
                        d = self.base_time + ascii_uppercase.index(j) + 1
                        w.give_job(j, d)
                        allocated += j
                        break
            if steps == len(complete):
                return second


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


class Worker:

    def __init__(self):
        self._job = None
        self._remaining = 0

    def give_job(self, job, duration):
        assert not self._job
        self._job = job
        self._remaining = duration

    @property
    def is_free(self):
        return self._remaining == 0 and not self._job 

    def check_completed(self):
        if not self._job:
            return
        self._remaining -= 1
        if self._remaining == 0:
            return self._release_job()
    
    def _release_job(self):
        job = self._job
        self._job = None
        return job



if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))