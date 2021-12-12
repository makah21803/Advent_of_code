import re

file = open("input_data.txt", "r")

map = [[int(i) for i in row.strip()] for row in file.readlines()]


low_points = []
for row, line in enumerate(map):
    for col, height in enumerate(line):
        height_coords = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
        neighbours = [map[r][c] for r, c in height_coords if r < len(map) and c < len(line) and r>=0 and c>=0]
        if all([height < height_n for height_n in neighbours]):
            low_points.append(height)

print(low_points)
total_sum = sum(h+1 for h in low_points)
print(total_sum)
