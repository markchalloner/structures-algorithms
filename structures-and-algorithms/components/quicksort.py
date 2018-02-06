class QuickSort:

    def __init__(self):
        pass

    @classmethod
    def sort(cls, items, start=0, end=None):
        if end is None:
            end = len(items) - 1

        def _sort(items, start, end):
            if end < start:
                return

            pivot = start
            left = start + 1
            right = end

            # Partition.
            while True:
                while left <= right and items[left] <= items[pivot]:
                    left += 1
                while right >= left and items[right] >= items[pivot]:
                    right -= 1
                if left >= right:
                    break
                items[left], items[right] = items[right], items[left]
            items[pivot], items[right] = items[right], items[pivot]

            # Sort left of the pivot.
            _sort(items, start, right - 1)

            # Sort right of the pivot.
            _sort(items, right + 1, end)

        _sort(items, start, end)
        return items
