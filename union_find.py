class UnionFind:
    """
    Implementation of the union-find data structure.
    """

    def __init__(self, S):
        """
        Creates a new instance of the union-find
        data structure, initially being the partition
        of S where each item lies in a set of its own.

        S should be an iterable, like a set.
        If S contains copies of items, only one will
        appear in this union-find instance.
        """

        self.parent = {x:x for x in S}
        self.rank = {x:0 for x in S}

    def find(self, x):
        """
        Returns the representative for the set in the
        partition that contains x.

        Assumes x is in the original set S that this
        instance was initialized with.

        Hard to test this one individually,
        but it can be tested in conjunction with union().
        """

        while self.parent[x] != x:
            x = self.parent[x]

        return x

    def union(self, x, y):
        """
        Merges the two sets containing x and y.
        Does nothing if they were already in the set.
        Assumes both are in the original set S that
        this instance was initialized with.

        >>> uf = UnionFind({1,2,3,4,5})
        >>> uf.find(1)
        1
        >>> uf.find(2)
        2
        >>> uf.union(1,2)
        >>> uf.find(1) in {1,2}
        True
        >>> uf.union(3,4)
        >>> uf.union(1,4)
        >>> uf.find(2) == uf.find(3)
        True
        """

        x_rep = self.find(x)
        y_rep = self.find(y)

        # Do nothing if they are part of the same set
        if x_rep == y_rep:
            return

        if self.rank[x_rep] > self.rank[y_rep]:
            self.parent[y_rep] = x_rep
        elif self.rank[y_rep] > self.rank[x_rep]:
            self.parent[x_rep] = y_rep
        else:
            # Their ranks are equal
            self.parent[y_rep] = x_rep
            self.rank[x_rep] += 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
