from collections import defaultdict

class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory"""
        with open(filename) as f:
            initial = f.readline().strip('initial state: ').strip('\n')
            dot = lambda:'.'
            state = defaultdict(dot)
            for i,s in enumerate(initial):
                state[i] = s            
            patterns = {l[:5]:l[9] for l in f.readlines() if l != '\n'}
        self.patterns = patterns
        self.state = state

    def print_state(self, state):
        ks = list(state.keys())
        ks.sort()
        s = ''.join((state[k] for k in ks))
        s = s.strip('.')
        print(s)
        return s

    def transform_state(self, state):
        S = state.copy()
        P = set(k for k,v in S.items() if v == '#')
        for k in range(min(P)-2, max(P)+2):
            ptn = ''.join((S[k+i] for i in (-2,-1,0,1,2)))
            state[k] = self.patterns.get(ptn, S[k])
        return state

    def solve_part1(self):
        """Returns result for part 1"""
        state = self.state.copy()
        for _ in range(20):
            self.print_state(state)
            state = self.transform_state(state)       
        return sum(k for k,v in state.items() if v =='#')



    def solve_part2(self):
        """Returns result for part 2"""
        state = self.state.copy()
        g = 0
        s = self.print_state(state)
        dct = {self.print_state(state): g}
        while True:
            g += 1
            state = self.transform_state(state)
            s = self.print_state(state)
            if s in dct.keys():
                break
            dct[s] = g

        for _ in range(10):
            g += 1
            state = self.transform_state(state)
            print(g, max(state.keys()), sum(k for k,v in state.items() if v =='#'))

        ## create equation
        e = lambda g: 62 * (g-100) + 6855
        
        return e(50000000000)



        

        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))