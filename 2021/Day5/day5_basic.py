import re

file = open("input_data.txt", "r")

list = file.readlines()

def ex_coord(line, a, b):
    coord = line.split(" -> ")[a].split(",")[b]
    return int(coord.strip())

coordinates = [[[ex_coord(l, 0,0),ex_coord(l, 0,1)],[ex_coord(l, 1,0),ex_coord(l, 1,1)]] for l in list]

def increment_coordinate(coord, dx, dy):
    return [coord[0]+dx, coord[1]+dy]

vent_coords = {}

for line in coordinates:
    if line[0][0] == line[1][0]:
        # print("line {} works".format(line))
        start = int(line[0][1] > line[1][1])
        # print("{} -> {}".format(line, line[start]))
        for dy in range(abs(line[0][1] - line[1][1])+1):
            coord = increment_coordinate(line[start], 0, dy)
            coord_key = "[{}, {}]".format(coord[0],coord[1])
            if coord_key not in vent_coords.keys():
                vent_coords[coord_key] = 1
                # print("Line {} added {}".format(line, coord_key))
            else:
                vent_coords[coord_key] += 1
                # print("Line {} increased {} to {}".format(line, coord_key, vent_coords[coord_key]))

    elif line[0][1] == line[1][1]:
        # print("line {} works".format(line))
        start = line[0][0] > line[1][0]
        # print("{} -> {}".format(line, line[start]))
        for dx in range(abs(line[0][0] - line[1][0]) +1):
            coord = increment_coordinate(line[start], dx, 0)
            coord_key = "[{}, {}]".format(coord[0],coord[1])
            if coord_key not in vent_coords.keys():
                # print("Line {} added {}".format(line, coord_key))
                vent_coords[coord_key] = 1
            else:
                vent_coords[coord_key] += 1
                # print("Line {} increased {} to {}".format(line, coord_key, vent_coords[coord_key]))

    else:
        # print("line {} skipped".format(line))
        continue

count = 0
for key in vent_coords.keys():
    if vent_coords[key] >= 2:
        count += 1

# print(vent_coords)
print(count)
