#!/usr/bin/env python3
import sys, utils

class Board(object):
    def __init__(self, l):
        self.board = []
        self.won = False
        for row in l:
            vals = [[int(v), False] for v in row.split()]
            self.board.append(vals)

    def __str__(self):
        s = ''
        for row in self.board:
            s += "\t".join([str(n[0]) for n in row]) + '\n'
        return s

    def check(self, n):
        if self.won:
            return None
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j][0] == n:
                    self.board[i][j][1] = True
        return self.has_winning_row() or self.has_winning_column()

    def has_winning_row(self) -> list:
        for row in self.board:
            winning = True
            for val in row:
                if not val[1]:
                    winning = False
            if winning:
                return self.sum_unmarked()
        return None

    def has_winning_column(self) -> list:
        for x in range(len(self.board[0])):
            column = [row[x] for row in self.board] 
            winning = True
            for val in column:
                if not val[1]:
                    winning = False
            if winning:
                return self.sum_unmarked()
        return None

    def sum_unmarked(self) -> int:
        self.won = True
        total = 0
        for row in self.board:
            for value in row:
                if not value[1]:
                    total += value[0]
        return total

def get_numbers(l):
    nums = [int(n) for n in l[0].split(',')]
    return nums

def init_boards(l):
    boards = []
    for i in range(2, len(l)-4, 6):
        b = Board(l[i:i+5])
        boards.append(b)
    return boards

def solve(boards, nums):
    for n in nums:
        for board in boards:
            s = board.check(n)
            if s:
                return s * n
    return "FUCK!"

def last_winning(boards, nums):
    last = None
    for n in nums:
        for board in boards:
            s = board.check(n)
            if s:
                last = s * n
    return last

def process(l):
    nums = get_numbers(l)
    boards = init_boards(l)
    return last_winning(boards, nums)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    l = utils.File(sys.argv[1]).get_strings()
    print(process(l))



