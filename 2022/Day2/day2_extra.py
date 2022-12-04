import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = [line.strip() for line in file.readlines()]

hand_index = {"A": 0, "B": 1, "C": 2}
action_index = {"X": -1, "Y": 0, "Z": 1}

score = 0
for both_hands in list:
    action = action_index[both_hands[-1]]

    score += (action + 1) * 3
    score += (hand_index[both_hands[0]] + action) % 3 + 1

print("Total score is: {}".format(score))

