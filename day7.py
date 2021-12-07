#!/usr/bin/env python3
import sys, utils

class OptimizeHoriz(object): 
    def __init__(self, init_state, progr=False):
        self.positions = init_state
        self.progr = progr

    def calc_horiz(self):
        positions = [0 for _ in range(max(self.positions))]
        for x in range(len(positions)):
            for cp in range(len(self.positions)):
                positions[x] += self.fuel(x, self.positions[cp])
        return min(positions)

    def fuel(self, x1, x2):
        n = abs(x1-x2)
        if self.progr:
            n = int(n * (1+n)/2)
        return n



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    init_state = utils.File(sys.argv[1]).get_ints_line()
    optim = OptimizeHoriz(init_state)
    print(optim.calc_horiz())
    
    optim2 = OptimizeHoriz(init_state, True)
    print(optim2.calc_horiz())
    

