import numpy as np
import random
from graph import Graph
from union_find import UnionFind
from cell import Cell

cell_choices = np.array(['north', 'south', 'east', 'west'])

direction_increment = {
    'north': (0, -1),
    'east': (1, 0),
    'south': (0, 1),
    'west': (-1, 0)
}

opposite_direction = {
    'north': 'south',
    'east': 'west',
    'south': 'north',
    'west': 'east'
}


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[Cell((x, y)) for x in range(width)] for y in range(height)]

        self.graph = Graph()

        for cell in self:
            self.graph.add_vertex(cell.get_pos())

        self.areas = UnionFind([cell.get_pos() for cell in self])

        # TODO: make undirected graph
        # where each vertex is the center of a cell
        # and each edge (4 max) is a direction
        # up / down / left / right
        # that is NOT blocked by a wall
        # TODO: adding a wall will simply remove this edge
        # see https://www.youtube.com/watch?v=_gHtMsPjsMo

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
            next_cell = self.grid[self._i][self._j]

            self._i += 1
            if self._i == self.width:
                self._i = 0
                self._j += 1

            return next_cell
        else:
            # Done iterating over cells
            raise StopIteration

    def random_merge(self):
        rx1 = random.randint(0, self.width - 1)
        ry1 = random.randint(0, self.height - 1)

        # Choose a direction for the edge
        edge_direction = np.random.choice(cell_choices, 1)[0]

        cell = self.grid[ry1][rx1]
        step = direction_increment[edge_direction]
        rx2, ry2 = cell.x + step[0], cell.y + step[1]

        # We can make an edge here
        if not cell.has_edge(edge_direction) and rx2 > 0 and ry2 > 0 \
                and rx2 < self.width and ry2 < self.height:

            cell2 = self.grid[ry2][rx2]

            if self.areas.union((rx1, ry1), (rx2, ry2)):
                # We merged the two cells
                cell.add_edge(edge_direction, cell2)
                cell2.add_edge(opposite_direction[edge_direction], cell)
