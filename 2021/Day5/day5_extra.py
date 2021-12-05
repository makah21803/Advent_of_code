
file = open("input_data.txt", "r")

list = file.readlines()


def ex_coord(line, a, b):
    coord = line.split(" -> ")[a].split(",")[b]
    return int(coord.strip())

coordinates = [[[ex_coord(l, 0,0),ex_coord(l, 0,1)],[ex_coord(l, 1,0),ex_coord(l, 1,1)]] for l in list]


class MappingSystem():
    def __init__(self, vent_lines):
        self.vent_lines = vent_lines
        self.vent_coords = {}
        self.run()

    def run(self):
        for line in self.vent_lines:
            x1 = line[0][0]
            x2 = line[0][1]
            y1 = line[1][0]
            y2 = line[1][1]

            if x1 == y1:
                # continue
                start = int(x2 > y2)
                increments = range(abs(x2 -y2) + 1)
                self.get_vent_coordinates(line[start], [0, 1], increments)

            elif x2 == y2:
                # continue
                start = x1 > y1
                increments = range(abs(x1 - y1) +1)
                self.get_vent_coordinates(line[start], [1, 0], increments)

            elif abs(x1 - x2) == abs(y1 - y2) or abs(x1 - y1) == abs(x2 - y2):
                # continue
                increments = range(abs(x1 - y1) + 1)
                direction = [int(x1 < y1) *2-1, int(x2 < y2) *2-1]
                self.get_vent_coordinates(line[0], direction, increments)

            else:
                print("line {} does not work".format(line))

    def get_vent_coordinates(self, start_coord, direction, _range):
        """
        Saves coordinates from starting coord, withing the given range,
        in directions defined byt inc_coord to self.vent_coords.
        :param start_coord: [int, int]
        :param direction: [int, int] values between -1 and 1
        :param _range: iterable
        :return:
        """
        for d in _range:
            coord = self.increment_coordinate(start_coord, d * direction[0], d * direction[1])
            coord_key = "[{}, {}]".format(coord[0], coord[1])
            if coord_key not in self.vent_coords.keys():
                self.vent_coords[coord_key] = 1
            else:
                self.vent_coords[coord_key] += 1
        return

    def increment_coordinate(self, coord, dx, dy):
        """
        Returns the given coordinate increased by dx and dy.
        :param coord: [int, int]
        :param dx: int
        :param dy: int
        :return: [int, int]
        """
        return [coord[0]+dx, coord[1]+dy]

    def count_multi_vents(self, limit=2):
        """
        Checks the vent locations and counts those that are larger then the given limit.
        :param limit: int
        :return: int
        """
        count = 0
        for key in self.vent_coords.keys():
            if self.vent_coords[key] >= limit:
                count += 1
        return count

    def print_map(self, map_size):
        """
        Prints square map of a given size.
        :param map_size: int
        :return:
        """
        for y in range(map_size):
            line = []
            for x in range(map_size):
                coord_key = "[{}, {}]".format(x, y)
                if coord_key in self.vent_coords.keys():
                    line.append(str(self.vent_coords[coord_key]))
                else:
                    line.append(' ')
            print(line)
        return


map = MappingSystem(coordinates)
# map.print_map(10)
print("There are {} locations with multiple vents.".format(map.count_multi_vents()))

