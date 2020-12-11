import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

class Day11():

    def __init__(self, list):
        self.list = list
        self.something_changed = True
        self.row_limits = (-1, len(list))
        self.col_limits = (-1, len(list[0]))

    def run(self):
        while self.something_changed:
            self.seat_change(self.list)

        return self.list

    def seat_change(self, list):
        self.something_changed = False
        new_list = []
        for row, line in enumerate(list):
            new_line = []
            for col, seat in enumerate(line):
                seat = self.change_evalueation(row, col, list)
                new_line.append((seat))

            new_list.append(new_line)

        self.list = new_list

    def change_evalueation(self, row, col, list):

        adjacent = self.get_adjacent(row, col, list)
        seat = self.list[row][col]

        if seat == '.':
            return '.'

        elif seat == 'L' and '#' not in adjacent:
            self.something_changed = True
            return '#'

        elif seat == '#' and sum(1 for s in adjacent if s == '#') >= 5:
            self.something_changed = True
            return 'L'

        else:
            return seat

    def get_adjacent(self, row, col, list):
        directions = ((-1, -1), (-1, 0), (-1, +1),
                  (0, -1), (0, +1),
                  (+1, -1), (+1, 0), (+1, +1))

        adjacement = []
        for y, x in directions:
            r = row + y
            c = col + x
            seat = '.'
            while seat == '.' and r not in self.row_limits and c not in self.col_limits:
                seat = self.list[r][c]
                r += y
                c += x

            adjacement.append(seat)

        return adjacement

        # adjacement = [list[r][c] for r, c in coords if r not in self.row_limits and c not in self.col_limits]


final_list = Day11(input_list).run()

count = []
[count.extend([1 for seat in line if seat == '#']) for line in final_list]
count = len(count)

print('In the end there are {} occupied seats.'.format(count))
