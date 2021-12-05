#!/usr/bin/env python3
import sys, utils

def power_consumption(l: list):
    most, least = calculate_common(l)
    return int(most, 2) * int(least, 2)

def calculate_common(l: list):
    counter = [0 for _ in range(len(l[0]))]
    for line in l:
        for i in range(len(line)):
            if line[i] == '1':
                counter[i] += 1

    half_len = len(l) / 2
    most_common, least_common = '', ''

    for val in counter:
        if val >= half_len:
            most_common += '1'
            least_common += '0'
        else:
            most_common += '0'
            least_common += '1'
    return most_common, least_common

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    f = utils.File(sys.argv[1])

    print(power_consumption(f.get_strings()))


