import re
import numpy as np
import time
import os


class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        self.arr = None
        self.sub_arr = None
        
    def load_into_memory(self, filename):
        """load input into memory (list)"""
        with open(filename) as f:
            data = f.readlines()
        return data

    def extract_coords(self):
        d = self.data
        py = re.compile(r'y=(\d+)..(\d+)?')
        px = re.compile(r'x=(\d+)..(\d+)?')
        X,Y = [],[]
        for line in d:
            Y.append([int(r) for r in re.findall(py, line)[0] if r != ''])
            X.append([int(r) for r in re.findall(px, line)[0] if r != ''])
        return X,Y

    def create_arr(self, X, Y):
        i_max = max([max(y) for y in Y])
        j_max = max([max(x) for x in X])
        self.j_min = min([min(x) for x in X])

        self.arr = np.full((i_max+1, j_max+2), ['.'], dtype=str)
        self.arr[:, :self.j_min-1] = '@'
        self.arr[(0, 500)] = '+'

        for i,j in zip(Y,X):
            if len(i) == 2:
                self.arr[i[0]:i[1]+1, j[0]] = '#'
            elif len(j) == 2:
                self.arr[i[0], j[0]:j[1]+1] = '#'
    

    def printer(self, arr, t=0.01):

        os.system('cls' if os.name == 'nt' else 'clear')

        # for row in arr[:,self.j_min-1:]:
            # print(''.join(row))

        for row in arr:
            print(''.join(row))

        time.sleep(t)


    def drop(self, curr):

        while True:
            nxt = (curr[0] + 1 , curr[1])
            try:
                if self.arr[nxt] == '|':
                    return (0, 500)
                if self.arr[nxt] == '.':
                    self.arr[curr] = '.' if self.arr[curr] != '+' else '+'
                    self.arr[nxt] = '|'
                    curr = nxt
                else:
                    return curr
            except IndexError:
                return (0, 500)

            # self.printer()


    def is_container(self, curr):

        row, col = curr

        clay = np.where(self.arr[row] == '#')[0]
        left, right = False, False
        for i in range(1, len(clay)):
            if clay[i-1] < col < clay[i]:
                left, right = clay[i-1], clay[i]

        if left and right:
            base = np.all(self.arr[row+1, left+1:right] != '.')

            if base:
                self.arr[row, left+1:right] = '~'
                # self.printer()
                return True
        
        return False

    
    def check_flow(self, curr):

        row, col = curr
        flow = np.where(self.arr[row] != '.')[0]
        indx = np.argwhere(flow==col)
        flow = np.delete(flow, indx)
        left, right = False, False
        for i in range(1, len(flow)):
            if flow[i-1] < col < flow[i]:
                left, right = flow[i-1], flow[i]

        base = False
        if left and right:
            base = np.all(self.arr[row+1, left+1:right] != '.')

        if base:
                self.arr[row, left+1:right] = '|'
                # self.printer()
                return True
        
        return False


    def traverse(self, curr):
        
        if self.check_flow(curr):
            return (0, 500)

        left = True


        while True:
            row, col = curr

            if left:
                nxt = (row, col-1)
                base = (row+1, col-1)
                if self.arr[nxt] == '.':
                    self.arr[nxt] = '|'
                    self.arr[curr] = '.'
                    curr = nxt
                    if self.arr[base] == '.':
                        return curr
                    if self.arr[base] == '|':
                        return (0, 500)
                else:
                    left = False
                
                
            
            else:  # right
                nxt = (row, col+1)
                base = (row+1, col+1)
                
                if self.arr[nxt] == '.':
                    self.arr[nxt] = '|'
                    self.arr[curr] = '.'
                    curr = nxt
                    if self.arr[base] == '.':
                        return curr
                    if self.arr[base] == '|':
                        return (0, 500)

            if '|' in self.arr[0]:
                pass
                return curr

            # self.printer()

    

    def solve_part1(self):
        """Returns result for part 1"""
        X,Y = self.extract_coords()
        self.create_arr(X,Y)
        self.sub_arr = self.arr[0:20, 480:520]
        self.printer(arr=self.sub_arr)


        start = (0, 500)
        curr = start
        while True:
            

            curr = self.drop(curr)
                
            if self.is_container(curr):
                curr = (0, 500)
                continue
            
            else:
                curr = self.traverse(curr)


            if '|' in self.arr[0]:
                pass
            if self.arr[1,500] == '|':
                break

            # self.printer(arr=self.sub_arr)
            # print(self.arr[0:20, 490:510])
            # print(curr)

        self.printer(arr=self.sub_arr)

        settled = np.count_nonzero(self.arr == '~')
        flow = np.count_nonzero(self.arr == '|')

        return (settled, flow, sum([settled, flow]))
        




    def solve_part2(self):
        """Returns result for part 2"""
        pass
        

if __name__ == "__main__":
    puzzle = Puzzle(test=False)
    print("Part 1 = {} + {} = {}".format(*puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))