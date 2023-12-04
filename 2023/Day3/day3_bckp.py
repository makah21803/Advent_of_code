import os
import re



dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
data = file.readlines()

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

# data = test_data

def get_neighbour_coords(coord, max_coords):
    r, c = coord
    possible_coords = [[r-1, c-1], [r-1, c], [r-1, c+1],
                       [r, c-1], [r, c+1],
                       [r+1, c-1], [r+1, c], [r+1, c+1],]
    return [coord for coord in possible_coords if 0 <= coord[0] <= max_coords[0] and 0 <= coord[-1] <= max_coords[-1]]

def extract_numbers(data):
    results = {}
    number = ""
    neighbours = []
    number_coords = []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if re.match("[0-9]", char):
                number = number + char
                number_coords.append([r, c])
                new_neighbours = get_neighbour_coords([r, c], [len(data)-1, len(row)-1])
                neighbours.extend([coord for coord in new_neighbours if coord not in neighbours])

            else:
                if number != "":
                    results[f"r{r}c{c}:{number}"] = [coord for coord in neighbours if coord not in number_coords]

                number = ""
                neighbours = []
                number_coords = []
    return results


def check_for_symbol(data, coord):
    r, c = coord
    char = data[r][c]
    if re.match("[0-9.]", char):
        return None
    return char


extracted_numbers = extract_numbers(data)


valid_numbers = []
results = []
for key in extracted_numbers.keys():
    num = int(key.split(":")[-1])
    for coord in extracted_numbers[key]:
        char = check_for_symbol(data, coord)
        if char is not None:
            valid_numbers.append(num)
            break
    print(f"{key} - {char}: {extracted_numbers[key]}")


# print(valid_numbers)
print(sum(valid_numbers))

