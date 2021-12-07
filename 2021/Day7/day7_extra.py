file = open("input_data.txt", "r")

list = [int(n.strip()) for n in file.readlines()[0].split(",")]

min_fuel = 9999999999999999999

for i in range(2000):
    fuel = sum([(abs(i-p)+1)*abs(i-p)/2 for p in list])
    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)

