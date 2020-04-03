class SelectionSort:
    @staticmethod
    def sort(items):
        items = list(items)
        for current in range(len(items)):
            for candidate in range(current):
                if items[current] <= items[candidate]:
                    items.insert(candidate, items.pop(current))
                    break
        return items
