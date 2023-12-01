import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

valid_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

sum = 0
for line in list:
    for i, number in enumerate(valid_words):
        line = re.sub(number, number[0]+str(i+1)+number[-1], line) # that's a big nono :D ...just a stupid patch to fix the issue 
    found = re.findall('[0-9]', line)
    sum = sum + int(found[0] + found[-1])

print(f"Sum of all calibration values is: {sum}")
