from graph import Graph
from union_find import UnionFind
from managed_set import ManagedSet
from binary_heap import BinaryHeap


class Maze:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.generated = False
        self.graph = Graph((width, length, height))

        self.edge_queue = BinaryHeap()
        self.edges_added = 0
        self.inter_layer_edges = 0

        for x in range(width):
            for y in range(length):
                for z in range(height):
                    self.graph.add_vertex((x, y, z))

        self.areas = UnionFind([cell.get_pos() for cell in self])
        self.edge_choices = ManagedSet(self.graph.get_all_edges())
        self.queue_factor = len(self.edge_choices) // 7

        for _ in range(self.queue_factor):
            edge = self.edge_choices.pop_random()
            self._queue_edge(edge)

        self.player = self.graph.get_cell((0, 0, 0))

        self.end_cell = self.graph.get_cell((self.width - 1, self.length - 1, self.height - 1))
        self.end_cell.is_end = True

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

    def get_layer(self, layer):
        return self.graph.get_layer(layer)

    def get_player(self):
        return self.player

    def generate(self):

        # Loop until we have removed a wall
        while not self.generated:

            # chooses a random item from all possible edges
            # and removes this choice
            if len(self.edge_choices) > 1:
                self._queue_edge(self.edge_choices.pop_random())

            (p1, p2), _ = self.edge_queue.popmin()

            # adds an edge (removes a wall) if it is valid
            if self.areas.union(p1, p2):
                self.graph.add_edge((p1, p2))
                return self.graph.get_cell(p1), self.graph.get_cell(p2)

            # Check if maze is completely generated
            if len(self.edge_queue) == 0:
                self.generated = True

        return None

    def _queue_edge(self, edge):
        # Inter-layer edges cost more, and are placed progressively later in the queue
        if edge[0][2] != edge[1][2]:
            cost = self.queue_factor * self.inter_layer_edges
            self.inter_layer_edges += 1
        else:
            cost = self.edges_added
            self.edges_added += 1

        self.edge_queue.insert(edge, cost)

    def player_move(self, dx, dy, dz):
        # checks if an edge exists between current and next cell
        # if so, update player
        p1 = self.player.get_pos()
        p2 = self.player.x + dx, self.player.y + dy, self.player.z + dz

        if self.graph.is_edge((p1, p2)):
            self.player = self.graph.get_cell(p2)
        else:
            p2 = p1

        return self.graph.get_cell(p1), self.graph.get_cell(p2)

    def check_layer(self, new_layer):
        if new_layer < 0:
            return 0
        elif new_layer >= self.height:
            return self.height - 1
        else:
            return new_layer
