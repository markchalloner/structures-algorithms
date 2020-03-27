class RedBlackTreeItem:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.black = False
        self.value = value


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.black_height = 0

    def _flip_item(self, item):
        item.black = not item.black

    def _get_uncle(self, item):
        parent = item.parent
        if parent is None:
            return None
        grandparent = parent.parent
        if grandparent is None:
            return None
        return grandparent.left if item is parent.right else grandparent.right

    def _swap(self, item_1, item_2):
        if item_1.parent:
            if item_1 is item_1.parent.left:
                item_1.parent.left = item_2
            else:
                item_1.parent.right = item_2
        if item_2.parent:
            if item_2 is item_2.parent.left:
                item_2.parent.left = item_1
            else:
                item_2.parent.right = item_1
        item_2.parent, item_1.parent = item_1.parent, item_2.parent
        return item_2, item_1

    def add(self, value):
        item = RedBlackTreeItem(value)

        # If there is no root set the item and colour it black.
        if self.root is None:
            item.black = True
            self.root = item
            self.black_height = 1
            return

        # Insert the item in the tree.
        current = self.root
        while current:
            if item.value < current.value:
                if current.left is None:
                    current.left = item
                    item.parent = current
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = item
                    item.parent = current
                    break
                else:
                    current = current.right

        # If the parent is black then there is nothing more to do.
        parent = item.parent
        if parent.black:
            return

        uncle = self._get_uncle(item)
        grandparent = parent.parent

        # If uncle is red then flip the color of grandparent, parent and item.
        if uncle is not None and not uncle.black:
            # Only flip an existing non-root grandparent.
            if grandparent is not None and grandparent is not self.root:
                grandparent.black = not grandparent.black
            parent.black = not parent.black
            item.black = not item.black
            return

        # If uncle is not present or black then we need to rotate the tree.
        if uncle is None or uncle.black:
            if parent is grandparent.left:
                if item is parent.right:
                    item, parent = self._swap(item, parent)
                parent, grandparent = self._swap(parent, grandparent)
            else:
                if item is parent.left:
                    item, parent = self._swap(item, parent)
                parent, grandparent = self._swap(parent, grandparent)

    def to_list(self, root):
        items = []
        current = root or self.root
        if current:
            if current.left:
                items.extend(self.to_list(current.left))
            items.append(current.value)
            if current.right:
                items.extend(self.to_list(current.right))
        return items