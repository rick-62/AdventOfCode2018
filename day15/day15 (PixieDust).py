import numpy as np
import time
from itertools import chain
from queue import PriorityQueue
import os

def printer(arr, t=0.5):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in arr:
        print(''.join(row), )
    time.sleep(t)

def manhatten(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def adjacent(l, arr):
    x, y = l
    adj = [(x-1, y),(x, y+1),(x+1, y),(x, y-1)]
    return {n: arr[n] for n in adj if arr[n] not in '#'}

def spaces(l, arr):
    return sorted([k for k,v in adjacent(l, arr).items() if v == '.'])

def closest(l, targets):
    sort = sorted([t for t in targets])
    return min(manhatten(l, t) for t in sort)


def AStar(start, arr, targets):
    
    q = PriorityQueue()
    q.put((0, start))
    seen = {start: 0}
    viz = arr.copy()

    while not q.empty():
        current = q.get()[1]

        if current in targets:
            break

        available = spaces(current, arr)

        # viz[current] = '@'
        # printer(viz)

        for nxt in available:

            
            steps = seen[current] + 1
            
            if nxt not in seen.keys() or steps < seen.get(nxt, 0):

                seen[nxt] = steps
                score = steps + closest(current, targets)
                q.put((score, nxt))


    reach = seen.keys() & targets
    if len(reach) == 0:
        return -1
    mn = min([seen[x] for x in reach])
    best = sorted([k for k in reach if seen[k] == mn])
    return seen[best[0]]



class character:

    def __init__(self, ctype, loc, arr):
        self.type = ctype
        self.loc = loc
        self.enemy = 'E' if ctype == 'G' else 'G'
        self.arr = arr
        self.hp = 200
        self.attk = 3

    @property
    def dead(self):
        return self.hp <= 0
        
    @property
    def adjacent(self):
        return adjacent(self.loc, self.arr)

    @property
    def spaces(self):
        return sorted([k for k,v in self.adjacent.items() if v == '.'])

    @property
    def in_battle(self):
        return self.enemy in self.adjacent.values()

    @property
    def adj_enemies(self):
        return [k for k,v in self.adjacent.items() if v == self.enemy]

    def __repr__(self):
        return self.type
    



def main(plus=0):

    ## Import data ##
    filename = "input.txt"
    with open(filename) as f:
        arr = np.array([list(row.strip('\n')) for row in f.readlines()])

    ## Assign characters ##
    C = []
    for c in zip(*np.where((arr == 'G') | (arr == 'E'))):
        C.append(character(arr[c], c, arr))

    # for part 2
    for c in C:
        if c.type == 'E':
            c.attk += plus

    ## LOOP ##
    # printer(arr, t=0.01)


    rounds = 0
    while True:

        

        ## sort characters by location - top to bottom ##

        C = sorted([c for c in C if not c.dead], key=lambda c: c.loc)

        for c in C:

            if c.dead:
                continue

            # Check whether any more enemies available
            enemies = [e for e in C if e.type == c.enemy and not e.dead]
            if len(enemies) == 0:
                sum_hp = sum([c.hp for c in C if not c.dead])
                print("Complete - no more enemies")
                print(f"Rounds:{rounds}\t Total_HP:{sum_hp}\t Output:{rounds*sum_hp}")
                return c.type

            if not c.in_battle:

                # creates list of target squares (around enemy)
                targets = set(chain.from_iterable([e.spaces for e in enemies]))

                if len(targets) == 0:
                    continue  # skip to next character

                # best direction to go next
                mn = np.inf
                next_loc = None
                for s in c.spaces.copy():
                    steps = AStar(s, arr, targets)
                    if steps == -1:
                        continue
                    elif steps < mn: 
                        mn = steps
                        next_loc = s

                # refresh character and update arr
                if next_loc != None:
                    arr[c.loc] = '.'
                    arr[next_loc] = c
                    c.loc = next_loc
                    # input()
                    # printer(arr, t=0.01)
                    

            if c.in_battle:

                defenders = sorted([e for e in enemies if e.loc in c.adj_enemies], key=lambda e: e.loc)

                mn = np.inf
                ne = None
                for e in defenders:
                    if e.hp < mn:
                        mn = e.hp 
                        ne = e 
                
                ne.hp -= c.attk

                if ne.dead:
                    arr[ne.loc] = '.'
                    # printer(arr, t=0.01)
                    if ne.type == 'E':
                        return 'G'  # No elves can die

        # for c in C:
        #     print(c.hp)
        
        # printer(arr, t=0.05)
        
        rounds += 1

print("part1:")
part1 = main()

print("part2:")
winner = part1

plus = 0
while winner != 'E':
    plus += 1
    winner = main(plus=plus)


        
        









    








    





    












