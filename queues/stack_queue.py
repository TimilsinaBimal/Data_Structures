import sys
sys.path.append('/Data_Structures/')
from stacks.stack import Stack
from queue import QueueUnderflowError, QueueOverflowError

class StackQueue:
    """
    Implementation of Queue using two Stacks.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.stack_one = Stack(limit)
        self.stack_two = Stack(limit)

    def enqueue(self, item):
        if self.isFull():
            raise QueueOverflowError("Cannot insert item in a full queue.")
        self.stack_one.push(item)

    def _move_item_to_second_stack(self):
        if self.stack_two.is_empty():
            while not self.stack_one.is_empty():
                self.stack_two.push(self.stack_one.pop())

    def dequeue(self):
        if self.isEmpty():
            raise QueueUnderflowError(
                "Cannot Remove an item from empty Queue.")
        self._move_item_to_second_stack()
        return self.stack_two.pop()

    def peek(self):
        self._move_item_to_second_stack()
        return self.stack_two.peek()

    def isEmpty(self):
        return self.stack_one.is_empty() and self.stack_two.is_empty()

    def isFull(self):
        return (self.stack_one.size() + self.stack_two.size()) >= self.limit


if __name__ == "__main__":
    queue = StackQueue(3)
    queue.enqueue(10)
    queue.enqueue(20)
    print(queue.dequeue())
    print(queue.peek())
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue.peek())
