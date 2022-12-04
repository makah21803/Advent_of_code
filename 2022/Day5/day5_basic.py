import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]



