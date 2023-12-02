import os
import re



dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
data = file.readlines()

test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
             "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
             "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
             "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
             "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",]

dice_in_game = [12, 13, 14]

def decode_hand(hand):
    colour_dict = {"red": 0, "green": 1, "blue": 2}
    result_vector = [0, 0, 0]
    for dice in hand:
        colour = dice.split(" ")[-1]
        result_vector[colour_dict[colour]] = int(dice.split(" ")[0].strip())
    return result_vector

def check_game_validity(max_draw):
    for i, max_dice in enumerate(max_draw):
        if max_dice > dice_in_game[i]:
            return False
    return True

valid_games = []
game_powers = []
for game in data:
    maxima = [0, 0, 0]
    game_id = int(game.split(":")[0].split(" ")[-1])
    revelations = game.split(":")[-1].split(";")

    for revelation in revelations:
        hand = [dice.strip() for dice in revelation.split(",")]
        vector = decode_hand(hand)
        for i in range(3):
            maxima[i] = max(vector[i], maxima[i])

    game_power = maxima[0] * maxima[1] * maxima[2]
    game_powers.append(game_power)

    if check_game_validity(maxima):
        valid_games.append(game_id)

print(f"Valid games are: {valid_games}\n")
print(f"The sum of ids of valid games is: {sum(valid_games)}")
print(f"The sum of the powers of all games is:{sum(game_powers)}")










