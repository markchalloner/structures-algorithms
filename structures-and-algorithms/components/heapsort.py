class HeapSort:

    def __init__(self):
        pass

    @classmethod
    def sort(cls, heap):
        out = []
        for i in range(len(heap)):
            out.append(heap.dequeue())
        return out
