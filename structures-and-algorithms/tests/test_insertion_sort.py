from ..components.insertion_sort import InsertionSort
import unittest


class TestInsertionSort(unittest.TestCase):

    def testSort(self):
        items = [1, 2, 6, 5, 33, 2, 100]
        self.assertListEqual(InsertionSort.sort(items), sorted(items))


if __name__ == '__main__':
    unittest.main()