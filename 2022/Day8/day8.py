
import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")
test_file = open(dirname+"/test_data.txt", "r")

input_list = [line.strip() for line in file.readlines()]
# input_list = [line.strip() for line in test_file.readlines()]



class Forest():
    def __init__(self, tree_rows):
        self.tree_grid = [[int(tree) for tree in row] for row in tree_rows]

    def part_one(self):
        self.visibility_grid = [[0 for c in range(len(self.tree_grid[0]))] for r in range(len(self.tree_grid))]
        for r, row in enumerate(self.tree_grid):
            # from left
            tallest = -1
            for c, tree in enumerate(row):
                if tree > tallest:
                    self.visibility_grid[r][c] = 1
                    tallest = tree
                    continue
                if tallest == 9:
                    break
            # from right
            tallest = -1
            for c in range(len(row)):
                c = -c-1
                tree = row[c]
                if tree > tallest:
                    self.visibility_grid[r][c] = 1
                    tallest = tree
                    continue
                if tallest == 9:
                    break

        for c in range(len(self.tree_grid[0])):
            column = [row[c] for row in self.tree_grid]
            # from top
            tallest = -1
            for r, tree in enumerate(column):
                if tree > tallest:
                    self.visibility_grid[r][c] = 1
                    tallest = tree
                    continue
                if tallest == 9:
                    break
            # from bot
            tallest = -1
            for r in range(len(column)):
                r = -r-1
                tree = column[r]
                if tree > tallest:
                    self.visibility_grid[r][c] = 1
                    tallest = tree
                    continue
                if tallest == 9:
                    break

        return sum([sum(row) for row in self.visibility_grid])

    def look_east(self, start_r, start_c):
        start_tree = self.tree_grid[start_r][start_c]
        r = start_r
        visible_trees = 0
        for c in range(start_c+1, len(self.tree_grid[0])):
            visible_trees += 1
            tree = self.tree_grid[r][c]
            if tree >= start_tree:
                break
        return visible_trees

    def look_west(self, start_r, start_c):
        start_tree = self.tree_grid[start_r][start_c]
        r = start_r
        visible_trees = 0
        for c in range(-start_c, 0):
            c = -c-1
            visible_trees += 1
            tree = self.tree_grid[r][c]
            if tree >= start_tree:
                break
        return visible_trees

    def look_south(self, start_r, start_c):
        start_tree = self.tree_grid[start_r][start_c]
        c = start_c
        visible_trees = 0
        for r in range(start_r+1, len(self.tree_grid)):
            visible_trees += 1
            tree = self.tree_grid[r][c]
            if tree >= start_tree:
                break
        return visible_trees

    def look_north(self, start_r, start_c):
        start_tree = self.tree_grid[start_r][start_c]
        c = start_c
        visible_trees = 0
        for r in range(-start_r, 0):
            r = -r-1
            visible_trees += 1
            tree = self.tree_grid[r][c]
            if tree >= start_tree:
                break
        return visible_trees

    def part_two(self):
        self.view_grid = [[0 for c in range(len(self.tree_grid[0]))] for r in range(len(self.tree_grid))]

        for r, row in enumerate(self.tree_grid):
            for c in range(len(row)):
                tree_score = self.look_north(r, c)
                tree_score *= self.look_east(r, c)
                tree_score *= self.look_south(r, c)
                tree_score *= self.look_west(r, c)

                self.view_grid[r][c] = tree_score

        return max([max(row) for row in self.view_grid])



forest_grid = Forest(input_list)
print(f"The total number of visible trees is {forest_grid.part_one()}")
print(f"The highest tree score possible is {forest_grid.part_two()}")

