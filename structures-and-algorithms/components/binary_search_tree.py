class BinarySearchTreeItem:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        item = BinarySearchTreeItem(value)
        if self.root is None:
            self.root = item
        else:
            current = self.root
            while current:
                if item.value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = item
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = item
                        break

    def search(self, index):
        return self.to_list()[index]

    def to_list(self, root=None):
        items = []
        current = root or self.root
        if current:
            if current.left:
                items.extend(self.to_list(current.left))
            items.append(current.value)
            if current.right:
                items.extend(self.to_list(current.right))
        return items
