from ..components.red_black_tree import RedBlackTree
import unittest


class TestRedBlackTree(unittest.TestCase):

    def testAdd(self):
        red_black_tree = RedBlackTree()
        red_black_tree.add(5)
        red_black_tree.add(3)
        red_black_tree.add(100)
        red_black_tree.add(1)
        red_black_tree.add(2)
        assert red_black_tree.to_list() == [1, 2, 3, 5, 100]
