import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

rules = {}
all_tickets = []
setup_stage = 0
ignore_next = False

# sort teh main data to rules and tickets
for line in input_list:
    if ignore_next:
        ignore_next = False
        continue
    if line == '':
        setup_stage += 1
        ignore_next = True
        continue

    #rules
    if setup_stage == 0:
        both_rules = []
        for rule_range in line.split(':')[-1].strip().split(' or '):
            A = int(rule_range.split('-')[0].strip())
            B = int(rule_range.split('-')[1].strip())
            rule = [i for i in range(A, B+1)]
            both_rules.extend(rule)
        rules[line.split(':')[0].rstrip()] = both_rules

    # tickets
    elif setup_stage == 1:
        my_ticket = [int(num.strip()) for num in line.split(',')]
        all_tickets.append(my_ticket)
        continue
    elif setup_stage ==2:
        ticket_nums = [int(num.strip()) for num in line.split(',')]
        all_tickets.append(ticket_nums)

# checking validity of tickets
possible = []
for name, numbers in rules.items():
    possible.extend(numbers)

valid_tickets = []
invalid_nums = []
for ticket in all_tickets:
    validity = True
    for num in ticket:
        if num not in possible:
            invalid_nums.append(num)
            validity = False
            break
    if validity:
        valid_tickets.append(ticket)

print('Validation number is: {}'.format(sum(invalid_nums)))

# writing all possible fields per column
possibilities = {}
for n in range(len(my_ticket)):
    field_values = [ticket[n] for ticket in valid_tickets]
    possible_fields = []
    for rule_name, rule in rules.items():
        validity = True
        for num in field_values:
            if num not in rule:
                validity = False
                break
        if validity:
            possible_fields.append(rule_name)

    possibilities[n] = possible_fields

# eliminating used possibilities
for i in range(len(possibilities)):
    for field_num, field_names in possibilities.items():
        if len(field_names) == 1:
            for fnum, fnames in possibilities.items():
                if fnum != field_num and field_names[0] in fnames:
                    fnames.remove(field_names[0])
                    possibilities[fnum] = fnames

# getting column numbers for departure fields
required_field_nums = []
for field_num, field_names in possibilities.items():
    if re.search('^departure', field_names[0]):
        required_field_nums.append(field_num)

# getting answer
answer = 1
for i in required_field_nums:
    answer *= my_ticket[i]

print('The answer is: {}'.format(answer))
