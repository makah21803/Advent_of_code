import math

file = open("input_data.txt", "r")

list = [int(n.strip()) for n in file.readlines()[0].split(",")]
list.sort()

"""
model of one fish pregnant at day 0 
row   day                                 fish born
0     0                                   1
1     7, 9                                1, 1 
2     14,16,18                            1, 2 , 1
3     21,23,25,27                         1, 3 , 3 , 1
4     28,30,32,34,36                      1, 4 , 6 , 4 , 1
5     35,37,39,41,43,45                   1, 5 , 10, 10, 5 , 1
6     42,44,46,48,50,52,54                1, 6 , 15, 20, 15, 6 , 1
7     49,51,53,55,57,59,61,63             1, 7 , 21, 35, 35, 21, 7 , 1
8     56,58,60,62,64,66,68,70,72          1, 8 , 28, 56, 70, 56, 28, 8 , 1
9     63,65,67,69,71,73,75,77,79,81       1, 9 , 36, 84,126,126, 84, 36, 9 , 1
10    70,72,74,76,78,80,82,84,86,88,90    1, 10, 45,120,210,254,210,120, 45, 10, 1
...                                 ...
"""


days = 100000

day_rows = []
birth_rows = []
# birth_row_values = []
for r in range(math.ceil(days/7)+1):
    day_rows.append([7 * r + 2 * i + 1 for i in range(r + 1)])

    if r == 0:
        row_births = [1, ]
    else:
        row_births = [birth_rows[r-1][i - 1] + birth_rows[r-1][i] for i in range(len(birth_rows[r-1]))]
        row_births.append(1)
        row_births[0] = 1
    birth_rows.append(row_births)

fish_total = 0
for fish_start in list:
    fish_in_model = 1
    fish_days = days - fish_start

    # max day in row is i*7 + i*2, where I is row index
    first_unsafe_row = math.floor(fish_days/9)
    fish_in_model += sum(2**i for i in range(first_unsafe_row))

    max_row = math.ceil(fish_days/7)
    for r in range(first_unsafe_row, max_row):
        row_value = sum([b for i, b in enumerate(birth_rows[r]) if day_rows[r][i] <= fish_days])
        fish_in_model += row_value

    fish_total += fish_in_model

print("On the day {} there are {} fish in the sea.".format(days, fish_total))
