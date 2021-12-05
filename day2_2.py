#!/usr/bin/env python3
import sys, utils

def where_are_we_going2(l: list):
    h, v = 0, 0
    aim = 0
    for d in l:
        d = d.split()
        n = int(d[1])
        if d[0] == 'forward':
            h += n 
            v += aim * n
        elif d[0] == 'down':
            aim += n
        elif d[0] == 'up':
            aim -= n
    return h * v 

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    f = utils.File(sys.argv[1])

    print(where_are_we_going2(f.get_strings()))


