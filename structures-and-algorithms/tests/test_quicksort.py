from ..components.quicksort import QuickSort
import unittest


class TestQuickSort(unittest.TestCase):

    def testSort(self):
        items = [22, 2, 6, 5, 33, 2, 100]
        self.assertListEqual(QuickSort.sort(items), sorted(items))

if __name__ == '__main__':
    unittest.main()