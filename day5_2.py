#!/usr/bin/env python3
import sys, utils

class Map(object):
    def __init__(self, x, y):
        self.points = []
        self._create_map(x, y)

    def __str__(self):
        s = f'maps size is {len(self.points)}x{len(self.points[0])}\n' 
        for y in range(len(self.points[0])):
            for x in range(len(self.points)):
                s += str(self.points[x][y])
            s += '\n'
        return s

    def _create_map(self, x, y):
        self.points = [[0 for _ in range(y+1)] for _ in range(x+1)]

    def _add_straight_line(self, x1, y1, x2, y2):
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            self._add_vertical(y1, y2, x1)
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            self._add_horizontal(x1, x2, y1)

    def _add_horizontal(self, x1, x2, y):
        for i in range(x1, x2+1):
            self.points[i][y] += 1

    def _add_vertical(self, y1, y2, x):
        for i in range(y1, y2+1):
            self.points[x][i] += 1

    def _add_diagonal(self, x1, y1, x2, y2):
        if x1 > x2: # switch em' to start with smaller x
            x1, y1, x2, y2 = x2, y2, x1, y1 
        if y1 < y2:
            self._add_top_to_bottom(x1, y1, x2, y2)
        else:
            self._add_bottom_to_top(x1, y1, x2, y2)

    def _add_top_to_bottom(self, x1, y1, x2, y2):
        x, y = x1, y1
        while x <= x2 and y <= y2:
            self.points[x][y] += 1
            x += 1
            y += 1

    def _add_bottom_to_top(self, x1, y1, x2, y2):
        x, y = x1, y1
        while x <= x2 and y >= y2:
            self.points[x][y] += 1
            x += 1
            y -= 1

    def add_point(self, x, y):
        self.points[x][y] = 8

    def add_line(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            self._add_straight_line(x1, y1, x2, y2)
        else:
            self._add_diagonal(x1, y1, x2, y2)

    def calculate_points(self, treshold) -> int:
        total = 0
        for row in self.points:
            for point in row:
                if point >= treshold:
                    total += 1
        return total

def find_max_coords(coords):
    x, y = 0, 0
    for group in coords:
        x = max(x, group[0], group[2])
        y = max(y, group[1], group[3])
    return x, y

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please supply input file")
        sys.exit()

    coords = utils.File(sys.argv[1]).get_coords()
    x, y = find_max_coords(coords)
    m = Map(x, y)
    for x1, y1, x2, y2 in coords:
        m.add_line(x1, y1, x2, y2)
    print(m)
    print(m.calculate_points(2))



