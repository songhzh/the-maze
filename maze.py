from time import sleep
from graph import Graph
from union_find import UnionFind
from cell import Cell

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.graph = Graph((width, height))

        for x in range(width):
            for y in range(height):
                self.graph.add_vertex((x, y))

        self.areas = UnionFind([cell.get_pos() for cell in self])
        self.edge_choices = self.graph.get_all_edges()

        self.player = self.graph.get_cell((0,0))

    def __iter__(self):
        """
        Returns an iterator to the start of the grid
        """

        self._i = 0
        self._j = 0

        return self

    def __next__(self):
        """
        Returns the next cell in the grid
        """

        if self._i < self.width and self._j < self.height:
            next_cell = self.graph.get_cell((self._i, self._j))

            self._i += 1
            if self._i == self.width:
                self._i = 0
                self._j += 1

            return next_cell
        else:
            # Done iterating over cells
            raise StopIteration

    def get_player(self):
        return self.player

    def generate(self, delay):
        # chooses a random item from all possible edges
        # and removes this choice
        choice = self.edge_choices.pop()

        # adds an edge if it is valid
        if self.areas.union(choice[0], choice[1]):
            self.graph.add_edge(choice)
        else:
            # TODO: draw wall to improve coolness B-)
            pass

        sleep(delay)

        # returns if maze is completely generated
        return len(self.edge_choices) == 1

    def player_move(self, dx, dy):
        # checks if an edge exists between current and next cell
        # if so, update player
        p1 = self.player.get_pos()
        p2 = self.player.x + dx, self.player.y + dy

        if self.graph.is_edge((p1, p2)):
            self.player = self.graph.get_cell(p2)
