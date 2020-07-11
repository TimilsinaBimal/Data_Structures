class Stack:
    """
    A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).
    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

    def __init__(self, limit=10):
        self.stack = []
        self._size = 0
        self.limit = limit

    def __bool__(self):
        return bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        """
        Accepts an item as parameter and appends at the top of stack.
        Returns Nothing.

        The runtime for this method is O(1) or constant time,
        because appending at the top of stack happens in constant time.
        """
        if len(self.stack) >= self.limit:
            raise StackOverflowError("Cannot insert item in full stack!")
        self.stack.append(data)
        self._size += 1

    def pop(self):
        """
        Removes the items present at the top of stack.
        Returns the popped item.

        The runtime for this method is O(1) or constant time,
        because removing an item from the top happens in constant time.
        """
        if self.stack:
            self._size -= 1
            return self.stack.pop()
        raise StackUnderflowError("Cannot remove item from empty stack!")

    def peek(self):
        """
        Returns an item present at the top of stack.

        The runtime of this method is O(1) or constant time,
        because searching the top of stack happens in constant time.
        """
        if self.stack:
            return self.stack[self._size-1]
        raise EmptyStackError("Cannot return top from empty stack!")

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

    def __contains__(self, item) -> bool:
        """
        Return if the item is in stack or not.

        The runtime Complexity of this method is O(n) or linear time,
        because searching a item in an array costs n time.
        """
        return item in self.stack


class StackOverflowError(BaseException):
    pass


class StackUnderflowError(BaseException):
    pass

class EmptyStackError(BaseException):
    pass


if __name__ == "__main__":
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack.is_empty())
    stack.pop()
    stack.push(10)
    stack.pop()
    stack.push(10)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.size())
    print(stack)
