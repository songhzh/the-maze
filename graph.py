class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v):
        # v is tuple (x, y)
        if not is_vertex(v):
            self.vertices[v] = list()

    def add_edge(self, e):
        # e is a tuple (a, b) where a, b are tuples (x, y)
        if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
            raise ValueError('A vertex is not in the graph')

        self.vertices[e[0]].append(e[1])

    def get_vertices(self):
        return self.vertices

    def get_edges(self, v):
        return self.vertices[v]

    def is_vertex(self, v):
        return v in self.vertices

    def is_edge(self, e):
        if not self.is_vertex(e[0]):
            return False
        else:
            return e[1] in self.vertices[e[0]]

    def neighbours(self, v):
        if not self.is_vertex(v):
            raise ValueError('Vertex is not in the graph')

        return self.vertices[v]
