import re

file = open("input_data.txt", "r")
lines = [line.strip() for line in file]

dot_coords = [line.strip().split(",") for line in lines if re.match("^[0-9]*,[0-9]*$", line.strip())]
dot_coords = [[int(line[0]), int(line[1])] for line in dot_coords]

folds = [line for line in lines if re.match("^[a-z ]*=[0-9]*$", line)]


class Folding():
    def __init__(self, coords, folds):
        """
        Fold the coordinates according to fold instructions
        :param coords: [[x,y],]
        :param folds: [str]
        """
        self.dot_coords = coords
        self.folds = folds
        self.run()

    def run(self):
        """ Runs the folding """
        for fold_line in self.folds:
            axis, val = self.extract_fold(fold_line)
            self.dot_coords = self.fold(self.dot_coords, axis, val)

    def print_dots(self):
        """
        Print the folder result.
        (Inverted x and y for readability)
        :return: str matrix
        """
        for x in range(6):
            row = []
            for y in range(40):
                if [y, x] in self.dot_coords:
                    row.append("*")
                else:
                    row.append(" ")
            print(row)

    def fold(self, coords, axis, axis_val):
        """
        Fold by x or y axis
        :param coords: [[x, y],]
        :param axis: str ('x' or 'y')
        :param axis_val: int
        :return: [[x, y],]
        """
        if axis not in ['x', 'y']:
            return False

        coords_folded = []
        for x, y in coords:
            if axis == 'x':
                if x > axis_val:
                    x = 2 * axis_val - x
            elif axis == 'y':
                if y > axis_val:
                    y = 2 * axis_val - y
            if [x, y] not in coords_folded:
                coords_folded.append([x, y])

        return coords_folded

    def extract_fold(self, fold_line):
        """
        Extracts axis and axis_value from fold string
        :param fold_line: str
        :return: str, int
        """
        value = int(re.findall("[0-9]{1,9}$",fold_line)[0])
        if re.match("^[a-z ]*x=[0-9]*$", fold_line):
            return 'x', value
        elif re.match("^[a-z ]*y=[0-9]*$", fold_line):
            return 'y', value
        return False


Folding(dot_coords, folds).print_dots()

