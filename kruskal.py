from graph import Graph

def kruskal(g):
    # https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
    # TODO: may also need to make tree class
    ret = set()


    for (u, v) in g.get_all_edges():
