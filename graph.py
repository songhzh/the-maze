from itertools import count


class Vertex:
    # a way to keep track of connected vertices in the maze
    _id = count(0)

    def __init__(self):
        self.id = next(self._id)
        self.edges = set()

    def add_edge(self, v):
        self.edges |= {v}

    def get_edges(self):
        return self.edges


class Graph:
    # TODO: switch to Vertex class
    # Slightly modified graph class from lectures
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v):
        # v is tuple (x, y)
        if not self.is_vertex(v):
            self.vertices[v] = Vertex() # changed this from list

    def add_edge(self, e):
        # e is a tuple (a, b) where a, b are tuples (x, y)
        if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
            raise ValueError('A vertex is not in the graph')

        self.vertices[e[0]] |= {e[1]}
        self.vertices[e[1]] |= {e[0]}

    def get_vertices(self):
        return self.vertices

    def get_edges(self, v):
        return self.vertices[v]

    def get_all_vertices(self):
        # TODO
        # needs to return a partition
        # where each element/set is a vertex
        ret = set()
        for v in self.get_vertices().keys():
            ret |= {v}
        return ret

    def get_all_edges(self):
        ret = set()

        for u in self.get_vertices():
            for v in self.get_edges(u):
                ret |= {(u, v)}

        return ret

    def get_all_children(self, v):
        # a way to tell if two vertices are connected to each other
        pass

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


a = Vertex()
b = Vertex()
