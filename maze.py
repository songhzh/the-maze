from graph import Graph
from union_find import UnionFind
from display import draw_cell


class Maze:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.generated = False
        self.graph = Graph((width, length, height))

        for x in range(width):
            for y in range(length):
                for z in range(height):
                    self.graph.add_vertex((x, y, z))

        self.areas = UnionFind([cell.get_pos() for cell in self])
        self.edge_choices = self.graph.get_all_edges()

        self.player = self.graph.get_cell((0, 0, 0))

    def __iter__(self):
        """
        Returns an iterator to the start of the grid
        """

        self._i = 0
        self._j = 0
        self._k = 0

        return self

    def __next__(self):
        """
        Returns the next cell in the grid
        """

        if self._i < self.width and self._j < self.length \
                and self._k < self.height:

            next_cell = self.graph.get_cell((self._i, self._j, self._k))

            self._i += 1
            if self._i == self.width:
                self._i = 0
                self._j += 1
            if self._j == self.length:
                self._j = 0
                self._k += 1

            return next_cell
        else:
            # Done iterating over cells
            raise StopIteration

    def get_player(self):
        return self.player

    def generate(self, delay):

        # Loop until we have removed a wall
        while not self.generated:
            # chooses a random item from all possible edges
            # and removes this choice
            p1, p2 = self.edge_choices.pop()

            # adds an edge (removes a wall) if it is valid
            if self.areas.union(p1, p2):
                self.graph.add_edge((p1, p2))
                return self.graph.get_cell(p1), self.graph.get_cell(p2)
            else:
                # TODO: draw wall to improve coolness B-)
                pass

            # Check if maze is completely generated
            if len(self.edge_choices) == 1:
                self.generated = True

        return None

    def player_move(self, dx, dy):
        # checks if an edge exists between current and next cell
        # if so, update player
        p1 = self.player.get_pos()
        p2 = self.player.x + dx, self.player.y + dy

        if self.graph.is_edge((p1, p2)):
            self.player = self.graph.get_cell(p2)
