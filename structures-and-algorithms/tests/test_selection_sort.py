from ..components.selection_sort import SelectionSort
import unittest


class TestSelectionSort(unittest.TestCase):

    def testSort(self):
        items = [99, 1, 2, 6, 5, 33, 2, 100]
        self.assertListEqual(SelectionSort.sort(items), sorted(items))


if __name__ == '__main__':
    unittest.main()