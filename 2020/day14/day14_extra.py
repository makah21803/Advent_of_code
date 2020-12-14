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

            if fce == 'mask':
                self.mask = value

            elif fce[0:3] == 'mem':
                mem_number = re.sub('\D', '', fce)
                bin_str = '{:036b}'.format(int(value))

                new_value = int(self.apply_mask(bin_str), 2)
                self.write_memory(mem_number, new_value)


        return self.mem_dict

    def run_extra(self, list):
        for row in list:
            fce = row.split(' ')[0].lstrip()
            value = row.split(' ')[-1].strip()

            if fce == 'mask':
                self.mask = value

            elif fce[0:3] == 'mem':
                mem_number = re.sub('\D', '', fce)
                mems_to_write = self.get_addresses_from_mask(mem_number)

                for mem in mems_to_write:
                    self.write_memory(mem, int(value))

        return self.mem_dict

    def apply_mask(self, bin_str):
        bin_list = list(bin_str)
        for i, m in enumerate(self.mask):
            if m != 'X':
                bin_list[i] = m

        return ''.join(bin_list)

    def get_addresses_from_mask(self, input_mem):
        mem_adresses = []
        bin_mem = list('{:036b}'.format(int(input_mem)))
        xcount = 0
        for i, m in enumerate(self.mask):
            if m != '0':
                bin_mem[i] = m
            if m == 'X':
                xcount += 1

        floating_max = pow(2, xcount)
        for floating_num in range(floating_max):
            format_str = '{:0'+str(xcount)+'b}'
            bin = format_str.format(int(floating_num))
            x_num = 0
            new_mem = [i for i in bin_mem]
            for i, n in enumerate(new_mem):
                if n == 'X':
                    new_mem[i] = bin[x_num]
                    x_num += 1

            new_mem = ''.join(new_mem)
            mem_adresses.append(new_mem)

        return mem_adresses

    def write_memory(self, mem_number, value):
        self.mem_dict[str(mem_number)] = value
        # print('Mem #{} set to {}'.format(mem_number, value))


# part 1
written_memories = Day14().run(input_list)
sum_of_memories = 0
for mem, value in written_memories.items():
    sum_of_memories += value

print('Sum of memories in part1 is: {}'.format(sum_of_memories))


# part 2
written_memories = Day14().run_extra(input_list)
sum_of_memories = 0
for mem, value in written_memories.items():
    sum_of_memories += value

print('Sum of memories in part2 is: {}'.format(sum_of_memories))
