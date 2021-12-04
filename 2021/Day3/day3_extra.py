import re

file = open("input_data.txt", "r")

list = file.readlines()


class OxygenLevels():
    def __init__(self, list):
        self.bin_len = len(list[0])
        self.oxy_list = [s.strip() for s in list]
        self.coo_list = [s.strip() for s in list]

    def run(self):
        oxy = self.generator(self.oxy_list)
        coo = self.generator(self.oxy_list, invert=True)
        return [oxy, coo]

    def find_common(self, list, index):
        cumulative = 0
        for line in list:
            cumulative += int(line[index])
        return int(cumulative >= len(list)/2)

    def generator(self, entries, invert=False):
        for n in range(self.bin_len):
            common = self.find_common(entries, n)
            entries_tmp = [s for s in entries]

            for entry in entries:
                if (int(entry[n]) != common) is not invert:
                    entries_tmp.remove(entry)
            entries = entries_tmp

            if len(entries) == 1:
                return entries[0]
                break
        return False


oxygen_levels = OxygenLevels(list).run()
oxy = int(oxygen_levels[0], 2)
coo = int(oxygen_levels[1], 2)

print("Oxygen: {}\nC02: {}\nanswer: {}".format(oxy, coo, oxy*coo))




