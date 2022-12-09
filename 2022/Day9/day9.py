
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
# input_list = [line.strip() for line in test_file.readlines()]



class RopeBridge():
    def __init__(self, rope_length):
        self.direction_options = {"R": [1, 0], "U": [0, 1], "L": [-1, 0], "D": [0, -1]}
        self.visited_coords = [[0, 0], ]
        self.knot_coords = [[0, 0] for n in range(rope_length)]


    def run_movements(self, cmds, print_result=False):
        for l, cmd in enumerate(cmds):
            direction = cmd[0]
            steps = int(cmd.split(" ")[-1].strip())

            for i in range(steps):
                self.move(direction)

        if print_result:
            print("\nFinal")
            self.print_grid()
        return len(self.visited_coords)

    def move(self, direction):
        self.knot_coords[0] = self.add_vectors(self.knot_coords[0], self.direction_options[direction])

        for n in range(len(self.knot_coords)):
            if n == 0:
                continue

            distance_vector = self.subtract_vectors(self.knot_coords[n-1], self.knot_coords[n])
            if abs(distance_vector[0]) > 1 or abs(distance_vector[1]) > 1:
                self.knot_coords[n] = self.add_vectors(self.knot_coords[n], self.normalise_vector(distance_vector))

        if self.knot_coords[-1] not in self.visited_coords:
            self.visited_coords.append(self.knot_coords[-1])

    def add_vectors(self, a, b):
        return [a[i] + b[i] for i in range(len(a))]

    def subtract_vectors(self, a, b):
        return [a[i] - b[i] for i in range(len(a))]

    def normalise_vector(self, a):
        norm_vector = [0 for i in range(len(a))]
        for i in range(len(a)):
            if a[i] != 0:
                norm_vector[i] = a[i] // abs(a[i])
            else:
                norm_vector[i] = 0
        return norm_vector

    def print_grid(self):
        min_x = min([coords[0] for coords in self.visited_coords])-10
        min_y = min([coords[1] for coords in self.visited_coords])-10
        max_x = max([coords[0] for coords in self.visited_coords])+10
        max_y = max([coords[1] for coords in self.visited_coords])+10
        grid = [["." for c in range(max_x -min_x)] for r in range(max_y -min_y)]

        for coord in self.visited_coords:
            grid[coord[1]-min_y][coord[0]-min_x] = "#"

        grid[-min_y][-min_x] = "s"
        grid[self.knot_coords[-1][1]-min_y][self.knot_coords[-1][0]-min_x] = "T"
        grid[self.knot_coords[-1][1]-min_y][self.knot_coords[-1][0]-min_x] = "H"

        for i in range(len(grid)):
            print("".join(grid[-i-1]))


print(f"Part One: Tail visited {RopeBridge(rope_length=2).run_movements(input_list)} coordinates.")
print(f"Part Two: Tail visited {RopeBridge(rope_length=10).run_movements(input_list)} coordinates.")

