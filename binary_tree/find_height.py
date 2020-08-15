from tree import tree


def height(root):
    if not root.left_child and not root.right_child:
        return 0

    return 1 + max(height(root.left_child), height(root.right_child))


if __name__ == "__main__":
    print("Height: ", height(tree.root))
