import os
import re
import math

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["Time:      7  15   30",
             "Distance:  9  40  200"]

class BoatRace():
    def __init__(self, data):
        self.times = [int(time.strip()) for time in data[0].split(":")[-1].strip().split(" ") if time.strip() != ""]
        self.distances = [int(time.strip()) for time in data[1].split(":")[-1].strip().split(" ") if time.strip() != ""]

        self.new_time = int("".join([time.strip() for time in data[0].split(":")[-1].strip().split(" ") if time.strip() != ""]))
        self.new_distance = int("".join([time.strip() for time in data[1].split(":")[-1].strip().split(" ") if time.strip() != ""]))
        print(f"Times: {self.new_time}\nDistances: {self.new_distance}")

    def solve_race(self, time, dist):
        """
        (time - x) * x > dist
        x**2 - time*x + dist < 0
        x12 = (-(-t) +- sqrt(t**2 - 4*dist)) / 2
        x12 = t +- sqrt(t**2 - 4*dist)/2
        """
        lover_bound = (time - pow(time**2 - 4*dist, 0.5)) / 2
        if lover_bound % 1 == 0:
            # is equal to the max dist
            lover_bound = lover_bound + 1
        lover_bound = math.ceil(lover_bound)

        upper_bound = (time + pow(time**2 - 4*dist, 0.5)) / 2
        if upper_bound % 1 == 0:
            # is equal to the max dist
            upper_bound = upper_bound - 1
        upper_bound = math.floor(upper_bound)

        return [i for i in range(lover_bound, upper_bound + 1)]

    def task_one(self):
        number_of_options = []
        for i, time in enumerate(self.times):
            number_of_options.append(len(self.solve_race(time, self.distances[i])))

        result = 1
        for num in number_of_options:
            result = result * num
        return result

    def task_two(self):
        return len(self.solve_race(self.new_time, self.new_distance))



# DATA = test_data

BoatRace = BoatRace(DATA)
print(f"Task 1: Number of ways to win is {BoatRace.task_one()}")
print(f"Task 2: Number of ways to win is {BoatRace.task_two()}")