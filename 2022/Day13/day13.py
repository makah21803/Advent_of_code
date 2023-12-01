
import ast
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line for line in file.readlines()]
# input_list = [line for line in test_file.readlines()]

packet_pairs = [[],]
index = 0
for line in input_list:
    if line == "\n":
        packet_pairs.append([])
        index += 1
        continue
    packet_pairs[index].append(line.strip())

# for i, pair in enumerate(packet_pairs):
#     print(f"{i}: \n{pair[0]} \n{pair[1]}")
#
# print('\n')

class RadioSignal:
    def __init__(self,packet_pairs):
        self.correct_pairs = []

        for index in range(len(packet_pairs)):
            packetA = ast.literal_eval(packet_pairs[index][0])
            packetB = ast.literal_eval(packet_pairs[index][1])
            index += 1
            comparison = self.compare_items(packetA, packetB)
            print(f'index: {index} is correct: {comparison}\n')
            if comparison is not False:
                self.correct_pairs.append(index)

    def check_list_type(self, item):
        if isinstance(item, list):
            return item
        return [item,]

    def run(self):
        return sum(self.correct_pairs)

    def compare_items(self, parent_itemA, parent_itemB):
        parent_itemA = self.check_list_type(parent_itemA)
        parent_itemB = self.check_list_type(parent_itemB)
        print(f'comparing: \n{parent_itemA}, \n{parent_itemB}')
        for i, itemA in enumerate(parent_itemA):
            if i >= len(parent_itemB):
                return False
            itemB = parent_itemB[i]

            if not isinstance(itemA, list) and not isinstance(itemB, list):
                comparison = self.compare_numbers(int(itemA), int(itemB))
                if comparison is not None:
                    return comparison

            else:
                itemA = self.check_list_type(itemA)
                itemB = self.check_list_type(parent_itemB[i])
                print(f'lists: \n{itemA}, \n{itemB}')

                for n in range(len(itemA)):
                    if n >= len(itemB):
                        return False
                    if isinstance(itemA[n], list) or isinstance(itemB[n], list):
                        comparison = self.compare_items(itemA[n], itemB[n])
                        if comparison is not None:
                            return comparison
                        continue
                    comparison = self.compare_numbers(int(itemA[n]), int(itemB[n]))
                    if comparison is not None:
                        return comparison

                if len(itemA) < len(itemB):
                    return True
            # print('undecied, next item')

        return None

    def compare_numbers(self, numberA, numberB):
        if numberA < numberB:
            # print(f"{numberA} < {numberB}")
            return True
        if numberA > numberB:
            # print(f"{numberA} > {numberB}")
            return False

        # print(f"{numberA} = {numberB}")
        return None


signal_packets = RadioSignal(packet_pairs)
print(f"Part One: {signal_packets.run()}")