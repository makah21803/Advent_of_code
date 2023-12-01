import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

sum = 0
for line in list:
    found = re.findall('[0-9]', line)
    sum = sum + int(found[0] + found[-1])

print(f"Sum of all calibration values is: {sum}")
