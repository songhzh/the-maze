class BinaryHeap:
    """
    An implementation of a binary heap
    """

    def __init__(self):
        """
        Initialize an empty hear
        """

        self.nodes = list()

    def __len__(self):
        """
        Returns the number of items in the heap
        """

        return len(self.nodes)

    def min(self):
        """
        Returns the minimum-key item and its key as a pair
        """

        if len(self.nodes) == 0:
            raise IndexError('getting min from an empty heap')

        # min key item is always at the top of the heap
        return self.nodes[0]

    def _lchild(self, index):
        """
        Returns the index of the left child
        No bounds checking
        """

        return 2 * index + 1

    def _rchild(self, index):
        """
        Returns the index of the right child
        No bounds checking
        """

        return 2 * index + 2

    def _parent(selfself, index):
        """
        Retruns the index of the parent.
        No bounds checking.
        """

        return (index - 1) // 2

    def insert(self, item, key):
        """
        Inserts the item with the given key

        >>> heap = BinaryHeap()
        >>> heap.insert('cat', 4)
        >>> heap.insert('dog', 1)
        >>> heap.insert('pig', 2)
        >>> heap.min() == ('dog', 1)
        True
        >>> heap.insert('bear', 0)
        >>> heap.min() == ('bear', 0)
        True
        """

        index = len(self.nodes)
        self.nodes.append((item, key))

        while index > 0:
            parent = self._parent(index)
            if self.nodes[parent][1] > key:
                self.nodes[parent], self.nodes[index] = \
                    self.nodes[index], self.nodes[parent]
            index = parent

    def popmin(self):
        """
        Pop the minimum element from the heap

        >>> heap = BinaryHeap()
        >>> heap.insert('cat', 4)
        >>> heap.insert('dog', 1)
        >>> heap.insert('pig', 2)
        >>> heap.min() == ('dog', 1)
        True
        >>> heap.popmin() == ('dog', 1)
        True
        >>> heap.popmin() == ('pig', 2)
        True
        """

        min_item = self.min()

        # move last item to the root
        self.nodes[0] = self.nodes[-1]
        self.nodes.pop()

        index = 0

        while True:
            lc ,rc = self._lchild(index), self._rchild(index)

            if lc >= len(self):
                break

            # get minimum-index child
            if rc >= len(self) or self.nodes[lc][1] <= self.nodes[rc][1]:
                min_child = lc
            else:
                min_child = rc

            # check if there is a heap property violation
            if self.nodes[index][1] <= self.nodes[min_child][1]:
                break

            # Swap current vertex with minimum child
            self.nodes[min_child], self.nodes[index] = \
                self.nodes[index], self.nodes[min_child]

            index = min_child

        return min_item


def heapsort(items):
    """
    Return the sorted list of items

    >>> heapsort([5,4,2,1,2,3]) == [1, 2, 2, 3, 4, 5]
    True
    """

    heap = BinaryHeap()
    for x in items:
        heap.insert(None, x)

    s = []

    while heap:
        s.append(heap.popmin()[1])

    return s


if __name__ == '__main__':
    import doctest
    doctest.testmod()