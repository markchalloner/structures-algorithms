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
                    if current.left is None:
                        current.left = item
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = item
                        break
                    else:
                        current = current.right

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
