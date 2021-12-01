import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

increased_counter = 0
previous_depths = [d for i, d in enumerate(int_list) if i < 3]
for i, depth in enumerate(int_list):
    if i == 0 or i > len(int_list)-3:
        continue
    previous_sum = sum([int_list[i+n-1] for n in range(3)])
    current_sum = sum([int_list[i+n] for n in range(3)])

    if current_sum > previous_sum:
        increased_counter += 1

    print("depth: {}\nprevious sum: {}\ncurrent sum: {}\n".format(depth, previous_sum, current_sum))

print("answer is: {}".format(increased_counter))

