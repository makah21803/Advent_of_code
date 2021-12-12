file = open("input_data.txt", "r")

list = [int(n.strip()) for n in file.readlines()[0].split(",")]
list.sort()

for day in range(80):
    """ Runs for about 100s """
    # print([i-day for i in list])
    # print("Day: {}".format(day))
    list.sort()
    new_borns = 0
    for f, fish in enumerate(list):
        if list[0] == day:
            list.pop(0)
            new_borns += 1
            list.append(day+9)
            list.append(day+7)
            continue
        break

    if new_borns > 0:
        print("Day: {} was born {}".format(day, new_borns))

print(len(list))
