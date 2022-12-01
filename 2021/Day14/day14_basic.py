from collections import Counter
import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

input = lines[0]
lines.pop(0)
lines.pop(0)


orig_rules_dict = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines}
rules_dict_low = {key:''.join([key[0], orig_rules_dict[key].lower(), key[-1]]) for key in orig_rules_dict.keys()}

steps = 40
for i in range(steps):
    for pair in rules_dict_low.keys():
        substitude = rules_dict_low[pair]
        input = re.sub(pair, substitude, input)
        if pair[0] == pair[-1]:
            input = re.sub(pair, substitude, input)
    input = input.upper()
    print(i)

output = input


frequency = Counter(output)
min = 99999999999999999999
max = 0
for key in frequency.keys():
    value = frequency[key]
    if min > value:
        min = value
    if max < value:
        max = value

print(len(output))
print(frequency)
print(max-min)


crosses_row = []
for cross in crosses:
    crosses_row.append(cross[0])


