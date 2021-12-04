
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
    """
    Determines winning or loosing strategies for the given set of bingo tables and numbers
    """

    def __init__(self, bingo_tables, numbers):
        self.size = 5
        self.numbers = numbers
        self.bingo_tables = bingo_tables
        self.crosses = [[] for t in self.bingo_tables]
        self.winning_tables = []

    def run(self, want_to_win=True):
        """
        :param want_to_win: bool
        :return: int
        """

        for n in numbers:
            for t, table in enumerate(bingo_tables):
                if self.cross_number(n, table, t):
                    print("Table {} crossed number {}".format(t, n))
                    if self.check_crosses(self.crosses[t]):
                        print("\nTable {} won with number {}".format(t, n))
                        if want_to_win:
                            return self.count_result(table, self.crosses[t])
                        # want to loose
                        if t not in self.winning_tables:
                            self.winning_tables.append(t)
                        if len(self.winning_tables) == len(self.bingo_tables):
                            return self.count_result(table, self.crosses[t])
        return False

    def cross_number(self, number, table, t):
        """
        Looks for a number in a table and appends it to crossed when found.
        :param number: int
        :param table: list(list(int))
        :param t: int #table index
        :return: bool
        """

        for row in range(self.size):
            for col in range(self.size):
                if table[row][col] == number:
                    self.crosses[t].append([row, col])
                    return True
        return False

    def check_crosses(self, crosses):
        """
        Checks if table won.
        :param crosses: [int, int]
        :return: bool
        """

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
        """
        Compute the final AoC answer: sum of numbers in the table that arent crossed
        multiplied by the winning number/

        :param table: list(list(int))
        :param crosses: [int, int]
        :return: int
        """

        result = 0
        for row in range(self.size):
            for col in range(self.size):
                if [row, col] not in crosses:
                    result += table[row][col]

        last_cross = crosses[-1]
        result *= table[last_cross[0]][last_cross[1]]
        return result


print(PlayBingo(bingo_tables, numbers).run(want_to_win=False))

