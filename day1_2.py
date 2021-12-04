#!/usr/bin/env python3
import sys, utils

def find_increasing_window(l: list):
    win = l[:3]  
    count = 0
    for n in range(3, len(l)):
        new_win = [l[n-2], l[n-1], l[n]]
        if sum(new_win) > sum(win):
            count += 1
        win = new_win
    return count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()
    f = utils.File(sys.argv[1])
    print(find_increasing_window(f.get_ints()))


