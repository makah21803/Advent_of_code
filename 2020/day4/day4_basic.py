import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

passports = []
passport_dict = {}
for line in list:
    if line == "\n":
        passports.append(passport_dict)
        passport_dict = {}
        continue
    parts = str(line).split(" ")
    for field in parts:
        field_name = str(field.split(":")[0])
        field_value = field.split(":")[1]
        field_value = re.sub("\n$", "", field_value)
        passport_dict[field_name] = field_value

# passports.append(passport_dict)

count = 0
for passport in passports:
    if len(passport) >= 7:

        no_cid = [field for field in passport if field != "cid"]
        if len(no_cid) >= 7:
            count += 1


print('finished, answer is: {}'.format(count))
