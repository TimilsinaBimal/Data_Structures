class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def __str__(self):
        return str(self.toArray())

    def isEmpty(self):
        """
        Checks if the linked list is empty or not.
        """
        if self.first is None:
            return True
        else:
            return False

    def addLast(self, item):
        """
        Adds an item at the end of Linked list.
        """
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
        """
        Adds an item at the start of Linked list.
        """
        node = Node(item)
        if self.isEmpty():
            self.first = self.last = node
        else:
            current = self.first
            self.first = node
            node.next = current
        self._size += 1

    def removeFirst(self):
        """
        Removes the first item of linked list.
        """
        if self.first:
            temp = self.first
            self.first = temp.next
            self._size -= 1
        else:
            return -1

    def removeLast(self):
        """
        Removed the last item of linked list.
        """
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

    def indexOf(self, item):
        """
        Returns the index of an item.
        """
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

    def remove(self, item):
        index = self.indexOf(item)
        if self.first:
            previous = None
            current = self.first
            while current:
                if current.value == item:
                    previous.next = current.next
                    self._size -= 1
                    return current.value
                else:
                    previous = current
                    current = current.next
        else:
            return -1

    def __contains__(self, item) -> bool:
        """
        Return if the item contains in list or not.
        >>> linked_list = LinkedList()
        >>> 10 in linked_list
        False
        >>> linked_list.addFirst(10)
        >>> linked_list.addLast(20)
        >>> 10 in linked_list
        True
        >>> 30 in linked_list
        False
        """
        return item in self.toArray()

    def __len__(self):
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.addLast("tail")
        >>> len(linked_list)
        1
        >>> linked_list.addFirst("head")
        >>> len(linked_list)
        2
        >>> linked_list.removeLast()
        >>> len(linked_list)
        1
        >>> linked_list.removeFirst()
        >>> len(linked_list)
        0
        """
        return self._size

    def size(self):
        """
        Returns the size of Linked list.
        """
        return self._size

    def toArray(self):
        """
        Converts Linked list to a list.
        """
        array = []
        if self.first:
            current = self.first
            while current:
                array.append(current.value)
                current = current.next
        return array

    def reverse(self):
        """
        Reverse the linked list.
        """
        if self.first:
            current = self.first
            prev = None
            while current:
                _next = current.next
                current.next = prev
                prev = current
                current = _next
            self.last = self.first
            self.first = prev
        return -1

    def getKthNodeFromEnd(self, k):
        """
        :param k: int
        :return: kth element from the last node.
        """
        if not self.first:
            raise EmptyListError("Cannot Search element in empty list.")
        if k > self.size():
            raise IndexError(
                "K cannot be greater than the size of linked list.")
        _last = self.first
        previous = self.first

        for _ in range(k-1):
            _last = _last.next
        while _last != self.last:
            previous = previous.next
            _last = _last.next
        return previous.value


class EmptyListError(BaseException):
    pass


if __name__ == "__main__":
    llist = LinkedList()
    print(llist.isEmpty())
    print(llist.size())
    llist.addFirst(10)
    print(llist.size())
    llist.addLast(20)
    llist.addLast(30)
    llist.removeLast()
    llist.addLast(40)
    llist.addLast(50)
    llist.remove(20)
    print(llist.getKthNodeFromEnd(1))
    # llist.reverse()
    print(llist.isEmpty())
    print(llist)
