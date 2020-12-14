import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

class Day14():

    def __init__(self):
        self.mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.mem_dict = {}

    def run(self, list):
        for row in list:
            fce = row.split(' ')[0].lstrip()
            value = row.split(' ')[-1].strip()
            print(fce)

            if fce == 'mask':
                self.mask = value

            elif fce[0:3] == 'mem':
                mem_number = re.sub('\D', '', fce)
                bin_str = '{:036b}'.format(int(value))

                new_value = int(self.apply_mask(bin_str), 2)
                self.write_memory(mem_number, new_value)


        return self.mem_dict

    def apply_mask(self, bin_str):
        bin_list = list(bin_str)
        for i, m in enumerate(self.mask):
            if m != 'X':
                bin_list[i] = m

        return ''.join(bin_list)

    def write_memory(self, mem_number, value):
        self.mem_dict[str(mem_number)] = value
        print('Mem #{} set to {}'.format(mem_number, value))


written_memories = Day14().run(input_list)
print(written_memories)

sum_of_memories = 0
for mem, value in written_memories.items():
    sum_of_memories += value

print('Sum of memories is: {}'.format(sum_of_memories))
