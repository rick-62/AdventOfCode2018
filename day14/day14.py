from collections import deque
from functools import lru_cache
from collections import defaultdict
import numpy as np
import time

timing_dct = defaultdict(list)
def timing(f):
    def wrap(*args):
        name = f.__name__
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        timing_dct[name].append(time2 - time1)
        return ret
    return wrap





# def extract_recipes(self, start, end):
#     code = ''
#     for i in range(start, end+1):
#         code += self.recipes[i]
#     return code

# def printer(start=0):
#     out = ''
#     for i in range(start, len(self.recipes)):
#         out += ' ' + self.recipes[i]
#         if i == self.elf1:
#             out += '*'
#         if i == self.elf2:
#             out += '**'
#     input(out)

    
# @timing
# def part1(self, puzzle):
#     self.simulate(puzzle+10)
#     return self.extract_recipes(puzzle, puzzle+9)

def part1(puzzle):
    elf1 = 0
    elf2 = 1
    recipes = '37'
    dct_next = {0:3, 1:7}
    keys = dct_next.keys
    l = len(recipes)
    while l < puzzle+10:
        if elf1 in keys():
            r1 = dct_next[elf1]
        else:
            r1 = int(recipes[elf1])
            dct_next[elf1] = r1
        if elf2 in keys():
            r2 = dct_next[elf2]
        else:
            r2 = int(recipes[elf2])
            dct_next[elf2] = r2
        recipes += str(r1 + r2)
        elf1 += 1 + r1
        elf2 += 1 + r2
        l = len(recipes)
        if elf1 >= l:
            elf1 %= l
        if elf2 >= l:
            elf2 %= l
    return recipes[puzzle:]
        


def part2(puzzle):
    elf1 = 0
    elf2 = 1
    recipes = '37'
    dct_next = {0:3, 1:7}
    keys = dct_next.keys
    l = len(recipes)
    while puzzle not in recipes[-7:]:
        if elf1 in keys():
            r1 = dct_next[elf1]
        else:
            r1 = int(recipes[elf1])
            dct_next[elf1] = r1
        if elf2 in keys():
            r2 = dct_next[elf2]
        else:
            r2 = int(recipes[elf2])
            dct_next[elf2] = r2
        recipes += str(r1 + r2)
        elf1 += 1 + r1
        elf2 += 1 + r2
        l = len(recipes)
        if elf1 >= l:
            elf1 %= l
        if elf2 >= l:
            elf2 %= l

    return recipes.index(puzzle)

# def part2(puzzle):
#     elf1 = 0
#     elf2 = 1
#     recipes = deque([3,7])
#     dct_next = {0:3, 1:7}
#     keys = dct_next.keys
#     l = len(recipes)
#     lp = len(puzzle)
#     i = False
#     while not i:
#         if elf1 in keys():
#             r1 = dct_next[elf1]
#         else:
#             r1 = recipes[elf1]
#             dct_next[elf1] = r1
#         if elf2 in keys():
#             r2 = dct_next[elf2]
#         else:
#             r2 = recipes[elf2]
#             dct_next[elf2] = r2
#         s = r1 + r2
#         if s > 9:
#             recipes.append(1)
#             recipes.append(s % 10)
#         else:
#             recipes.append(s)
#         elf1 += 1 + r1
#         elf2 += 1 + r2
#         l = len(recipes)
#         if elf1 >= l:
#             elf1 %= l
#         if elf2 >= l:
#             elf2 %= l
#         try:
#             if recipes[-lp] == int(puzzle[0]):
#                 i = l-lp
#                 for j in range(1,lp):
#                     if recipes[-lp+j] != int(puzzle[j]):
#                         i = False
#                         break
                

#         except IndexError:
#             pass



#     return i

            
            


        





if __name__ == "__main__":

    puzzle = input("Enter Puzzle Input: ")
    print("Part 1: {}".format(part1(int(puzzle))))
    print("Part 2: {}".format(part2(puzzle)))
    for k,v in timing_dct.items():
        count = len(v)
        avg = np.mean(v)
        print(f"{k}\t Avg: {avg*1000:.5f}\t Cnt: {count}")

