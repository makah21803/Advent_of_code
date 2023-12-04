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

# DATA = test_data

def get_neighbour_coords(coord, max_coords):
    r, c = coord
    possible_coords = [[r-1, c-1], [r-1, c], [r-1, c+1],
                       [r, c-1], [r, c+1],
                       [r+1, c-1], [r+1, c], [r+1, c+1],]
    valid_coords = [coord for coord in possible_coords if 0 <= coord[0] <= max_coords[0] and 0 <= coord[-1] <= max_coords[-1]]

    return valid_coords

def extract_numbers(data):
    results = {}
    number = ""
    neighbours = []
    number_coords = []
    count = 0
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if re.match("[0-9]", char):
                number = number + char
                number_coords.append([r, c])
                new_neighbours = get_neighbour_coords([r, c], [len(data)-1, len(row)-1])
                neighbours.extend([coord for coord in new_neighbours if coord not in neighbours])

            else:
                if number != "":
                    count = count + 1
                    results[f"r{r+1}_c{c}:{number}"] = [coord for coord in neighbours if coord not in number_coords]

                number = ""
                neighbours = []
                number_coords = []

    print(f"{count}: {count==len(results)}")
    return results


def get_char(data, coord):
    r, c = coord
    return data[r][c]


def check_for_symbol(data, coord):
    char = get_char(data, coord)
    if re.match("[0-9.]", char):
        return None
    return char


extracted_numbers = extract_numbers(DATA)

valid_numbers = []
count = 0
for key in extracted_numbers.keys():
    num = int(key.split(":")[-1])
    for coord in extracted_numbers[key]:
        char = check_for_symbol(DATA, coord)
        if char is not None:
            count = count + 1
            valid_numbers.append(num)
            # print(f"{key} - {char}: {extracted_numbers[key]}")
            break

    # neighbours = [DATA[coord[0]][coord[-1]] for coord in extracted_numbers[key]]
    # if char is not None:
    #     print(f"{key} - {char}: {neighbours}")
    # else:
    #     print(f"{key} - {get_char(DATA, coord)}: {neighbours}")

print(f"{count}: {count==len(valid_numbers)}")


# print(valid_numbers)
print(sum(valid_numbers))

