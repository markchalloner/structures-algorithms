from ..components.red_black_tree import RedBlackTree
import unittest


class TestRedBlackTree(unittest.TestCase):

    def testAdd(self):
        red_black_tree = RedBlackTree()
        red_black_tree.add(5)
        red_black_tree.add(3)
        red_black_tree.add(1)
        print(red_black_tree)
