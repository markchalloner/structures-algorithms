class HashTable:
    def __init__(self, size=100):
        self.table = [[] for _ in range(size)]
        self.size = size

    def add(self, key, value):
        self.table[self._calculate_index(self.size, key)].append((key, value))

    def delete(self, key):
        bucket = self.table[self._calculate_index(self.size, key)]
        index = self._index(bucket, key)
        del bucket[index]

    def search(self, key):
        bucket = self.table[self._calculate_index(self.size, key)]
        index = self._index(bucket, key)
        return bucket[index][1]

    @staticmethod
    def _index(bucket, key):
        for i in range(len(bucket)):
            k, _ = bucket[i]
            if key == k:
                return i

    @staticmethod
    def _calculate_index(size, key):
        return hash(key) % size
