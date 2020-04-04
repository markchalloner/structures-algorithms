from ..components.quicksort import Quicksort
import unittest


class TestQuicksort(unittest.TestCase):

    def testSort(self):
        items = [22, 2, 6, 5, 33, 2, 100]
        self.assertListEqual(Quicksort.sort(items), sorted(items))


if __name__ == '__main__':
    unittest.main()