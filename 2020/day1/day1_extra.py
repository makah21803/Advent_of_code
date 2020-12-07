import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

for i, numA in enumerate(int_list):
    for n in range (len(int_list)-i):
        numB = int_list[i+n]
        if numA + numB <= 2020:
            for m in range(len(int_list)-i-n):
                numC = int_list[i+n+m]
                if numA + numB + numC == 2020:
                    mult = numA * numB * numC
                    print('Finished, {0} + {1} + {2} is 2020 \n their multiple is {3}'.format(numA, numB, numC, mult))
                    

print('finished')
