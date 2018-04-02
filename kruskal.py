from graph import Graph

def kruskal(g):
    # https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    s = set()

    for v in g.get_vertices():
