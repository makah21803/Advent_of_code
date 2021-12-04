import re

file = open("input_data.txt", "r")

list = file.readlines()

numbers = [int(n) for n in list[0].split(",")]
list.pop(0)
list.pop(0)

bingo_tables = []

table = []
for line in list:
    if line == "\n":
        bingo_tables.append(table)
        table = []
        continue

    table.append([int(n.strip()) for n in line.split(" ") if n.strip() != ""])


class PlayBingo():
    def __init__(self):
        self.size = 5
        self.crosses = []

    def run(self, bingo_tables, numbers):
        self.crosses = [[] for t in bingo_tables]
        for n in numbers:
            for t, table in enumerate(bingo_tables):
                if self.cross_number(n, table, t):
                    print("Table {} crossed number {}".format(t, n))
                    if self.check_crosses(self.crosses[t]):
                        print("\nTable {} won with number {}".format(t, n))
                        return self.count_result(table, self.crosses[t])
        return False

    def cross_number(self, number, table, t):
        for row in range(self.size):
            for col in range(self.size):
                if table[row][col] == number:
                    self.crosses[t].append([row, col])
                    return True
        return False

    def check_crosses(self, crosses):
        crosses_row = [cross[0] for cross in crosses]
        crosses_col = [cross[1] for cross in crosses]

        for cross in crosses_row:
            if crosses_row.count(cross) == self.size:
                return True

        for cross in crosses_col:
            if crosses_col.count(cross) == self.size:
                return True

        return False

    def count_result(self, table, crosses):
        result = 0
        for row in range(self.size):
            for col in range(self.size):
                if [row, col] not in crosses:
                    result += table[row][col]

        last_cross = crosses[-1]
        result *= table[last_cross[0]][last_cross[1]]
        return result


print(PlayBingo().run(bingo_tables, numbers))

