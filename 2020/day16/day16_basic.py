import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

rules = {}
nearby_tickets = []
setup_stage = 0
ignore_next = False

for line in input_list:
    if ignore_next:
        ignore_next = False
        continue
    if line == '':
        setup_stage += 1
        ignore_next = True
        continue

    if setup_stage == 0:
        both_rules = []
        for rule_range in line.split(':')[-1].strip().split(' or '):
            A = int(rule_range.split('-')[0].strip())
            B = int(rule_range.split('-')[1].strip())
            rule = [i for i in range(A, B+1)]
            both_rules.extend(rule)
        rules[line.split(':')[0].rstrip()[0:-1]] = both_rules

    elif setup_stage == 1:
        # my list
        continue
    elif setup_stage ==2:
        ticket_nums = [int(num.strip()) for num in line.split(',')]
        nearby_tickets.append(ticket_nums)

invalid_nums = []

possible = []
for name, numbers in rules.items():
    possible.extend(numbers)

for ticket in nearby_tickets:
    for num in ticket:
        if num not in possible:
            invalid_nums.append(num)
            break

error_rate = 0
for num in invalid_nums:
    error_rate += int(num)

print(invalid_nums)
print(error_rate)
