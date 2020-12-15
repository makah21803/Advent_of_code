import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [int(i.strip()) for i in [row.strip() for row in file.readlines()][0].split(',')]

lenght = 30000000

used = {}
next = 0
last = None
for i in range(lenght):
    if i >= len(input_list):
        if next not in used:
            next = 0
        else:
            next = i - (used[next]+1)
    else:
        next = input_list[i]

    if last is not None:
        used[last] = i-1
    last = next

print('The {}th number is: {}'.format(lenght, next))
