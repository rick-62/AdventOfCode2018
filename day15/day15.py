import numpy as np

def printer(arr):
    for row in arr:
        print(''.join(row), )

def manhatten(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def adjacent(l, arr):
    x, y = l
    adj = [(x-1, y),(x, y+1),(x+1, y),(x, y-1)]
    return [(n, arr[n]) for n in adj if arr[n] not in '#']

class character:

    def __init__(self, ctype, loc):
        self.type = ctype
        self.loc = loc
        self.enemy = 'E' if ctype == 'G' else 'G'

    def __repr__(self):
        return self.type
    

## Import data ##
filename = "test.txt"
with open(filename) as f:
    arr = np.array([list(row.strip('\n')) for row in f.readlines()])

## Assign characters ##
C = []
for c in zip(*np.where((arr == 'G') | (arr == 'E'))):
    C.append(character(arr[c], c))

## TODO: LOOP ##

## sort characters by location - top to bottom ##
C = sorted(C, key=lambda c: c.loc)

## Test ##
c = C[0]


# available directions - check for "." only or other opposing character (stop and attk)
# check to ensure opposing character has available adjacent ".", otherwise do nothing
# for each available direction:
    # repeat the following until the target has been reached
    # calc steps taken (1 at beginning)
    # calc manhatten distance from each elf/goblin (pick shortest)
    # score = sum of distance and steps taken
    # add steps with scores, steps and distance to stack
    # select lowest score as next 
# from top to bottom, left to right pick direction with lowest score


print(adjacent(c.loc, arr))


    












