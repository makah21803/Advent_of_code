
import math

test_solutions = open("test_solutions.txt", "r")
test_lines = [line.strip() for line in test_solutions]

test_velocities = set()
for line in test_lines:
    for coord in line.split(" "):
        if len(coord) != 0:
            x = int(coord.strip().split(",")[0])
            y = int(coord.strip().split(",")[-1])
            test_velocities.add((x, y))


target_area = "x=153..199, y=-114..-75"
test_area = "x=20..30, y=-10..-5"

range_x = [153, 199]
range_y = [-114, -75]

possible_velocities = set()

# final x is (x+1)*x/2 -> x**2 + x = range_x*2
# final y is -y-1

# when X stops before hits target
x_coords = [x for x in range(math.ceil(range_x[1]**(1/2))*2) if range_x[0] <= (x+1)*x/2 <= range_x[1]]
y_coords = [y-1 for y in range(-range_y[1], -range_y[0]+1)]

for x in x_coords:
    for y in y_coords:
        possible_velocities.add((x, y))

# when hits target before X stops
y_coords_new = []
for y_start in range(range_y[0], min(y_coords)+1):
    y_delta = y_start
    y = y_delta
    i = 1
    while y >= range_y[0]:
        if y <= range_y[1]:
            y_coords_new.append([y_start, i])
        y_delta -= 1
        y += y_delta
        i += 1

# print(y_coords_new)

for y, n in y_coords_new:
    for x in range(range_x[1]+1):
        if n >= x:
            x_fin = (x+1)*x/2
        else:
            x_fin = x*n - sum([i for i in range(n)])
        if range_x[0] <= x_fin <= range_x[1]:
            possible_velocities.add((x, y))


# print(len(test_velocities))
# print(sorted(test_velocities))
print(len(possible_velocities))
print(sorted(possible_velocities))

