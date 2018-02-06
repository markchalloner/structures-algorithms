from ..components.queue import Queue
import unittest


class TestQueue(unittest.TestCase):

    def testEnqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.items, [1, 2, 3])

    def testEnqueueList(self):
        queue = Queue()
        queue.enqueue_list([1, 2, 3])
        self.assertEqual(queue.items, [1, 2, 3])

    def testDequeue(self):
        queue = Queue()
        queue.enqueue_list([1, 2, 3])
        item = queue.dequeue()
        self.assertEqual(item, 1)
        self.assertEqual(queue.items, [2, 3])


if __name__ == '__main__':
    unittest.main()
