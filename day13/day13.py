import time
import os
import numpy as np
from itertools import cycle



class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.arr = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            lst = [list(l.strip('\n')) for l in f.readlines()]
            arr = np.array(lst)
        return arr

    def printer(self, arr, pause=1):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in arr:
            print(''.join(row))
        time.sleep(pause)

    def create_carts(self, arr):
        carts = []
        for c in '<>^v':
            i,j = np.where(arr == c)
            for l in zip(i,j):
                carts.append(Cart(l,c))
        return carts

    def update(self, cart, arr):
        arr[cart.loc] = cart.track
        x,y = cart.next_loc()

        cart.update(arr[x,y])
        arr[x,y] = cart.cart
        self.arr = arr

    def check_collided(self, carts):
        for c in carts:
            if c.collide:
                return c.loc

    def order_carts(self, carts):
        locs = [c.loc for c in carts]
        return [c for _,c in zip(locs, carts)]
    

    def solve_part1(self):
        """Returns result for part 1"""
        carts = self.create_carts(self.arr)

        while True:
            self.printer(self.arr)
            carts = self.order_carts(carts)
            for c in carts:
                self.update(c, self.arr)

            loc = self.check_collided(carts)
            if loc != None:
                break

        return loc




        





    def solve_part2(self):
        """Returns result for part 2"""
        pass
        
class Cart:
    D = {'<': (0,-1), 
         '>': (0,1),
         '^': (-1,0),
         'v': (1,0)}
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    def __init__(self, location, direction):
        self.loc = location
        self.dir = self.D.get(direction)
        self.track = '-' if direction in '<>' else '|'
        self.collide = False

    def next_loc(self):
        x = self.loc[0] + self.dir[0]
        y = self.loc[1] + self.dir[1]
        return x,y 
        

    def update(self, track):
        self.loc = self.next_loc()
        if self.track == track:
            pass
        elif track == '+':
            self.dir = next(self._cross_road())
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
        for d in cycle([-1, 0, 1]):
            r = self._rotate(d)
            yield r

    def _rotate(self, d):
        i = self.dirs.index(self.dir)
        i += d
        i = i if i < 4 else 0
        return self.dirs[i]

    def cart(self):
        for k,v in self.D:
            if self.dir == v:
                return k
 

        

    

if __name__ == "__main__":
    puzzle = Puzzle(test=True)
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))