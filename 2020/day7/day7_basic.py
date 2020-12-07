import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

class Bag():
    def __init__(self, bag, rules):
        self.content = [re.sub('[0-9]|bags|bag|\.', '', slice).strip() for slice in rules.split(',') if not re.search('no other', slice)]

    def extend_rules(self):
        for bag in self.content:
            new_bags = [new_bag for new_bag in bags[bag].content if new_bag not in self.content]
            self.content.extend(new_bags)


bags = {}
for line in list:
    if line != '\n':
        name = line.split('bags contain')[0].rstrip()
        rule = line.split('bags contain')[1].strip()
        bags[name] = Bag(name, rule) 

for bag in bags:
    bags[bag].extend_rules()

count = 0
for bag in bags:
    if 'shiny gold' in bags[bag].content:
        count += 1

print ('Shiny gold bag can be carried in {} different bags.'.format(count))
