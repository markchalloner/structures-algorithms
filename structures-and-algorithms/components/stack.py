# Or use a built in array or collections.deque.

class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def push_list(self, items):
        for item in items:
            self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek():
        return self.items.peek()
