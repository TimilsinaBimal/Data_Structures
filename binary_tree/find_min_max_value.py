from tree import tree


def find_minimum_value(root):
    if not root.left_child and not root.right_child:
        return root.value
    return min(min(find_minimum_value(root.left_child), find_minimum_value(root.right_child)), root.value)


def find_minimum_value_BST(root):
    current_node = root
    last_leaf_node = root
    while current_node:
        last_leaf_node = current_node
        current_node = current_node.left_child
    return last_leaf_node.value


def find_maximum_value(root):
    if not root.left_child and not root.right_child:
        return root.value
    return max(max(find_maximum_value(root.left_child), find_maximum_value(root.right_child)), root.value)


def find_maximum_value_BST(root):
    current_node = root
    last_leaf_node = root
    while current_node:
        last_leaf_node = current_node
        current_node = current_node.right_child
    return last_leaf_node.value


if __name__ == "__main__":
    print("Minimum Value: ", find_minimum_value(tree.root))
    print("Minimum Value(BST): ", find_minimum_value_BST(tree.root))
    print("Maximum Value: ", find_maximum_value(tree.root))
    print("Maximum Value(BST): ", find_maximum_value_BST(tree.root))
