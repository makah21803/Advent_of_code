import os

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

input_list = [line for line in file.readlines()]


""" Prepare """
break_index = 0
for i, line in enumerate(input_list):
    if line.strip() == "":
        break_index = i
        break

n_stacks = int(input_list[break_index-1].strip()[-1])


""" Extract Stacks """
stacks_dict = {}
for stack_n in range(1, n_stacks+1):
    stacks_dict[stack_n] = list()

for i in range(break_index-1):
    line = input_list[i]

    for stack_n in range(1, n_stacks+1):
        crate_line_index = 1 + (stack_n-1)*4
        if crate_line_index >= len(line):
            break
        new_crate = line[crate_line_index]
        if new_crate != " ":
            stacks_dict[stack_n].append(new_crate)


for stack_n in range(1, n_stacks+1):
    stacks_dict[stack_n].reverse()
    print(stacks_dict[stack_n])


""" Move crates """
def move_crate(source, dest, n_crates=1):
    crates = [stacks_dict[source].pop() for i in range(n_crates)]
    crates.reverse()
    stacks_dict[dest].extend(crates)

for i in range(break_index+1, len(input_list)):
    command = input_list[i].split(" ")
    n_crates = int(command[1])
    source = int(command[3])
    destination = int(command[5])

    move_crate(source, destination, n_crates)

answer = "".join([stacks_dict[stack_n][-1] for stack_n in range(1, n_stacks+1)])

print(f"\nThe top crates are: {answer}")

