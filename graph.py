from itertools import count


class Vertex:
    # a way to keep track of connected vertices in the maze
    # apparently id is a reserved keyword so we are using idn

    def __init__(self, idn):
        self.idn = idn
        self.edges = set()

    def add_edge(self, v):
        self.edges |= {v}

    def get_edges(self):
        return self.edges

    def get_idn(self):
        return self.idn

    def set_idn(self, idn):
        # TODO: recursively change the idn of all connected vertices as well
        self.idn = idn

class Graph:
    # Slightly modified graph class from lectures
    _idn = count(0)

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v):
        # v is tuple (x, y)
        if not self.is_vertex(v):
            idn = next(self._idn)
            self.vertices[v] = Vertex(idn) # changed this from list

    def add_edge(self, e):
        # e is a tuple (a, b) where a, b are tuples (x, y)
        if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
            raise ValueError('A vertex is not in the graph')

        if self.get_idn(e[0]) == self.get_idn(e[1]):
            # make sure maze shape is retained
            raise ValueError('Vertices are already connected')

        self.vertices[e[0]].add_edge(e[1])
        self.vertices[e[1]].add_edge(e[0])

        # links vertices together
        self.set_idn(e[1], self.get_idn(e[0]))

        # print(self.vertices[e[0]].get_idn())
        # print(self.vertices[e[1]].get_idn())

    def set_idn(self, v, idn):
        if not self.is_vertex(v):
            raise ValueError('The vertex is not in the graph')

        self.vertices[v].set_idn(idn)

    def get_idn(self, v):
        if not self.is_vertex(v):
            raise ValueError('The vertex is not in the graph')

        return self.vertices[v].get_idn()

    def get_vertices(self):
        return self.vertices

    def get_edges(self, v):
        return self.vertices[v].get_edges()

    def get_all_edges(self):
        ret = set()

        for u in self.get_vertices():
            for v in self.get_edges(u):
                # only adds 1 edge direction to set
                # 2nd direction may be needed later
                ret |= {(u, v)}
                # ret |= {(v, u)}
        return ret

    def is_vertex(self, v):
        return v in self.vertices

    def is_edge(self, e):
        if not self.is_vertex(e[0]) or not self.is_vertex(e[1]):
            return False
        else:
            # undirected graph, so either direction should should be ok
            return e[0] in self.get_edges(e[1])


if __name__ == '__main__':
    # sandbox

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')

    g.add_edge(('a', 'b'))

    print(g.get_vertices())
    print(g.get_edges('a'))
    print(g.get_edges('b'))
