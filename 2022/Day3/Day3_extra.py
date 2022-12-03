import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]

def get_priority(letter):
    priority = ord(letter)-64
    if priority <= 26:
        # capitals
        priority += 26
    else:
        priority -= 32
    return priority


grouped_lines = []
for i in range(len(input_list)):
    if i % 3 == 0:
        current_group = []

    current_group.append(input_list[i])

    if i % 3 == 2:
        grouped_lines.append(current_group)


sum = 0
for line_group in grouped_lines:
    rucksackA = line_group[0]
    rucksackB = line_group[1]
    rucksackC = line_group[2]

    common = list(set(rucksackA).intersection(rucksackB).intersection(rucksackC))
    priority = get_priority(common[0])
    sum += priority


print("The total priority of rucksacks is {}".format(sum))

