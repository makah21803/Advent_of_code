import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [row.strip() for row in file.readlines()]

busses = [int(i.strip()) if i!='x' else i for i in input_list[1].split(',')]

arrivals = []
timetable = {}
skipped = 0
for i, bus in enumerate(busses):
    if bus == 'x':
        skipped += 1
        continue
    else:
        bus_info = {'i':i, 'skip':skipped}
        timetable[bus] = i
        skipped = 0

for n in (0, 1068781, 1068781):
    found = False
    for id, i in timetable.items():
        if (n+i) %(id) == 0:
            found = True
        else:
            found = False
            break
    if found:
        print(n)

upper_bound = 1
for id, i in timetable.items():
    upper_bound *= id
    print('(n+{}) %{} = 0'.format(i, id))

lower_bound = 2000000000000000

print(upper_bound)
print(lower_bound)

for n in range(round(lower_bound/983), round(upper_bound/983)):
    n = n*983-72
    found = False
    for id, i in timetable.items():
        if (n+i) %(id) == 0:
            found = True
        else:
            found = False
            break
    if found:
        print(n,' works')

n = 1
for id, i in timetable.items():
    n *= (id-i)

# n = p0 * (i1 + p1 * (...))


n = 1
for id, i in timetable.items():
    n = 1 + id*n

print(n)

print(timetable)
