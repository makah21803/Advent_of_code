import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/input_data.txt", "r")

input_string = file.readlines()[0].strip()


latest = []
unique = []
target_length = 14
found_at = 0
for i, l in enumerate(input_string):
    unique = []
    for x in latest:
        if x not in unique:
            unique.append(x)

    # print(f"\ni: {i}, l: {l}, \nlatest: {latest} \nunique: {unique}")

    if len(unique) == target_length-1 and l not in latest:
        found_at = i + 1
        break
    latest.append(l)
    if len(latest) > target_length-1:
        latest.pop(0)


print(f"The first marker is after character {found_at}")

