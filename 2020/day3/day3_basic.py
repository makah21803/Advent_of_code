import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

step = (3, 1)
col = 0

coords = [(row, row*step[0] % (len(line)-1)) for row, line in enumerate(list)]

print (coords)

count = 0
for coord in coords:
    if list[coord[0]][coord[1]] == "#":
        count += 1

print('finished, answer is: {}'.format(count))

