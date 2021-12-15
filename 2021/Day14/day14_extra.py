from collections import Counter
import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

input = lines[0]
lines.pop(0)
lines.pop(0)

input_len = len(input)

rules_dict = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines}

steps = 2

# steps -= 1

frequency = {rules_dict[key]:0 for key in rules_dict.keys()}
for l in input:
    frequency[l] += 1


for i in range(len(input)-1):
    first = input[i]
    second = input[i+1]

    for j in range(steps):
        pair = first + second
        insert = rules_dict[pair]
        if second == insert:
            frequency[insert] += steps - j
            break
        frequency[insert] += 1
        second = insert


print(frequency)