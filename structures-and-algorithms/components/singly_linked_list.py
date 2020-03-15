class SinglyLinkedListItem:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item, index=None):
        item = SinglyLinkedListItem(item)
        head = self.head
        self.head = item
        item.next = head

    def delete(self, value):
        prev = head = self.head
        if not head:
            raise ValueError
        else:
            while head:
                if head.value == value:
                    prev.next = head.next
                    return head
                prev = head
                head = head.next
        raise ValueError

    def search(self, value):
        prev = head = self.head
        if not head:
            raise ValueError
        while head:
            if head.value == value:
                return head
            prev = head
            head = head.next
        raise ValueError

    def to_list(self):
        list = []
        head = self.head
        while head:
            list.append(head.value)
            head = head.next
        return list
