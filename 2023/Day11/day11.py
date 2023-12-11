import os
import re
import math

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["...#......",
             ".......#..",
             "#.........",
             "..........",
             "......#...",
             ".#........",
             ".........#",
             "..........",
             ".......#..",
             "#...#....."]


class StarMap():
    def __init__(self, data):
        self.galaxies = {}
        self.empty_rows = []
        self.empty_cols = []
        self.unpack_data(data)

    def unpack_data(self, data):
        empty_cols = list(range(len(data[0])))
        galaxy_id = 0
        for r, line in enumerate(data):
            empty_row = True
            for c, char in enumerate(line):
                if char == ".":
                    continue
                elif char == "#":
                    if c in empty_cols:
                        empty_cols.remove(c)
                    empty_row = False
                    galaxy_id = galaxy_id + 1
                    self.galaxies[galaxy_id] = [r, c]
            if empty_row is True:
                self.empty_rows.append(r)
        self.empty_cols = empty_cols

    def find_distance(self, start_id, end_id, exp_mult):
        start = self.galaxies[start_id]
        end = self.galaxies[end_id]
        # im not replacing empty lines, im just adding on top
        exp_mult = exp_mult - 1
        vertical_expansion = exp_mult * len([r for r in self.empty_rows if start[0] < r < end[0] or end[0] < r < start[0]])
        horizontal_expansion = exp_mult * len([c for c in self.empty_cols if start[1] < c < end[1] or end[1] < c < start[1]])

        distance = abs(end[0] - start[0]) + vertical_expansion + abs(end[1] - start[1]) + horizontal_expansion
        return distance

    def find_sum_of_all_distances(self, exp_mult=1):
        sum_of_distances = 0
        for galaxy_id in self.galaxies.keys():
            for near_galaxy_id in range(galaxy_id+1, list(self.galaxies.keys())[-1]+1):

                distance = self.find_distance(galaxy_id, near_galaxy_id, exp_mult=exp_mult)
                sum_of_distances = sum_of_distances + distance

        return sum_of_distances



# DATA = test_data

StarMap = StarMap(DATA)
print(f"Task 1: The sum of all distances with expansion 1 is {StarMap.find_sum_of_all_distances(exp_mult=2)}")
print(f"Task 2: The sum of all distances with expansion 1mil is {StarMap.find_sum_of_all_distances(exp_mult=1000000)}")

