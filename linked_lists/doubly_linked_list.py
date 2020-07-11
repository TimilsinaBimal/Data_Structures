class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def isEmpty(self):
        # return True if self.first is None else False
        if self.first is None:
            return True
        else:
            return False

    def addFirst(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            current = self.first
            self.first = node
            node.prev = None
            node.next = current
        self._size += 1

    def addLast(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            current = self.first
            while current.next:
                current = current.next
            last = current
            current.next = node
            self.last = node
            node.prev = last
        self._size += 1

    def removeFirst(self):
        if self.first:
            current = self.first
            self.first = current.next
            current.next.prev = None
            self._size -= 1

    def removeLast(self):
        if self.first:
            second_last = self.last.prev
            self.last = second_last
            self.last.next = None
            self._size -= 1

    def toArray(self):
        array = []
        if self.first:
            current = self.first
            while current:
                array.append(current.value)
                current = current.next
        return array

    def size(self):
        return self._size


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.addFirst(10)
    dll.addLast(20)
    dll.addLast(30)
    dll.addLast(40)
    dll.removeFirst()
    dll.removeLast()
    print(dll.toArray())
    print(dll.isEmpty())
    print("Hello world")