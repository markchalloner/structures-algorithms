class Heap:
    comparator = None
    heap = None

    def __init__(self, comparator=None):
        if comparator is None:
            comparator = lambda a, b: a > b
        self.comparator = comparator
        self.heap = []

    def __getitem__(self, key):
        return self.heap[key]

    def __iter__(self):
        for i in self.heap:
            yield i

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return repr(self.heap)

    def __str__(self):
        return str(self.heap)

    def add(self, item):
        self.heap.append(item)
        self.restore_heap_property()

    def add_list(self, items):
        for item in items:
            self.add(item)

    def pop(self):
        item = self.heap.pop(0)
        count = len(self.heap)

        # Restore heap property on all leaf nodes.
        for i in range(count // 2, count):
            self.restore_heap_property(i)
        return item

    def restore_heap_property(self, child=None):
        if len(self) == 0:
            return

        if child is None:
            child = len(self) - 1

        if child == 0:
            return

        parent = (child - 1) // 2

        # Swap if child node does not compare succesfully to parent.
        if self.comparator(self.heap[child], self.heap[parent]):
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[child]
            self.heap[child] = tmp

        # Recurse up the tree.
        self.restore_heap_property(parent)
