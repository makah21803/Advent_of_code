import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
             "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
             "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
             "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
             "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
             "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# DATA = test_data

class Lottery():
    def __init__(self, card_list):
        self.card_dict = {}
        self.card_value_dict = {}

        self.unpack_list(card_list)
        self.extract_total_card_values()

    def unpack_list(self, list):
        """ Read cards and save them to dict """
        for card in list:
            card_id, matches = self.read_card(card)
            self.card_dict[card_id] = [card_id + i+1 for i in range(matches)]

    def extract_total_card_values(self):
        """ Check card values, including child cards, and save them to dict """
        for card_id in self.card_dict.keys():
            self.check_value(card_id)

    def task_one(self):
        """ Get sum of card values as 2**(num_matches - 1) """
        for card_id in self.card_dict.keys():
            value = 0
            num_matches = len(self.card_dict[card_id])
            if num_matches > 0:
                value = 2 ** (num_matches - 1)
            yield value

    def task_two(self):
        """ Get total number of card after winning """
        for card_id in self.card_value_dict.keys():
            yield self.card_value_dict[card_id]

    def read_card(self, card_line):
        card, numbers = [s.strip() for s in card_line.split(":")]
        card_id = int(card.split(" ")[-1].strip())
        winning_str, actual_str = [s.strip() for s in numbers.split("|")]
        winning_nums = [int(num.strip()) for num in winning_str.split(" ") if num.strip() != ""]
        actual_nums = [int(num.strip()) for num in actual_str.split(" ") if num.strip() != ""]

        matching_nums = []
        for num in winning_nums:
            if num in actual_nums:
                matching_nums.append(num)

        num_matches = len(matching_nums)
        return card_id, num_matches

    def check_value(self, id):
        # if already went to loosing
        if id in self.card_value_dict.keys():
            return self.card_value_dict[id]

        # if wasn't checked before
        matches = self.card_dict[id]
        value = 1
        if len(matches) > 0:
            for child_id in matches:
                value = value + self.check_value(child_id)

        self.card_value_dict[id] = value
        return value


Lottery = Lottery(DATA)

total_value = sum(Lottery.task_one())
print(f"Task 1: Total value is {total_value}")

total_cards = sum(Lottery.task_two())
print(f"Task 2: Number of cards is {total_cards}")

