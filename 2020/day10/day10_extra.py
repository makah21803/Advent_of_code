import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = [int(row.strip()) for row in file.readlines()]
list.sort()
phone_jolts = list[-1]+3
arrangements = [[0]]

print(list)

class NumberOfArrangements():
    """
    Run method returns the bumber of possible array combinations based rules in possible jumps
    """
    def __init__(self, array):

        self.count = 0
        start = array[0]
        self.array = array

        self.array_jumps = self.get_possible_jumps(array)

    def get_possible_jumps(self, array):
        """
        Returns a dictionary with possible jumps in the given list
        :param array: int
        :return: dict
        """
        array_jumps = {}
        for i, n in enumerate(array):
            one = False
            two = False
            three = False

            for j in range(4):
                if i + j >= len(array):
                    continue
                m = array[i + j]
                if m - n == 1:
                    one = m
                if m - n == 2:
                    two = m
                if m - n == 3:
                    three = m

            possible_jumps = (one, two, three)
            array_jumps[str(n)] = possible_jumps

        return array_jumps

    def run(self, number):
        self.call_number(number)
        return self.count

    def call_number(self, number):
        """
        Jumps from number to number in array based on the rules in dict for each number
        :param number: int # starting number
        """
        for step in range(3):
            next = self.array_jumps[str(number)][step]
            if next:
                if next == self.array[-1]:
                    self.count += 1
                    continue
                else:
                    self.call_number(next)

# create basic arrays used for counting
basic_arrs = [[n for n in range(i)] for i in range (6) if i > 0]
basic_arrs_noa = [NumberOfArrangements(array).run(array[0]) for array in basic_arrs]

# slice the original list to small lists of continuous jumps of 1,
lists_of_continuous = []
continues_ones = []
for i, num in enumerate(list):
    continues_ones.append(num)
    if num == list[-1]:
        lists_of_continuous.append(continues_ones)
        break
    if list[i+1] - num == 3:
        lists_of_continuous.append(continues_ones)
        continues_ones = []
# remove snippents of length 1
lists_of_continuous = [arr for arr in lists_of_continuous if len(arr) > 1]
print(lists_of_continuous)

# count multipluing the arrangements of snippents results in total arrengements
noa = 1
for continuous_ones in lists_of_continuous:
    if len(continuous_ones)-1 >= len (basic_arrs_noa):
        print('basic_arrs_noa not long enough, please extend.')
        break
    noa *= basic_arrs_noa[len(continuous_ones)-1]

print('There is total of {} arrangements'.format(noa))