import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

