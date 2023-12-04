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

class Engine():
    def __init__(self, data):
        self.data = data
        self.max_coords = [len(data)-1, len(data[0])-1]

    def get_neighbour_coords(self, coord):
        r, c = coord
        possible_coords = [[r-1, c-1], [r-1, c], [r-1, c+1],
                           [r, c-1], [r, c+1],
                           [r+1, c-1], [r+1, c], [r+1, c+1],]
        for coord in possible_coords:
            if 0 <= coord[0] <= self.max_coords[0] and 0 <= coord[-1] <= self.max_coords[-1]:
                yield coord

    def get_char(self, coord):
        r, c = coord
        return self.data[r][c]

    def check_for_symbol(self, coord):
        char = self.get_char(coord)
        if re.match("[0-9.]", char):
            return None
        return char

    def check_for_num(self, coord):
        char = self.get_char(coord)
        if re.match("[0-9]", char):
            return char
        return None

    def extract_numbers(self):
        # there is some issue with reading the numbers at the end of the line,
        # so I added ".' to the input_data at the end of each line
        results = {}
        for r, row in enumerate(self.data):
            number = ""
            neighbours = []
            number_coords = []
            for c, char in enumerate(row):
                if re.match("[0-9]", char):
                    number = number + char
                    number_coords.append([r, c])
                    new_neighbours = self.get_neighbour_coords([r, c])
                    neighbours.extend([coord for coord in new_neighbours if coord not in neighbours])
                    continue

                if number != "":
                    results[f"r{r+1}_c{c}:{number}"] = [coord for coord in neighbours if coord not in number_coords]

                number = ""
                neighbours = []
                number_coords = []

            if number != "":
                results[f"r{r + 1}_cE:{number}"] = [coord for coord in neighbours if coord not in number_coords]

        self.extracted_numbers = results

    def task_one(self):
        self.extract_numbers()
        count = 0
        for key in self.extracted_numbers.keys():
            num = int(key.split(":")[-1])
            for coord in self.extracted_numbers[key]:
                char = self.check_for_symbol(coord)
                if char is not None:
                    count = count + 1
                    yield num
                    break

    def get_whole_number(self, coord):
        r, c = coord
        start = c
        end = c
        for i in range(1, 4):
            if c - i < 0 or self.check_for_num([r, c - i]) is None:
                start = c -i+1
                break
        for i in range(1, 4):
            if c + 1 > len(self.data[r]) or self.check_for_num([r, c + i]) is None:
                end = c +i-1
                break

        number = ""
        num_coords = []
        for i in range(3):
            if start + i > end:
                break
            number = number + self.data[r][start + i]
            num_coords.append([r, start+i])

        return int(number), num_coords

    def get_neighbour_nums(self, coord):
        checked_coords = []
        neighbour_nums = []
        for neighbour_coord in self.get_neighbour_coords(coord):
            if neighbour_coord in checked_coords:
                continue

            char = self.check_for_num(neighbour_coord)
            if char is None:
                checked_coords.append(neighbour_coord)
                continue

            number, new_coords = self.get_whole_number(neighbour_coord)
            checked_coords.extend(new_coords)
            neighbour_nums.append(number)

        return neighbour_nums

    def task_two(self):
        results = []
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                if char != "*":
                    continue

                neighbour_nums = self.get_neighbour_nums([r, c])
                if len(neighbour_nums) != 2:
                    continue

                gear_ratio = neighbour_nums[0] * neighbour_nums[1]
                results.append(gear_ratio)
        return results



Engine = Engine(DATA)

# there is some issue with reading the numbers at the end of the line,
# so I added ".' to the input_data at the end of each line
answer_one = sum(Engine.task_one())
print(f"Task 1: The sum of all valid numbers is: {answer_one}")

answer_two = sum(Engine.task_two())
print(f"Task 1: The sum of all gear rations is: {answer_two}")

print(list(Engine.get_neighbour_coords([1,9])))
