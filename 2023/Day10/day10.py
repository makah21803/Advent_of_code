import os
import re
import math

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = [""]


class Day10():
    def __init__(self, data):
        self.unpack_data(data)

    def unpack_data(self, data):
        pass

    def task_one(self):
        pass

    def task_two(self):
        pass



DATA = test_data

Day10 = Day10(DATA)
print(f"Task 1: is {Day10.task_one()}")
print(f"Task 2: is {Day10.task_two()}")

