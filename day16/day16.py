import numpy as np
import ast
from collections import defaultdict, Counter

funcs = {
'addr': lambda A,B,r: r[A] + r[B],
'addi': lambda A,B,r: r[A] + B ,
'mulr': lambda A,B,r: r[A] * r[B],
'muli': lambda A,B,r: r[A] * B ,
'banr': lambda A,B,r: r[A] & r[B],
'bani': lambda A,B,r: r[A] & B ,
'borr': lambda A,B,r: r[A] | r[B],
'bori': lambda A,B,r: r[A] | B ,
'setr': lambda A,B,r: r[A],
'seti': lambda A,B,r: A ,
'gtir': lambda A,B,r: A > r[B],
'gtri': lambda A,B,r: r[A] > B ,
'gtrr': lambda A,B,r: r[A] > r[B],
'eqir': lambda A,B,r: A == r[B],
'eqri': lambda A,B,r: r[A] == B ,
'eqrr': lambda A,B,r: r[A] == r[B] }


class Puzzle:


    def import_data(self, filename="input_part1.txt"):
        before = []
        after = []
        opcode = []
        convert = lambda line: ast.literal_eval(line[8:])
        with open("input_part1.txt") as f:
            for line in f.readlines():
                line = line.strip('\n')
                if line.startswith('Before'):
                    before.append(convert(line))
                elif line.startswith('After'):
                    after.append(convert(line))
                elif line == '':
                    continue
                else:
                    opcode.append([int(x) for x in line.split(' ')])
        return before, after, opcode



    def solve_part1(self):
        """Returns result for part 1"""
    
        before, after, opcode = self.import_data()

        count = 0

        for r1, r2, op in zip(before, after, opcode):

            O,A,B,C = op
            
            i = 0
            for v in funcs.values():
                r = r1.copy()
                r[C] = v(A,B,r1)
                i += r == r2
                if i >= 3:
                    count += 1
                    break

        return count
                

    def get_opcodes(self):

        before, after, opcode = self.import_data()

        operations = defaultdict(set)
        nonoperations = defaultdict(set)
        confirmed = {}
        found = set()

        while len(confirmed.keys()) < 16:
            operations.clear()

            for r1, r2, op in zip(before, after, opcode):

                O,A,B,C = op
            
                for k,v in funcs.items():

                    if k in confirmed.keys():
                        continue

                    r = r1.copy()
                    r[C] = v(A,B,r1)

                    if r == r2:
                        operations[k].add(O)

                    elif r != r2:
                        nonoperations[k].add(O)

            
            for k,v in operations.copy().items():
                operations[k] -= nonoperations[k]
                operations[k] -= found
            
                if len(operations[k]) == 1:
                    confirmed[k] = operations[k].pop()
                    found.add(confirmed[k])


        ops = {v:k for k,v in confirmed.items()}

        return ops


    def solve_part2(self):
        """Returns result for part 2"""
        r = [0,0,0,0]
        ops = self.get_opcodes()

        with open("input_part2.txt") as f:
            for line in f.readlines():
                O,A,B,C = [int(x) for x in line.split(' ')]
                r[C] = funcs[ops[O]](A,B,r)

        return r
        
        


        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))