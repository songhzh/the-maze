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

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

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

        self.vertices[e[0]].add_edge(e[1])
        self.vertices[e[1]].add_edge(e[0])

        id = self.vertices[e[0]].get_id()
        self.vertices[e[1]].set_id(id)

        # print(self.vertices[e[0]].get_id())
        # print(self.vertices[e[1]].get_id())

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
            return e[0] in self.vertices[e[1]].get_edges()


if __name__ == '__main__':
    # sandbox

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')

    g.add_edge(('a', 'b'))

    print(g.get_vertices())
    print(g.get_edges('a'))
    print(g.get_edges('b'))
