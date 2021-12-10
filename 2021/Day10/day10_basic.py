from collections import Counter
import re


file = open("input_data.txt", "r")

list = [line.strip() for line in file.readlines()]
regex = "(\(\))|(\[])|({})|(<>)"

errors = []

for line in list:
    while re.findall(regex, line):
        line = re.sub(regex, "", line)
    for s in line:
        if s in [")", "]", "}", ">"]:
            errors.append(s)
            break

error_value = 0
error_dict = Counter(errors)
print(error_dict)
for key in error_dict.keys():
    if key == ")":
        error_value += error_dict[key] *3
    if key == "]":
        error_value += error_dict[key] *57
    if key == "}":
        error_value += error_dict[key] *1197
    if key == ">":
        error_value += error_dict[key] *25137

print(error_value)




