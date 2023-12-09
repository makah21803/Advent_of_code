import os
import re
import math

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["0 3 6 9 12 15",
             "1 3 6 10 15 21",
             "10 13 16 21 30 45", ]


class Day9():
    def __init__(self, data):
        self.sequences = []
        self.unpack_data(data)

    def unpack_data(self, data):
        for line in data:
            self.sequences.append([int(num.strip()) for num in line.split(" ")])

    def check_sequence(self, sequence):
        for num in sequence:
            if num != 0:
                return False
        return True

    def loop_through_sequence(self, sequence):
        last_numbers = []
        first_numbers = []
        if self.check_sequence(sequence):
            return [[0], [0,]]

        last_numbers.append(sequence[-1])
        first_numbers.append(sequence[0])

        new_sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
        new_first_numbers, new_last_numbers = self.loop_through_sequence(new_sequence)
        last_numbers.extend(new_last_numbers)
        first_numbers.extend(new_first_numbers)

        return [first_numbers, last_numbers]

    def get_new_numbers(self, sequence):
        first_numbers, last_numbers = self.loop_through_sequence(sequence)
        following_number = sum(last_numbers)
        previous_number = sum([num * (pow(-1, i)) for i, num in enumerate(first_numbers)])

        return previous_number, following_number

    def run(self):
        new_following_numbers = []
        new_previous_numbers = []
        for sequence in self.sequences:
            previous_number, following_number = self.get_new_numbers(sequence)
            new_following_numbers.append(following_number)
            new_previous_numbers.append(previous_number)
        return sum(new_following_numbers), sum(new_previous_numbers)



# DATA = test_data

answer_one, answer_two = Day9(DATA).run()
print(f"Task 1: The sum of all first following numbers is {answer_one}")
print(f"Task 1: is {answer_two}")

