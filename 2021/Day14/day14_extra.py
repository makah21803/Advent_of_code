from collections import Counter
import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

orig = lines[0]
input = lines[0]
lines.pop(0)
lines.pop(0)

input_len = len(input)

orig_rules_dict = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines}
rules_dict_low = {key:''.join([key[0], orig_rules_dict[key].lower(), key[-1]]) for key in orig_rules_dict.keys()}

frequency = {}
def save_letters(string, steps_remaining):
    # value = sum([2**i for i in range(steps_remaining)])
    value = 2**steps_remaining
    for l in string:
        if l in frequency.keys():
            frequency[l] += value
        else:
            frequency[l] = value

steps = 10
for i in range(steps):
    for pair in rules_dict_low.keys():
        substitude = rules_dict_low[pair]
        input = re.sub(pair, substitude, input)
        if pair[0] == pair[-1]:
            input = re.sub(pair, substitude, input)
    input = input.upper()
    while re.findall("NBBN", input):
        input = re.sub("NBBN", 'N', input)
        save_letters("NBB", steps-i)
    print(i)
    print(input)

print(frequency)

output = input

frequency_out = Counter(output)
print(frequency_out)
for key in frequency_out.keys():
    if key in frequency.keys():
        frequency[key] += frequency_out[key]
    else:
        frequency[key] = frequency_out[key]

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

