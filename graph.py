from cell import Cell


class Graph:

    def __init__(self, size):
        # size is tuple (w, l, h)
        self.cells = dict()
        self.width = size[0]
        self.length = size[1]
        self.height = size[2]

    def add_vertex(self, pos):
        # pos is tuple (x, y) or (x, y, z)

        if pos in self.cells:
            raise ValueError('Cell already in grid')

        self.cells[pos] = Cell(pos)

    def add_edge(self, edge):
        # edge is tuple (pos, pos)
        # only 1 direction is needed

        p1, p2 = edge[0], edge[1]

        if not self.is_vertex(p1) or not self.is_vertex(p2):
            raise ValueError('Cells not in grid')

        # undirected graph, add both directions
        self.cells[p1].add_edge(self.cells[p2])
        self.cells[p2].add_edge(self.cells[p1])

    def get_all_edges(self):
        ret = set()

        for cell in self.cells.values():
            # returns one direction for the edge
            # i.e. even though the graph is bidirectional,
            # we only return 1 of the 2 directions
            pos1 = (cell.x, cell.y)

            if cell.x < self.width - 1:
                # edge from current cell to cell on right
                pos2 = (cell.x + 1, cell.y)
                ret |= {(pos1, pos2)}

            if cell.y < self.height - 1:
                # edge from current cell to cell below
                pos3 = (cell.x, cell.y + 1)
                ret |= {(pos1, pos3)}

        return ret

    def get_cell(self, pos):
        if pos not in self.cells:
            raise ValueError('Cell not in grid')

        return self.cells[pos]

    def get_vertices(self):
        return self.cells

    def get_edges(self, pos):
        if pos not in self.cells:
            raise ValueError('Cell not in grid')

        return self.cells[pos].get_edges()

    def is_vertex(self, pos):
        return pos in self.cells

    def is_edge(self, edge):
        p1, p2 = edge[0], edge[1]

        if not self.is_vertex(p1) or not self.is_vertex(p2):
            return False

        # either direction is ok
        return self.cells[p1] in self.cells[p2].get_edges()


if __name__ == '__main__':
    g = Graph()
    g.add_vertex((1, 1))
    g.add_vertex((2,2))
    g.add_vertex((3,3))
    g.add_edge(((1,1), (2,2)))
    print(g.is_edge(((4,4), (3,3))))
