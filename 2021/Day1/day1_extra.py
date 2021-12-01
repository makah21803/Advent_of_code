
file = open("input_data.txt", "r")

list = file.readlines()
int_list = [int(i) for i in list]

counter = 0

for i in range(1, len(int_list)-2):

    # previous_sum = sum([int_list[i+n-1] for n in range(3)])
    # current_sum = sum([int_list[i+n] for n in range(3)])
    previous_sum = sum(int_list[i-1:i+2])
    current_sum = sum(int_list[i:i+3])

    if current_sum > previous_sum:
        counter += 1

    print("depth: {}\nprevious sum: {}\ncurrent sum: {}\n".format(int_list[i], previous_sum, current_sum))

print("answer is: {}".format(counter))

