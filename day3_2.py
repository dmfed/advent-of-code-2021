#!/usr/bin/env python3
import sys, utils

def life_support_rating(l: list):
    most, least = filter(l)
    return int(most, 2) * int(least, 2)

def count(l: list):
    counter = [0 for _ in range(len(l[0]))]
    for line in l:
        for i in range(len(line)):
            if line[i] == '1':
                counter[i] += 1

    half_len = len(l) / 2
    for i in range(len(counter)):
        if counter[i] >= half_len:
            counter[i] = ('1', '0')
        else:
            counter[i] = ('0', '1')
    return counter


def filter(l):
    pos = 0
    most = l.copy()
    least = l.copy()
    while len(most) > 1:
        counter = count(most)
        i = 0
        while i < len(most):
            if len(most) == 1:
                break
            elif most[i][pos] != counter[pos][0]:
                del most[i]
                continue
            i += 1
        pos += 1
    pos = 0
    while len(least) > 1:
        counter = count(least)
        i = 0
        while i < len(least):
            if len(least) == 1:
                break
            elif least[i][pos] != counter[pos][1]:
                del least[i]
                continue
            i += 1
        pos += 1
    return most[0], least[0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    f = utils.File(sys.argv[1])

    print(life_support_rating(f.get_strings()))


