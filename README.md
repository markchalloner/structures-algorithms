# Structures and Algorithms.

A collection of data structrures and algorithms written in python.

### Usage

``` python
from structures-and-algorithms.components.heap import Heap
from structures-and-algorithms.components.heapsort import HeapSort


heap = Heap(comparator=lambda a, b: a > b)
heap.add_list([1, 2, 6, 5, 33, 2, 100])

# Prints `[100, 6, 33, 1, 5, 2, 2]`.
print heap

# Prints `[100, 33, 6, 5, 2, 2, 1]`.
print HeapSort.sort(heap)
```

## Tests

```
$ python setup.py test
```
