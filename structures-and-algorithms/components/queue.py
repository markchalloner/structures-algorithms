# Or use collections.deque.

class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def enqueue_list(self, items):
        for item in items:
            self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
