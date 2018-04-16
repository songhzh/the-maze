from collections import deque


class Solver:
    """
    Uses breadth-first search to find the path from the start to the end of the maze
    Note that since our maze is a Minimum Spanning Tree, there is only one solution
    """
    def __init__(self, maze):
        self.graph = maze.graph
        self.path = list()

        tree = self.get_tree(maze.player)
        self.solve(tree, maze.player, maze.end_cell)

    def get_tree(self, start):
        # implementation of breadth-first search from class
        reached = {start: start}
        todo = deque([start])

        while todo:
            curr = todo.popleft()
            for cell in self.graph.get_edges(curr.get_pos()):
                if cell not in reached:
                    reached[cell] = curr
                    todo.append(cell)

        return reached

    def solve(self, reached, start, final):
        # implementation of path-finder from class
        # order does not matter so list is not reversed
        if final not in reached:
            raise ValueError('Maze has no solutions?')

        self.path = [final]

        while final != start:
            final = reached[final]
            self.path.append(final)

    def show_hint(self):
        for cell in self.path:
            cell.flip_hint()
