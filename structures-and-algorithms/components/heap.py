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

    def enqueue(self, item):
        self.heap.append(item)

        # Restore heap order up the tree.
        self.restore_heap_order_up()

    def enqueue_list(self, items):
        for item in items:
            self.enqueue(item)

    def dequeue(self):
        count = len(self.heap)

        if count == 0:
            return

        if count == 1:
            return self.heap.pop()

        item = self.heap[0]

        # Replace root node with last item.
        self.heap[0] = self.heap.pop()

        # Restore heap order down the tree.
        self.restore_heap_order_down()

        return item

    def restore_heap_order_up(self, child=None):
        count = len(self)

        if count == 0:
            return

        if child is None:
            child = count - 1

        if child == 0:
            return

        parent = (child - 1) // 2

        # Swap if child node does not compare successfully to parent.
        if self.comparator(self.heap[child], self.heap[parent]):
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]


        self.restore_heap_order_up(parent)

    def restore_heap_order_down(self, parent=None):
        count = len(self)

        if count == 0:
            return

        if parent is None:
            parent = 0

        if parent == count - 1:
            return

        # Get child to swap with
        child1 = (parent * 2) + 1
        child2 = child1 + 1

        if child1 > count - 1:
            return

        if child2 > count - 1 or self.comparator(self.heap[child1], self.heap[child2]):
            child = child1
        else:
            child = child2

        # Swap if parent node does not compare successfully to child.
        if self.comparator(self.heap[child], self.heap[parent]):
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]

        # Recurse down tree.
        self.restore_heap_order_down(child)
