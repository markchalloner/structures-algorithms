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

    def _is_not_root_or_root_and_black(self, item):
        if item is not self.root:
            return True
        if not item.black:
            return False
        return True

    def _is_black_or_red_with_black_children(self, item):
        if item.black:
            return True
        if item.left is not None and not item.left.black:
            return False
        if item.right is not None and not item.right.black:
            return False
        return True

    def _is_black_height_correct(self, item):
        # Path to item must have same number of black items as all other paths in the tree.
        black_height = 0
        while item:
            if item.black:
                black_height += 1
            item = item.parent
        if black_height != self.black_height:
            return False
        return True

    def _is_valid(self, item):
        return (
            self._is_not_root_or_root_and_black(item)
            and self._is_black_or_red_with_black_children(item)
            and self._is_black_height_correct(item)
        )

    # Todo: take only item and allow rotating with a left child.
    def _rotate_left(self, item, parent):
        if item.left is not None:
            raise NotImplementedError
        grandparent = parent.parent
        if grandparent is not None:
            if parent is grandparent.left:
                grandparent.left = item
            elif parent is grandparent.right:
                grandparent.right = item
        if parent is self.root:
            self.root = item
        item.parent = grandparent
        item.left = parent
        parent.parent = item
        parent.right = None
        return item, parent

    # Todo: take only item and allow rotating with a right child.
    def _rotate_right(self, item, parent):
        if item.right is not None:
            raise NotImplementedError
        grandparent = parent.parent
        if grandparent is not None:
            if parent is grandparent.left:
                grandparent.left = item
            elif parent is grandparent.right:
                grandparent.right = item
        if parent is self.root:
            self.root = item
        parent.parent = item
        parent.left = None
        item.parent = grandparent
        item.right = parent
        return item, parent

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
                    item, parent = self._rotate_left(item, parent)
                parent, grandparent = self._rotate_right(parent, grandparent)
            else:
                if item is parent.left:
                    item, parent = self._rotate_right(item, parent)
                parent, grandparent = self._rotate_left(parent, grandparent)
        self._is_valid(item)

    def delete(self, item):
        pass
        # Todo: implement delete.
        # self.remove_from_tree(item)
        # if item.red:
        #     if item.left and item.left.red:
        #         item = item.left
        #         item.red = False
        #     if item.right and item.right.red:
        #         item = item.right
        #         item.red = False
        #     return
        # current = item
        # while current:
        #     parent = current.parent
        #     sibling = self._get_sibling(current)
        #     if item is parent.left:
        #         if sibling.red:
        #             parent.red = True
        #             sibling.red = False
        #             current, parent = self._rotate_left(current, parent)
        #             sibling = self._get_sibling(current)
        #         if not sibling.left or not sibling.left.red or not sibling.right or not sibling.right.red:
        #             sibling.red = True
        #             if parent.red:
        #                 parent.red = False
        #                 return
        #             current = parent
        #             continue
        #         if sibling.left and sibling.left.red:
        #             sibling.red = True
        #             sibling.left.red = False
        #             self._rotate_right(sibling.left, sibling)
        #         if sibling.right and sibling.right.red:
        #             sibling.right.red = False
        #             parent.red = False
        #             self._rotate_left(sibling, parent)
        #     else:
        #         do mirror
        # return

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
