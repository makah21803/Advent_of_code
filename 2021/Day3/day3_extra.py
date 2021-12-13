import re

file = open("input_data.txt", "r")

list = file.readlines()


class OxygenLevels():
    def __init__(self, list):
        self.bin_len = len(list[0])
        self.list = [s.strip() for s in list]

    def run(self):
        oxy = self.generator(self.list)
        coo = self.generator(self.list, invert=True)
        return [oxy, coo]

    def find_common(self, list, index):
        """
        Returns the most common bin value on the given index of list entries
        :param list: [str]
        :param index: int
        :return: int
        """
        cumulative = 0
        for line in list:
            # adding each value in the given index: +1 or +0
            cumulative += int(line[index])
        # true if 1 was the most common
        return int(cumulative >= len(list)/2)

    def generator(self, entries, invert=False):
        """
        Iterates through each 0|1 of the entries (binary length defined by self.bin_len)
        :param entries: [str]
        :param invert: bool
        :return: str
        """

        for n in range(self.bin_len):
            common = self.find_common(entries, n)

            # necessary for modifying list while iterating through it
            entries_tmp = [s for s in entries]
            for entry in entries:
                # entry is binary string, i.e. '100000101101', int(entry[n]) is the n-th digit in that string
                # comparing whether it is the common with True or False depending on Oxy or Coo
                # Oxy (invert = False): not common is not False -> remove when not common
                # Coo (invert = True ): not common is not True  -> keep when not common, i.e. remove when common
                if (int(entry[n]) != common) is not invert:
                    entries_tmp.remove(entry)
            entries = entries_tmp

            # last remaining, return the value
            if len(entries) == 1:
                return entries[0]

        return False


oxygen_levels = OxygenLevels(list).run()
oxy = int(oxygen_levels[0], 2)
coo = int(oxygen_levels[1], 2)

print("Oxygen: {}\nC02: {}\nanswer: {}".format(oxy, coo, oxy*coo))




