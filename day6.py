#!/usr/bin/env python3
import sys, utils

class Fish(object):
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def tick(self):
        out = None
        self.state -= 1
        if self.state == -1:
            self.state = 6
            out = Fish(8)
        return out

class Simulator(object):
    def __init__(self, init_states):
        self.fishes = [Fish(n) for n in init_states]

    def tick(self):
        new_gen = []
        for fish in self.fishes:
            new_fish = fish.tick()
            if new_fish:
                new_gen.append(new_fish)
        self.fishes.extend(new_gen) # LOL :) :) :) we'll need 256 generations

    def get_total_fishes(self):
        return len(self.fishes)

class Simulator2(object):
    def __init__(self, init_states):
        self.fish_states = [0 for _ in range(9)]
        for fish in init_states:
            self.fish_states[fish] += 1

    def __str__(self):
        out = 'Fishes with ttl:\n'
        for i in range(0, 9):
            out += f'{i} gens: {self.fish_states[i]}\n'
        return out

    def tick(self):
        new_gen = self.fish_states[0] # this many newcomers
        for i in range(1, len(self.fish_states)): # let's just rotate
            self.fish_states[i-1] = self.fish_states[i]
        self.fish_states[6] += new_gen # fishes with ttl 6 after producing new gen
        self.fish_states[8] = new_gen # new gen with ttl 6


    def get_total_fishes(self):
        return sum(self.fish_states)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    fishes = utils.File(sys.argv[1]).get_ints_line()
    
    sim = Simulator(fishes)
    for _ in range(80): # 80 generations are ok but 256 are not :)
        sim.tick()
    print(sim.get_total_fishes())

    sim2 = Simulator2(fishes)
    for _ in range(256):
        sim2.tick()
        #print(sim2)
        #print('total:', sim2.get_total_fishes())
    print(sim2.get_total_fishes())



