from tree import tree
from math import inf


def validateBST(root, range: tuple) -> bool:
    minimum, maximum = range[0], range[1]
    if not root:
        return True
    if root.value <= minimum or root.value >= maximum:
        return False
    return validateBST(root.left_child, (minimum, root.value)) and validateBST(
        root.right_child, (root.value, maximum))


def swap_root(root):
    root.left_child, root.right_child = root.right_child, root.left_child


if __name__ == "__main__":
    print(validateBST(tree.root, (-inf, inf)))
    swap_root(tree.root)
    print(validateBST(tree.root, (-inf, inf)))
