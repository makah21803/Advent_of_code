import re

file = open("2020/day2/input_data.txt", "r")

list = file.readlines()

n = 0
for line in list:
    string = str(line)
    parts = string.split(" ")
    first = int(parts[0].split("-")[0])-1
    second = int(parts[0].split("-")[1])-1
    letter = parts[1][0]
    pswd = parts[2]

    if len(pswd) >= second and pswd[first] == letter and pswd[second] != letter:
        n += 1
    elif len(pswd) >= second and pswd[first] != letter and pswd[second] == letter:
        n += 1
print n
