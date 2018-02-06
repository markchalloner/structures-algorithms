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

    def testEnqueue(self):
        heap = Heap()
        heap.enqueue(1)
        heap.enqueue(2)
        heap.enqueue(6)
        heap.enqueue(5)
        heap.enqueue(33)
        heap.enqueue(2)
        heap.enqueue(100)
        self.assertHasHeapProperty(heap)
        self.assertListEqual([100, 6, 33, 1, 5, 2, 2], heap.heap)

    def testEnqueueList(self):
        heap = Heap()
        heap.enqueue_list([1, 2, 6, 5, 33, 2, 100])
        self.assertHasHeapProperty(heap)
        self.assertListEqual([100, 6, 33, 1, 5, 2, 2], heap.heap)

    def testDequeue(self):
        heap = Heap()
        heap.enqueue_list([1, 2, 6, 5, 33, 2, 100])
        heap.dequeue()
        self.assertHasHeapProperty(heap)
        self.assertListEqual([33, 6, 2, 1, 5, 2], heap.heap)


if __name__ == '__main__':
    unittest.main()
