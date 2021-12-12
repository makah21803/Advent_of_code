testdata =    [5483143223,
2745854711,
5264556173,
6141336146,
6357385478,
4167524645,
2176841721,
6882881134,
4846848554,
5283751526,]

data = [1553421288,
5255384882,
1224315732,
4258242274,
1658564216,
6872651182,
5775552238,
5622545172,
8766672318,
2178374835,]

class MapOctopuses():
    def __init__(self, data):
        self.map = [[int(n) for n in str(line)] for line in data]
        self.number_of_fashes = 0
        self.active = [0, 0]
        
    def puzzle_one(self, steps):
        for i in range(steps):
            self.run_step()
            if i%10 == 9 and i < 40:
                print("Step: {}".format(i+1))
                self.print_map()
        return self.number_of_fashes
        
    def puzzle_two(self, step_limit):
        for i in range(step_limit):
            self.run_step()
            if self.sync_check():
                return i+1
        return -1
            
    def run_step(self):
        for r, row in enumerate(self.map):
            for c, value in enumerate(row):
                self.active = [r, c]
                self.map[r][c] += 1
                
        for r, row in enumerate(self.map):
            for c, value in enumerate(row):
                self.flash([r,c])
        
        for r, row in enumerate(self.map):
            for c, value in enumerate(row):
                if value > 9:
                    self.map[r][c] = 0
        return
        
    def sync_check(self):
        for row in self.map:
            for value in row:
                if value != 0:
                    return False
        return True
                    
    def flash(self, coord):
        row,col = coord
        if self.map[row][col] != 10:
            return
        self.number_of_fashes += 1
        self.map[row][col] = 11
        neighbours = self.get_neighbours([row,col])
        for r,c in neighbours:
            if self.map[r][c] < 10:
                self.map[r][c] += 1
            if (r<=self.active[0] or (r==self.active[0] and c<=self.active[1])) and self.map[r][c]==10:
                self.flash([r,c])
        return
        
    def get_neighbours(self, coords):
        row, col = coords
        nbs = [[row-1,col],[row,col-1],
                    [row+1,col],[row,col+1],
                    [row-1,col-1],[row+1,col+1],
                    [row-1,col+1],[row+1,col-1]]
        return [c for c in nbs if self.validate_coord(c)]
                    
    def validate_coord(self, coord):
        row,col = coord
        return 0<=row<len(self.map) and 0<=col<len(self.map[0])
    
    def print_map(self):
        [print(row) for row in self.map]
        
map = MapOctopuses(testdata)
#map.print_map()
#print(map.puzzle_one(100))
print(map.puzzle_two(1000))

        