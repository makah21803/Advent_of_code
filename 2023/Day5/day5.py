import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

DATA = file.readlines()

test_data = ["seeds: 79 14 55 13",
             "",
             "seed-to-soil map:",
             "50 98 2",
             "52 50 48",
             "",
             "soil-to-fertilizer map:",
             "0 15 37",
             "37 52 2",
             "39 0 15",
             "",
             "fertilizer-to-water map:",
             "49 53 8",
             "0 11 42",
             "42 0 7",
             "57 7 4",
             "",
             "water-to-light map:",
             "88 18 7",
             "18 25 70",
             "",
             "light-to-temperature map:",
             "45 77 23",
             "81 45 19",
             "68 64 13",
             "",
             "temperature-to-humidity map:",
             "0 69 1",
             "1 0 69",
             "",
             "humidity-to-location map:",
             "60 56 37",
             "56 93 4",
             ""]



class Almanach():
    def __init__(self, data):
        self.seed_numbers = [int(seed.strip()) for seed in data[0].split(":")[-1].strip().split(" ")]
        self.maps = {}
        self.unpack_data(data)

    def unpack_data(self, data):
        map_name = "source-to-destination"
        planting_map = []
        for line in data:
            if line.split(":")[0] == "seeds":
                continue
            if line in ["", "\n"]:
                if map_name != "source-to-destination":
                    self.save_map(map_name, planting_map)
                continue
            if line.split(" ")[-1].strip() == "map:":
                map_name = line.split(" ")[0].strip()
                planting_map = []
                continue

            planting_map.append([int(num.strip()) for num in line.split(" ") if num.strip() != ""])

    def save_map(self, map_name, planting_map):
        self.maps[map_name] = planting_map

    def print_maps(self):
        for key in self.maps.keys():
            print(f"{key}:\n{self.maps[key]}")

    def extract_map(self, source, num_pair):
        for map_name in self.maps.keys():
            if map_name.split("-")[0] != source:
                continue

            next_source = map_name.split("-")[-1]
            planting_map = self.maps[map_name]
            new_num_pairs = []
            for single_range in planting_map:
                destination, source, range_length = single_range

                # pair outside
                if num_pair[1] < source or num_pair[0] >= source + range_length:
                    continue

                # pair inside
                elif (source <= num_pair[0] < source + range_length) and (source <= num_pair[1] < source + range_length):
                    new_num_pairs.append([destination + (num_pair[0] - source), destination + (num_pair[1] - source)])
                    num_pair = None
                    break

                # pair starts before ends inside
                elif num_pair[0] < source <= num_pair[1]:
                    new_num_pairs.append([destination, destination + (num_pair[1] - source)])
                    num_pair = [num_pair[0], source - 1]
                    continue

                # pair starts inside ends outside
                elif num_pair[0] < source + range_length <= num_pair[1]:
                    new_num_pairs.append([destination + (num_pair[0] - source), destination + range_length - 1])
                    num_pair = [source + range_length, num_pair[1]]
                    continue

            if num_pair is not None:
                new_num_pairs.append(num_pair)
            return new_num_pairs, next_source

    def loop_to_location(self, source, orig_num_pairs):
        num_pairs = []
        next_source = source
        for num_pair in orig_num_pairs:
            new_num_pairs, next_source = self.extract_map(source, num_pair)
            num_pairs.extend(new_num_pairs)
        # print(f"{source}s: {orig_num_pairs}")
        # print(f"{source} to {next_source}: {num_pairs}\n")
        source = next_source
        if source != "location":
            num_pairs = self.loop_to_location(source, num_pairs)
        return num_pairs

    def find_location(self, seed_pair):
        return self.loop_to_location("seed", [seed_pair,])

    def task_one(self):
        locations = []
        for seed in self.seed_numbers:
            location_pairs = self.find_location([seed, seed])
            locations.append(location_pairs[0][0])
        return min(locations)

    def get_seed_pairs(self):
        seed_pairs = []
        for i, seed_first in enumerate(self.seed_numbers):
            if i%2 != 0:
                continue

            seed_last = seed_first + self.seed_numbers[i + 1] - 1
            seed_pairs.append([seed_first, seed_last])
        return seed_pairs

    def task_two(self):
        locations = []
        for seed_pair in self.get_seed_pairs():
            location_pairs = self.loop_to_location("seed", [seed_pair,])
            # print(f"{seed_pair} > {location_pairs}")
            locations.append(min([location_pair[0] for location_pair in location_pairs]))
        return min(locations)



# DATA = test_data

Almanach = Almanach(DATA)
print(f"Task 1: Smallest location number is: {Almanach.task_one()}")
print(f"Task 2: Smallest location number is: {Almanach.task_two()}")

