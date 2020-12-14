import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

etd = int(input_list[0])
busses = [int(i.strip()) if i!='x' else i for i in input_list[1].split(',')]

print(busses)

arrivals = []
timetable = {}
for bus in busses:
    if bus == 'x':
        arrival = len(busses)
    else:
        arrival = bus - (etd % bus)
    timetable[arrival] = bus
    arrivals.append(arrival)

first_arrival = min(arrivals)
print(timetable[first_arrival] * first_arrival)
