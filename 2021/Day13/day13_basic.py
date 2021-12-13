import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

dot_coords = [line.strip().split(",") for line in lines if re.match("^[0-9]*,[0-9]*$", line.strip())]
dot_coords = [[int(line[0]), int(line[1])] for line in dot_coords]

"""extracting folds from test example"""
# fold_x = int(re.findall("[0-9]{1,9}$", lines[-1].strip())[0])
# fold_y = int(re.findall("[0-9]{1,9}$", lines[-2].strip())[0])

"""
I decided to enter the fold parameters manually for the first puzzle
"""
dot_coords_folded = []
fold_x = 655

# for x, y in dot_coords:
#     if y > fold_y:
#         y = 2*fold_y - y
#     if [x, y] not in dot_coords_folded:
#         dot_coords_folded.append([x, y])

for x, y in dot_coords:
    if x > fold_x:
        x = 2*fold_x - x
    if [x, y] not in dot_coords_folded:
        dot_coords_folded.append([x, y])

print(len(dot_coords_folded))

