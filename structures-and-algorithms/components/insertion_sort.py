class InsertionSort:
    @staticmethod
    def sort(items):
        items = list(items)
        for current in range(1, len(items)):
            candidate = current - 1
            while items[current] < items[candidate]:
                items.insert(candidate, items.pop(current))
                current = candidate
                candidate -= 1
        return items
