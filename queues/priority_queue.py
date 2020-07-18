from queue import QueueUnderflowError, QueueOverflowError


class PriorityQueue:
    """
    Add and Remove items based on its priority.
    The small the number the greater its priority.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, item):
        """
        Add item according to its priority.
        """
        if self.is_full():
            raise QueueOverflowError("Cannot insert item in a full queue.")
        size = len(self.queue)
        idx = 0
        # Linear Search
        # size -= 1
        while idx < size:
            # Binary Searching
            mid = (idx + size)//2
            if item < self.queue[mid]:
                size = mid
            else:
                idx = mid+1

            # Linear Searching
            # if item < self.queue[size]:
            #     size = size-1
            # else:
            #     idx = size+1

        self.queue.insert(idx, item)

    def dequeue(self):
        """
        Remove item based on its priority.
        """
        if self.is_empty():
            raise QueueUnderflowError(
                "Cannot Remove an item from empty Queue.")
        return self.queue.pop()

    def peek(self):
        if not self.is_empty():
            return self.queue[self.size()-1]
        return -1

    def size(self):
        return len(self.queue)

    def is_full(self):
        return self.size() >= self.limit

    def is_empty(self):
        return not self.queue


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.enqueue(10)
    queue.enqueue(30)
    queue.enqueue(20)
    queue.enqueue(19)
    print(queue.peek())
    print(queue)
