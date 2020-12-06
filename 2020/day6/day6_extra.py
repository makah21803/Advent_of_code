import re

file = open("2020/day6/input_data.txt", "r")

list = file.readlines()

answers = []
all_groups = []
answer_first = [l for l in list[0] if l not in ('\n', ' ')]
answers_wrong = []
for i, line in enumerate(list):
    if line == "\n":
        answers = [l for l in answer_first if l not in answers_wrong]
        answers.sort()
        all_groups.append(answers)
        print(answers)
        answers = []
        answers_wrong = []
        if i+1 < len (list):
            answer_first = [l for l in list[i+1] if l not in ('\n', ' ')]
        continue

    for letter in answer_first:
        if letter not in line and letter not in answers_wrong:
            answers_wrong.append(letter)
        

count = 0
for answers in all_groups:
    count += len(answers)


print('finished, answer is: {}'.format(count))
