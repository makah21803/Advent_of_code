import re

file = open("input_data.txt", "r")

list = file.readlines()
# int_list = [int(i) for i in list]

list = [i.strip() for i in list]

bin_len = len(list[0])

cumulative = [0 for i in range(bin_len)]

for line in list:
    for i in range(bin_len):
        cumulative[i] += int(line[i])

gama = 0
epsilon = 0
for i, n in enumerate(cumulative):
    value = 0
    if n > len(list)/2:
        value = 1
    gama += 10**(bin_len-1-i) * value
    epsilon += 10**(bin_len-1-i) * (1-value)

gama = int(str(gama), 2)
epsilon = int(str(epsilon), 2)

print("gama: {}\nepsilon: {}\nanswer: {}".format(gama, epsilon, gama*epsilon))
