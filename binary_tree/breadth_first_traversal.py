from tree import tree
from find_height import height
from get_nodes_at_distance import get_nodes_at_distance


def breadth_first_traversal(root):
    for h in range(height(root)+1):
        get_nodes_at_distance(root, h)


if __name__ == "__main__":
    breadth_first_traversal(tree.root)
