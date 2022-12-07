
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
test_list = [line.strip() for line in test_file.readlines()]



class FileManager():

    def __init__(self, terminal_commands):
        self.directories = {}
        self.files = {}
        self.active_dirs = []

        for command in terminal_commands:
            if command[0:4] == "$ cd":
                self.cd(command[4:].strip())
            elif re.search("^[0-9]", command.strip()):
                file_bits = [bit.strip() for bit in command.split(" ")]
                file_path = "/".join(self.active_dirs) + "/" + file_bits[1]
                self.file_found(file_size=file_bits[0])

    def cd(self, directory):
        """ Adds or removes directory from the list of active directories (all up to the current dir) """

        if directory == "..":
            self.active_dirs.pop()
        else:
            self.active_dirs.append(directory)

    def file_found(self, file_size):
        """ Adds the filesize to all directories up to the active directory """

        for i, dir_name in enumerate(self.active_dirs):
            dir_path = "/".join([self.active_dirs[j] for j in range(i+1)])
            if dir_path not in self.directories.keys():
                self.directories[dir_path] = 0

            self.directories[dir_path] += int(file_size)

    def part_one(self, size_limit):
        total_size = 0
        for dir_name in self.directories.keys():
            dir_size = self.directories[dir_name]
            if dir_size <= size_limit:
                total_size += dir_size
        return total_size

    def part_two(self, needed_size, total_size):
        taken_size = self.directories["/"]
        size_to_free = needed_size - (total_size - taken_size)

        smallest_fitting = taken_size
        for dir_name in self.directories.keys():
            dir_size = self.directories[dir_name]
            if smallest_fitting > dir_size >= size_to_free:
                smallest_fitting = dir_size

        return smallest_fitting


file_system = FileManager(input_list)

print(f"The sum of the total sizes of directories under limit is {file_system.part_one(100000)}")
print(f"The sizes of the smallest directory which frees enough space is {file_system.part_two(30000000, 70000000)}")

