import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

for i, num in enumerate(int_list):
    for n in range (len(int_list)-i):
        if num + int_list[i+n] == 2020:
            mult = num * int_list[i+n]
            print('Finished, {0} + {1} is 2020 \n their multiple is {2}'.format(num, int_list[i+n], mult))
            break
