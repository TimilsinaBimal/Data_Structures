class Stack:
    """
    A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """
    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self,data):
        """
        Accepts an item as parameter and appends at the top of stack.
        Returns Nothing.

        The runtime for this method is O(1) or constant time,
        because appending at the top of stack happens in constant time.
        """
        self.stack.append(data)
        self._size += 1

    def pop(self):
        """
        Removes the items present at the top of stack.
        Returns Nothing

        The runtime for this method is O(1) or constant time,
        because removing an item from the top happens in constant time.
        """
        self.stack.pop()
        self._size -=1

    def peek(self):
        """
        Returns an item present at the top of stack.

        The runtime of this method is O(1) or constant time,
        because searching the top of stack happens in constant time.
        """
        return self.stack[self._size-1]

    def size(self):
        """
        Returns the size of stack.
        """
        return self._size

    def is_empty(self):
        """
        Returns True if the stack is empty otherwise False.

        The runtime complexity of this method is O(1) or constant time,
        because checking if the stack is empty is happen in constant time.
        """
        return not bool(self.stack)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.pop()
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())