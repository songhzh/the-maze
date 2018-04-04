class Cell:
    
    def __init__(self, pos):
        # pos is tuple (x, y) or (x, y, z)
        self.x = pos[0]
        self.y = pos[1]
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        # self.above = None
        # self.below = None

    def add_edge(self, cell):
        relative = self.get_relative_pos(cell)

        if relative == 'north' and self.north is None:
            self.north = cell
        elif relative == 'south' and self.south is None:
            self.south = cell
        elif relative == 'east' and self.east is None:
            self.east = cell
        elif relative == 'west' and self.west is None:
            self.west = cell
        else:
            raise ValueError('Unable to connect cell')

    def get_relative_pos(self, cell):
        if cell.get_y() < self.get_y():
            return 'north'
        elif cell.get_y() > self.get_y():
            return 'south'
        elif cell.get_x() > self.get_x():
            return 'east'
        elif cell.get_x() < self.get_x():
            return 'west'
        else:
            return None

    def get_pos(self):
        return (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_edges(self):
        return {self.north, self.south, self.east, self.west}
