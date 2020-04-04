class BubbleSort:
    @staticmethod
    def sort(items):
        items = list(items)
        end = len(items)
        while end > 0:
            for current in range(1, end):
                candidate = current - 1
                if items[current] < items[candidate]:
                    items.insert(candidate, items.pop(current))
            end -= 1
        return items
