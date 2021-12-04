import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

class Day18():
    def __init__(self):

    def run(self):

    def block(self, list, start):
        i = start

        while i < len(list):
            if list[i] == '+':
                # add
            elif list[i] == '*':
                # mult
            elif list[i][0] == '(':
                # new block
            elif list[i][-1] == ')':
                # end block
            else:
                # num

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
