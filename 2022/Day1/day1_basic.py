import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

sum = 0
totals = []
for line in list:
    if line == "\n":
        totals.append(sum)
        sum = 0
    else:
        sum += int(line)

totals.sort()
print(totals)
print("Most calories one elf has is {}".format(totals[-1]))
topElves = 0
for i in range(3):
    i += 1
    topElves += totals[-i]

print("Top elves carry {} calories.".format(topElves))

