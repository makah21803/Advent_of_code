import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

class Bag():
    def __init__(self, bag, rules):
        self.content = [re.sub('[0-9]|bags|bag|\.', '', slice).strip() for slice in rules.split(',') if not re.search('no other', slice)]
        self.content_all = self.propper_content(rules)

    def extend_rules(self):
        for bag in self.content:
            new_bags = [new_bag for new_bag in bags[bag].content if new_bag not in self.content]
            self.content.extend(new_bags)

    def num_of_bags_inside(self):
        bags_inside = self.content_all
        for bag in bags_inside:
            bags_inside.extend([new_bag for new_bag in bags[bag].content_all])
        return len(bags_inside)

    def propper_content(self, rules):
        content = []
        for  slice in rules.split(','):
             if not re.search('no other', slice):
                bag = re.sub('bags|bag|\.', '', slice).strip()
                n = 1
                if re.search('^[0-9]', bag):
                    n = int(bag.split(' ')[0])
                    bag = re.sub('^[0-9]', '', bag).lstrip()
                    
                content.extend([bag for i in range(n)])
        return content



bags = {}
for line in list:
    if line != '\n':
        name = line.split('bags contain')[0].rstrip()
        rule = line.split('bags contain')[1].strip()
        bags[name] = Bag(name, rule) 

for bag in bags:
    bags[bag].extend_rules()

count = 0
inside_shiny = 0
for bag in bags:
    if 'shiny gold' in bags[bag].content:
        count += 1
    if bag == 'shiny gold':
        print ('shiny is there')
        inside_shiny = bags[bag].num_of_bags_inside()
        

print ('Shiny gold bag can be carried in {} different bags.'.format(count))

print ('Shiny gold bag must contain {} other bags'.format(inside_shiny))
