import re

file = open("2020/day6/input_data.txt", "r")

list = file.readlines()

answers = []
all_groups = []
for line in list:
    if line == "\n":
        answers.sort()
        all_groups.append(answers)
        answers = []
        continue
    for letter in line:
        if letter not in answers and letter not in ('\n', ' '):
            answers.append(letter)

count = 0
for answers in all_groups:
    count += len(answers)


print('finished, answer is: {}'.format(count))
