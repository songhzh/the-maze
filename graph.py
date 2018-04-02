class Graph:
    # Slightly modified graph class from lectures
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v):
        # v is tuple (x, y)
        if not self.is_vertex(v):
            self.vertices[v] = set() # changed this from list

    def add_edge(self, e):
        # e is a tuple (a, b) where a, b are tuples (x, y)
        if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
            raise ValueError('A vertex is not in the graph')

        self.vertices[e[0]] += {e[1]}

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

        # maybe make ret a list
        # sort it by manhattan distance
        # before returning
        return ret

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

g = Graph()

g.add_vertex((1,1))
g.add_vertex((2,2))

k = g.get_all_vertices()

print(k)
