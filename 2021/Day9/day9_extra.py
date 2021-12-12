
file = open("input_data.txt", "r")

map = [[int(i) for i in row.strip()] for row in file.readlines()]

class MapFloor():
    """
    Class containing methods for locating low areas in a map.
    """
    def __init__(self, map):
        """
        low-points - the locations that are lower than any of its adjacent locations
        basin - all locations that eventually flow downward to a single low point
        :param map: [[int,],]
        """
        self.map = map
        self.low_points = self.get_lowpoints()
        self.ridge = 9

    def puzzle_one(self):
        """
        What is the sum of the risk levels of all low points on your heightmap?
        :return: int
        """
        return sum([self.get_height(coords, adjusted=True) for coords in self.low_points])

    def puzzle_two(self):
        """
        What do you get if you multiply together the sizes of the three largest basins?
        :return: int
        """
        basins = []
        for coords in self.low_points:
            basins.append(len(self.get_basin(coords)))
        answer = 1
        for i in range(1, 4):
            answer *= sorted(basins)[-i]
        return answer

    def get_basin(self, low_point):
        """
        Find coordinates of of a basin from a low point
        :param low_point: [int, int]
        :return: [[int, int],]
        """
        basin_points = [low_point,]
        for point in basin_points:
            for coord in self.get_neigbours(point):
                if self.validate_coord(coord) and coord not in basin_points and self.get_height(coord) < self.ridge:
                    basin_points.append(coord)
        return basin_points

    def get_height(self, coords, adjusted=False):
        """
        Return the height value on the map coordinate. Adjusted for +1 if True.
        :param coords: [int, int]
        :param adjusted: bool
        :return: int
        """
        return self.map[coords[0]][coords[1]] + int(adjusted)

    def get_lowpoints(self):
        """
        Find all the low-points in the map
        :return: [[int, int],]
        """
        low_points = []
        for row, line in enumerate(self.map):
            for col, height in enumerate(line):
                height_coords = self.get_neigbours([row, col])
                neighbours = [map[r][c] for r, c in height_coords if self.validate_coord([r, c])]
                if all([height < height_n for height_n in neighbours]):
                    low_points.append([row, col])
        return low_points

    def get_neigbours(self, coords):
        """
        Return all the valid neighbour coordinates.
        :param coords: [int, int]
        :return: [[int, int],]
        """
        row, col = coords
        return [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]

    def print_map(self):
        """ Prints the map. """
        [print(row) for row in self.map]
        return

    def validate_coord(self, coord):
        """
        Checks that the coordinate is within the map
        :param coord: [int, int]
        :return: bool
        """
        row, col = coord
        return 0 <= row < len(self.map) and 0 <= col < len(self.map[0])


mapping_system = MapFloor(map)
# mapping_system.print_map()
print("The sum of low-point heights is:\n {}".format(mapping_system.puzzle_one()))
print("The multiplication of three largest basins is:\n {}".format(mapping_system.puzzle_two()))

