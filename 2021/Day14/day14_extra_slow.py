from collections import Counter
import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

input = lines[0]
lines.pop(0)
lines.pop(0)

input_len = len(input)

orig_rules_dict = {line.split(" -> ")[0]:line.split(" -> ")[1] for line in lines}
# rules_dict = {key:''.join([key[0], orig_rules_dict[key], key[-1]]) for key in orig_rules_dict.keys()}
# rules_dict_low = {key:''.join([key[0], orig_rules_dict[key].lower(), key[-1]]) for key in orig_rules_dict.keys()}

steps = 40
# steps -= 1
output_len = 2
for i in range(steps):
    output_len += output_len -1

output_len = (output_len-2) * (input_len-1) + input_len

output_list = ['' for i in range(output_len)]
output_list[0] = input[0]
# output_list[-1] = input[-1]
step = 2**steps
# output_list[-step-1] = input[-2]

# first step
index = 0
for n in range(input_len):
    index = n*step
    output_list[index] = input[n]
step = int(step/2)

string = ''.join(output_list)

#remaining steps
for i in range(steps):
    for n in range(int((output_len-1)/step)):
        index = step + 2*n*step
        if index > output_len-1:
            break

        # print("index: {} i, n: {}, {}".format(index, i, n))
        # print(string)

        pair = ''.join([string[n], string[n+1]])
        output_list[index] = orig_rules_dict[pair]
    print(i)

    string = ''.join(output_list)
    step = int(step /2)

output = string

# print(rules_dict_low)
# steps = 10
# for i in range(steps):
#     for pair in rules_dict_low.keys():
#         substitude = rules_dict_low[pair]
#         input = re.sub(pair, substitude, input)
#         if pair[0] == pair[-1]:
#             input = re.sub(pair, substitude, input)
#     input = input.upper()
#
# output = input

# stepped_rules_dict = {key:rules_dict[key] for key in rules_dict.keys()}
#
# for i in range(steps-1):
#     for key in stepped_rules_dict.keys():
#         value = stepped_rules_dict[key]
#
#         new_bits = [value[0]]
#         for j in range(len(value)-1):
#             pair = value[j:j+2]
#             if pair in rules_dict.keys():
#                 new_bits.append(rules_dict[pair][1:])
#
#         stepped_rules_dict[key] = ''.join(new_bits)
#
#
# new_bits = [input[0]]
# for j in range(len(input)-1):
#     pair = input[j:j+2]
#     if pair in stepped_rules_dict.keys():
#         new_bits.append(stepped_rules_dict[pair][1:])
# output = ''.join(new_bits)
#
#
frequency = Counter(output)
min = 99999999999999999999
max = 0
for key in frequency.keys():
    value = frequency[key]
    if min > value:
        min = value
    if max < value:
        max = value


print(frequency)
print(max-min)

