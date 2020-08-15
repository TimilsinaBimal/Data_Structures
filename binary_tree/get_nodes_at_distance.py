from tree import tree


def get_nodes_at_distance(root, distance: int):
    if not root:
        return
    if distance == 0:
        print(root.value, end=" ")
        return

    get_nodes_at_distance(
        root.left_child, distance-1)
    get_nodes_at_distance(
        root.right_child, distance-1)


if __name__ == "__main__":
    get_nodes_at_distance(tree.root, 2)
