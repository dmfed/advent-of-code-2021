#!/usr/bin/env python3
import sys, utils

def where_are_we_going(l: list):
    h, v = 0, 0
    for d in l:
        d = d.split()
        if d[0] == 'forward':
            h += int(d[1]) 
        elif d[0] == 'down':
            v += int(d[1])
        elif d[0] == 'up':
            v -= int(d[1])
    return h * v 

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    f = utils.File(sys.argv[1])

    print(where_are_we_going(f.get_strings()))


