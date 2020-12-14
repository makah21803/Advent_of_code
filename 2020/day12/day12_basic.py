import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]


class LogTravel():

    def __init__(self):
        self.longtitude = 0
        self.latitude = 0
        self.facing = 'E'
        self.facing_encode = {'N':0, 'E':1, 'S':2, 'W':3}
        self.facing_decode = ('N', 'E', 'S', 'W')

        self.call_dict = {'N': {'fce': self.travel, 'dir': 'long', 'add':1},
                          'S': {'fce': self.travel, 'dir': 'long', 'add':-1},
                          'E': {'fce': self.travel, 'dir': 'lat', 'add':1},
                          'W': {'fce': self.travel, 'dir': 'lat', 'add':-1},
                          'L': {'fce': self.turn, 'dir': None, 'add':-1},
                          'R': {'fce': self.turn, 'dir': None, 'add':1},
                          }

    def run(self, list):
        for line in list:
            call = str(line[0])
            arg = int(line[1:])
            print('call {}'.format(line))
            if call == 'F':
                call = self.facing
            print(call)

            fce = self.call_dict[call]['fce']
            dir = self.call_dict[call]['dir']
            add = self.call_dict[call]['add']
            fce(dir, add, arg)

        manhattan_distance = abs(self.latitude) + abs(self.longtitude)
        return manhattan_distance

    def travel(self, direction, add, value):
        if direction == 'lat':
            self.latitude += add * value
        if direction == 'long':
            self.longtitude += add * value

        print('Latitude: {}, Longtitude: {}'.format(self.latitude, self.longtitude))

    def turn(self, direction, add, value):
        steps = int(value /90)
        self.facing = self.facing_decode[(self.facing_encode[self.facing] + add*steps) %4]


manhattan_distance = LogTravel().run(input_list)

print('The Manhattan Distance of the ship is {}'.format(manhattan_distance))


