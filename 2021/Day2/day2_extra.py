import re

file = open("input_data.txt", "r")

list = file.readlines()
# int_list = [int(i) for i in list]

class Piloting():
    def __init__(self):
        self.distance = 0
        self.depth = 0
        self.aim_val = 0
        self.movement_dict = {"forward":self.move, "down":self.aim_up, "up":self.aim_down}

    def move(self, val):
        self.distance += val
        self.depth += self.aim_val * val

    def aim_up(self, val):
        self.aim_val += val

    def aim_down(self, val):
        self.aim_val -= val

    def run(self, list):

        for command in list:
            dir = re.match("^[a-z]*", command).group()
            val = int(re.search("[0-9]*$", command).group())

            self.movement_dict[dir](val)

        return "depth: {}\ndistance: {}\nanswer: {}".format(self.depth, self.distance, self.depth*self.distance)


print(Piloting().run(list))
