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

sum = 0
for line in input_list:
    middle = len(line)//2
    compartmentA = line[:middle]
    compartmentB = line[middle:]

    common = list(set(compartmentA).intersection(compartmentB))
    priority = get_priority(common[0])
    sum += priority


print("The total priority of rucksacks is {}".format(sum))

