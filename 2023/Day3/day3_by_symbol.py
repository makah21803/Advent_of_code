import os
import re



dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
DATA = file.readlines()

test_data = ["467..114..",
             "...*......",
             "..35..633.",
             "......#...",
             "617*......",
             ".....+.58.",
             "..592.....",
             "......755.",
             "...$.*....",
             ".664.598..",]

DATA = test_data
MAX_COORDS = [len(DATA)-1, len(DATA[0])-1]

def get_neighbour_coords(coord, max_coords):
    r, c = coord
    possible_coords = [[r-1, c-1], [r-1, c], [r-1, c+1],
                       [r, c-1], [r, c+1],
                       [r+1, c-1], [r+1, c], [r+1, c+1],]
    return [coord for coord in possible_coords if 0 <= coord[0] <= max_coords[0] and 0 <= coord[-1] <= max_coords[-1]]


def get_char(data, coord):
    r, c = coord
    return data[r][c]

def check_for_num(data, coord):
    char = get_char(data, coord)
    if re.match("[0-9]", char):
        return char
    return None

def check_for_symbol(data, coord):
    char = get_char(data, coord)
    if re.match("[0-9.]", char):
        return None
    return char

def get_whole_number(data, coord):
    r, c = coord
    start = c
    end = c
    for i in range(1, 2):
        if c - i < 0 or check_for_num(data, [r, c - i]) is None:
            start = c -i+1
        if c + 1 > len(data[r]) or check_for_num(data, [r, c + i]) is None:
            end = c +i-1

    number = ""
    num_coords = []
    for i in range(3):
        if start + i > end:
            break
        number = number + data[r][start + i]
        num_coords.append([r, start+i])

    return int(number), num_coords


def get_neighbour_nums(data, coord):
    checked_coords = []
    neighbour_nums = []
    for neighbour_coord in get_neighbour_coords(coord, MAX_COORDS):
        if neighbour_coord in checked_coords:
            continue

        char = check_for_num(data, neighbour_coord)
        if char is None:
            checked_coords.append(neighbour_coord)
            continue

        number, new_coords = get_whole_number(data, neighbour_coord)
        checked_coords.extend(new_coords)
        neighbour_nums.append(number)

    return neighbour_nums


def task_one(data):
    valid_numbers = []
    for r, row in enumerate(data):
        for c in range(len(row)):
            char = check_for_symbol(data, [r, c])
            if char is None:
                continue
            new_numbers = get_neighbour_nums(data, [r, c])
            print(f"{[r, c]}:{char} - {new_numbers}")
            valid_numbers.extend(new_numbers)
    print(valid_numbers)
    return sum(valid_numbers)



# print(valid_numbers)
print(task_one(DATA))

