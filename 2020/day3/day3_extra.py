import re

file = open("2020/day3/input_data.txt", "r")

list = file.readlines()


slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))

counts = []
for step in slopes:
    coords = [(row, (row/step[1]*step[0]) % (len(line)-1)) for row, line in enumerate(list) if row % step[1] == 0]
    
    count = 0
    for coord in coords:
        if list[coord[0]][coord[1]] == "#":
            count += 1
    counts.append(count)

mult = 1
for c in counts:
    mult *= c

print (counts)

print('finished, answer is: {}'.format(mult))
