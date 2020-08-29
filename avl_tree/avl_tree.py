class AVLNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(f"Left Child: {self.left_child} Value: {self.value} Right Child: {self.right_child}")


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root: AVLNode, value) -> AVLNode:
        if root is None:
            return AVLNode(value)
        if value < root.value:
            root.left_child = self._insert(root.left_child, value)
        else:
            root.right_child = self._insert(root.right_child, value)

        self._set_height(root)

        return self._balance(root)

    def _balance(self, root: AVLNode):
        if self._is_left_heavy(root):
            if self._balance_factor(root.right_child) < 0:
                root.left_child = self._left_rotate(root.left_child)
            return self._right_rotate(root)

        elif self._is_right_heavy(root):
            if self._balance_factor(root.right_child) > 0:
                root.right_child = self._right_rotate(root.right_child)
            return self._left_rotate(root)
        else:
            return root

    def _left_rotate(self, root: AVLNode) -> AVLNode:
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root

        self._set_height(new_root)
        self._set_height(root)
        return root

    def _right_rotate(self, root: AVLNode) -> AVLNode:
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root

        self._set_height(new_root)
        self._set_height(root)
        return root

    def _height(self, node: AVLNode) -> float:
        return -1 if node is None else node.height

    def _set_height(self, node):
        node.height = max(self._height(
            node.left_child), self._height(node.right_child)) + 1

    def _balance_factor(self, node: AVLNode) -> float:
        return 0 if node is None else (self._height(node.left_child) - self._height(node.right_child))

    def _is_left_heavy(self, node: AVLNode) -> bool:
        return self._balance_factor(node) > 1

    def _is_right_heavy(self, node: AVLNode) -> bool:
        return self._balance_factor(node) < -1


if __name__ == "__main__":
    tree = AVLTree()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
