import re

file = open("input_data.txt", "r")

list = file.readlines()



def split_input_output(line, output=True):
    display = re.split(" \| ", line)[int(output)]
    digits = [d.strip() for d in re.split(" ", display) if d.strip() != ""]
    return digits

def is_unique_digit(digit):
    if len(digit) in [2, 4, 3, 7]:
        return True
    return False

unique_num = 0
for line in list:
    digits = split_input_output(line)
    unique = [d for d in digits if is_unique_digit(d)]
    unique_num += len(unique)

print(unique_num)

