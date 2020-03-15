from ..components.stack import Stack
import unittest


class TestStack(unittest.TestCase):

    def testPush(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.items, [1, 2, 3])

    def testPushList(self):
        stack = Stack()
        stack.push_list([1, 2, 3])
        self.assertEqual(stack.items, [1, 2, 3])

    def testPop(self):
        stack = Stack()
        stack.push_list([1, 2, 3])
        item = stack.pop()
        self.assertEqual(item, 3)
        self.assertEqual(stack.items, [1, 2])


if __name__ == '__main__':
    unittest.main()
