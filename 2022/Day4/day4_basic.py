import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]

count = 0
for line in input_list:
    line_int = [[int(n) for n in elf.strip().split("-")] for elf in line.split(",")]

    if (line_int[0][0] >= line_int[1][0] and line_int[0][1] <= line_int[1][1] or
        line_int[1][0] >= line_int[0][0] and line_int[1][1] <= line_int[0][1]):
        count += 1

print("Number of completely overlapping pairs is: {}".format(count))

