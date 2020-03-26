class RedBlackTreeItem:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.red = True
        self.value = value


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.black_height = 0

    def _is_not_root_or_root_and_black(self, item):
        # Root must be black.
        if item is self.root and not item.red:
            return False
        return True

    def _is_black_or_red_with_black_children(self, item):
        # Red item must only have black children.
        if item.red and ((item.left and item.left.red) or (item.right and item.right.red)):
            return False
        return True

    def _is_black_height_correct(self, item):
        # Path to item must have same number of black items as all other paths in the tree.
        black_height = 0
        while item:
            if not item.red:
                black_height += 1
            item = item.parent
        if black_height != self.black_height:
            return False
        return True

    def add(self, value):
        item = RedBlackTreeItem(value)
        if self.root is None:
            self.root = item
            self.black_height = 1
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
        # Todo: 1. check validity of tree, 2. rebalance.
