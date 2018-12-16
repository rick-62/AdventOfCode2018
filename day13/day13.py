import time
import os
import numpy as np
from itertools import cycle
from collections import deque


def load_into_memory():
    with open(filename) as f:
        lst = [list(l.strip('\n')) for l in f.readlines()]
        arr = np.array(lst)
    return arr


def printer(arr, pause=1):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in arr:
        print(''.join(row))
    if pause:
        time.sleep(pause)
    else:
        input()

def create_carts(arr):
    carts = []
    for c in '<>^v':
        i,j = np.where(arr == c)
        for l in zip(i,j):
            carts.append(Cart(l,c))
    return carts

def update(cart, arr):
    arr[cart.loc] = cart.track
    x,y = cart.next_loc()
    cart.update(arr[x,y])
    arr[x,y] = cart.cart()
    return arr

def check_collided(carts):
    for c in carts:
        if c.collide:
            return c.loc

def order_carts(carts):
    carts = sorted(carts, key=lambda x: x.loc)
    return carts
    

def solve_part1():
    """Returns result for part 1"""
    arr = load_into_memory()
    carts = create_carts(arr)

    while True:
        # if test: printer(arr, pause=0)
        carts = order_carts(carts)
        for c in carts:
            update(c, arr)

        loc = check_collided(carts)
        if loc != None:
            break

    return loc


def solve_part2():
    """Returns result for part 2"""
    pass

        
class Cart:
    D = {'<': (0,-1), 
         '>': (0, 1),
         '^': (-1,0),
         'v': (1, 0)}
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]

    def __init__(self, location, direction):
        self.loc = location
        self.dir = self.D.get(direction)
        self.track = '-' if direction in '<>' else '|'
        self.collide = False
        self.cycle = cycle([-1,0,1])

    def next_loc(self):
        x = self.loc[0] + self.dir[0]
        y = self.loc[1] + self.dir[1]
        return x,y 
        
    def update(self, track):
        self.loc = self.next_loc()
        if track == '+':
            self.dir = self._cross_road()
        elif track in '\\/':
            self.dir = self._corner(track)
        elif track in '<>^v':
            self.collide = True
        elif track in '|-':
            pass
        else:
            print("ERROR: cart came of the tracks {}".format(self.loc))
        self.track = track


    def _corner(self, track):
        C = {(-1,0): {'\\': (0,-1), '/':(0, 1)},
             (1, 0): {'\\': (0, 1), '/':(0,-1)},
             (0,-1): {'\\': (-1,0), '/':(1, 0)},
             (0, 1): {'\\': (1, 0), '/':(-1,0)}}
        return C[self.dir][track]
        
    def _cross_road(self):
        r = self._rotate(next(self.cycle))
        return r

    def _rotate(self, d):
        i = self.dirs.index(self.dir)
        i += d
        i = i if i < 4 else 0
        return self.dirs[i]

    def cart(self):
        for k,v in self.D.items():
            if self.dir == v:
                return k

    def __str__(self):
        return str(self.loc)

    def __repr__(self):
        return str(self.loc)
 

if __name__ == "__main__":
    test = False
    filename = "test.txt" if test else "input.txt"
    print("Part 1 = {}".format(solve_part1()))
    print("Part 2 = {}".format(solve_part2()))