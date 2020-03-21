from ..components.hash_table import HashTable
import unittest


class TestHashTable(unittest.TestCase):
    def testAdd(self):
        hash_table = HashTable()
        hash_table.add(0, 'a')
        hash_table.add(100, 'b')
        assert hash_table.table[0] == [(0, 'a'), (100, 'b')]
        assert len(hash_table.table) == 100

    def testDelete(self):
        hash_table = HashTable()
        hash_table.add(0, 'a')
        hash_table.add(100, 'b')
        hash_table.add(200, 'c')
        hash_table.delete(100)
        assert hash_table.table[0] == [(0, 'a'), (200, 'c')]

    def testSearch(self):
        hash_table = HashTable()
        hash_table.add(0, 'a')
        hash_table.add(100, 'b')
        hash_table.add(200, 'c')
        assert hash_table.search(100) == 'b'


if __name__ == '__main__':
    unittest.main()

