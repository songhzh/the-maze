from graph import Graph
from union_find import UnionFind
from kruskal import kruskal
from random import randint
from cell import Cell


class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[Cell((x, y)) for x in range(width)] for y in range(height)]

        # TODO: make undirected graph
        # where each vertex is the center of a cell
        # and each edge (4 max) is a direction
        # up / down / left / right
        # that is NOT blocked by a wall
        # TODO: adding a wall will simply remove this edge
        # see https://www.youtube.com/watch?v=_gHtMsPjsMo
