import re

file = open("input_data.txt", "r")

list = file.readlines()
# int_list = [int(i) for i in list]

distance = 0
depth = 0

for command in list:
    dir = re.split(" ", command)[0]
    val = int(re.split(" ", command)[1])

    if dir == "forward":
        distance += val
    elif dir == "down":
        depth += val
    elif dir == "up":
        depth -= val

print("depth: {}\ndistance: {}\nanswer: {}".format(depth, distance, depth*distance))
