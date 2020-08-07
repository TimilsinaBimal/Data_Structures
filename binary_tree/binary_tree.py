class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(f"Left: {self.left_child.value} Value: {self.value} Right: {self.right_child.value}")

    def __repr__(self):
        return f"Left: {self.left_child.value} Value: {self.value} Right: {self.right_child.value}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def find(self, value) -> bool:
        if self.root:
            current = self.root
            while current:
                if value == current.value:
                    return True
                elif value > current.value:
                    current = current.right_child
                else:
                    current = current.left_child
            return False

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left_child:
                    current.left_child = node
                    break
                current = current.left_child
            else:
                if not current.right_child:
                    current.right_child = node
                    break
                current = current.right_child


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(9)
    tree.insert(1)
    tree.insert(6)
    tree.insert(8)
    tree.insert(10)
    print(tree.find(10))
    print(tree.find(100))
