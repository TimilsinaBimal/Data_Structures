from tree import tree


def areEqual(root1, root2) -> bool:
    if not root1 and not root2:
        return True
    if root1 and root2:
        return root1.value == root2.value and areEqual(root1.left_child, root2.left_child) and areEqual(root1.right_child, root2.right_child)

    return False


if __name__ == "__main__":
    tree1 = tree
    tree2 = tree
    print(areEqual(tree1.root, tree2.root))
