import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [int(i.strip()) for i in [row.strip() for row in file.readlines()][0].split(',')]

used = [n for n in input_list]
# used = []
next = 0
for i in range(2020):
    if i < len(input_list):
        continue

    next = used[-1]
    if next not in used[0:-1]:
        next = 0
    else:
        tmp = [n for n in used[0:-1]]
        tmp.reverse()
        used_reversed = tmp
        next = used_reversed.index(next)+1
    used.append(next)

print('The 2020th number is: {}'.format(next))
