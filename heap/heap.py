class HeapOverflowError(BaseException):
    pass


class HeapUnderflowError(BaseException):
    pass


class Heap:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.items = [None for _ in range(max_size)]
        self.size = 0

    def __str__(self):
        return str([i for i in self.items if i])

    def __len__(self):
        return self.size

    def insert(self, value):
        if self.is_full():
            raise HeapOverflowError("Cannot insert item in already filled heap.")

        self.items[self.size] = value
        self.size += 1
        self._bubble_up()

    def remove(self):
        if self.is_empty():
            raise HeapUnderflowError("Cannot remove item from empty heap.")

        root = self.items[0]
        self.items[0], self.items[self.size-1] = self.items[self.size-1], None
        self.size -= 1
        self._bubble_down()
        return root

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def _has_left_child(self, idx):
        return self._left_child_index(idx) <= self.size

    def _has_right_child(self,idx):
        return self._right_child_index(idx) <= self.size

    def _largest_index(self, index):
        if not self._has_left_child(index):
            return index

        if not self._has_right_child(index):
            return self._left_child_index(index)

        return self._left_child_index(index) if self._left_child(index) > self._right_child(
            index) else self._right_child_index(index)

    def _bubble_down(self):
        index = 0
        while index <= self.size and not self._is_valid_parent(index):
            largest_index = self._largest_index(index)
            self.items[index], self.items[largest_index] = \
                self.items[largest_index], self.items[index]
            index = largest_index

    def _bubble_up(self):
        index = self.size - 1
        while index > 0 and (self.items[index] > self.items[self._parent_index(index)]):
            self.items[index], self.items[self._parent_index(index)] = \
                self.items[self._parent_index(index)], self.items[index]
            index = self._parent_index(index)

    def _is_valid_parent(self, idx) -> bool:
        if not self._has_left_child(idx):
            return True

        is_valid = self.items[idx] >= self._left_child(idx)

        if self._has_right_child(idx):
            is_valid &= self.items[idx] >= self._right_child(idx)

        return is_valid

    def _parent(self, idx):
        return self.items[idx]

    def _right_child(self, idx):
        return self.items[self._right_child_index(idx)]

    def _left_child(self, idx):
        return self.items[self._left_child_index(idx)]

    @staticmethod
    def _left_child_index(idx) -> int:
        return int((idx * 2) + 1)

    @staticmethod
    def _right_child_index(idx) -> int:
        return int((idx * 2) + 2)

    @staticmethod
    def _parent_index(idx):
        return int((idx - 1) / 2)


if __name__ == '__main__':
    heap = Heap()
    heap.insert(15)
    heap.insert(21)
    heap.insert(20)
    heap.insert(1)
    heap.insert(4)
    print(heap.remove())
    print(heap)

