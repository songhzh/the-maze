valid_directions = {'north', 'south', 'east', 'west', 'above', 'below'}


class Cell:

    def __init__(self, pos):
        # pos is tuple (x, y) or (x, y, z)
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.above = None
        self.below = None
        self.is_end = False

        self.visited = False
        self.hint = False

    def add_edge(self, cell):
        direction = self.get_relative_pos(cell)

        if direction in valid_directions and self.__dict__[direction] is None:
            self.__dict__[direction] = cell
        else:
            raise ValueError('Unable to connect cell')

    def has_edge(self, direction):
        if direction in valid_directions:
            return self.__dict__[direction] is not None

        raise ValueError('Invalid edge direction')

    def get_relative_pos(self, cell):
        if cell.y < self.y:
            return 'north'
        elif cell.y > self.y:
            return 'south'
        elif cell.x > self.x:
            return 'east'
        elif cell.x < self.x:
            return 'west'
        elif cell.z > self.z:
            return 'above'
        elif cell.z < self.z:
            return 'below'
        else:
            return None

    def get_pos(self):
        return self.x, self.y, self.z

    def get_edges(self):
        ret = set()

        for direction in valid_directions:
            if self.__dict__[direction] is not None:
                ret.add(self.__dict__[direction])

        return ret

    def flip_visit(self):
        self.visited = not self.visited

    def flip_hint(self):
        self.hint = not self.hint
