from ..components.heap import Heap
import unittest


class TestHeap(unittest.TestCase):

    @classmethod
    def assertHasHeapProperty(cls, heap):
        count = len(heap)
        for child in range(count // 2, count):
            while child > 0:
                parent = (child - 1) // 2
                if heap.comparator(heap[child], heap[parent]):
                    raise AssertionError(
                        "Data structure does not have heap property: heap[%s] = %s compared to heap[%s] = %s\n\n%s" % (
                            parent,
                            heap[parent],
                            child,
                            heap[child],
                            heap,
                        )
                    )
                child = parent

    def testAdd(self):
        heap = Heap()
        heap.add(1)
        heap.add(2)
        heap.add(6)
        heap.add(5)
        heap.add(33)
        heap.add(2)
        heap.add(100)
        self.assertHasHeapProperty(heap)
        self.assertListEqual([100, 6, 33, 1, 5, 2, 2], heap.heap)

    def testAddList(self):
        heap = Heap()
        heap.add_list([1, 2, 6, 5, 33, 2, 100])
        self.assertHasHeapProperty(heap)
        self.assertListEqual([100, 6, 33, 1, 5, 2, 2], heap.heap)

    def testPop(self):
        heap = Heap()
        heap.add_list([1, 2, 6, 5, 33, 2, 100])
        heap.pop()
        self.assertHasHeapProperty(heap)
        self.assertListEqual([33, 6, 2, 5, 2, 1], heap.heap)

    def testSort(self):
        heap = Heap()
        heap.add_list([1, 2, 6, 5, 33, 2, 100])
        sorted_by_builtin = sorted(heap.heap, reverse=True)
        sorted_by_heap = []
        for i in range(len(heap)):
            sorted_by_heap.append(heap.pop())

        self.assertListEqual(sorted_by_heap, sorted_by_builtin)


if __name__ == '__main__':
    unittest.main()
