from ..components.heap import Heap
from ..components.heapsort import HeapSort
import unittest


class TestHeapSort(unittest.TestCase):

    def testSort(self):
        items = [1, 2, 6, 5, 33, 2, 100]
        heap = Heap()
        heap.enqueue_list(items)
        self.assertListEqual(HeapSort.sort(heap), sorted(items, reverse=True))


if __name__ == '__main__':
    unittest.main()