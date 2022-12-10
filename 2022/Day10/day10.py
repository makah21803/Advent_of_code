
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
# input_list = [line.strip() for line in test_file.readlines()]



class ClassName():
    def __init__(self, cmds):
        self.cycle_n = 0
        self.x = 1
        self.cpu_cycles = []
        self.crt = [["." for c in range(40)] for r in range(6)]
        self.run(cmds)

    def addx(self, value):
        if value[0] == "-":
            value = -1 * int(value[1:])
        else:
            value = int(value)

        self.cycle_n += 1
        self.check_cycle()
        self.cycle_n += 1
        self.check_cycle()
        self.x += value

    def noop(self):
        self.cycle_n += 1
        self.check_cycle()

    def run(self, cmds):
        for i, cmd in enumerate(cmds):

            cmd_bits = cmd.split(" ")
            if cmd_bits[0] == "noop":
                self.noop()
            else:
                self.addx(cmd_bits[-1])

    def check_cycle(self):
        # cpu check
        if self.cycle_n % 40 == 20:
            self.cpu_cycles.append(self.cycle_n * self.x)

        # crt check
        #todo: there is some mismatch with positioning (one starts with 0 the other with 1)
        sprite_position = self.x % 40
        if self.cycle_n % 40 in [sprite_position, sprite_position+2, sprite_position+1]:
            row = self.cycle_n // 40
            drawing_pixel = self.cycle_n % 40
            self.crt[row][drawing_pixel] = "#"

    def part_one(self):
        return sum(self.cpu_cycles)

    def part_two(self):
        for row in self.crt:
            print("".join(row))


class_name = ClassName(input_list)
print(f"Part One: {class_name.part_one()}\n===")
print("Part Two:\nThe display is still a bit broken at the start, \nbut you should be able to read most and guess the rest:")
class_name.part_two()

