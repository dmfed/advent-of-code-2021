#!/usr/bin/env python3
import sys, utils

def find_increasing(l: list):
    prev = 0
    count = 0
    for n in l:
        if n > prev:
            count += 1
        prev = n
    return count - 1 # because first measurement doesn't count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()
    f = utils.File(sys.argv[1])
    print(find_increasing(f.get_ints()))


