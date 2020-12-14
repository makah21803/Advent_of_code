import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]


class LogTravel():

    def __init__(self):
        self.longtitude = 0
        self.latitude = 0
        self.waypoint_long = 1
        self.waypoint_lat = 10

        self.call_dict = {'N': {'fce': self.waypoint, 'dir': 'long', 'add':1},
                          'S': {'fce': self.waypoint, 'dir': 'long', 'add':-1},
                          'E': {'fce': self.waypoint, 'dir': 'lat', 'add':1},
                          'W': {'fce': self.waypoint, 'dir': 'lat', 'add':-1},
                          'F': {'fce': self.travel, 'dir': None, 'add': None},
                          'L': {'fce': self.turn, 'dir': None, 'add':-1},
                          'R': {'fce': self.turn, 'dir': None, 'add':1},
                          }

    def run(self, list):
        for line in list:
            call = str(line[0])
            arg = int(line[1:])

            fce = self.call_dict[call]['fce']
            dir = self.call_dict[call]['dir']
            add = self.call_dict[call]['add']
            fce(dir, add, arg)

        manhattan_distance = abs(self.latitude) + abs(self.longtitude)
        return manhattan_distance

    def waypoint(self, direction, add, value):
        if direction == 'lat':
            self.waypoint_lat += add * value
        if direction == 'long':
            self.waypoint_long += add * value

    def turn(self, direction, add, value):
        """
        I had it set that NE are the positive values of long/lat
        :param int add: cw = +1, ccw = -1
        :param int value: the input argument in degrees
        """
        for step in range(int(value /90)):
            lat = self.waypoint_lat
            long = self.waypoint_long
            self.waypoint_lat = add * long
            self.waypoint_long = -add * lat

    def travel(self, direction, add, value):
        self.latitude += value * self.waypoint_lat
        self.longtitude += value * self.waypoint_long


manhattan_distance = LogTravel().run(input_list)

print('The Manhattan Distance of the ship is {}'.format(manhattan_distance))


