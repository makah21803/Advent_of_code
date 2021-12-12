from collections import Counter
import math
import re



file = open("input_data.txt", "r")

list = [line.strip() for line in file.readlines()]
regex = "(\(\))|(\[])|({})|(<>)"

corrupted = []
incomplete = []

for line in list:
    not_corrupted = True
    chunks = str(line)
    while re.findall(regex, chunks):
        chunks = re.sub(regex, "", chunks)
    for s in chunks:
        if s in [")", "]", "}", ">"]:
            corrupted.append(s)
            not_corrupted = False
            break

    if not_corrupted:
        chunks = ''.join([chunks[-i-1] for i in range(len(chunks))])
        incomplete.append(chunks)


corrupted_score = 0
corrupted_dict = Counter(corrupted)
for key in corrupted_dict.keys():
    if key == ")":
        corrupted_score += corrupted_dict[key] *3
    if key == "]":
        corrupted_score += corrupted_dict[key] *57
    if key == "}":
        corrupted_score += corrupted_dict[key] *1197
    if key == ">":
        corrupted_score += corrupted_dict[key] *25137

print("Corrupted score: {}".format(corrupted_score))


incomplete_scores = []
incomplete_scoring = {"(":1, "[":2, "{":3, "<":4}
for chunk in incomplete:
    chunk_score = 0
    for s in chunk:
        chunk_score = chunk_score*5 + incomplete_scoring[s]
    incomplete_scores.append(chunk_score)

winner_index = math.floor(len(incomplete_scores)/2)
incomplete_winner = sorted(incomplete_scores)[winner_index]

print("Incomplete score: {}".format(incomplete_winner))

