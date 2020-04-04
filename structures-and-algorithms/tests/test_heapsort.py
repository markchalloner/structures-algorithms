from ..components.heap import Heap
from ..components.heapsort import Heapsort
import unittest


class TestHeapsort(unittest.TestCase):

    def testSort(self):
        items = [99, 1, 2, 6, 5, 33, 2, 100]
        heap = Heap()
        heap.enqueue_list(items)
        self.assertListEqual(Heapsort.sort(heap), sorted(items))


if __name__ == '__main__':
    unittest.main()
