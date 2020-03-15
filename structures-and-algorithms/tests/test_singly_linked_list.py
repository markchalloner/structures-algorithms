from ..components.singly_linked_list import SinglyLinkedList, SinglyLinkedListItem
import unittest


class TestSinglyLinkedList(unittest.TestCase):

    def testInsert(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert(3)
        singly_linked_list.insert(2)
        singly_linked_list.insert(1)
        self.assertEqual(singly_linked_list.to_list(), [1, 2, 3])

    def testDelete(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert(3)
        singly_linked_list.insert(2)
        singly_linked_list.insert(1)
        singly_linked_list.delete(3)
        self.assertEqual(singly_linked_list.to_list(), [1, 2])

    def testSearch(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert(3)
        singly_linked_list.insert(2)
        singly_linked_list.insert(1)
        self.assertEqual(singly_linked_list.search(2).value, 2)


if __name__ == '__main__':
    unittest.main()
