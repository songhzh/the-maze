valid_directions = {'north', 'south', 'east', 'west', 'above', 'below'}


class Cell:
    """
    Represents one tile in the 3D maze grid
    """
    def __init__(self, pos):
        # pos is tuple (x, y) or (x, y, z)
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

        # Keep track of presence for all possible edges
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.above = None
        self.below = None
        self.is_end = False

        # Trace statuses
        self.visited = False
        self.hint = False

    def add_edge(self, cell):
        """
        Helper function to determine which edge type is being created
        Note: does not validate the cell pair
        """
        direction = self.get_relative_pos(cell)

        if direction in valid_directions and self.__dict__[direction] is None:
            self.__dict__[direction] = cell
        else:
            raise ValueError('Unable to connect cell')

    def has_edge(self, direction):
        """
        Return True if cell has an edge on ordinal 'direction'
        """
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
        """
        Return the set of all directions on which the cell has an edge
        """
        ret = set()

        for direction in valid_directions:
            if self.__dict__[direction] is not None:
                ret.add(self.__dict__[direction])

        return ret

    def flip_visit(self):
        """
        Toggle the visited state
        """
        self.visited = not self.visited

    def flip_hint(self):
        """
        Toggle the hint state
        """
        self.hint = not self.hint
