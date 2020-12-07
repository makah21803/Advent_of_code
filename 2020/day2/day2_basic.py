import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

n = 0
for line in list:
    string = str(line)
    parts = string.split(" ")
    min = int(parts[0].split("-")[0])
    max = int(parts[0].split("-")[1])
    letter = parts[1][0]
    pswd = parts[2]

    count = len(re.findall(letter, pswd))
    if count >= min and count <= max:
        n += 1
print n
