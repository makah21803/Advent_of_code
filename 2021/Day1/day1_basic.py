import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

increased_counter = 0
previous_depth = None
for depth in int_list:
    if previous_depth and depth > previous_depth:
        increased_counter += 1
    previous_depth = depth

print(increased_counter)

