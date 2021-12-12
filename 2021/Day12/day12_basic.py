import re

file = open("input_data.txt", "r")

list = [[cave for cave in re.split("-", line.strip())] for line in file.readlines()]

cave_exits = {}

for line in list:

    for i, cave in enumerate(line):
        if cave not in cave_exits.keys():
            cave_exits[cave] = [line[i - 1],]
            continue
        cave_exits[cave].append(line[i-1])

class PathFinder():
    def __init__(self, cave_exits):
        self.cave_exits = cave_exits
        self.number_of_paths = 0
        self.possible_paths = []
        self.active_path = []
        self.cave_blacklist = []

    def puzzle_one(self, start):
        for cave in self.cave_exits[start]:
            self.cave_blacklist = [start,]
            self.go_to_cave(cave)
            print(self.active_path)
            self.active_path = []

        return self.number_of_paths

    def go_to_cave(self, this_cave):
        if this_cave in self.cave_blacklist:
            return

        self.active_path.append(this_cave)

        if this_cave == "end":
            # self.possible_paths.append(self.active_path)
            self.number_of_paths += 1
            return

        if self.is_small_cave(this_cave):
            self.cave_blacklist.append(this_cave)


        blacklist_backup = [c for c in self.cave_blacklist]
        for next_cave in self.cave_exits[this_cave]:
            self.cave_blacklist = [c for c in blacklist_backup]
            if next_cave not in self.cave_blacklist:
                self.go_to_cave(next_cave)
        return

    def is_small_cave(self, cave):
        # if re.match("^\w", cave):
        # if cave in ["start", "dc", "kj", "sa", "end"]:
        # if cave in ["start", "fs", "he", "pj", "zg", "sl"]:
        if cave in ["start", "bp", "sq", "em", "to", "hr", "st", "er"]:
            # print("Cave {} is small".format(cave))
            return True
        return False


print(PathFinder(cave_exits).puzzle_one("start"))

