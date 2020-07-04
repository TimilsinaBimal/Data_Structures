class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def isEmpty(self):
        if self.first is None:
            return True
        else:
            return False

    def addLast(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            current = self.first
            while current.next:  # Traverse to the last elemet
                current = current.next
            current.next = node  # set next item as node
            self.last = node  # set last node as current node
        self._size += 1

    def addFirst(self, item):
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            current = self.first
            self.first = node
            node.next = current
        self._size += 1

    def removeFirst(self):
        if self.first:
            temp = self.first
            self.first = temp.next
            self._size -= 1
        else:
            return -1

    def removeLast(self):
        if self.first:
            current = self.first
            while current.next:
                if current.next == self.last:
                    break
                current = current.next
            current.next = None
            self.last = current
            self._size -= 1
        else:
            return -1

    def indexOf(self,item):
        index = 0
        if self.first:
            current = self.first
            while current:
                if current.value == item:
                    return index
                else:
                    current = current.next
                    index += 1
            return -1
        else:
            return -1

    def contains(self,item):
        if not self.indexOf(item) == -1:
            return True
        else:
            return False

    def size(self):
        return self._size

    def toArray(self):
        array = []
        if self.first:
            current = self.first
            while current:
                array.append(current.value)
                current = current.next
        return array


def main():
    llist = LinkedList()
    print(llist.isEmpty())
    print(llist.size())
    llist.addFirst(10)
    print(llist.size())
    llist.addLast(20)
    llist.addLast(30)
    llist.removeLast()
    print(llist.size())
    print(llist.toArray())
    # print(llist.indexOf(40))
    # print(llist.contains(40))
    print(llist.isEmpty())

if __name__ == "__main__":
    main()
    print("Hello World")