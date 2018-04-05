from random import randint


class ManagedSet:
    """
    A class resembling the interface of a set that has the following properties:
    * If an element is already in the ManagedSet, don't add it again
    * O(1) insertion
    * O(1) find
    * O(1) random access
    * O(1) removal
    """

    def __init__(self, s=None):
        """
        Create a new managed set
        s can be any iterable to initialize the set
        """
        self._index_map = {}
        self._list = []

        if s is not None:
            for item in s:
                self.add(item)

    def __contains__(self, item):
        """
        Returns True if the item is in the set
        """
        return item in self._index_map

    def __len__(self):
        return len(self._list)

    def add(self, item):
        """
        Add an element to the ManagedSet if it doesn't yet exist
        """

        if item not in self:
            self._index_map[item] = len(self._list)
            self._list.append(item)

    def remove(self, item):
        """
        Remove an item from the ManagedSet if it exists
        """

        if item in self:
            item_index = self._index_map[item]
            last_item = self._list[-1]

            # Swap in the item from the end of the list
            self._list[item_index] = last_item
            self._list.pop()

            self._index_map[last_item] = item_index

    def pop_random(self):
        """
        Remove a random item from the set, and return it
        """

        rand_index = randint(0, len(self._list) - 1)
        item = self._list[rand_index]
        self.remove(item)
        return item


if __name__ == '__main__':
    test = ManagedSet({1, 2, 3})
    for _ in range(3):
        test.pop_random()

    print(len(test))
