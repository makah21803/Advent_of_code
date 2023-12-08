import os
import re
import math

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["RL",
             "AAA = (BBB, CCC)",
             "BBB = (DDD, EEE)",
             "CCC = (ZZZ, GGG)",
             "DDD = (DDD, DDD)",
             "EEE = (EEE, EEE)",
             "GGG = (GGG, GGG)",
             "ZZZ = (ZZZ, ZZZ)",]

test_data2 = ["LLR",
             "AAA = (BBB, BBB)",
             "BBB = (AAA, ZZZ)",
             "ZZZ = (ZZZ, ZZZ)",]

test_data3 = ["LR",
              "",
              "11A = (11B, XXX)",
              "11B = (XXX, 11Z)",
              "11Z = (11B, XXX)",
              "22A = (22B, XXX)",
              "22B = (22C, 22C)",
              "22C = (22Z, 22Z)",
              "22Z = (22B, 22B)",
              "XXX = (XXX, XXX)",]


class Map():
    def __init__(self, data):
        self.directions = list(self.extract_directions(data))
        self.map = {}
        self.start_nodes = []
        self.end_nodes = []
        self.unpack_map(data)

    def extract_directions(self, data):
        for char in data[0]:
            if char.strip() == "L":
                yield 0
            if char.strip() == "R":
                yield 1

    def unpack_map(self, data):
        for i, row in enumerate(data):
            if i == 0 or row in ["", "\n"]:
                continue
            node, directions = [bit.strip() for bit in row.split("=")]
            if node[-1] == "A":
                self.start_nodes.append(node)
            elif node[-1] == "Z":
                self.end_nodes.append(node)

            directions = re.sub("[()]", "", directions)
            left, right = [direction.strip() for direction in directions.split(",")]
            self.map[node] = [left, right]

    def get_number_of_steps(self, node, ends=None):
        if ends is None:
            ends = self.end_nodes
        steps = 0
        while node not in ends:
            direction = self.directions[steps % len(self.directions)]
            node = self.map[node][direction]
            steps = steps + 1
        return steps

    def task_one(self):
        return self.get_number_of_steps("AAA", ["ZZZ",])

    def get_individual_cycles(self):
        node_cycles = []
        for node in self.start_nodes:
            node_cycles.append(self.get_number_of_steps(node))
            
        return node_cycles



# DATA = test_data3

Map = Map(DATA)
print(f"Task 1: is {Map.task_one()}")
print(f"Task 2: Individual paths are {Map.get_individual_cycles()}."
      f"\nJust find lowest common multiplier with math.lcm()\n")
print(math.lcm(21883, 13019, 19667, 16343, 18559, 14681))

