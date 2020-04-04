from ..components.bubble_sort import BubbleSort
import unittest


class TestBubbleSort(unittest.TestCase):

    def testSort(self):
        items = [99, 1, 2, 6, 5, 33, 2, 100]
        self.assertListEqual(BubbleSort.sort(items), sorted(items))


if __name__ == '__main__':
    unittest.main()