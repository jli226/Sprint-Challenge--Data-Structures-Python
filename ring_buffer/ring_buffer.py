from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if self.current is None:
                self.current = self.storage.tail

        else:
            self.storage.add_to_tail(item)
            if self.storage.head is self.current:
                self.storage.remove_from_head()
                self.current = self.storage.tail
            else:
                self.storage.remove_from_head()

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        j = self.storage.head
        i = self.current
        while len(list_buffer_contents) < self.storage.length:
            if i is not None:
                list_buffer_contents.append(i.value)
                i = i.next
            else:
                list_buffer_contents.append(j.value)
                j = j.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = 0

    def append(self, item):
        # Update the value in the "current" index
        self.storage[self.current] = item
        self.current += 1
        # Reset the current index when you reach the end
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        # Filter out None values
        return [item for item in self.storage if item is not None]
