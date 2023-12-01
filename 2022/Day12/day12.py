
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
# input_list = [line.strip() for line in test_file.readlines()]



class ElevationMap:
    def __init__(self, map_data):
        self.map_data = map_data
        self.elevation_data = [[self.get_elevation(letter) for letter in row] for row in self.map_data]

        self.test_validity()

        for row in self.map_data:
            print(row)

    def get_elevation(self, letter):
        if letter == "S":
            letter = "a"
            return "S"
        elif letter == "E":
            letter = "z"
            return "E"
        return ord(letter) - 96

    def test_validity(self):
        new_map = []
        for r, row in enumerate(self.map_data):
            new_row = []
            for c, letter in enumerate(row):
                if (0 < r < len(self.map_data)-1 and 0 < c < len(row)-1
                    and self.map_data[r+1][c] == letter
                    and self.map_data[r-1][c] == letter
                    and self.map_data[r][c+1] == letter
                    and self.map_data[r][c-1] == letter):
                    new_row.append(".")
                else:
                    new_row.append(letter)

            new_map.append("".join(new_row))

        self.map_data = new_map


    def run(self):
        return


elevation_map = ElevationMap(input_list)
# print(elevation_map.elevation_data)
# print(f"\nPart One: {class_name.run()}")