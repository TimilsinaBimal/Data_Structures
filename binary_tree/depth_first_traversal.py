from tree import tree


def preorder_traversal(root):
    if not root:
        return
    print(root.value, end=" ")
    preorder_traversal(root.left_child)
    preorder_traversal(root.right_child)


def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left_child)
    print(root.value, end=" ")
    inorder_traversal(root.right_child)


def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left_child)
    postorder_traversal(root.right_child)
    print(root.value, end=" ")


if __name__ == "__main__":
    print("Preorder Traversal:")
    preorder_traversal(tree.root)
    print("\nPostorder Traversal:")
    postorder_traversal(tree.root)
    print("\nInorder Traversal:")
    inorder_traversal(tree.root)
